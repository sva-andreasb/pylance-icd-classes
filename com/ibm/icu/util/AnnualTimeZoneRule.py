MAX_YEAR = "int  Integer.MAX_VALUE"
def ():
    '''returns AnnualTimeZoneRule\n\n
    (final String name, final int rawOffset, final int dstSavings, final DateTimeRule dateTimeRule, final int startYear, final int endYear)\n
    '''
def getRule():
    '''returns DateTimeRule\n\n
    getRule()\n
    '''
def getStartYear():
    '''returns int\n\n
    getStartYear()\n
    '''
def getEndYear():
    '''returns int\n\n
    getEndYear()\n
    '''
def getStartInYear():
    '''returns Date\n\n
    getStartInYear(final int year, final int prevRawOffset, final int prevDSTSavings)\n
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
    getNextStart(final long base, final int prevRawOffset, final int prevDSTSavings, final boolean inclusive)\n
    '''
def getPreviousStart():
    '''returns Date\n\n
    getPreviousStart(final long base, final int prevRawOffset, final int prevDSTSavings, final boolean inclusive)\n
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
