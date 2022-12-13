WALL_TIME = "int  0"
STANDARD_TIME = "int  1"
UTC_TIME = "int  2"
def SimpleTimeZone():
    '''    public SimpleTimeZone(final int rawOffset, final String ID)
    public SimpleTimeZone(final int rawOffset, final String ID, final int startMonth, final int startDay, final int startDayOfWeek, final int startTime, final int endMonth, final int endDay, final int endDayOfWeek, final int endTime)
    public SimpleTimeZone(final int rawOffset, final String ID, final int startMonth, final int startDay, final int startDayOfWeek, final int startTime, final int startTimeMode, final int endMonth, final int endDay, final int endDayOfWeek, final int endTime, final int endTimeMode, final int dstSavings)
    public SimpleTimeZone(final int rawOffset, final String ID, final int startMonth, final int startDay, final int startDayOfWeek, final int startTime, final int endMonth, final int endDay, final int endDayOfWeek, final int endTime, final int dstSavings)
    '''
def setID():
    '''    public void setID(final String ID)
    '''
def setRawOffset():
    '''    public void setRawOffset(final int offsetMillis)
    '''
def getRawOffset():
    '''    public int getRawOffset()
    '''
def setStartYear():
    '''    public void setStartYear(final int year)
    '''
def setStartRule():
    '''    public void setStartRule(final int month, final int dayOfWeekInMonth, final int dayOfWeek, final int time)
    public void setStartRule(final int month, final int dayOfMonth, final int time)
    public void setStartRule(final int month, final int dayOfMonth, final int dayOfWeek, final int time, final boolean after)
    '''
def setEndRule():
    '''    public void setEndRule(final int month, final int dayOfWeekInMonth, final int dayOfWeek, final int time)
    public void setEndRule(final int month, final int dayOfMonth, final int time)
    public void setEndRule(final int month, final int dayOfMonth, final int dayOfWeek, final int time, final boolean after)
    '''
def setDSTSavings():
    '''    public void setDSTSavings(final int millisSavedDuringDST)
    '''
def getDSTSavings():
    '''    public int getDSTSavings()
    '''
def toString():
    '''    public String toString()
    '''
def getOffset():
    '''    public int getOffset(final int era, final int year, final int month, final int day, final int dayOfWeek, final int millis)
    public int getOffset(final int era, final int year, final int month, final int day, final int dayOfWeek, final int millis, final int monthLength)
    '''
def getOffsetFromLocal():
    '''    public void getOffsetFromLocal(long date, final int nonExistingTimeOpt, final int duplicatedTimeOpt, final int[] offsets)
    '''
def useDaylightTime():
    '''    public boolean useDaylightTime()
    '''
def observesDaylightTime():
    '''    public boolean observesDaylightTime()
    '''
def inDaylightTime():
    '''    public boolean inDaylightTime(final Date date)
    '''
def equals():
    '''    public boolean equals(final Object obj)
    '''
def hashCode():
    '''    public int hashCode()
    '''
def clone():
    '''    public Object clone()
    '''
def hasSameRules():
    '''    public boolean hasSameRules(final TimeZone othr)
    '''
def getNextTransition():
    '''    public TimeZoneTransition getNextTransition(final long base, final boolean inclusive)
    '''
def getPreviousTransition():
    '''    public TimeZoneTransition getPreviousTransition(final long base, final boolean inclusive)
    '''
def getTimeZoneRules():
    '''    public TimeZoneRule[] getTimeZoneRules()
    '''
def isFrozen():
    '''    public boolean isFrozen()
    '''
def freeze():
    '''    public TimeZone freeze()
    '''
def cloneAsThawed():
    '''    public TimeZone cloneAsThawed()
    '''
