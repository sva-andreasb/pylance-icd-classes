ERROR_REPORTER = "String  \"http://apache.org/xml/properties/internal/error-reporter\""
GENERATE_SYNTHETIC_ANNOTATION = "String  \"http://apache.org/xml/features/generate-synthetic-annotations\""
def ():
    '''returns BooleanStack\n\n
    (final XMLParserConfiguration config)\n
    ()\n
    '''
def startDocument():
    '''returns None\n\n
    startDocument(final XMLLocator fLocator, final String s, final NamespaceContext fNamespaceContext, final Augmentations augmentations)\n
    '''
def endDocument():
    '''returns None\n\n
    endDocument(final Augmentations augmentations)\n
    '''
def comment():
    '''returns None\n\n
    comment(final XMLString xmlString, final Augmentations augmentations)\n
    '''
def processingInstruction():
    '''returns None\n\n
    processingInstruction(final String s, final XMLString xmlString, final Augmentations augmentations)\n
    '''
def characters():
    '''returns None\n\n
    characters(final XMLString xmlString, final Augmentations augmentations)\n
    '''
def startElement():
    '''returns None\n\n
    startElement(final QName qName, final XMLAttributes xmlAttributes, final Augmentations augmentations)\n
    '''
def emptyElement():
    '''returns None\n\n
    emptyElement(final QName qName, final XMLAttributes xmlAttributes, final Augmentations augmentations)\n
    '''
def endElement():
    '''returns None\n\n
    endElement(final QName qName, final Augmentations augmentations)\n
    '''
def ignorableWhitespace():
    '''returns None\n\n
    ignorableWhitespace(final XMLString xmlString, final Augmentations augmentations)\n
    '''
def startCDATA():
    '''returns None\n\n
    startCDATA(final Augmentations augmentations)\n
    '''
def endCDATA():
    '''returns None\n\n
    endCDATA(final Augmentations augmentations)\n
    '''
def getDocument():
    '''returns Document\n\n
    getDocument()\n
    '''
def setFeature():
    '''returns None\n\n
    setFeature(final String s, final boolean b)\n
    '''
def getFeature():
    '''returns boolean\n\n
    getFeature(final String s)\n
    '''
def setProperty():
    '''returns None\n\n
    setProperty(final String s, final Object o)\n
    '''
def getProperty():
    '''returns Object\n\n
    getProperty(final String s)\n
    '''
def setEntityResolver():
    '''returns None\n\n
    setEntityResolver(final XMLEntityResolver entityResolver)\n
    '''
def parse():
    '''returns None\n\n
    parse(final XMLInputSource xmlInputSource)\n
    '''
def reset():
    '''returns None\n\n
    reset()\n
    '''
def resetNodePool():
    '''returns None\n\n
    resetNodePool()\n
    '''
def size():
    '''returns int\n\n
    size()\n
    '''
def push():
    '''returns None\n\n
    push(final boolean b)\n
    '''
def pop():
    '''returns boolean\n\n
    pop()\n
    '''
def clear():
    '''returns None\n\n
    clear()\n
    '''
