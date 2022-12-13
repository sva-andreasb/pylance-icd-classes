OFF_INT = "int  Integer.MAX_VALUE"
FATAL_INT = "int  50000"
ERROR_INT = "int  40000"
WARN_INT = "int  30000"
INFO_INT = "int  20000"
DEBUG_INT = "int  10000"
ALL_INT = "int  Integer.MIN_VALUE"
def equals():
    '''public boolean equals(final Object o)
    '''
def hashCode():
    '''public int hashCode()
    '''
def getSyslogEquivalent():
    '''public final int getSyslogEquivalent()
    '''
def isGreaterOrEqual():
    '''public boolean isGreaterOrEqual(final Priority r)
    '''
def getAllPossiblePriorities():
    '''public static Priority[] getAllPossiblePriorities()
    '''
def toString():
    '''public final String toString()
    '''
def toInt():
    '''public final int toInt()
    '''
def toPriority():
    '''public static Priority toPriority(final String sArg)
    public static Priority toPriority(final int val)
    public static Priority toPriority(final int val, final Priority defaultPriority)
    public static Priority toPriority(final String sArg, final Priority defaultPriority)
    '''
