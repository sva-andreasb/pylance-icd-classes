def startDocument():
    '''returns None\n\n
    startDocument(final XMLLocator xmlLocator, final String s, final NamespaceContext fNamespaceContext, final Augmentations augmentations)\n
    '''
def xmlDecl():
    '''returns None\n\n
    xmlDecl(final String fVersion, final String s, final String anObject, final Augmentations augmentations)\n
    '''
def doctypeDecl():
    '''returns None\n\n
    doctypeDecl(final String s, final String s2, final String s3, final Augmentations augmentations)\n
    '''
def startGeneralEntity():
    '''returns None\n\n
    startGeneralEntity(final String s, final XMLResourceIdentifier xmlResourceIdentifier, final String s2, final Augmentations augmentations)\n
    '''
def endGeneralEntity():
    '''returns None\n\n
    endGeneralEntity(final String s, final Augmentations augmentations)\n
    '''
def startElement():
    '''returns None\n\n
    startElement(final QName qName, final XMLAttributes xmlAttributes, final Augmentations fAugmentations)\n
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
    endElement(final QName qName, final Augmentations fAugmentations)\n
    '''
def startCDATA():
    '''returns None\n\n
    startCDATA(final Augmentations augmentations)\n
    '''
def endCDATA():
    '''returns None\n\n
    endCDATA(final Augmentations augmentations)\n
    '''
def comment():
    '''returns None\n\n
    comment(final XMLString xmlString, final Augmentations augmentations)\n
    '''
def processingInstruction():
    '''returns None\n\n
    processingInstruction(final String s, final XMLString xmlString, final Augmentations augmentations)\n
    '''
def endDocument():
    '''returns None\n\n
    endDocument(final Augmentations augmentations)\n
    '''
def startExternalSubset():
    '''returns None\n\n
    startExternalSubset(final XMLResourceIdentifier xmlResourceIdentifier, final Augmentations augmentations)\n
    '''
def endExternalSubset():
    '''returns None\n\n
    endExternalSubset(final Augmentations augmentations)\n
    '''
def startParameterEntity():
    '''returns None\n\n
    startParameterEntity(final String s, final XMLResourceIdentifier xmlResourceIdentifier, final String s2, final Augmentations augmentations)\n
    '''
def endParameterEntity():
    '''returns None\n\n
    endParameterEntity(final String s, final Augmentations augmentations)\n
    '''
def elementDecl():
    '''returns None\n\n
    elementDecl(final String s, final String s2, final Augmentations augmentations)\n
    '''
def attributeDecl():
    '''returns None\n\n
    attributeDecl(final String str, final String str2, String string, final String[] array, final String s, final XMLString xmlString, final XMLString xmlString2, final Augmentations augmentations)\n
    '''
def internalEntityDecl():
    '''returns None\n\n
    internalEntityDecl(final String s, final XMLString xmlString, final XMLString xmlString2, final Augmentations augmentations)\n
    '''
def externalEntityDecl():
    '''returns None\n\n
    externalEntityDecl(final String s, final XMLResourceIdentifier xmlResourceIdentifier, final Augmentations augmentations)\n
    '''
def unparsedEntityDecl():
    '''returns None\n\n
    unparsedEntityDecl(final String s, final XMLResourceIdentifier xmlResourceIdentifier, final String s2, final Augmentations augmentations)\n
    '''
def notationDecl():
    '''returns None\n\n
    notationDecl(final String s, final XMLResourceIdentifier xmlResourceIdentifier, final Augmentations augmentations)\n
    '''
def endDTD():
    '''returns None\n\n
    endDTD(final Augmentations augmentations)\n
    '''
def parse():
    '''returns None\n\n
    parse(final String s)\n
    parse(final InputSource inputSource)\n
    '''
def setEntityResolver():
    '''returns None\n\n
    setEntityResolver(final EntityResolver entityResolver)\n
    '''
def getEntityResolver():
    '''returns EntityResolver\n\n
    getEntityResolver()\n
    '''
def setErrorHandler():
    '''returns None\n\n
    setErrorHandler(final ErrorHandler errorHandler)\n
    '''
def getErrorHandler():
    '''returns ErrorHandler\n\n
    getErrorHandler()\n
    '''
def setLocale():
    '''returns None\n\n
    setLocale(final Locale locale)\n
    '''
def setDTDHandler():
    '''returns None\n\n
    setDTDHandler(final DTDHandler fdtdHandler)\n
    '''
def setDocumentHandler():
    '''returns None\n\n
    setDocumentHandler(final DocumentHandler fDocumentHandler)\n
    '''
def setContentHandler():
    '''returns None\n\n
    setContentHandler(final ContentHandler fContentHandler)\n
    '''
def getContentHandler():
    '''returns ContentHandler\n\n
    getContentHandler()\n
    '''
def getDTDHandler():
    '''returns DTDHandler\n\n
    getDTDHandler()\n
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
def reset():
    '''returns None\n\n
    reset()\n
    '''
def getElementPSVI():
    '''returns ElementPSVI\n\n
    getElementPSVI()\n
    '''
def getAttributePSVI():
    '''returns AttributePSVI\n\n
    getAttributePSVI(final int n)\n
    '''
def getAttributePSVIByName():
    '''returns AttributePSVI\n\n
    getAttributePSVIByName(final String s, final String s2)\n
    '''
def setAttributes():
    '''returns None\n\n
    setAttributes(final XMLAttributes fAttributes)\n
    '''
def getLength():
    '''returns int\n\n
    getLength()\n
    '''
def getName():
    '''returns String\n\n
    getName(final int n)\n
    '''
def getQName():
    '''returns String\n\n
    getQName(final int n)\n
    '''
def getURI():
    '''returns String\n\n
    getURI(final int n)\n
    '''
def getLocalName():
    '''returns String\n\n
    getLocalName(final int n)\n
    '''
def getType():
    '''returns String\n\n
    getType(final int n)\n
    getType(final String s)\n
    getType(final String s, final String s2)\n
    '''
def getValue():
    '''returns String\n\n
    getValue(final int n)\n
    getValue(final String s)\n
    getValue(final String s, final String s2)\n
    '''
def getIndex():
    '''returns int\n\n
    getIndex(final String s)\n
    getIndex(final String s, final String s2)\n
    '''
def isDeclared():
    '''returns boolean\n\n
    isDeclared(final int index)\n
    isDeclared(final String s)\n
    isDeclared(final String s, final String s2)\n
    '''
def isSpecified():
    '''returns boolean\n\n
    isSpecified(final int index)\n
    isSpecified(final String s)\n
    isSpecified(final String s, final String s2)\n
    '''
def ():
    '''returns LocatorProxy\n\n
    (final XMLLocator fLocator)\n
    '''
def getPublicId():
    '''returns String\n\n
    getPublicId()\n
    '''
def getSystemId():
    '''returns String\n\n
    getSystemId()\n
    '''
def getLineNumber():
    '''returns int\n\n
    getLineNumber()\n
    '''
def getColumnNumber():
    '''returns int\n\n
    getColumnNumber()\n
    '''
def getXMLVersion():
    '''returns String\n\n
    getXMLVersion()\n
    '''
def getEncoding():
    '''returns String\n\n
    getEncoding()\n
    '''
