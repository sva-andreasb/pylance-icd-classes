def ():
    '''returns XMLDTDValidator\n\n
    ()\n
    '''
def reset():
    '''returns None\n\n
    reset(final XMLComponentManager xmlComponentManager)\n
    '''
def getRecognizedFeatures():
    '''returns String[]\n\n
    getRecognizedFeatures()\n
    '''
def setFeature():
    '''returns None\n\n
    setFeature(final String s, final boolean b)\n
    '''
def getRecognizedProperties():
    '''returns String[]\n\n
    getRecognizedProperties()\n
    '''
def setProperty():
    '''returns None\n\n
    setProperty(final String s, final Object o)\n
    '''
def getFeatureDefault():
    '''returns Boolean\n\n
    getFeatureDefault(final String anObject)\n
    '''
def getPropertyDefault():
    '''returns Object\n\n
    getPropertyDefault(final String anObject)\n
    '''
def setDocumentHandler():
    '''returns None\n\n
    setDocumentHandler(final XMLDocumentHandler fDocumentHandler)\n
    '''
def getDocumentHandler():
    '''returns XMLDocumentHandler\n\n
    getDocumentHandler()\n
    '''
def setDocumentSource():
    '''returns None\n\n
    setDocumentSource(final XMLDocumentSource fDocumentSource)\n
    '''
def getDocumentSource():
    '''returns XMLDocumentSource\n\n
    getDocumentSource()\n
    '''
def startDocument():
    '''returns None\n\n
    startDocument(final XMLLocator fDocLocation, final String s, final NamespaceContext fNamespaceContext, final Augmentations augmentations)\n
    '''
def xmlDecl():
    '''returns None\n\n
    xmlDecl(final String s, final String s2, final String s3, final Augmentations augmentations)\n
    '''
def doctypeDecl():
    '''returns None\n\n
    doctypeDecl(final String s, final String s2, final String s3, final Augmentations augmentations)\n
    '''
def startElement():
    '''returns None\n\n
    startElement(final QName qName, final XMLAttributes xmlAttributes, final Augmentations augmentations)\n
    '''
def emptyElement():
    '''returns None\n\n
    emptyElement(final QName qName, final XMLAttributes xmlAttributes, final Augmentations augmentations)\n
    '''
def characters():
    '''returns None\n\n
    characters(final XMLString xmlString, final Augmentations augmentations)\n
    '''
def ignorableWhitespace():
    '''returns None\n\n
    ignorableWhitespace(final XMLString xmlString, final Augmentations augmentations)\n
    '''
def endElement():
    '''returns None\n\n
    endElement(final QName qName, final Augmentations augmentations)\n
    '''
def startCDATA():
    '''returns None\n\n
    startCDATA(final Augmentations augmentations)\n
    '''
def endCDATA():
    '''returns None\n\n
    endCDATA(final Augmentations augmentations)\n
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
def startGeneralEntity():
    '''returns None\n\n
    startGeneralEntity(final String s, final XMLResourceIdentifier xmlResourceIdentifier, final String s2, final Augmentations augmentations)\n
    '''
def endGeneralEntity():
    '''returns None\n\n
    endGeneralEntity(final String s, final Augmentations augmentations)\n
    '''
def textDecl():
    '''returns None\n\n
    textDecl(final String s, final String s2, final Augmentations augmentations)\n
    '''
def characterData():
    '''returns boolean\n\n
    characterData(final String s, final Augmentations augmentations)\n
    '''
