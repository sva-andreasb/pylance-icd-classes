def ():
    '''returns DOMFragmentParser\n\n
    ()\n
    '''
def parse():
    '''returns None\n\n
    parse(final String systemId, final DocumentFragment fragment)\n
    parse(final InputSource source, final DocumentFragment fragment)\n
    '''
def setErrorHandler():
    '''returns None\n\n
    setErrorHandler(final ErrorHandler errorHandler)\n
    '''
def getErrorHandler():
    '''returns ErrorHandler\n\n
    getErrorHandler()\n
    '''
def setFeature():
    '''returns None\n\n
    setFeature(final String featureId, final boolean state)\n
    '''
def getFeature():
    '''returns boolean\n\n
    getFeature(final String featureId)\n
    '''
def setProperty():
    '''returns None\n\n
    setProperty(final String propertyId, final Object value)\n
    '''
def getProperty():
    '''returns Object\n\n
    getProperty(final String propertyId)\n
    '''
def setDocumentSource():
    '''returns None\n\n
    setDocumentSource(final XMLDocumentSource source)\n
    '''
def getDocumentSource():
    '''returns XMLDocumentSource\n\n
    getDocumentSource()\n
    '''
def startDocument():
    '''returns None\n\n
    startDocument(final XMLLocator locator, final String encoding, final Augmentations augs)\n
    startDocument(final XMLLocator locator, final String encoding, final NamespaceContext nscontext, final Augmentations augs)\n
    '''
def xmlDecl():
    '''returns None\n\n
    xmlDecl(final String version, final String encoding, final String standalone, final Augmentations augs)\n
    '''
def doctypeDecl():
    '''returns None\n\n
    doctypeDecl(final String root, final String pubid, final String sysid, final Augmentations augs)\n
    '''
def processingInstruction():
    '''returns None\n\n
    processingInstruction(final String target, final XMLString data, final Augmentations augs)\n
    '''
def comment():
    '''returns None\n\n
    comment(final XMLString text, final Augmentations augs)\n
    '''
def startPrefixMapping():
    '''returns None\n\n
    startPrefixMapping(final String prefix, final String uri, final Augmentations augs)\n
    '''
def endPrefixMapping():
    '''returns None\n\n
    endPrefixMapping(final String prefix, final Augmentations augs)\n
    '''
def startElement():
    '''returns None\n\n
    startElement(final QName element, final XMLAttributes attrs, final Augmentations augs)\n
    '''
def emptyElement():
    '''returns None\n\n
    emptyElement(final QName element, final XMLAttributes attrs, final Augmentations augs)\n
    '''
def characters():
    '''returns None\n\n
    characters(final XMLString text, final Augmentations augs)\n
    '''
def ignorableWhitespace():
    '''returns None\n\n
    ignorableWhitespace(final XMLString text, final Augmentations augs)\n
    '''
def startGeneralEntity():
    '''returns None\n\n
    startGeneralEntity(final String name, final XMLResourceIdentifier id, final String encoding, final Augmentations augs)\n
    '''
def textDecl():
    '''returns None\n\n
    textDecl(final String version, final String encoding, final Augmentations augs)\n
    '''
def endGeneralEntity():
    '''returns None\n\n
    endGeneralEntity(final String name, final Augmentations augs)\n
    '''
def startCDATA():
    '''returns None\n\n
    startCDATA(final Augmentations augs)\n
    '''
def endCDATA():
    '''returns None\n\n
    endCDATA(final Augmentations augs)\n
    '''
def endElement():
    '''returns None\n\n
    endElement(final QName element, final Augmentations augs)\n
    '''
def endDocument():
    '''returns None\n\n
    endDocument(final Augmentations augs)\n
    '''
