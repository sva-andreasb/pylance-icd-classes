def ():
    '''returns TimeArrayTimeZoneRule\n\n
    (final String name, final int rawOffset, final int dstSavings, final long[] startTimes, final int timeType)\n
    '''
def getStartTimes():
    '''returns long[]\n\n
    getStartTimes()\n
    '''
def getTimeType():
    '''returns int\n\n
    getTimeType()\n
    '''
def getFirstStart():
    '''returns Date\n\n
    getFirstStart(final int prevRawOffset, final int prevDSTSavings)\n
    '''
def getFinalStart():
    '''returns Date\n\n
    getFinalStart(final int prevRawOffset, final int prevDSTSavings)\n
    '''
def getNextStart():
    '''returns Date\n\n
    getNextStart(final long base, final int prevOffset, final int prevDSTSavings, final boolean inclusive)\n
    '''
def getPreviousStart():
    '''returns Date\n\n
    getPreviousStart(final long base, final int prevOffset, final int prevDSTSavings, final boolean inclusive)\n
    '''
def isEquivalentTo():
    '''returns boolean\n\n
    isEquivalentTo(final TimeZoneRule other)\n
    '''
def isTransitionRule():
    '''returns boolean\n\n
    isTransitionRule()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
