def setDocumentHandler():
    '''returns None\n\n
    setDocumentHandler(final XMLDocumentHandler handler)\n
    '''
def getDocumentHandler():
    '''returns XMLDocumentHandler\n\n
    getDocumentHandler()\n
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
    startDocument(final XMLLocator locator, final String encoding, final NamespaceContext nscontext, final Augmentations augs)\n
    startDocument(final XMLLocator locator, final String encoding, final Augmentations augs)\n
    '''
def xmlDecl():
    '''returns None\n\n
    xmlDecl(final String version, final String encoding, final String standalone, final Augmentations augs)\n
    '''
def doctypeDecl():
    '''returns None\n\n
    doctypeDecl(final String root, final String publicId, final String systemId, final Augmentations augs)\n
    '''
def comment():
    '''returns None\n\n
    comment(final XMLString text, final Augmentations augs)\n
    '''
def processingInstruction():
    '''returns None\n\n
    processingInstruction(final String target, final XMLString data, final Augmentations augs)\n
    '''
def startElement():
    '''returns None\n\n
    startElement(final QName element, final XMLAttributes attributes, final Augmentations augs)\n
    '''
def emptyElement():
    '''returns None\n\n
    emptyElement(final QName element, final XMLAttributes attributes, final Augmentations augs)\n
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
def startPrefixMapping():
    '''returns None\n\n
    startPrefixMapping(final String prefix, final String uri, final Augmentations augs)\n
    '''
def endPrefixMapping():
    '''returns None\n\n
    endPrefixMapping(final String prefix, final Augmentations augs)\n
    '''
def getRecognizedFeatures():
    '''returns String[]\n\n
    getRecognizedFeatures()\n
    '''
def getFeatureDefault():
    '''returns Boolean\n\n
    getFeatureDefault(final String featureId)\n
    '''
def getRecognizedProperties():
    '''returns String[]\n\n
    getRecognizedProperties()\n
    '''
def getPropertyDefault():
    '''returns Object\n\n
    getPropertyDefault(final String propertyId)\n
    '''
def reset():
    '''returns None\n\n
    reset(final XMLComponentManager componentManager)\n
    '''
def setFeature():
    '''returns None\n\n
    setFeature(final String featureId, final boolean state)\n
    '''
def setProperty():
    '''returns None\n\n
    setProperty(final String propertyId, final Object value)\n
    '''
