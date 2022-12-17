def ():
    '''returns DocumentEntityScanner\n\n
    ()\n
    '''
def reset():
    '''returns None\n\n
    reset(final boolean b)\n
    '''
def setScannerHelper():
    '''returns None\n\n
    setScannerHelper(final ScannerHelper fHelper)\n
    '''
def setDTDSupport():
    '''returns None\n\n
    setDTDSupport(final DTDSupport fdtdSupport)\n
    '''
def parseDocumentEntity():
    '''returns None\n\n
    parseDocumentEntity(final ParsedEntity documentEntity)\n
    '''
def setDocumentEntity():
    '''returns None\n\n
    setDocumentEntity(final ParsedEntity parsedEntity)\n
    '''
def currentState():
    '''returns int\n\n
    currentState()\n
    '''
def setCurrentState():
    '''returns None\n\n
    setCurrentState(final int fCurrentState)\n
    '''
def produceEvent():
    '''returns boolean\n\n
    produceEvent()\n
    '''
def produceEvents():
    '''returns boolean\n\n
    produceEvents()\n
    '''
def endDocument():
    '''returns boolean\n\n
    endDocument()\n
    '''
def hasDefaultAttributes():
    '''returns boolean\n\n
    hasDefaultAttributes()\n
    '''
def addDefaultAttributes():
    '''returns boolean\n\n
    addDefaultAttributes(final QName qName, final NSDeclList list, final AttrList list2, final boolean b)\n
    '''
def finishStartElementBuffered():
    '''returns None\n\n
    finishStartElementBuffered()\n
    '''
def finishStartElementUnbuffered():
    '''returns None\n\n
    finishStartElementUnbuffered()\n
    '''
def finishStartElement():
    '''returns None\n\n
    finishStartElement()\n
    '''
def finishEmptyElementBuffered():
    '''returns None\n\n
    finishEmptyElementBuffered(final int n)\n
    '''
def finishEmptyElementUnbuffered():
    '''returns None\n\n
    finishEmptyElementUnbuffered(final int n)\n
    '''
def finishEmptyElement():
    '''returns None\n\n
    finishEmptyElement(final int n)\n
    '''
def finishEndElementBuffered():
    '''returns None\n\n
    finishEndElementBuffered(final int n)\n
    '''
def finishEndElementUnbuffered():
    '''returns None\n\n
    finishEndElementUnbuffered(final int n)\n
    '''
def setEntityContent():
    '''returns None\n\n
    setEntityContent(final ParsedEntity parsedEntity)\n
    '''
def scanAttrValueBuffered():
    '''returns boolean\n\n
    scanAttrValueBuffered(final XMLString xmlString, final int n)\n
    '''
def scanAttrValueUnbuffered():
    '''returns boolean\n\n
    scanAttrValueUnbuffered(final XMLString xmlString, final int n)\n
    '''
def scanNamespaceURIBuffered():
    '''returns boolean\n\n
    scanNamespaceURIBuffered(final XMLString xmlString, final int n)\n
    '''
def scanNamespaceURIUnbuffered():
    '''returns boolean\n\n
    scanNamespaceURIUnbuffered(final XMLString xmlString, final int n)\n
    '''
def scanContentBuffered():
    '''returns boolean\n\n
    scanContentBuffered(XMLString xmlString)\n
    '''
def scanElementContentBuffered():
    '''returns boolean\n\n
    scanElementContentBuffered(XMLString contentToProduce)\n
    '''
def scanStartElementBuffered():
    '''returns boolean\n\n
    scanStartElementBuffered()\n
    '''
def scanEndElementBuffered():
    '''returns boolean\n\n
    scanEndElementBuffered()\n
    '''
def scanContentUnbuffered():
    '''returns boolean\n\n
    scanContentUnbuffered(final XMLString xmlString)\n
    '''
def scanElementContentUnbuffered():
    '''returns boolean\n\n
    scanElementContentUnbuffered(XMLString contentToProduce)\n
    '''
def scanStartElementUnbuffered():
    '''returns boolean\n\n
    scanStartElementUnbuffered()\n
    '''
def scanEndElementUnbuffered():
    '''returns boolean\n\n
    scanEndElementUnbuffered()\n
    '''
def skipContentBuffered():
    '''returns boolean\n\n
    skipContentBuffered(final XMLString xmlString)\n
    '''
def skipContentUnbuffered():
    '''returns boolean\n\n
    skipContentUnbuffered(final XMLString xmlString)\n
    '''
