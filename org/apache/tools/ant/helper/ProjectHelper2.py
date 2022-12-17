REFID_TARGETS = "String  \"ant.targets\""
def canParseAntlibDescriptor():
    '''returns boolean\n\n
    canParseAntlibDescriptor(final Resource resource)\n
    '''
def parseAntlibDescriptor():
    '''returns UnknownElement\n\n
    parseAntlibDescriptor(final Project containingProject, final Resource resource)\n
    '''
def parseUnknownElement():
    '''returns UnknownElement\n\n
    parseUnknownElement(final Project project, final URL source)\n
    '''
def parse():
    '''returns None\n\n
    parse(final Project project, final Object source)\n
    parse(final Project project, final Object source, final RootHandler handler)\n
    '''
def onStartElement():
    '''returns None\n\n
    onStartElement(final String uri, final String tag, final String qname, final Attributes attrs, final AntXMLContext context)\n
    onStartElement(final String uri, final String tag, final String qname, final Attributes attrs, final AntXMLContext context)\n
    onStartElement(final String uri, final String tag, final String qname, final Attributes attrs, final AntXMLContext context)\n
    onStartElement(final String uri, final String tag, final String qname, final Attributes attrs, final AntXMLContext context)\n
    '''
def onStartChild():
    '''returns AntHandler\n\n
    onStartChild(final String uri, final String tag, final String qname, final Attributes attrs, final AntXMLContext context)\n
    onStartChild(final String uri, final String name, final String qname, final Attributes attrs, final AntXMLContext context)\n
    onStartChild(final String uri, final String name, final String qname, final Attributes attrs, final AntXMLContext context)\n
    onStartChild(final String uri, final String name, final String qname, final Attributes attrs, final AntXMLContext context)\n
    onStartChild(final String uri, final String tag, final String qname, final Attributes attrs, final AntXMLContext context)\n
    '''
def onEndChild():
    '''returns None\n\n
    onEndChild(final String uri, final String tag, final String qname, final AntXMLContext context)\n
    '''
def onEndElement():
    '''returns None\n\n
    onEndElement(final String uri, final String tag, final AntXMLContext context)\n
    onEndElement(final String uri, final String tag, final AntXMLContext context)\n
    onEndElement(final String uri, final String tag, final AntXMLContext context)\n
    '''
def characters():
    '''returns None\n\n
    characters(final char[] buf, final int start, final int count, final AntXMLContext context)\n
    characters(final char[] buf, final int start, final int count)\n
    characters(final char[] buf, final int start, final int count, final AntXMLContext context)\n
    '''
def ():
    '''returns RootHandler\n\n
    (final AntXMLContext context, final AntHandler rootHandler)\n
    '''
def getCurrentAntHandler():
    '''returns AntHandler\n\n
    getCurrentAntHandler()\n
    '''
def resolveEntity():
    '''returns InputSource\n\n
    resolveEntity(final String publicId, final String systemId)\n
    '''
def startElement():
    '''returns None\n\n
    startElement(final String uri, final String tag, final String qname, final Attributes attrs)\n
    '''
def setDocumentLocator():
    '''returns None\n\n
    setDocumentLocator(final org.xml.sax.Locator locator)\n
    '''
def endElement():
    '''returns None\n\n
    endElement(final String uri, final String name, final String qName)\n
    '''
def startPrefixMapping():
    '''returns None\n\n
    startPrefixMapping(final String prefix, final String uri)\n
    '''
def endPrefixMapping():
    '''returns None\n\n
    endPrefixMapping(final String prefix)\n
    '''
