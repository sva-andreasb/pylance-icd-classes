LOWER = "int 0"
UPPER = "int 1"
UPPER_LONG = "int 2"
COUNT = "int 3"
def CollationKey():
'''public CollationKey(final String source, final byte[] key)
public CollationKey(final String source, final RawCollationKey key)
'''
pass
def getSourceString():
'''public String getSourceString()
'''
pass
def toByteArray():
'''public byte[] toByteArray()
'''
pass
def compareTo():
'''public int compareTo(final CollationKey target)
'''
pass
def equals():
'''public boolean equals(final Object target)
public boolean equals(final CollationKey target)
'''
pass
def hashCode():
'''public int hashCode()
'''
pass
def getBound():
'''public CollationKey getBound(final int boundType, int noOfLevels)
'''
pass
def merge():
'''public CollationKey merge(final CollationKey source)
'''
pass
