STATE_HEADER = "int  0"
STATE_CONTENT = "int  2"
STATE_FLUSHING = "int  3"
STATE_END = "int  4"
def AbstractGenerator():
    '''    public AbstractGenerator(final Buffers buffers, final EndPoint io)
    '''
def isOpen():
    '''    public boolean isOpen()
    '''
def reset():
    '''    public void reset()
    '''
def returnBuffers():
    '''    public void returnBuffers()
    '''
def resetBuffer():
    '''    public void resetBuffer()
    '''
def getContentBufferSize():
    '''    public int getContentBufferSize()
    '''
def increaseContentBufferSize():
    '''    public void increaseContentBufferSize(final int contentBufferSize)
    '''
def getUncheckedBuffer():
    '''    public Buffer getUncheckedBuffer()
    '''
def getSendServerVersion():
    '''    public boolean getSendServerVersion()
    '''
def setSendServerVersion():
    '''    public void setSendServerVersion(final boolean sendServerVersion)
    '''
def getState():
    '''    public int getState()
    '''
def isState():
    '''    public boolean isState(final int state)
    '''
def isComplete():
    '''    public boolean isComplete()
    '''
def isIdle():
    '''    public boolean isIdle()
    '''
def isCommitted():
    '''    public boolean isCommitted()
    '''
def isHead():
    '''    public boolean isHead()
    '''
def setContentLength():
    '''    public void setContentLength(final long value)
    '''
def setHead():
    '''    public void setHead(final boolean head)
    '''
def isPersistent():
    '''    public boolean isPersistent()
    '''
def setPersistent():
    '''    public void setPersistent(final boolean persistent)
    '''
def setVersion():
    '''    public void setVersion(final int version)
    '''
def getVersion():
    '''    public int getVersion()
    '''
def setDate():
    '''    public void setDate(final Buffer timeStampBuffer)
    '''
def setRequest():
    '''    public void setRequest(final String method, final String uri)
    '''
def setResponse():
    '''    public void setResponse(final int status, final String reason)
    '''
def completeUncheckedAddContent():
    '''    public void completeUncheckedAddContent()
    '''
def isBufferFull():
    '''    public boolean isBufferFull()
    '''
def isWritten():
    '''    public boolean isWritten()
    '''
def isAllContentWritten():
    '''    public boolean isAllContentWritten()
    '''
def complete():
    '''    public void complete()
    '''
def flush():
    '''    public void flush(final long maxIdleTime)
    '''
def sendError():
    '''    public void sendError(final int code, final String reason, final String content, final boolean close)
    '''
def getContentWritten():
    '''    public long getContentWritten()
    '''
def blockForOutput():
    '''    public void blockForOutput(final long maxIdleTime)
    '''
