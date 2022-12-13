def getReasonBuffer():
    '''public static Buffer getReasonBuffer(final int code)
    '''
def setServerVersion():
    '''public static void setServerVersion(final String version)
    '''
def HttpGenerator():
    '''public HttpGenerator(final Buffers buffers, final EndPoint io)
    '''
def reset():
    '''public void reset()
    '''
def addContent():
    '''public void addContent(Buffer content, final boolean last)
    public boolean addContent(final byte b)
    '''
def sendResponse():
    '''public void sendResponse(final Buffer response)
    '''
def prepareUncheckedAddContent():
    '''public int prepareUncheckedAddContent()
    '''
def isBufferFull():
    '''public boolean isBufferFull()
    '''
def send1xx():
    '''public void send1xx(final int code)
    '''
def isRequest():
    '''public boolean isRequest()
    '''
def isResponse():
    '''public boolean isResponse()
    '''
def completeHeader():
    '''public void completeHeader(final HttpFields fields, final boolean allContentAdded)
    '''
def complete():
    '''public void complete()
    '''
def flushBuffer():
    '''public int flushBuffer()
    '''
def getBytesBuffered():
    '''public int getBytesBuffered()
    '''
def isEmpty():
    '''public boolean isEmpty()
    '''
def toString():
    '''public String toString()
    '''
