STATE_HEADER = "int  0"
STATE_CONTENT = "int  2"
STATE_FLUSHING = "int  3"
STATE_END = "int  4"
def AbstractGenerator():
'''public AbstractGenerator(final Buffers buffers, final EndPoint io)
'''
pass
def isOpen():
'''public boolean isOpen()
'''
pass
def reset():
'''public void reset()
'''
pass
def returnBuffers():
'''public void returnBuffers()
'''
pass
def resetBuffer():
'''public void resetBuffer()
'''
pass
def getContentBufferSize():
'''public int getContentBufferSize()
'''
pass
def increaseContentBufferSize():
'''public void increaseContentBufferSize(final int contentBufferSize)
'''
pass
def getUncheckedBuffer():
'''public Buffer getUncheckedBuffer()
'''
pass
def getSendServerVersion():
'''public boolean getSendServerVersion()
'''
pass
def setSendServerVersion():
'''public void setSendServerVersion(final boolean sendServerVersion)
'''
pass
def getState():
'''public int getState()
'''
pass
def isState():
'''public boolean isState(final int state)
'''
pass
def isComplete():
'''public boolean isComplete()
'''
pass
def isIdle():
'''public boolean isIdle()
'''
pass
def isCommitted():
'''public boolean isCommitted()
'''
pass
def isHead():
'''public boolean isHead()
'''
pass
def setContentLength():
'''public void setContentLength(final long value)
'''
pass
def setHead():
'''public void setHead(final boolean head)
'''
pass
def isPersistent():
'''public boolean isPersistent()
'''
pass
def setPersistent():
'''public void setPersistent(final boolean persistent)
'''
pass
def setVersion():
'''public void setVersion(final int version)
'''
pass
def getVersion():
'''public int getVersion()
'''
pass
def setDate():
'''public void setDate(final Buffer timeStampBuffer)
'''
pass
def setRequest():
'''public void setRequest(final String method, final String uri)
'''
pass
def setResponse():
'''public void setResponse(final int status, final String reason)
'''
pass
def completeUncheckedAddContent():
'''public void completeUncheckedAddContent()
'''
pass
def isBufferFull():
'''public boolean isBufferFull()
'''
pass
def isWritten():
'''public boolean isWritten()
'''
pass
def isAllContentWritten():
'''public boolean isAllContentWritten()
'''
pass
def complete():
'''public void complete()
'''
pass
def flush():
'''public void flush(final long maxIdleTime)
'''
pass
def sendError():
'''public void sendError(final int code, final String reason, final String content, final boolean close)
'''
pass
def getContentWritten():
'''public long getContentWritten()
'''
pass
def blockForOutput():
'''public void blockForOutput(final long maxIdleTime)
'''
pass
