STATE_HEADER = "int  0"
STATE_CONTENT = "int  2"
STATE_FLUSHING = "int  3"
STATE_END = "int  4"
def ():
    '''returns AbstractGenerator\n\n
    (final Buffers buffers, final EndPoint io)\n
    '''
def isOpen():
    '''returns boolean\n\n
    isOpen()\n
    '''
def reset():
    '''returns None\n\n
    reset()\n
    '''
def returnBuffers():
    '''returns None\n\n
    returnBuffers()\n
    '''
def resetBuffer():
    '''returns None\n\n
    resetBuffer()\n
    '''
def getContentBufferSize():
    '''returns int\n\n
    getContentBufferSize()\n
    '''
def increaseContentBufferSize():
    '''returns None\n\n
    increaseContentBufferSize(final int contentBufferSize)\n
    '''
def getUncheckedBuffer():
    '''returns Buffer\n\n
    getUncheckedBuffer()\n
    '''
def getSendServerVersion():
    '''returns boolean\n\n
    getSendServerVersion()\n
    '''
def setSendServerVersion():
    '''returns None\n\n
    setSendServerVersion(final boolean sendServerVersion)\n
    '''
def getState():
    '''returns int\n\n
    getState()\n
    '''
def isState():
    '''returns boolean\n\n
    isState(final int state)\n
    '''
def isComplete():
    '''returns boolean\n\n
    isComplete()\n
    '''
def isIdle():
    '''returns boolean\n\n
    isIdle()\n
    '''
def isCommitted():
    '''returns boolean\n\n
    isCommitted()\n
    '''
def isHead():
    '''returns boolean\n\n
    isHead()\n
    '''
def setContentLength():
    '''returns None\n\n
    setContentLength(final long value)\n
    '''
def setHead():
    '''returns None\n\n
    setHead(final boolean head)\n
    '''
def isPersistent():
    '''returns boolean\n\n
    isPersistent()\n
    '''
def setPersistent():
    '''returns None\n\n
    setPersistent(final boolean persistent)\n
    '''
def setVersion():
    '''returns None\n\n
    setVersion(final int version)\n
    '''
def getVersion():
    '''returns int\n\n
    getVersion()\n
    '''
def setDate():
    '''returns None\n\n
    setDate(final Buffer timeStampBuffer)\n
    '''
def setRequest():
    '''returns None\n\n
    setRequest(final String method, final String uri)\n
    '''
def setResponse():
    '''returns None\n\n
    setResponse(final int status, final String reason)\n
    '''
def completeUncheckedAddContent():
    '''returns None\n\n
    completeUncheckedAddContent()\n
    '''
def isBufferFull():
    '''returns boolean\n\n
    isBufferFull()\n
    '''
def isWritten():
    '''returns boolean\n\n
    isWritten()\n
    '''
def isAllContentWritten():
    '''returns boolean\n\n
    isAllContentWritten()\n
    '''
def complete():
    '''returns None\n\n
    complete()\n
    '''
def flush():
    '''returns None\n\n
    flush(final long maxIdleTime)\n
    '''
def sendError():
    '''returns None\n\n
    sendError(final int code, final String reason, final String content, final boolean close)\n
    '''
def getContentWritten():
    '''returns long\n\n
    getContentWritten()\n
    '''
def blockForOutput():
    '''returns None\n\n
    blockForOutput(final long maxIdleTime)\n
    '''
