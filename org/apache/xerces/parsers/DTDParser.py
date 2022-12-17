def ():
    '''returns DTDParser\n\n
    (final SymbolTable symbolTable)\n
    '''
def getDTDGrammar():
    '''returns DTDGrammar\n\n
    getDTDGrammar()\n
    '''
def startEntity():
    '''returns None\n\n
    startEntity(final String s, final String s2, final String s3, final String s4)\n
    '''
def textDecl():
    '''returns None\n\n
    textDecl(final String s, final String s2)\n
    '''
def startDTD():
    '''returns None\n\n
    startDTD(final XMLLocator xmlLocator, final Augmentations augmentations)\n
    '''
def comment():
    '''returns None\n\n
    comment(final XMLString xmlString, final Augmentations augmentations)\n
    '''
def processingInstruction():
    '''returns None\n\n
    processingInstruction(final String s, final XMLString xmlString, final Augmentations augmentations)\n
    '''
def startExternalSubset():
    '''returns None\n\n
    startExternalSubset(final XMLResourceIdentifier xmlResourceIdentifier, final Augmentations augmentations)\n
    '''
def endExternalSubset():
    '''returns None\n\n
    endExternalSubset(final Augmentations augmentations)\n
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
def endEntity():
    '''returns None\n\n
    endEntity(final String s, final Augmentations augmentations)\n
    '''
def startContentModel():
    '''returns None\n\n
    startContentModel(final String s, final short n)\n
    '''
def mixedElement():
    '''returns None\n\n
    mixedElement(final String s)\n
    '''
def childrenStartGroup():
    '''returns None\n\n
    childrenStartGroup()\n
    '''
def childrenElement():
    '''returns None\n\n
    childrenElement(final String s)\n
    '''
def childrenSeparator():
    '''returns None\n\n
    childrenSeparator(final short n)\n
    '''
def childrenOccurrence():
    '''returns None\n\n
    childrenOccurrence(final short n)\n
    '''
def childrenEndGroup():
    '''returns None\n\n
    childrenEndGroup()\n
    '''
def endContentModel():
    '''returns None\n\n
    endContentModel()\n
    '''
