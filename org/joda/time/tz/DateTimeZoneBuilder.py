def ():
    '''returns DateTimeZoneBuilder\n\n
    ()\n
    '''
def addCutover():
    '''returns DateTimeZoneBuilder\n\n
    addCutover(final int n, final char c, final int n2, final int n3, final int n4, final boolean b, final int n5)\n
    '''
def setStandardOffset():
    '''returns None\n\n
    setStandardOffset(final int standardOffset)\n
    setStandardOffset(final int iStandardOffset)\n
    '''
def setFixedSavings():
    '''returns None\n\n
    setFixedSavings(final String s, final int n)\n
    setFixedSavings(final String iInitialNameKey, final int iInitialSaveMillis)\n
    '''
def addRecurringSavings():
    '''returns DateTimeZoneBuilder\n\n
    addRecurringSavings(final String s, final int n, final int n2, final int n3, final char c, final int n4, final int n5, final int n6, final boolean b, final int n7)\n
    '''
def toDateTimeZone():
    '''returns DateTimeZone\n\n
    toDateTimeZone(final String s, final boolean b)\n
    '''
def writeTo():
    '''returns None\n\n
    writeTo(final String s, final OutputStream out)\n
    writeTo(final String s, final DataOutput dataOutput)\n
    writeTo(final DataOutput dataOutput)\n
    writeTo(final DataOutput dataOutput)\n
    writeTo(final DataOutput dataOutput)\n
    writeTo(final DataOutput dataOutput)\n
    '''
def setInstant():
    '''returns long\n\n
    setInstant(final int n, final int n2, final int n3)\n
    '''
def next():
    '''returns long\n\n
    next(long n, final int n2, final int n3)\n
    next(final long n, final int n2, final int n3)\n
    next(final long n, final int n2, final int n3)\n
    '''
def previous():
    '''returns long\n\n
    previous(long n, final int n2, final int n3)\n
    previous(final long n, final int n2, final int n3)\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object o)\n
    equals(final Object o)\n
    equals(final Object o)\n
    equals(final Object o)\n
    '''
def getOfYear():
    '''returns OfYear\n\n
    getOfYear()\n
    getOfYear()\n
    '''
def getNameKey():
    '''returns String\n\n
    getNameKey()\n
    getNameKey()\n
    getNameKey()\n
    getNameKey(final long n)\n
    getNameKey(final long key)\n
    '''
def getSaveMillis():
    '''returns int\n\n
    getSaveMillis()\n
    getSaveMillis()\n
    getSaveMillis()\n
    '''
def getFromYear():
    '''returns int\n\n
    getFromYear()\n
    '''
def getToYear():
    '''returns int\n\n
    getToYear()\n
    '''
def getMillis():
    '''returns long\n\n
    getMillis()\n
    '''
def getWallOffset():
    '''returns int\n\n
    getWallOffset()\n
    '''
def getStandardOffset():
    '''returns int\n\n
    getStandardOffset()\n
    getStandardOffset()\n
    getStandardOffset(final long n)\n
    getStandardOffset(final long key)\n
    '''
def isTransitionFrom():
    '''returns boolean\n\n
    isTransitionFrom(final Transition transition)\n
    '''
def addRule():
    '''returns None\n\n
    addRule(final Rule rule)\n
    '''
def setUpperLimit():
    '''returns None\n\n
    setUpperLimit(final int iUpperYear, final OfYear iUpperOfYear)\n
    '''
def firstTransition():
    '''returns Transition\n\n
    firstTransition(final long n)\n
    '''
def nextTransition():
    '''returns long\n\n
    nextTransition(final long n, final int n2)\n
    nextTransition(final long n)\n
    nextTransition(long key)\n
    '''
def getUpperLimit():
    '''returns long\n\n
    getUpperLimit(final int n)\n
    '''
def buildTailZone():
    '''returns DSTZone\n\n
    buildTailZone(final String s)\n
    '''
def getOffset():
    '''returns int\n\n
    getOffset(final long n)\n
    getOffset(final long key)\n
    '''
def isFixed():
    '''returns boolean\n\n
    isFixed()\n
    isFixed()\n
    '''
def previousTransition():
    '''returns long\n\n
    previousTransition(long n)\n
    previousTransition(final long key)\n
    '''
def isCachable():
    '''returns boolean\n\n
    isCachable()\n
    '''
