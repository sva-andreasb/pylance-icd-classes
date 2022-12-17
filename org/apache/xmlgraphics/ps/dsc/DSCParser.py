def ():
    '''returns DSCParser\n\n
    (final InputStream in)\n
    '''
def getInputStream():
    '''returns InputStream\n\n
    getInputStream()\n
    '''
def parse():
    '''returns None\n\n
    parse(final DSCHandler handler)\n
    '''
def hasNext():
    '''returns boolean\n\n
    hasNext()\n
    '''
def next():
    '''returns int\n\n
    next()\n
    '''
def nextEvent():
    '''returns DSCEvent\n\n
    nextEvent()\n
    '''
def getCurrentEvent():
    '''returns DSCEvent\n\n
    getCurrentEvent()\n
    '''
def peek():
    '''returns DSCEvent\n\n
    peek()\n
    '''
def getLine():
    '''returns String\n\n
    getLine()\n
    '''
def nextDSCComment():
    '''returns DSCComment\n\n
    nextDSCComment(final String name)\n
    nextDSCComment(final String name, final PSGenerator gen)\n
    '''
def nextPSComment():
    '''returns PostScriptComment\n\n
    nextPSComment(final String prefix, final PSGenerator gen)\n
    '''
def setFilter():
    '''returns None\n\n
    setFilter(final DSCFilter filter)\n
    '''
def addListener():
    '''returns None\n\n
    addListener(final DSCListener listener)\n
    '''
def removeListener():
    '''returns None\n\n
    removeListener(final DSCListener listener)\n
    '''
def setListenersDisabled():
    '''returns None\n\n
    setListenersDisabled(final boolean value)\n
    '''
def isListenersDisabled():
    '''returns boolean\n\n
    isListenersDisabled()\n
    '''
def setNestedDocumentHandler():
    '''returns None\n\n
    setNestedDocumentHandler(final NestedDocumentHandler handler)\n
    '''
def setCheckEOF():
    '''returns None\n\n
    setCheckEOF(final boolean value)\n
    '''
def isCheckEOF():
    '''returns boolean\n\n
    isCheckEOF()\n
    '''
def processEvent():
    '''returns None\n\n
    processEvent(final DSCEvent event, final DSCParser parser)\n
    '''
