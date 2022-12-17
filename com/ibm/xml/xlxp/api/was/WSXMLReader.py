def ():
    '''returns WSScannerHelper\n\n
    ()\n
    (final DocumentEntityScanner documentEntityScanner, final DataBufferFactory dataBufferFactory, final SymbolTable symbolTable, final WSXMLReader fParser)\n
    '''
def getProperty():
    '''returns Object\n\n
    getProperty(final String s)\n
    '''
def endDTD():
    '''returns None\n\n
    endDTD()\n
    '''
def skippedExternalSubsetEntity():
    '''returns boolean\n\n
    skippedExternalSubsetEntity()\n
    '''
def startDTDEntity():
    '''returns None\n\n
    startDTDEntity()\n
    '''
def endDTDEntity():
    '''returns None\n\n
    endDTDEntity()\n
    '''
def startPE():
    '''returns None\n\n
    startPE(final XMLString xmlString)\n
    '''
def endPE():
    '''returns None\n\n
    endPE(final XMLString xmlString)\n
    '''
def processingInstructionInDTD():
    '''returns None\n\n
    processingInstructionInDTD(final XMLString xmlString, final XMLString xmlString2)\n
    '''
def commentInDTD():
    '''returns None\n\n
    commentInDTD(final XMLString xmlString)\n
    '''
def getDTDHandler():
    '''returns DTDHandler\n\n
    getDTDHandler()\n
    '''
def setDTDHandler():
    '''returns None\n\n
    setDTDHandler(final DTDHandler dtdHandler)\n
    '''
def getEntityResolver():
    '''returns EntityResolver\n\n
    getEntityResolver()\n
    '''
def setEntityResolver():
    '''returns None\n\n
    setEntityResolver(final EntityResolver entityResolver)\n
    '''
def skipSubtree():
    '''returns boolean\n\n
    skipSubtree(final XMLString xmlString)\n
    '''
def produceXMLDeclEvent():
    '''returns boolean\n\n
    produceXMLDeclEvent()\n
    '''
def produceEmptyElementEvent():
    '''returns boolean\n\n
    produceEmptyElementEvent()\n
    '''
def produceStartElementEvent():
    '''returns boolean\n\n
    produceStartElementEvent()\n
    '''
def produceEndElementEvent():
    '''returns boolean\n\n
    produceEndElementEvent(final QName qName)\n
    '''
def produceCharactersEvent():
    '''returns boolean\n\n
    produceCharactersEvent()\n
    '''
def produceWhitespaceEvent():
    '''returns boolean\n\n
    produceWhitespaceEvent()\n
    '''
def produceCharacterEvent():
    '''returns boolean\n\n
    produceCharacterEvent(final int n)\n
    '''
def producePredefinedEntityEvent():
    '''returns boolean\n\n
    producePredefinedEntityEvent(final int n)\n
    '''
def produceProcessingInstructionEvent():
    '''returns boolean\n\n
    produceProcessingInstructionEvent()\n
    '''
def produceCommentEvent():
    '''returns boolean\n\n
    produceCommentEvent()\n
    '''
def produceStartCDATASectionEvent():
    '''returns boolean\n\n
    produceStartCDATASectionEvent()\n
    '''
def produceEndCDATASectionEvent():
    '''returns boolean\n\n
    produceEndCDATASectionEvent()\n
    '''
def produceDoctypeEvent():
    '''returns boolean\n\n
    produceDoctypeEvent(final boolean b)\n
    '''
def produceStartEntityEvent():
    '''returns boolean\n\n
    produceStartEntityEvent()\n
    '''
def produceEndEntityEvent():
    '''returns boolean\n\n
    produceEndEntityEvent()\n
    '''
def produceEntityReferenceEvent():
    '''returns boolean\n\n
    produceEntityReferenceEvent()\n
    '''
def produceWarningEvent():
    '''returns boolean\n\n
    produceWarningEvent(final String s, final int n)\n
    '''
def produceRecoverableErrorEvent():
    '''returns boolean\n\n
    produceRecoverableErrorEvent(final String s, final int n)\n
    '''
def produceFatalErrorEvent():
    '''returns boolean\n\n
    produceFatalErrorEvent(final String s, final int n)\n
    '''
