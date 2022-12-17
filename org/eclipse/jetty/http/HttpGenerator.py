def ():
    '''returns HttpGenerator\n\n
    (final Buffers buffers, final EndPoint io)\n
    '''
def reset():
    '''returns None\n\n
    reset()\n
    '''
def addContent():
    '''returns boolean\n\n
    addContent(Buffer content, final boolean last)\n
    addContent(final byte b)\n
    '''
def sendResponse():
    '''returns None\n\n
    sendResponse(final Buffer response)\n
    '''
def prepareUncheckedAddContent():
    '''returns int\n\n
    prepareUncheckedAddContent()\n
    '''
def isBufferFull():
    '''returns boolean\n\n
    isBufferFull()\n
    '''
def send1xx():
    '''returns None\n\n
    send1xx(final int code)\n
    '''
def isRequest():
    '''returns boolean\n\n
    isRequest()\n
    '''
def isResponse():
    '''returns boolean\n\n
    isResponse()\n
    '''
def completeHeader():
    '''returns None\n\n
    completeHeader(final HttpFields fields, final boolean allContentAdded)\n
    '''
def complete():
    '''returns None\n\n
    complete()\n
    '''
def flushBuffer():
    '''returns int\n\n
    flushBuffer()\n
    '''
def getBytesBuffered():
    '''returns int\n\n
    getBytesBuffered()\n
    '''
def isEmpty():
    '''returns boolean\n\n
    isEmpty()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
