def DOMFragmentParser():
    '''public DOMFragmentParser()
    '''
def parse():
    '''public void parse(final String systemId, final DocumentFragment fragment)
    public void parse(final InputSource source, final DocumentFragment fragment)
    '''
def setErrorHandler():
    '''public void setErrorHandler(final ErrorHandler errorHandler)
    '''
def getErrorHandler():
    '''public ErrorHandler getErrorHandler()
    '''
def setFeature():
    '''public void setFeature(final String featureId, final boolean state)
    '''
def getFeature():
    '''public boolean getFeature(final String featureId)
    '''
def setProperty():
    '''public void setProperty(final String propertyId, final Object value)
    '''
def getProperty():
    '''public Object getProperty(final String propertyId)
    '''
def setDocumentSource():
    '''public void setDocumentSource(final XMLDocumentSource source)
    '''
def getDocumentSource():
    '''public XMLDocumentSource getDocumentSource()
    '''
def startDocument():
    '''public void startDocument(final XMLLocator locator, final String encoding, final Augmentations augs)
    public void startDocument(final XMLLocator locator, final String encoding, final NamespaceContext nscontext, final Augmentations augs)
    '''
def xmlDecl():
    '''public void xmlDecl(final String version, final String encoding, final String standalone, final Augmentations augs)
    '''
def doctypeDecl():
    '''public void doctypeDecl(final String root, final String pubid, final String sysid, final Augmentations augs)
    '''
def processingInstruction():
    '''public void processingInstruction(final String target, final XMLString data, final Augmentations augs)
    '''
def comment():
    '''public void comment(final XMLString text, final Augmentations augs)
    '''
def startPrefixMapping():
    '''public void startPrefixMapping(final String prefix, final String uri, final Augmentations augs)
    '''
def endPrefixMapping():
    '''public void endPrefixMapping(final String prefix, final Augmentations augs)
    '''
def startElement():
    '''public void startElement(final QName element, final XMLAttributes attrs, final Augmentations augs)
    '''
def emptyElement():
    '''public void emptyElement(final QName element, final XMLAttributes attrs, final Augmentations augs)
    '''
def characters():
    '''public void characters(final XMLString text, final Augmentations augs)
    '''
def ignorableWhitespace():
    '''public void ignorableWhitespace(final XMLString text, final Augmentations augs)
    '''
def startGeneralEntity():
    '''public void startGeneralEntity(final String name, final XMLResourceIdentifier id, final String encoding, final Augmentations augs)
    '''
def textDecl():
    '''public void textDecl(final String version, final String encoding, final Augmentations augs)
    '''
def endGeneralEntity():
    '''public void endGeneralEntity(final String name, final Augmentations augs)
    '''
def startCDATA():
    '''public void startCDATA(final Augmentations augs)
    '''
def endCDATA():
    '''public void endCDATA(final Augmentations augs)
    '''
def endElement():
    '''public void endElement(final QName element, final Augmentations augs)
    '''
def endDocument():
    '''public void endDocument(final Augmentations augs)
    '''
