def getOffset():
    '''public int getOffset(final int era, final int year, final int month, final int day, final int dayOfWeek, final int milliseconds)
    public int getOffset(final int era, int year, final int month, final int dom, final int dow, final int millis, final int monthLength)
    public void getOffset(final long date, final boolean local, final int[] offsets)
    '''
def setRawOffset():
    '''public void setRawOffset(final int offsetMillis)
    '''
def clone():
    '''public Object clone()
    '''
def getOffsetFromLocal():
    '''public void getOffsetFromLocal(final long date, final int nonExistingTimeOpt, final int duplicatedTimeOpt, final int[] offsets)
    '''
def getRawOffset():
    '''public int getRawOffset()
    '''
def useDaylightTime():
    '''public boolean useDaylightTime()
    '''
def getDSTSavings():
    '''public int getDSTSavings()
    '''
def inDaylightTime():
    '''public boolean inDaylightTime(final Date date)
    '''
def hasSameRules():
    '''public boolean hasSameRules(final TimeZone other)
    '''
def OlsonTimeZone():
    '''public OlsonTimeZone(final UResourceBundle top, final UResourceBundle res)
    public OlsonTimeZone(final String id)
    '''
def setID():
    '''public void setID(final String id)
    '''
def toString():
    '''public String toString()
    '''
def equals():
    '''public boolean equals(final Object obj)
    '''
def hashCode():
    '''public int hashCode()
    '''
def getNextTransition():
    '''public TimeZoneTransition getNextTransition(final long base, final boolean inclusive)
    '''
def getPreviousTransition():
    '''public TimeZoneTransition getPreviousTransition(final long base, final boolean inclusive)
    '''
def getTimeZoneRules():
    '''public TimeZoneRule[] getTimeZoneRules()
    '''
