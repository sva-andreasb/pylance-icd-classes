def getOffset():
'''public int getOffset(final int era, final int year, final int month, final int day, final int dayOfWeek, final int milliseconds)
public int getOffset(final int era, int year, final int month, final int dom, final int dow, final int millis, final int monthLength)
public void getOffset(final long date, final boolean local, final int[] offsets)
'''
pass
def setRawOffset():
'''public void setRawOffset(final int offsetMillis)
'''
pass
def clone():
'''public Object clone()
'''
pass
def getOffsetFromLocal():
'''public void getOffsetFromLocal(final long date, final int nonExistingTimeOpt, final int duplicatedTimeOpt, final int[] offsets)
'''
pass
def getRawOffset():
'''public int getRawOffset()
'''
pass
def useDaylightTime():
'''public boolean useDaylightTime()
'''
pass
def getDSTSavings():
'''public int getDSTSavings()
'''
pass
def inDaylightTime():
'''public boolean inDaylightTime(final Date date)
'''
pass
def hasSameRules():
'''public boolean hasSameRules(final TimeZone other)
'''
pass
def OlsonTimeZone():
'''public OlsonTimeZone(final UResourceBundle top, final UResourceBundle res)
public OlsonTimeZone(final String id)
'''
pass
def setID():
'''public void setID(final String id)
'''
pass
def toString():
'''public String toString()
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
