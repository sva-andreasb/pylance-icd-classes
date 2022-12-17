END_STREAM = "short  1"
END_HEADERS = "short  4"
ACK = "short  1"
PADDED = "short  8"
PRIORITY = "short  32"
def ():
    '''returns Http2Flags\n\n
    ()\n
    (final short value)\n
    '''
def value():
    '''returns short\n\n
    value()\n
    '''
def endOfStream():
    '''returns Http2Flags\n\n
    endOfStream()\n
    endOfStream(final boolean endOfStream)\n
    '''
def endOfHeaders():
    '''returns Http2Flags\n\n
    endOfHeaders()\n
    endOfHeaders(final boolean endOfHeaders)\n
    '''
def priorityPresent():
    '''returns Http2Flags\n\n
    priorityPresent()\n
    priorityPresent(final boolean priorityPresent)\n
    '''
def ack():
    '''returns Http2Flags\n\n
    ack()\n
    ack(final boolean ack)\n
    '''
def paddingPresent():
    '''returns Http2Flags\n\n
    paddingPresent()\n
    paddingPresent(final boolean paddingPresent)\n
    '''
def getNumPriorityBytes():
    '''returns int\n\n
    getNumPriorityBytes()\n
    '''
def getPaddingPresenceFieldLength():
    '''returns int\n\n
    getPaddingPresenceFieldLength()\n
    '''
def setFlag():
    '''returns Http2Flags\n\n
    setFlag(final boolean on, final short mask)\n
    '''
def isFlagSet():
    '''returns boolean\n\n
    isFlagSet(final short mask)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object obj)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
