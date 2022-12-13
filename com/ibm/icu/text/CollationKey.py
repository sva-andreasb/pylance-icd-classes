LOWER = "int  0"
UPPER = "int  1"
UPPER_LONG = "int  2"
COUNT = "int  3"
def CollationKey():
    '''public CollationKey(final String source, final byte[] key)
    public CollationKey(final String source, final RawCollationKey key)
    '''
def getSourceString():
    '''public String getSourceString()
    '''
def toByteArray():
    '''public byte[] toByteArray()
    '''
def compareTo():
    '''public int compareTo(final CollationKey target)
    '''
def equals():
    '''public boolean equals(final Object target)
    public boolean equals(final CollationKey target)
    '''
def hashCode():
    '''public int hashCode()
    '''
def getBound():
    '''public CollationKey getBound(final int boundType, int noOfLevels)
    '''
def merge():
    '''public CollationKey merge(final CollationKey source)
    '''
