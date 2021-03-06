# -*- coding: utf-8 -*-

# compatibility with python 2.7 and 3
from __future__ import print_function


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


def get_pages_for_source(self, src):
    """Add a list of tagged pages to the main site object."""
    
    for page in self.pages:
        if page.source_path == src:
            return page

# bind these methods to the main Nikola object
Nikola.get_pages_per_tags = get_pages_per_tags
Nikola.get_pages_for_source = get_pages_for_source


class CommandMakeLists(Command):
    """Make list stuff."""

    name = "listof"
    doc_usage = ""
    doc_purpose = "build listof index"

    cmd_options = ()

    def _execute(self, options, args):
        self.site.scan_posts()
        tagged = self.site.get_pages_per_tags()
        base_map_dir = "output/map"
        
        # Update depends
        print( "TODO: record depends" )
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
        
        print( depends )
        
        
        # trigger a rebuild
        #self.site.doit.run( ["build"] )

class ListofExtensions(RestExtension):
    """Load RST extensions"""

    name = "listof_extensions"

    def set_site(self, site):
        ListOf.site = site
        directives.register_directive('listof', ListOf)
        directives.register_directive('usedby', UsedBy)
        directives.register_directive('members', Members)
        directives.register_directive('group_info', GroupInfo)
        directives.register_directive('method_info', MethodInfo)
        directives.register_directive('tool_header', ToolHeader)
        directives.register_directive('tool_info', ToolInfo)
        
        return super(RestExtension, self).set_site(site)


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
        check_content(self)
        
        mark = self.arguments[0]
        options = self.arguments[1:]
        depends = self.state.document.settings.record_dependencies
        text = get_page_listing(mark, options, depends)
        
        return [nodes.raw('', text, format='html')]

def get_page_listing(mark, options, depends, selected=None):
    pages = get_page_list(mark, options)
    
    if not pages:
        return ''
    
    groups = {}
    for page in pages:
        meta = page.meta[page.default_lang]
        slug = meta["slug"]
        if selected and slug not in selected:
            continue
        grp = None
        for t in page.tags:
            if t.startswith(":"):
                grp = t[1:]
                break
        if grp not in groups:
            groups[grp] = (None,[])
        if slug == grp:
            grp_pages = groups[grp][1]
            groups[grp] = (page, grp_pages)
            print( "found group entry: ", grp, page )
        else:
            groups[grp][1].append(page)
    text = ""
    for group in groups:
        entry_page, group_pages = groups[group]
        if group:
            text += "<div class='group'>"
            if entry_page:
                text += get_page_tile(entry_page)
                depends.add(page.source_path)
            else:
                text += "<div class='header'><span class='title'>"+group+"</span></div>"
            text += "<div class='content'>"
        for page in group_pages:
            text += get_page_tile(page)
            depends.add(page.source_path)
        if group:
            text += "</div></div>"
    
    return text


def get_page_tile(page):
    link = page.permalink()
    title = page.title()
    description = page.description()
    meta = page.meta[page.default_lang]
    subtitle = ""
    if "subtitle" in meta:
        subtitle = "<br><span class='subtitle'>"+meta["subtitle"]+"</span>"
    return "<a class='tile' href='"+link+"'><div class='header'><span class='title'>"+title+"</span>"+subtitle+"</div>"+description+"</a>"


class UsedBy(Directive):
    """ Restructured text extension for inserting a list of pages refering to the current one

    Usage:
        .. usedby:: <mark> <used_in>
    """
    
    required_arguments = 2
    optional_arguments = 2
    
    
    def run(self):
        """ Required by the Directive interface. Create docutils nodes """
        check_content(self)
        
        page = current_page(self)
        
        mark = self.arguments[0]
        usedin = self.arguments[1]
        options = self.arguments[1:]
        depends = self.state.document.settings.record_dependencies
        
        text = used_by(page, mark, usedin, options, depends)
        return [nodes.raw('', text, format='html')]



def used_by(page, mark, usedin, options, depends):
    """Shared method to show backlinks in various info blocks"""
    
    if not page:
        return [nodes.raw('', '', format='html')]

    slug = page.meta[page.default_lang]["slug"]
    pages = get_page_list(mark, options)
    
    if not pages:
        return [nodes.raw('', '', format='html')]

#        return [nodes.raw('', 'TODO: pages using "'+slug+'" as '+usedin, format='html')]
    
    # TODO: find a way to handle dependencies properly (mark the index as dirty in some situations)
    
    text = ""
    for page in pages:
        meta = page.meta[page.default_lang]
        if usedin not in meta:
            # the target page has no matching metadata
            continue
        used = [u.strip() for u in meta[usedin].split(",") ]
        if slug not in used:
            # the target page does not use the current page
            continue
        
        link = page.permalink()
        title = page.title()
        description = page.description()
        if description:
            description = "<br>"+description
        meta = page.meta[page.default_lang]
        text += "<a class='tile' href='"+link+"'><span class='title'>"+title+"</span>"+description+"</a>"
        depends.add(page.source_path)
    
    return text



class MapOf(Directive):
    """ Restructured text extension for inserting a map of marked pages.

    Usage:
        .. listof:: <mark>
    """

    has_content = True
    required_arguments = 1

    def run(self):
        """ Required by the Directive interface. Create docutils nodes """
        check_content(self)
        
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


class Members(Directive):
    """ Restructured text extension for inserting all members

    Usage:
        .. members:: <mark>
    """
    
    required_arguments = 1
    
    def run(self):
        """ Required by the Directive interface. Create docutils nodes """
        check_content(self)
        depends = self.state.document.settings.record_dependencies
        mark = self.arguments[0]
        text = get_members(mark, depends)
        
        return [nodes.raw('', text, format='html')]


class GroupInfo(Directive):
    """ Restructured text extension for inserting information about a group page
    Usage:
        .. group_info::
    """
    
    def run(self):
        page = current_page(self)
        depends = self.state.document.settings.record_dependencies
        text = get_group_info(page, depends)
        return [nodes.raw('', text, format='html')]



class MethodInfo(Directive):
    """ Restructured text extension for inserting information about a method page
    Usage:
        .. method_info::
    """
    
    def run(self):
        page = current_page(self)
        depends = self.state.document.settings.record_dependencies
        text = get_method_info(page, depends)
        return [nodes.raw('', text, format='html')]


class ToolInfo(Directive):
    """ Restructured text extension for inserting information about a software tool page
    Usage:
        .. tool_info::
    """
    
    def run(self):
        page = current_page(self)
        depends = self.state.document.settings.record_dependencies
        text = get_tool_info(page, depends)
        return [nodes.raw('', text, format='html')]

class ToolHeader(Directive):
    """ Restructured text extension for inserting information about a software tool page
    Usage:
        .. tool_header::
    """
    
    def run(self):
        page = current_page(self)
        depends = self.state.document.settings.record_dependencies
        text = get_tool_header(page, depends)
        return [nodes.raw('', text, format='html')]

def get_members(mark, depends):
    pages = get_page_list(mark)
    
    if not pages:
        return ''
    
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
    
    return text


def get_group_info(page, depends):
    if not page:
        return 'Group Info: Error finding the current page'
    
    text = "<hr>"
    web = page.meta[page.default_lang]["website"]
    text += "<p>Website: <a href='"+web+"'>"+web+"</a></p>"
    text += "Members involved in CoLoMoTo activities:"
    text += "<ul>"
    for member in page.meta[page.default_lang]["members"].split(","):
        text += "<li>"+member.strip()+"</li>"
    text += "</ul>"
    
    coords = page.meta["en"]["geolocation"]
    if coords: text += show_map(coords)
    
    return text


def get_method_info(page, depends):
    if not page:
        return 'Method Info: Error finding the current page'
    
    text = "<hr>"
    
    rel_tools = used_by(page, "tools", "methods", (), depends)
    if rel_tools:
        text += "<h3>Availability</h3>\n"+rel_tools
    
    return text


def get_tool_info(page, depends):
    """Get the bottom information block for a tool"""
    if not page:
        return 'Tool Info: Error finding the current page'
    
    meta = page.meta[page.default_lang]
    text = "<hr>"
    
    # add implemented methods and supported formats
    if "methods" in meta:
        sel_methods = [ m.strip() for m in meta["methods"].split(",") ]
        if sel_methods:
            text += "<h2>Implemented methods</h2>"
            text += get_page_listing("methods", [], depends, sel_methods)
    
    if "formats" in meta:
        sel_formats = [ m.strip() for m in meta["formats"].split(",") ]
        if sel_formats:
            text += "<h2>Supported formats</h2>"
            text += get_page_listing("formats", [], depends, sel_formats)
    
    return text

def get_tool_header(page, depends):
    """Get the top information block for a tool"""
    if not page:
        return 'Tool Info: Error finding the current page'
    
    meta = page.meta[page.default_lang]
    text = ""
    if "website" in meta:
        web = meta["website"]
        text += "<p>Website: <a href='"+web+"'>"+web+"</a></p>"
    text += "<hr>"
    
    return text


MAP_TILES= """L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);
"""

SMALL_MAP="""<div id="map" style="height: 300px; width:300px;"></div>
<script src="http://cdn.leafletjs.com/leaflet-0.7.2/leaflet.js"></script>
<script>
var map = L.map('map').setView([{1}], 4);
{0}
L.marker([{1}]).addTo(map);
</script>
"""

def show_map(coords):
    text = SMALL_MAP.format(MAP_TILES, coords)
    return text

def current_page(doc):
    return ListOf.site.get_pages_for_source(doc.state.document.settings._nikola_source_path)


def check_content(self):
    """ Emit a deprecation warning if there is content """
    if self.content:
        raise self.warning("This directive does not accept content. The "
                           "'key=value' format for options is deprecated, "
                           "use ':key: value' instead")


