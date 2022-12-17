def ():
    '''returns XMLDTDProcessor\n\n
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
def setDTDHandler():
    '''returns None\n\n
    setDTDHandler(final XMLDTDHandler fdtdHandler)\n
    '''
def getDTDHandler():
    '''returns XMLDTDHandler\n\n
    getDTDHandler()\n
    '''
def setDTDContentModelHandler():
    '''returns None\n\n
    setDTDContentModelHandler(final XMLDTDContentModelHandler fdtdContentModelHandler)\n
    '''
def getDTDContentModelHandler():
    '''returns XMLDTDContentModelHandler\n\n
    getDTDContentModelHandler()\n
    '''
def startExternalSubset():
    '''returns None\n\n
    startExternalSubset(final XMLResourceIdentifier xmlResourceIdentifier, final Augmentations augmentations)\n
    '''
def endExternalSubset():
    '''returns None\n\n
    endExternalSubset(final Augmentations augmentations)\n
    '''
def comment():
    '''returns None\n\n
    comment(final XMLString xmlString, final Augmentations augmentations)\n
    '''
def processingInstruction():
    '''returns None\n\n
    processingInstruction(final String s, final XMLString xmlString, final Augmentations augmentations)\n
    '''
def startDTD():
    '''returns None\n\n
    startDTD(final XMLLocator xmlLocator, final Augmentations augmentations)\n
    '''
def ignoredCharacters():
    '''returns None\n\n
    ignoredCharacters(final XMLString xmlString, final Augmentations augmentations)\n
    '''
def textDecl():
    '''returns None\n\n
    textDecl(final String s, final String s2, final Augmentations augmentations)\n
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
def startAttlist():
    '''returns None\n\n
    startAttlist(final String s, final Augmentations augmentations)\n
    '''
def attributeDecl():
    '''returns None\n\n
    attributeDecl(final String s, final String value, final String s2, final String[] array, final String s3, final XMLString xmlString, final XMLString xmlString2, final Augmentations augmentations)\n
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
    unparsedEntityDecl(final String key, final XMLResourceIdentifier xmlResourceIdentifier, final String value, final Augmentations augmentations)\n
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
def setDTDContentModelSource():
    '''returns None\n\n
    setDTDContentModelSource(final XMLDTDContentModelSource fdtdContentModelSource)\n
    '''
def getDTDContentModelSource():
    '''returns XMLDTDContentModelSource\n\n
    getDTDContentModelSource()\n
    '''
def startContentModel():
    '''returns None\n\n
    startContentModel(final String fdtdElementDeclName, final Augmentations augmentations)\n
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
