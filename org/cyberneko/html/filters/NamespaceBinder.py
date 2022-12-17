XHTML_1_0_URI = "String  \"http://www.w3.org/1999/xhtml\""
XML_URI = "String  \"http://www.w3.org/XML/1998/namespace\""
XMLNS_URI = "String  \"http://www.w3.org/2000/xmlns/\""
def ():
    '''returns Entry\n\n
    ()\n
    ()\n
    (final String prefix, final String uri)\n
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
    reset(final XMLComponentManager manager)\n
    reset()\n
    '''
def startDocument():
    '''returns None\n\n
    startDocument(final XMLLocator locator, final String encoding, final NamespaceContext nscontext, final Augmentations augs)\n
    '''
def startElement():
    '''returns None\n\n
    startElement(final QName element, final XMLAttributes attrs, final Augmentations augs)\n
    '''
def emptyElement():
    '''returns None\n\n
    emptyElement(final QName element, final XMLAttributes attrs, final Augmentations augs)\n
    '''
def endElement():
    '''returns None\n\n
    endElement(final QName element, final Augmentations augs)\n
    '''
def getURI():
    '''returns String\n\n
    getURI(final String prefix)\n
    '''
def getDeclaredPrefixCount():
    '''returns int\n\n
    getDeclaredPrefixCount()\n
    '''
def getDeclaredPrefixAt():
    '''returns String\n\n
    getDeclaredPrefixAt(final int index)\n
    '''
def getParentContext():
    '''returns NamespaceContext\n\n
    getParentContext()\n
    '''
def pushContext():
    '''returns None\n\n
    pushContext()\n
    '''
def popContext():
    '''returns None\n\n
    popContext()\n
    '''
def declarePrefix():
    '''returns boolean\n\n
    declarePrefix(final String prefix, final String uri)\n
    '''
def getPrefix():
    '''returns String\n\n
    getPrefix(final String uri)\n
    '''
def getAllPrefixes():
    '''returns Enumeration\n\n
    getAllPrefixes()\n
    '''
