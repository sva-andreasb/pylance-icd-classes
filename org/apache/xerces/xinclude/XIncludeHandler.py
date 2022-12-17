XINCLUDE_DEFAULT_CONFIGURATION = "String  \"org.apache.xerces.parsers.XIncludeParserConfiguration\""
HTTP_ACCEPT = "String  \"Accept\""
HTTP_ACCEPT_LANGUAGE = "String  \"Accept-Language\""
XPOINTER = "String  \"xpointer\""
CURRENT_BASE_URI = "String  \"currentBaseURI\""
def ():
    '''returns XIncludeHandler\n\n
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
    setFeature(final String s, final boolean fSendUEAndNotationEvents)\n
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
    setDocumentHandler(final XMLDocumentHandler documentHandler)\n
    '''
def getDocumentHandler():
    '''returns XMLDocumentHandler\n\n
    getDocumentHandler()\n
    '''
def startDocument():
    '''returns None\n\n
    startDocument(final XMLLocator xmlLocator, final String s, final NamespaceContext namespaceContext, Augmentations augmentations)\n
    '''
def xmlDecl():
    '''returns None\n\n
    xmlDecl(final String anObject, final String s, final String s2, final Augmentations augmentations)\n
    '''
def doctypeDecl():
    '''returns None\n\n
    doctypeDecl(final String s, final String s2, final String s3, final Augmentations augmentations)\n
    '''
def comment():
    '''returns None\n\n
    comment(final XMLString xmlString, Augmentations modifyAugmentations)\n
    '''
def processingInstruction():
    '''returns None\n\n
    processingInstruction(final String s, final XMLString xmlString, Augmentations modifyAugmentations)\n
    '''
def startElement():
    '''returns None\n\n
    startElement(final QName qName, XMLAttributes xmlAttributes, Augmentations augmentations)\n
    '''
def emptyElement():
    '''returns None\n\n
    emptyElement(final QName qName, XMLAttributes xmlAttributes, Augmentations augmentations)\n
    '''
def endElement():
    '''returns None\n\n
    endElement(final QName qName, final Augmentations augmentations)\n
    '''
def startGeneralEntity():
    '''returns None\n\n
    startGeneralEntity(final String s, final XMLResourceIdentifier xmlResourceIdentifier, final String s2, final Augmentations augmentations)\n
    '''
def textDecl():
    '''returns None\n\n
    textDecl(final String s, final String s2, final Augmentations augmentations)\n
    '''
def endGeneralEntity():
    '''returns None\n\n
    endGeneralEntity(final String s, final Augmentations augmentations)\n
    '''
def characters():
    '''returns None\n\n
    characters(final XMLString xmlString, Augmentations modifyAugmentations)\n
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
def endDocument():
    '''returns None\n\n
    endDocument(final Augmentations augmentations)\n
    '''
def setDocumentSource():
    '''returns None\n\n
    setDocumentSource(final XMLDocumentSource fDocumentSource)\n
    '''
def getDocumentSource():
    '''returns XMLDocumentSource\n\n
    getDocumentSource()\n
    '''
def attributeDecl():
    '''returns None\n\n
    attributeDecl(final String s, final String s2, final String s3, final String[] array, final String s4, final XMLString xmlString, final XMLString xmlString2, final Augmentations augmentations)\n
    '''
def elementDecl():
    '''returns None\n\n
    elementDecl(final String s, final String s2, final Augmentations augmentations)\n
    '''
def endAttlist():
    '''returns None\n\n
    endAttlist(final Augmentations augmentations)\n
    '''
def endConditional():
    '''returns None\n\n
    endConditional(final Augmentations augmentations)\n
    '''
def endDTD():
    '''returns None\n\n
    endDTD(final Augmentations augmentations)\n
    '''
def endExternalSubset():
    '''returns None\n\n
    endExternalSubset(final Augmentations augmentations)\n
    '''
def endParameterEntity():
    '''returns None\n\n
    endParameterEntity(final String s, final Augmentations augmentations)\n
    '''
def externalEntityDecl():
    '''returns None\n\n
    externalEntityDecl(final String s, final XMLResourceIdentifier xmlResourceIdentifier, final Augmentations augmentations)\n
    '''
def getDTDSource():
    '''returns XMLDTDSource\n\n
    getDTDSource()\n
    '''
def ignoredCharacters():
    '''returns None\n\n
    ignoredCharacters(final XMLString xmlString, final Augmentations augmentations)\n
    '''
def internalEntityDecl():
    '''returns None\n\n
    internalEntityDecl(final String s, final XMLString xmlString, final XMLString xmlString2, final Augmentations augmentations)\n
    '''
def notationDecl():
    '''returns None\n\n
    notationDecl(final String s, final XMLResourceIdentifier xmlResourceIdentifier, final Augmentations augmentations)\n
    '''
def setDTDSource():
    '''returns None\n\n
    setDTDSource(final XMLDTDSource fdtdSource)\n
    '''
def startAttlist():
    '''returns None\n\n
    startAttlist(final String s, final Augmentations augmentations)\n
    '''
def startConditional():
    '''returns None\n\n
    startConditional(final short n, final Augmentations augmentations)\n
    '''
def startDTD():
    '''returns None\n\n
    startDTD(final XMLLocator xmlLocator, final Augmentations augmentations)\n
    '''
def startExternalSubset():
    '''returns None\n\n
    startExternalSubset(final XMLResourceIdentifier xmlResourceIdentifier, final Augmentations augmentations)\n
    '''
def startParameterEntity():
    '''returns None\n\n
    startParameterEntity(final String s, final XMLResourceIdentifier xmlResourceIdentifier, final String s2, final Augmentations augmentations)\n
    '''
def unparsedEntityDecl():
    '''returns None\n\n
    unparsedEntityDecl(final String s, final XMLResourceIdentifier xmlResourceIdentifier, final String s2, final Augmentations augmentations)\n
    '''
def getDTDHandler():
    '''returns XMLDTDHandler\n\n
    getDTDHandler()\n
    '''
def setDTDHandler():
    '''returns None\n\n
    setDTDHandler(final XMLDTDHandler fdtdHandler)\n
    '''
def restoreLanguage():
    '''returns String\n\n
    restoreLanguage()\n
    '''
def getBaseURI():
    '''returns String\n\n
    getBaseURI(final int n)\n
    '''
def getLanguage():
    '''returns String\n\n
    getLanguage(final int n)\n
    '''
def getRelativeURI():
    '''returns String\n\n
    getRelativeURI(final int n)\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object o)\n
    equals(final Object o)\n
    '''
def isDuplicate():
    '''returns boolean\n\n
    isDuplicate(final Object o)\n
    isDuplicate(final Object o)\n
    '''
