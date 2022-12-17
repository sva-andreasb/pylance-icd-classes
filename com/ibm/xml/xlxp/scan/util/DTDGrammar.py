def ():
    '''returns DTDGrammar\n\n
    (final DataBufferFactory dataBufferFactory, final SymbolTable fSymbolTable)\n
    '''
def reset():
    '''returns None\n\n
    reset(final boolean b)\n
    '''
def getEntityDeclPool():
    '''returns EntityDeclPool\n\n
    getEntityDeclPool()\n
    '''
def getStringBuffer():
    '''returns XMLStringBuffer\n\n
    getStringBuffer()\n
    '''
def setDescription():
    '''returns None\n\n
    setDescription(final int fRootElementTypeHandle, final int fPublicIDHandle, final int fSystemIDHandle)\n
    '''
def addGrammarToCache():
    '''returns None\n\n
    addGrammarToCache(final DTDGrammarCache dtdGrammarCache)\n
    '''
def hasElementContentElements():
    '''returns boolean\n\n
    hasElementContentElements()\n
    '''
def hasElementContent():
    '''returns boolean\n\n
    hasElementContent(final int n)\n
    '''
def setElementContentElement():
    '''returns None\n\n
    setElementContentElement(final int n)\n
    '''
def hasAttDefs():
    '''returns boolean\n\n
    hasAttDefs()\n
    '''
def addDefaultAttributes():
    '''returns None\n\n
    addDefaultAttributes(final DTDScannerHelper dtdScannerHelper, final QName qName, final NSDeclList list, final AttrList list2, final boolean b, final boolean b2)\n
    '''
def attDefAttrName():
    '''returns QName\n\n
    attDefAttrName(final int n)\n
    '''
def attDefAttValue():
    '''returns XMLString\n\n
    attDefAttValue(final int n)\n
    '''
def lookupAttDef():
    '''returns int\n\n
    lookupAttDef(final QName qName, final QName qName2)\n
    '''
def startAttDef():
    '''returns None\n\n
    startAttDef(final QName qName, final XMLString xmlString)\n
    '''
def enumerationType():
    '''returns None\n\n
    enumerationType(final XMLString xmlString, final ErrorReporter errorReporter)\n
    '''
def saveAttDef():
    '''returns None\n\n
    saveAttDef(final QName qName, final QName qName2, final XMLString xmlString, final XMLString xmlString2, final XMLString xmlString3, final boolean b, final ErrorReporter errorReporter, final boolean b2)\n
    '''
