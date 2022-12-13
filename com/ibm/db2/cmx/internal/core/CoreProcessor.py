version_ = "int  1"
def processRequest():
'''public Message processRequest(final Message message, final CMXConnection cmxConnection)
public Message processRequest(final Message message, final HttpServletRequest httpServletRequest, final HttpServletResponse httpServletResponse, final LogLookupInfo logLookupInfo)
'''
pass
def processAsynchronousMessage():
'''public void processAsynchronousMessage(final Message message, final CMXConnection cmxConnection)
'''
pass
def getVersion():
'''public int getVersion()
'''
pass
def getProcessorName():
'''public String getProcessorName()
'''
pass
def checkForError():
'''public void checkForError(final Message message)
'''
pass
def createConnectToProcessorRequest():
'''public Message createConnectToProcessorRequest(final Processor processor)
'''
pass
def createErrorReply():
'''public static Message createErrorReply(final String s, final int i)
'''
pass
def parseConnectReply():
'''public int parseConnectReply(final Message message)
'''
pass
def getNegotiatedVersion():
'''public int getNegotiatedVersion(final int a)
'''
pass
def processMessage():
'''public void processMessage(final Message message, final HttpServletRequest httpServletRequest)
'''
pass
def invokeLogLookup():
'''public void invokeLogLookup(final LogLookupInfo logLookupInfo)
'''
pass
