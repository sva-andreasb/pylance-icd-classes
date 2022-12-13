END_STREAM = "short  1"
END_HEADERS = "short  4"
ACK = "short  1"
PADDED = "short  8"
PRIORITY = "short  32"
def Http2Flags():
    '''public Http2Flags()
    public Http2Flags(final short value)
    '''
def value():
    '''public short value()
    '''
def endOfStream():
    '''public boolean endOfStream()
    public Http2Flags endOfStream(final boolean endOfStream)
    '''
def endOfHeaders():
    '''public boolean endOfHeaders()
    public Http2Flags endOfHeaders(final boolean endOfHeaders)
    '''
def priorityPresent():
    '''public boolean priorityPresent()
    public Http2Flags priorityPresent(final boolean priorityPresent)
    '''
def ack():
    '''public boolean ack()
    public Http2Flags ack(final boolean ack)
    '''
def paddingPresent():
    '''public boolean paddingPresent()
    public Http2Flags paddingPresent(final boolean paddingPresent)
    '''
def getNumPriorityBytes():
    '''public int getNumPriorityBytes()
    '''
def getPaddingPresenceFieldLength():
    '''public int getPaddingPresenceFieldLength()
    '''
def setFlag():
    '''public Http2Flags setFlag(final boolean on, final short mask)
    '''
def isFlagSet():
    '''public boolean isFlagSet(final short mask)
    '''
def hashCode():
    '''public int hashCode()
    '''
def equals():
    '''public boolean equals(final Object obj)
    '''
def toString():
    '''public String toString()
    '''
