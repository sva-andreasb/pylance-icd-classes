def TimeArrayTimeZoneRule():
    '''public TimeArrayTimeZoneRule(final String name, final int rawOffset, final int dstSavings, final long[] startTimes, final int timeType)
    '''
def getStartTimes():
    '''public long[] getStartTimes()
    '''
def getTimeType():
    '''public int getTimeType()
    '''
def getFirstStart():
    '''public Date getFirstStart(final int prevRawOffset, final int prevDSTSavings)
    '''
def getFinalStart():
    '''public Date getFinalStart(final int prevRawOffset, final int prevDSTSavings)
    '''
def getNextStart():
    '''public Date getNextStart(final long base, final int prevOffset, final int prevDSTSavings, final boolean inclusive)
    '''
def getPreviousStart():
    '''public Date getPreviousStart(final long base, final int prevOffset, final int prevDSTSavings, final boolean inclusive)
    '''
def isEquivalentTo():
    '''public boolean isEquivalentTo(final TimeZoneRule other)
    '''
def isTransitionRule():
    '''public boolean isTransitionRule()
    '''
def toString():
    '''public String toString()
    '''
