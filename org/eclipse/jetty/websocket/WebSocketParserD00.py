STATE_START = "int  0"
STATE_SENTINEL_DATA = "int  1"
STATE_LENGTH = "int  2"
STATE_DATA = "int  3"
def ():
    '''returns WebSocketParserD00\n\n
    (final WebSocketBuffers buffers, final EndPoint endp, final FrameHandler handler)\n
    '''
def isBufferEmpty():
    '''returns boolean\n\n
    isBufferEmpty()\n
    '''
def getBuffer():
    '''returns Buffer\n\n
    getBuffer()\n
    '''
def parseNext():
    '''returns int\n\n
    parseNext()\n
    '''
def fill():
    '''returns None\n\n
    fill(final Buffer buffer)\n
    '''
