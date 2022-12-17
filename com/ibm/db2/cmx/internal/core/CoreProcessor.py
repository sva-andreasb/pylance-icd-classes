version_ = "int  1"
def processRequest():
    '''returns Message\n\n
    processRequest(final Message message, final CMXConnection cmxConnection)\n
    processRequest(final Message message, final HttpServletRequest httpServletRequest, final HttpServletResponse httpServletResponse, final LogLookupInfo logLookupInfo)\n
    '''
def processAsynchronousMessage():
    '''returns None\n\n
    processAsynchronousMessage(final Message message, final CMXConnection cmxConnection)\n
    '''
def getVersion():
    '''returns int\n\n
    getVersion()\n
    '''
def getProcessorName():
    '''returns String\n\n
    getProcessorName()\n
    '''
def checkForError():
    '''returns None\n\n
    checkForError(final Message message)\n
    '''
def createConnectToProcessorRequest():
    '''returns Message\n\n
    createConnectToProcessorRequest(final Processor processor)\n
    '''
def parseConnectReply():
    '''returns int\n\n
    parseConnectReply(final Message message)\n
    '''
def getNegotiatedVersion():
    '''returns int\n\n
    getNegotiatedVersion(final int a)\n
    '''
def processMessage():
    '''returns None\n\n
    processMessage(final Message message, final HttpServletRequest httpServletRequest)\n
    '''
def invokeLogLookup():
    '''returns None\n\n
    invokeLogLookup(final LogLookupInfo logLookupInfo)\n
    '''
