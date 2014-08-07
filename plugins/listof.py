# -*- coding: utf-8 -*-

import os
import json
from docutils import nodes
from docutils.parsers.rst import Directive, directives


from nikola import Nikola
from nikola.plugin_categories import RestExtension
from nikola.plugin_categories import Task
from nikola.plugin_categories import Command


def get_pages_per_tags(self):
    """Add a list of tagged pages to the main site object."""
    
    if hasattr(self, 'pages_per_tags'):
        return self.pages_per_tags
    
    pages_per_tags = {}
    self.pages_per_tags = pages_per_tags
    
    for page in self.pages:
        if not page.tags:
            continue
        
        meta = page.meta[page.default_lang]
        
        for tag in page.tags:

            # is this an index tag?
            listidx = 0
            if tag.startswith("listof:"):
                listidx = 1
                tag = tag[7:]
            
            if tag not in pages_per_tags:
                pages_per_tags[tag] = ([],[])
            
            pages_per_tags[tag][listidx].append(page)
    
    # sort the lists
    for tag in pages_per_tags:
        pages, index_pages = pages_per_tags[tag]
        pages.sort(key=lambda p: p.source_path)
    
    return pages_per_tags

# bind this method to the main Nikola object
Nikola.get_pages_per_tags = get_pages_per_tags


class CommandMakeLists(Command):
    """Make list stuff."""

    name = "listof"
    doc_usage = ""
    doc_purpose = "build listof index"

    cmd_options = ()

    def set_site(self, site):
        ListOf.site = site
        directives.register_directive('listof', ListOf)
        directives.register_directive('members', Members)
        
        return super(Command, self).set_site(site)
    
    def _execute(self, options, args):
        self.site.scan_posts()
        tagged = self.site.get_pages_per_tags()
        base_map_dir = "output/map"
        
        # Update depends
        print"TODO: record depends"
        for tag in tagged:
            geogroups = []
            pages = tagged[tag]
            for index_page in pages[1]:
                depends = index_page.fragment_deps(index_page.default_lang)
                for page in pages[0]:
                    depends.append(page.source_path)
                    grp = get_geo_info(page)
                    if grp:
                        grp["id"] = len(geogroups)+1
                        geogroups.append(grp)
            
            # save map data if any
            if len(geogroups) > 0:
                if not os.path.exists(base_map_dir):
                    os.makedirs(base_map_dir)
                geofeatures = {"type": "FeatureCollection", "features": geogroups}
                out = open(base_map_dir+"/geojson_%s.js" % tag, "w")
                out.write("var groups = ")
                json.dump(geofeatures, out)
                out.write(";\n")
                out.close()
        
        print depends
        
        
        # trigger a rebuild
        #self.site.doit.run( ["build"] )


def get_geo_info(page):
    meta = page.meta[page.default_lang]
    if "geolocation" not in meta:
        return
    
    properties = {"title": meta["title"], "content": meta["description"], "link":page.permalink()}
    coordinates = [ float(v.strip()) for v in meta["geolocation"].split(",") ]
    coordinates.reverse()
    geometry = {"type": "Point", "coordinates": coordinates }
    
    return {"type":"Feature", "properties":properties, "geometry":geometry}


def get_page_list(mark, options=[]):
    
    tagged = ListOf.site.get_pages_per_tags()
    
    if mark not in tagged:
        return None
    
    pages = tagged[mark][0]
    
    if "reversed" in options:
        pages = reversed(pages)
    
    return pages


class ListOf(Directive):
    """ Restructured text extension for inserting a list of marked pages

    Usage:
        .. listof:: <mark>
    """
    
    required_arguments = 1
    optional_arguments = 2
    
    
    def run(self):
        """ Required by the Directive interface. Create docutils nodes """
        self.check_content()
        
        mark = self.arguments[0]
        options = self.arguments[1:]
        pages = get_page_list(mark, options)
        
        if not pages:
            return [nodes.raw('', '', format='html')]
        
        # TODO: find a way to handle dependencies properly (mark the index as dirty in some situations)
        depends = self.state.document.settings.record_dependencies
        
        text = ""
        text += "<ul>"
        for page in pages:
            link = page.permalink()
            title = page.title()
            description = page.description()
            if description:
                description = "<br/>"+description
            meta = page.meta[page.default_lang]
            text += "<li><a href='"+link+"'>"+title+"</a>"+description+"</li>"
            depends.add(page.source_path)
        text += "</ul>"
        
        return [nodes.raw('', text, format='html')]

    def check_content(self):
        """ Emit a deprecation warning if there is content """
        if self.content:
            raise self.warning("This directive does not accept content. The "
                               "'key=value' format for options is deprecated, "
                               "use ':key: value' instead")



class MapOf(Directive):
    """ Restructured text extension for inserting a map of marked pages.

    Usage:
        .. listof:: <mark>
    """

    has_content = True
    required_arguments = 1

    def run(self):
        """ Required by the Directive interface. Create docutils nodes """
        self.check_content()
        
        mark = self.arguments[0]
        options = self.arguments[1:]
        pages = get_page_list(mark, options)
        
        if not pages:
            return [nodes.raw('', '', format='html')]
        
        # TODO: adapt code from ListOf to build a map instead
        
        # TODO: find a way to handle dependencies properly (mark the index as dirty in some situations)
        depends = self.state.document.settings.record_dependencies
        
        text += "<ul>"
        for page in tagged[mark][0]:
            link = page.permalink()
            title = page.title()
            description = page.description()
            if description:
                description = "<br/>"+description
            meta = page.meta[page.default_lang]
            text += "<li><a href='"+link+"'>"+title+"</a>"+description+"</li>"
            depends.add(page.source_path)
        text += "</ul>"
        
        return [nodes.raw('', text, format='html')]

    def check_content(self):
        """ Emit a deprecation warning if there is content """
        if self.content:
            raise self.warning("This directive does not accept content. The "
                               "'key=value' format for options is deprecated, "
                               "use ':key: value' instead")


class Members(Directive):
    """ Restructured text extension for inserting all members

    Usage:
        .. members:: <mark>
    """
    
    required_arguments = 1
    
    def run(self):
        """ Required by the Directive interface. Create docutils nodes """
        self.check_content()
        
        mark = self.arguments[0]
        pages = get_page_list(mark)
        
        if not pages:
            return [nodes.raw('', '', format='html')]
        
        # TODO: find a way to handle dependencies properly (mark the index as dirty in some situations)
        depends = self.state.document.settings.record_dependencies
        
        members = []
        for page in pages:
            link = page.permalink()
            title = page.title()
            parent = "<a href='"+link+"'>"+title+"</a>"
            pagemembers = [ (m.strip(), parent) for m in page.meta[page.default_lang]["members"].split(",") ]
            members += pagemembers
        
        members.sort( key=lambda m:m[0])
        
        text = ""
        text += "<ul>"
        for member,parent in members:
            text += "<li>"+member+" ("+parent+")</li>"
        text += "</ul>"
        
        return [nodes.raw('', text, format='html')]

    def check_content(self):
        """ Emit a deprecation warning if there is content """
        if self.content:
            raise self.warning("This directive does not accept content. The "
                               "'key=value' format for options is deprecated, "
                               "use ':key: value' instead")



