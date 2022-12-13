END_STREAM = "short  1"
END_HEADERS = "short  4"
ACK = "short  1"
PADDED = "short  8"
PRIORITY = "short  32"
def Http2Flags():
'''public Http2Flags()
public Http2Flags(final short value)
'''
pass
def value():
'''public short value()
'''
pass
def endOfStream():
'''public boolean endOfStream()
public Http2Flags endOfStream(final boolean endOfStream)
'''
pass
def endOfHeaders():
'''public boolean endOfHeaders()
public Http2Flags endOfHeaders(final boolean endOfHeaders)
'''
pass
def priorityPresent():
'''public boolean priorityPresent()
public Http2Flags priorityPresent(final boolean priorityPresent)
'''
pass
def ack():
'''public boolean ack()
public Http2Flags ack(final boolean ack)
'''
pass
def paddingPresent():
'''public boolean paddingPresent()
public Http2Flags paddingPresent(final boolean paddingPresent)
'''
pass
def getNumPriorityBytes():
'''public int getNumPriorityBytes()
'''
pass
def getPaddingPresenceFieldLength():
'''public int getPaddingPresenceFieldLength()
'''
pass
def setFlag():
'''public Http2Flags setFlag(final boolean on, final short mask)
'''
pass
def isFlagSet():
'''public boolean isFlagSet(final short mask)
'''
pass
def hashCode():
'''public int hashCode()
'''
pass
def equals():
'''public boolean equals(final Object obj)
'''
pass
def toString():
'''public String toString()
'''
pass
