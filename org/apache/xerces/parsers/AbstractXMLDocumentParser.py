def startDocument():
    '''returns None\n\n
    startDocument(final XMLLocator xmlLocator, final String s, final NamespaceContext namespaceContext, final Augmentations augmentations)\n
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
def comment():
    '''returns None\n\n
    comment(final XMLString xmlString, final Augmentations augmentations)\n
    '''
def processingInstruction():
    '''returns None\n\n
    processingInstruction(final String s, final XMLString xmlString, final Augmentations augmentations)\n
    '''
def setDocumentSource():
    '''returns None\n\n
    setDocumentSource(final XMLDocumentSource fDocumentSource)\n
    '''
def getDocumentSource():
    '''returns XMLDocumentSource\n\n
    getDocumentSource()\n
    '''
def startDTD():
    '''returns None\n\n
    startDTD(final XMLLocator xmlLocator, final Augmentations augmentations)\n
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
def ignoredCharacters():
    '''returns None\n\n
    ignoredCharacters(final XMLString xmlString, final Augmentations augmentations)\n
    '''
def elementDecl():
    '''returns None\n\n
    elementDecl(final String s, final String s2, final Augmentations augmentations)\n
    '''
def startAttlist():
    '''returns None\n\n
    startAttlist(final String s, final Augmentations augmentations)\n
    '''
def attributeDecl():
    '''returns None\n\n
    attributeDecl(final String s, final String s2, final String s3, final String[] array, final String s4, final XMLString xmlString, final XMLString xmlString2, final Augmentations augmentations)\n
    '''
def endAttlist():
    '''returns None\n\n
    endAttlist(final Augmentations augmentations)\n
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
def startConditional():
    '''returns None\n\n
    startConditional(final short n, final Augmentations augmentations)\n
    '''
def endConditional():
    '''returns None\n\n
    endConditional(final Augmentations augmentations)\n
    '''
def endDTD():
    '''returns None\n\n
    endDTD(final Augmentations augmentations)\n
    '''
def setDTDSource():
    '''returns None\n\n
    setDTDSource(final XMLDTDSource fdtdSource)\n
    '''
def getDTDSource():
    '''returns XMLDTDSource\n\n
    getDTDSource()\n
    '''
def startContentModel():
    '''returns None\n\n
    startContentModel(final String s, final Augmentations augmentations)\n
    '''
def any():
    '''returns None\n\n
    any(final Augmentations augmentations)\n
    '''
def empty():
    '''returns None\n\n
    empty(final Augmentations augmentations)\n
    '''
def startGroup():
    '''returns None\n\n
    startGroup(final Augmentations augmentations)\n
    '''
def pcdata():
    '''returns None\n\n
    pcdata(final Augmentations augmentations)\n
    '''
def element():
    '''returns None\n\n
    element(final String s, final Augmentations augmentations)\n
    '''
def separator():
    '''returns None\n\n
    separator(final short n, final Augmentations augmentations)\n
    '''
def occurrence():
    '''returns None\n\n
    occurrence(final short n, final Augmentations augmentations)\n
    '''
def endGroup():
    '''returns None\n\n
    endGroup(final Augmentations augmentations)\n
    '''
def endContentModel():
    '''returns None\n\n
    endContentModel(final Augmentations augmentations)\n
    '''
def setDTDContentModelSource():
    '''returns None\n\n
    setDTDContentModelSource(final XMLDTDContentModelSource fdtdContentModelSource)\n
    '''
def getDTDContentModelSource():
    '''returns XMLDTDContentModelSource\n\n
    getDTDContentModelSource()\n
    '''
