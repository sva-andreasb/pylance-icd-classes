version_ = "int  1"
def processRequest():
    '''public Message processRequest(final Message message, final CMXConnection cmxConnection)
    public Message processRequest(final Message message, final HttpServletRequest httpServletRequest, final HttpServletResponse httpServletResponse, final LogLookupInfo logLookupInfo)
    '''
def processAsynchronousMessage():
    '''public void processAsynchronousMessage(final Message message, final CMXConnection cmxConnection)
    '''
def getVersion():
    '''public int getVersion()
    '''
def getProcessorName():
    '''public String getProcessorName()
    '''
def checkForError():
    '''public void checkForError(final Message message)
    '''
def createConnectToProcessorRequest():
    '''public Message createConnectToProcessorRequest(final Processor processor)
    '''
def createErrorReply():
    '''public static Message createErrorReply(final String s, final int i)
    '''
def parseConnectReply():
    '''public int parseConnectReply(final Message message)
    '''
def getNegotiatedVersion():
    '''public int getNegotiatedVersion(final int a)
    '''
def processMessage():
    '''public void processMessage(final Message message, final HttpServletRequest httpServletRequest)
    '''
def invokeLogLookup():
    '''public void invokeLogLookup(final LogLookupInfo logLookupInfo)
    '''
