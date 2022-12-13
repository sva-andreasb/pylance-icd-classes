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
    '''    public HttpParser(final Buffer buffer, final EventHandler handler)
    public HttpParser(final Buffers buffers, final EndPoint endp, final EventHandler handler)
    '''
def getContentLength():
    '''    public long getContentLength()
    '''
def getContentRead():
    '''    public long getContentRead()
    '''
def setHeadResponse():
    '''    public void setHeadResponse(final boolean head)
    '''
def getState():
    '''    public int getState()
    '''
def inContentState():
    '''    public boolean inContentState()
    '''
def inHeaderState():
    '''    public boolean inHeaderState()
    '''
def isChunking():
    '''    public boolean isChunking()
    '''
def isIdle():
    '''    public boolean isIdle()
    '''
def isComplete():
    '''    public boolean isComplete()
    '''
def isMoreInBuffer():
    '''    public boolean isMoreInBuffer()
    '''
def isState():
    '''    public boolean isState(final int state)
    '''
def isPersistent():
    '''    public boolean isPersistent()
    '''
def setPersistent():
    '''    public void setPersistent(final boolean persistent)
    '''
def parse():
    '''    public void parse()
    '''
def parseAvailable():
    '''    public boolean parseAvailable()
    '''
def parseNext():
    '''    public int parseNext()
    '''
def reset():
    '''    public void reset()
    '''
def returnBuffers():
    '''    public void returnBuffers()
    '''
def setState():
    '''    public void setState(final int state)
    '''
def toString():
    '''    public String toString(final Buffer buf)
    public String toString()
    '''
def getHeaderBuffer():
    '''    public Buffer getHeaderBuffer()
    '''
def getBodyBuffer():
    '''    public Buffer getBodyBuffer()
    '''
def setForceContentBuffer():
    '''    public void setForceContentBuffer(final boolean force)
    '''
def blockForContent():
    '''    public Buffer blockForContent(final long maxIdleTime)
    '''
def available():
    '''    public int available()
    '''
def headerComplete():
    '''    public void headerComplete()
    '''
def messageComplete():
    '''    public void messageComplete(final long contentLength)
    '''
def parsedHeader():
    '''    public void parsedHeader(final Buffer name, final Buffer value)
    '''
def earlyEOF():
    '''    public void earlyEOF()
    '''
