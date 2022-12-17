TOP_LEVEL_SCOPE = "int  -1"
def ():
    '''returns ChildrenList\n\n
    (final SymbolTable fSymbolTable, final XMLDTDDescription fGrammarDescription)\n
    ()\n
    '''
def getGrammarDescription():
    '''returns XMLGrammarDescription\n\n
    getGrammarDescription()\n
    '''
def getElementDeclIsExternal():
    '''returns boolean\n\n
    getElementDeclIsExternal(final int n)\n
    '''
def getAttributeDeclIsExternal():
    '''returns boolean\n\n
    getAttributeDeclIsExternal(final int n)\n
    '''
def getAttributeDeclIndex():
    '''returns int\n\n
    getAttributeDeclIndex(final int n, final String s)\n
    '''
def startDTD():
    '''returns None\n\n
    startDTD(final XMLLocator xmlLocator, final Augmentations augmentations)\n
    '''
def startParameterEntity():
    '''returns None\n\n
    startParameterEntity(final String s, final XMLResourceIdentifier xmlResourceIdentifier, final String s2, final Augmentations augmentations)\n
    '''
def startExternalSubset():
    '''returns None\n\n
    startExternalSubset(final XMLResourceIdentifier xmlResourceIdentifier, final Augmentations augmentations)\n
    '''
def endParameterEntity():
    '''returns None\n\n
    endParameterEntity(final String s, final Augmentations augmentations)\n
    '''
def endExternalSubset():
    '''returns None\n\n
    endExternalSubset(final Augmentations augmentations)\n
    '''
def elementDecl():
    '''returns None\n\n
    elementDecl(final String s, final String s2, final Augmentations augmentations)\n
    '''
def attributeDecl():
    '''returns None\n\n
    attributeDecl(final String s, final String s2, final String str, final String[] enumeration, final String s3, final XMLString xmlString, final XMLString xmlString2, final Augmentations augmentations)\n
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
def setDTDSource():
    '''returns None\n\n
    setDTDSource(final XMLDTDSource fdtdSource)\n
    '''
def getDTDSource():
    '''returns XMLDTDSource\n\n
    getDTDSource()\n
    '''
def textDecl():
    '''returns None\n\n
    textDecl(final String s, final String s2, final Augmentations augmentations)\n
    '''
def comment():
    '''returns None\n\n
    comment(final XMLString xmlString, final Augmentations augmentations)\n
    '''
def processingInstruction():
    '''returns None\n\n
    processingInstruction(final String s, final XMLString xmlString, final Augmentations augmentations)\n
    '''
def startAttlist():
    '''returns None\n\n
    startAttlist(final String s, final Augmentations augmentations)\n
    '''
def endAttlist():
    '''returns None\n\n
    endAttlist(final Augmentations augmentations)\n
    '''
def startConditional():
    '''returns None\n\n
    startConditional(final short n, final Augmentations augmentations)\n
    '''
def ignoredCharacters():
    '''returns None\n\n
    ignoredCharacters(final XMLString xmlString, final Augmentations augmentations)\n
    '''
def endConditional():
    '''returns None\n\n
    endConditional(final Augmentations augmentations)\n
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
    startContentModel(final String key, final Augmentations augmentations)\n
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
def any():
    '''returns None\n\n
    any(final Augmentations augmentations)\n
    '''
def empty():
    '''returns None\n\n
    empty(final Augmentations augmentations)\n
    '''
def endContentModel():
    '''returns None\n\n
    endContentModel(final Augmentations augmentations)\n
    '''
def isNamespaceAware():
    '''returns boolean\n\n
    isNamespaceAware()\n
    '''
def getSymbolTable():
    '''returns SymbolTable\n\n
    getSymbolTable()\n
    '''
def getFirstElementDeclIndex():
    '''returns int\n\n
    getFirstElementDeclIndex()\n
    '''
def getNextElementDeclIndex():
    '''returns int\n\n
    getNextElementDeclIndex(final int n)\n
    '''
def getElementDeclIndex():
    '''returns int\n\n
    getElementDeclIndex(final String s)\n
    getElementDeclIndex(final QName qName)\n
    '''
def getContentSpecType():
    '''returns short\n\n
    getContentSpecType(final int n)\n
    '''
def getElementDecl():
    '''returns boolean\n\n
    getElementDecl(final int n, final XMLElementDecl xmlElementDecl)\n
    '''
def getFirstAttributeDeclIndex():
    '''returns int\n\n
    getFirstAttributeDeclIndex(final int n)\n
    '''
def getNextAttributeDeclIndex():
    '''returns int\n\n
    getNextAttributeDeclIndex(final int n)\n
    '''
def getAttributeDecl():
    '''returns boolean\n\n
    getAttributeDecl(final int n, final XMLAttributeDecl xmlAttributeDecl)\n
    '''
def isCDATAAttribute():
    '''returns boolean\n\n
    isCDATAAttribute(final QName qName, final QName qName2)\n
    '''
def getEntityDeclIndex():
    '''returns int\n\n
    getEntityDeclIndex(final String s)\n
    '''
def getEntityDecl():
    '''returns boolean\n\n
    getEntityDecl(final int n, final XMLEntityDecl xmlEntityDecl)\n
    '''
def getNotationDeclIndex():
    '''returns int\n\n
    getNotationDeclIndex(final String s)\n
    '''
def getNotationDecl():
    '''returns boolean\n\n
    getNotationDecl(final int n, final XMLNotationDecl xmlNotationDecl)\n
    '''
def getContentSpec():
    '''returns boolean\n\n
    getContentSpec(final int n, final XMLContentSpec xmlContentSpec)\n
    '''
def getContentSpecIndex():
    '''returns int\n\n
    getContentSpecIndex(final int n)\n
    '''
def getContentSpecAsString():
    '''returns String\n\n
    getContentSpecAsString(final int n)\n
    '''
def printElements():
    '''returns None\n\n
    printElements()\n
    '''
def printAttributes():
    '''returns None\n\n
    printAttributes(final int i)\n
    '''
def isEntityDeclared():
    '''returns boolean\n\n
    isEntityDeclared(final String s)\n
    '''
def isEntityUnparsed():
    '''returns boolean\n\n
    isEntityUnparsed(final String s)\n
    '''
def put():
    '''returns None\n\n
    put(final String s, final int n)\n
    '''
def get():
    '''returns int\n\n
    get(final String s)\n
    '''
def hash():
    '''returns int\n\n
    hash(final String s)\n
    '''
