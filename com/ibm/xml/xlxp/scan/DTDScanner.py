SEPARATOR_CHOICE = "int  0"
SEPARATOR_SEQUENCE = "int  1"
OCCURRENCE_ZERO_OR_ONE = "int  0"
OCCURRENCE_ZERO_OR_MORE = "int  1"
OCCURRENCE_ONE_OR_MORE = "int  2"
def ():
    '''returns DTDScanner\n\n
    (final DTDScannerHelper fHelper, final DocumentEntityScanner fScanner, final DataBufferFactory fBufferFactory, final SymbolTable fSymbolTable, final DTDParsedEntityFactory fEntityFactory)\n
    '''
def reset():
    '''returns None\n\n
    reset(final boolean b)\n
    '''
def hasDefaultAttributes():
    '''returns boolean\n\n
    hasDefaultAttributes()\n
    '''
def addDefaultAttributes():
    '''returns boolean\n\n
    addDefaultAttributes(final QName qName, final NSDeclList list, final AttrList list2, final boolean b)\n
    '''
def entityDepth():
    '''returns int\n\n
    entityDepth()\n
    '''
def endOfEntity():
    '''returns boolean\n\n
    endOfEntity(final int n)\n
    '''
def scanDoctypeDecl():
    '''returns boolean\n\n
    scanDoctypeDecl(final ParsedEntity parsedEntity)\n
    '''
def scanInternalDTDSubset():
    '''returns boolean\n\n
    scanInternalDTDSubset()\n
    '''
def scanExternalDTDSubset():
    '''returns boolean\n\n
    scanExternalDTDSubset()\n
    '''
def setScanInternalGeneralEntities():
    '''returns None\n\n
    setScanInternalGeneralEntities(final boolean fScanInternalGeneralEntities)\n
    '''
def getScanInternalGeneralEntities():
    '''returns boolean\n\n
    getScanInternalGeneralEntities()\n
    '''
def setScanExternalGeneralEntities():
    '''returns None\n\n
    setScanExternalGeneralEntities(final boolean fScanExternalGeneralEntities)\n
    '''
def getScanExternalGeneralEntities():
    '''returns boolean\n\n
    getScanExternalGeneralEntities()\n
    '''
def setScanExternalParameterEntities():
    '''returns None\n\n
    setScanExternalParameterEntities(final boolean fScanExternalParameterEntities)\n
    '''
def getScanExternalParameterEntities():
    '''returns boolean\n\n
    getScanExternalParameterEntities()\n
    '''
def setSupportDTD():
    '''returns None\n\n
    setSupportDTD(final boolean b)\n
    '''
def setResolveDTDURIs():
    '''returns None\n\n
    setResolveDTDURIs(final String s, final boolean fResolveDTDURIs)\n
    '''
def getResolveDTDURIs():
    '''returns boolean\n\n
    getResolveDTDURIs(final String s)\n
    '''
def setStandalone():
    '''returns None\n\n
    setStandalone()\n
    '''
def isStandalone():
    '''returns boolean\n\n
    isStandalone()\n
    '''
def getDTDGrammar():
    '''returns DTDGrammar\n\n
    getDTDGrammar()\n
    '''
def hadExternalEntity():
    '''returns boolean\n\n
    hadExternalEntity()\n
    '''
def setDocumentEntity():
    '''returns None\n\n
    setDocumentEntity(final ParsedEntity fCurrentEntity)\n
    '''
def entityReferenceInContent():
    '''returns boolean\n\n
    entityReferenceInContent()\n
    '''
def entityReferenceInAttValue():
    '''returns boolean\n\n
    entityReferenceInAttValue()\n
    '''
def run():
    '''returns Object\n\n
    run()\n
    '''
