def ():
    '''returns InitialTimeZoneRule\n\n
    (final String name, final int rawOffset, final int dstSavings)\n
    '''
def isEquivalentTo():
    '''returns boolean\n\n
    isEquivalentTo(final TimeZoneRule other)\n
    '''
def getFinalStart():
    '''returns Date\n\n
    getFinalStart(final int prevRawOffset, final int prevDSTSavings)\n
    '''
def getFirstStart():
    '''returns Date\n\n
    getFirstStart(final int prevRawOffset, final int prevDSTSavings)\n
    '''
def getNextStart():
    '''returns Date\n\n
    getNextStart(final long base, final int prevRawOffset, final int prevDSTSavings, final boolean inclusive)\n
    '''
def getPreviousStart():
    '''returns Date\n\n
    getPreviousStart(final long base, final int prevRawOffset, final int prevDSTSavings, final boolean inclusive)\n
    '''
def isTransitionRule():
    '''returns boolean\n\n
    isTransitionRule()\n
    '''
