WALL_TIME = "int 0"
STANDARD_TIME = "int 1"
UTC_TIME = "int 2"
def SimpleTimeZone():
'''public SimpleTimeZone(final int rawOffset, final String ID)
public SimpleTimeZone(final int rawOffset, final String ID, final int startMonth, final int startDay, final int startDayOfWeek, final int startTime, final int endMonth, final int endDay, final int endDayOfWeek, final int endTime)
public SimpleTimeZone(final int rawOffset, final String ID, final int startMonth, final int startDay, final int startDayOfWeek, final int startTime, final int startTimeMode, final int endMonth, final int endDay, final int endDayOfWeek, final int endTime, final int endTimeMode, final int dstSavings)
public SimpleTimeZone(final int rawOffset, final String ID, final int startMonth, final int startDay, final int startDayOfWeek, final int startTime, final int endMonth, final int endDay, final int endDayOfWeek, final int endTime, final int dstSavings)
'''
pass
def setID():
'''public void setID(final String ID)
'''
pass
def setRawOffset():
'''public void setRawOffset(final int offsetMillis)
'''
pass
def getRawOffset():
'''public int getRawOffset()
'''
pass
def setStartYear():
'''public void setStartYear(final int year)
'''
pass
def setStartRule():
'''public void setStartRule(final int month, final int dayOfWeekInMonth, final int dayOfWeek, final int time)
public void setStartRule(final int month, final int dayOfMonth, final int time)
public void setStartRule(final int month, final int dayOfMonth, final int dayOfWeek, final int time, final boolean after)
'''
pass
def setEndRule():
'''public void setEndRule(final int month, final int dayOfWeekInMonth, final int dayOfWeek, final int time)
public void setEndRule(final int month, final int dayOfMonth, final int time)
public void setEndRule(final int month, final int dayOfMonth, final int dayOfWeek, final int time, final boolean after)
'''
pass
def setDSTSavings():
'''public void setDSTSavings(final int millisSavedDuringDST)
'''
pass
def getDSTSavings():
'''public int getDSTSavings()
'''
pass
def toString():
'''public String toString()
'''
pass
def getOffset():
'''public int getOffset(final int era, final int year, final int month, final int day, final int dayOfWeek, final int millis)
public int getOffset(final int era, final int year, final int month, final int day, final int dayOfWeek, final int millis, final int monthLength)
'''
pass
def getOffsetFromLocal():
'''public void getOffsetFromLocal(long date, final int nonExistingTimeOpt, final int duplicatedTimeOpt, final int[] offsets)
'''
pass
def useDaylightTime():
'''public boolean useDaylightTime()
'''
pass
def observesDaylightTime():
'''public boolean observesDaylightTime()
'''
pass
def inDaylightTime():
'''public boolean inDaylightTime(final Date date)
'''
pass
def equals():
'''public boolean equals(final Object obj)
'''
pass
def hashCode():
'''public int hashCode()
'''
pass
def clone():
'''public Object clone()
'''
pass
def hasSameRules():
'''public boolean hasSameRules(final TimeZone othr)
'''
pass
def getNextTransition():
'''public TimeZoneTransition getNextTransition(final long base, final boolean inclusive)
'''
pass
def getPreviousTransition():
'''public TimeZoneTransition getPreviousTransition(final long base, final boolean inclusive)
'''
pass
def getTimeZoneRules():
'''public TimeZoneRule[] getTimeZoneRules()
'''
pass
def isFrozen():
'''public boolean isFrozen()
'''
pass
def freeze():
'''public TimeZone freeze()
'''
pass
def cloneAsThawed():
'''public TimeZone cloneAsThawed()
'''
pass
