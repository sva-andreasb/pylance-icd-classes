STATE_START = "int  -14"
STATE_FIELD0 = "int  -13"
STATE_SPACE1 = "int  -12"
STATE_STATUS = "int  -11"
STATE_URI = "int  -10"
STATE_SPACE2 = "int  -9"
STATE_END0 = "int  -8"
STATE_END1 = "int  -7"
STATE_FIELD2 = "int  -6"
STATE_HEADER = "int  -5"
STATE_HEADER_NAME = "int  -4"
STATE_HEADER_IN_NAME = "int  -3"
STATE_HEADER_VALUE = "int  -2"
STATE_HEADER_IN_VALUE = "int  -1"
STATE_END = "int  0"
STATE_EOF_CONTENT = "int  1"
STATE_CONTENT = "int  2"
STATE_CHUNKED_CONTENT = "int  3"
STATE_CHUNK_SIZE = "int  4"
STATE_CHUNK_PARAMS = "int  5"
STATE_CHUNK = "int  6"
STATE_SEEKING_EOF = "int  7"
def HttpParser():
'''public HttpParser(final Buffer buffer, final EventHandler handler)
public HttpParser(final Buffers buffers, final EndPoint endp, final EventHandler handler)
'''
pass
def getContentLength():
'''public long getContentLength()
'''
pass
def getContentRead():
'''public long getContentRead()
'''
pass
def setHeadResponse():
'''public void setHeadResponse(final boolean head)
'''
pass
def getState():
'''public int getState()
'''
pass
def inContentState():
'''public boolean inContentState()
'''
pass
def inHeaderState():
'''public boolean inHeaderState()
'''
pass
def isChunking():
'''public boolean isChunking()
'''
pass
def isIdle():
'''public boolean isIdle()
'''
pass
def isComplete():
'''public boolean isComplete()
'''
pass
def isMoreInBuffer():
'''public boolean isMoreInBuffer()
'''
pass
def isState():
'''public boolean isState(final int state)
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
def parse():
'''public void parse()
'''
pass
def parseAvailable():
'''public boolean parseAvailable()
'''
pass
def parseNext():
'''public int parseNext()
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
def setState():
'''public void setState(final int state)
'''
pass
def toString():
'''public String toString(final Buffer buf)
public String toString()
'''
pass
def getHeaderBuffer():
'''public Buffer getHeaderBuffer()
'''
pass
def getBodyBuffer():
'''public Buffer getBodyBuffer()
'''
pass
def setForceContentBuffer():
'''public void setForceContentBuffer(final boolean force)
'''
pass
def blockForContent():
'''public Buffer blockForContent(final long maxIdleTime)
'''
pass
def available():
'''public int available()
'''
pass
def headerComplete():
'''public void headerComplete()
'''
pass
def messageComplete():
'''public void messageComplete(final long contentLength)
'''
pass
def parsedHeader():
'''public void parsedHeader(final Buffer name, final Buffer value)
'''
pass
def earlyEOF():
'''public void earlyEOF()
'''
pass
