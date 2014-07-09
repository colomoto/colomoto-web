# -*- coding: utf-8 -*-

import os
import json
from docutils import nodes
from docutils.parsers.rst import Directive, directives, roles


from nikola.plugin_categories import RestExtension

class Plugin(RestExtension):

    name = "rest_bib"

    def set_site(self, site):
        self.site = site
        directives.register_directive('ref', Reference)
        directives.register_directive('bibliography', Bibliography)
        roles.register_local_role("cite", cite_fn)
        return super(Plugin, self).set_site(site)

CODE = u"""<div class="ref">
{key}
<span class="title">{title}</span>
<br/><span class="authors">{authors}</span>
<span class="year">({year})</span>
<br/><span class="journal">{journal}</span>
<span class="position">{position}</span>
<span class="links">{links}</span>
<span class="extra">{extra}</span>
</div>"""

BASE = "references/"
PDFBASE = "files/references/"
REFS = {}

CUR_REFS = {}
CUR_REFS_IDX = []
CUR_DOC = None


def cur_refs(doc):
    
    global CUR_DOC, CUR_REFS, CUR_REFS_IDX
    if CUR_DOC != doc:
        CUR_DOC = doc
        CUR_REFS = {}
        CUR_REFS_IDX = []

def get_ref(key, depends):
    path = BASE+key+".json"
    depends.add(path)

    if key not in REFS:
        if os.path.exists(path):
            f = open(path)
            REFS[key] = json.load(f)
            f.close()
            if os.path.exists(PDFBASE+key+".pdf"):
                REFS[key]["pdf"] = key+".pdf"
        else:
            REFS[key] = None

    return REFS[key]

def cite(text, directive):
    cur_refs(directive)
    
    cited = []
    
    for key in text.split(","):
        key = key.strip()
        if key in CUR_REFS:
            idx = CUR_REFS[key]
        else:
            CUR_REFS_IDX.append(key)
            idx = len(CUR_REFS_IDX)
            CUR_REFS[key] = idx
        cited.append(idx)
    
    content = ",".join( [ "<a href='ref_%s'>%s</a>" % (c,c) for c in cited ] )
    content = ",".join( [ str(c) for c in cited ] )
    return "[%s]" % content


def biblio(document):
    cur_refs(document)
    
    # TODO: print all references!
    deps = document.settings.record_dependencies
    formatted = []
    idx = 0
    for key in CUR_REFS_IDX:
        idx = CUR_REFS[key]
        ref = get_ref(key, deps)
        if ref is None:
            formatted.append("<br>%s: not found" % idx)
        else:
            formatted.append( format_ref(ref, idx) )
    
    return formatted


def extract_name(author):
    family, given = author.split(", ")
    if family.startswith("{") and family.startswith("{"):
        family = family[1:-1]
    given = [g[0]+"." for g in given.split(" ")]
    
    return "".join(given)+" "+family

def format_ref(ref, key=None):
    
    info = {
        "title": "Not found!!",
        "authors": "",
        "year": "",
        "journal": "",
        "position": "",
        "links": ""
    }

    if ref is not None:
        info["title"] = ref["title"]
        if key:
            info["key"] = "<span class='key'><a name='ref_%s' />[%s]</span>" % (key, key)
        else:
            info["key"] = ""
        
        # format authors
        if "author" in ref:
            authors = []
            for a in ref["author"]:
                authors.append(extract_name(a))
            info["authors"] = ", ".join(authors)
        
        if "year" in ref:
            info["year"] = ref["year"]
        
        if "journal" in ref:
            info["journal"] = ref["journal"]
        elif "booktitle" in ref:
            info["journal"] = ref["booktitle"]
        position = ""
        if "series" in ref:
            info["journal"] += ". "+ref["series"]
            
        if "volume" in ref:
            position = ref["volume"]
            if "number" in ref:
                position += "("+ref["number"]+")"
        
        if "pages" in ref:
            position += ":"+ref["pages"]
        info["position"] = position

        extra = ""
        if "keyword" in ref:
            keywords = ref["keyword"].split(",")
            if "#Openaccess" in keywords:
                extra += '<img src="/assets/icons/openaccess.png" alt="Open Access" title="Open Access"/>'
        info["extra"] = extra
        
        links = ""
        if "doi" in ref:
            doi = ref["doi"]
            links += '[<a href="http://dx.doi.org/%s">doi:%s</a>] ' % (doi, doi)
        if "pmid" in ref:
            pmid = ref["pmid"]
            links += '[<a href="http://www.ncbi.nlm.nih.gov/pubmed/%s">pubmed:%s</a>] ' % (pmid, pmid)
        if "pdf" in ref:
            pdf = ref["pdf"]
            links += '<a href="/references/%s"><img src="/assets/icons/pdf.png"/></a> ' % (pdf)
        info["links"] = links
        
        return CODE.format(**info)
    
    return ""

class Reference(Directive):
    """ Restructured text extension for inserting References

    Usage:
        .. ref:: <ref id>
    """

    has_content = True
    required_arguments = 1

    def run(self):
        """ Required by the Directive interface. Create docutils nodes """
        self.check_content()
        ref = get_ref(self.arguments[0], self.state.document.settings.record_dependencies)
        
        return [nodes.raw('', format_ref(ref), format='html')]

    def check_content(self):
        """ Emit a deprecation warning if there is content """
        if self.content:
            raise self.warning("This directive does not accept content. The "
                               "'key=value' format for options is deprecated, "
                               "use ':key: value' instead")

def cite_fn(name, rawtext, text, lineno, inliner, options={}, content=[]):
    cited = cite(text, inliner.document)
    return nodes.raw('', cited, format='html'),[]


class Bibliography(Directive):
    """ Restructured text extension for inserting References

    Usage:
        .. bibliography:: <bibliography>
    """
    
    has_content = False
    required_arguments = 0

    def run(self):
        """ Required by the Directive interface. Create docutils nodes """
        
        text = "".join( biblio(self.state.document) )
        text = "<div class='bib'>%s</div>" % text
        return [nodes.raw('', text, format='html')]

