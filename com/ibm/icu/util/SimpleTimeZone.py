WALL_TIME = "int  0"
STANDARD_TIME = "int  1"
UTC_TIME = "int  2"
def ():
    '''returns SimpleTimeZone\n\n
    (final int rawOffset, final String ID)\n
    (final int rawOffset, final String ID, final int startMonth, final int startDay, final int startDayOfWeek, final int startTime, final int endMonth, final int endDay, final int endDayOfWeek, final int endTime)\n
    (final int rawOffset, final String ID, final int startMonth, final int startDay, final int startDayOfWeek, final int startTime, final int startTimeMode, final int endMonth, final int endDay, final int endDayOfWeek, final int endTime, final int endTimeMode, final int dstSavings)\n
    (final int rawOffset, final String ID, final int startMonth, final int startDay, final int startDayOfWeek, final int startTime, final int endMonth, final int endDay, final int endDayOfWeek, final int endTime, final int dstSavings)\n
    '''
def setID():
    '''returns None\n\n
    setID(final String ID)\n
    '''
def setRawOffset():
    '''returns None\n\n
    setRawOffset(final int offsetMillis)\n
    '''
def getRawOffset():
    '''returns int\n\n
    getRawOffset()\n
    '''
def setStartYear():
    '''returns None\n\n
    setStartYear(final int year)\n
    '''
def setStartRule():
    '''returns None\n\n
    setStartRule(final int month, final int dayOfWeekInMonth, final int dayOfWeek, final int time)\n
    setStartRule(final int month, final int dayOfMonth, final int time)\n
    setStartRule(final int month, final int dayOfMonth, final int dayOfWeek, final int time, final boolean after)\n
    '''
def setEndRule():
    '''returns None\n\n
    setEndRule(final int month, final int dayOfWeekInMonth, final int dayOfWeek, final int time)\n
    setEndRule(final int month, final int dayOfMonth, final int time)\n
    setEndRule(final int month, final int dayOfMonth, final int dayOfWeek, final int time, final boolean after)\n
    '''
def setDSTSavings():
    '''returns None\n\n
    setDSTSavings(final int millisSavedDuringDST)\n
    '''
def getDSTSavings():
    '''returns int\n\n
    getDSTSavings()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def getOffset():
    '''returns int\n\n
    getOffset(final int era, final int year, final int month, final int day, final int dayOfWeek, final int millis)\n
    getOffset(final int era, final int year, final int month, final int day, final int dayOfWeek, final int millis, final int monthLength)\n
    '''
def getOffsetFromLocal():
    '''returns None\n\n
    getOffsetFromLocal(long date, final int nonExistingTimeOpt, final int duplicatedTimeOpt, final int[] offsets)\n
    '''
def useDaylightTime():
    '''returns boolean\n\n
    useDaylightTime()\n
    '''
def inDaylightTime():
    '''returns boolean\n\n
    inDaylightTime(final Date date)\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object obj)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def clone():
    '''returns Object\n\n
    clone()\n
    '''
def hasSameRules():
    '''returns boolean\n\n
    hasSameRules(final TimeZone othr)\n
    '''
def getNextTransition():
    '''returns TimeZoneTransition\n\n
    getNextTransition(final long base, final boolean inclusive)\n
    '''
def getPreviousTransition():
    '''returns TimeZoneTransition\n\n
    getPreviousTransition(final long base, final boolean inclusive)\n
    '''
def getTimeZoneRules():
    '''returns TimeZoneRule[]\n\n
    getTimeZoneRules()\n
    '''
