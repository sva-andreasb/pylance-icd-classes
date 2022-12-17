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
def ():
    '''returns HttpParser\n\n
    (final Buffer buffer, final EventHandler handler)\n
    (final Buffers buffers, final EndPoint endp, final EventHandler handler)\n
    '''
def getContentLength():
    '''returns long\n\n
    getContentLength()\n
    '''
def getContentRead():
    '''returns long\n\n
    getContentRead()\n
    '''
def setHeadResponse():
    '''returns None\n\n
    setHeadResponse(final boolean head)\n
    '''
def getState():
    '''returns int\n\n
    getState()\n
    '''
def inContentState():
    '''returns boolean\n\n
    inContentState()\n
    '''
def inHeaderState():
    '''returns boolean\n\n
    inHeaderState()\n
    '''
def isChunking():
    '''returns boolean\n\n
    isChunking()\n
    '''
def isIdle():
    '''returns boolean\n\n
    isIdle()\n
    '''
def isComplete():
    '''returns boolean\n\n
    isComplete()\n
    '''
def isMoreInBuffer():
    '''returns boolean\n\n
    isMoreInBuffer()\n
    '''
def isState():
    '''returns boolean\n\n
    isState(final int state)\n
    '''
def isPersistent():
    '''returns boolean\n\n
    isPersistent()\n
    '''
def setPersistent():
    '''returns None\n\n
    setPersistent(final boolean persistent)\n
    '''
def parse():
    '''returns None\n\n
    parse()\n
    '''
def parseAvailable():
    '''returns boolean\n\n
    parseAvailable()\n
    '''
def parseNext():
    '''returns int\n\n
    parseNext()\n
    '''
def reset():
    '''returns None\n\n
    reset()\n
    '''
def returnBuffers():
    '''returns None\n\n
    returnBuffers()\n
    '''
def setState():
    '''returns None\n\n
    setState(final int state)\n
    '''
def toString():
    '''returns String\n\n
    toString(final Buffer buf)\n
    toString()\n
    '''
def getHeaderBuffer():
    '''returns Buffer\n\n
    getHeaderBuffer()\n
    '''
def getBodyBuffer():
    '''returns Buffer\n\n
    getBodyBuffer()\n
    '''
def setForceContentBuffer():
    '''returns None\n\n
    setForceContentBuffer(final boolean force)\n
    '''
def blockForContent():
    '''returns Buffer\n\n
    blockForContent(final long maxIdleTime)\n
    '''
def available():
    '''returns int\n\n
    available()\n
    '''
def headerComplete():
    '''returns None\n\n
    headerComplete()\n
    '''
def messageComplete():
    '''returns None\n\n
    messageComplete(final long contentLength)\n
    '''
def parsedHeader():
    '''returns None\n\n
    parsedHeader(final Buffer name, final Buffer value)\n
    '''
def earlyEOF():
    '''returns None\n\n
    earlyEOF()\n
    '''
