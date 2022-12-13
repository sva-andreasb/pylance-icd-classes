def create():
'''public static VTimeZone create(final String tzid)
public static VTimeZone create(final Reader reader)
'''
pass
def getOffset():
'''public int getOffset(final int era, final int year, final int month, final int day, final int dayOfWeek, final int milliseconds)
public void getOffset(final long date, final boolean local, final int[] offsets)
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
def inDaylightTime():
'''public boolean inDaylightTime(final Date date)
'''
pass
def setRawOffset():
'''public void setRawOffset(final int offsetMillis)
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
def hasSameRules():
'''public boolean hasSameRules(final TimeZone other)
'''
pass
def getTZURL():
'''public String getTZURL()
'''
pass
def setTZURL():
'''public void setTZURL(final String url)
'''
pass
def getLastModified():
'''public Date getLastModified()
'''
pass
def setLastModified():
'''public void setLastModified(final Date date)
'''
pass
def write():
'''public void write(final Writer writer)
public void write(final Writer writer, final long start)
'''
pass
def writeSimple():
'''public void writeSimple(final Writer writer, final long time)
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
def hasEquivalentTransitions():
'''public boolean hasEquivalentTransitions(final TimeZone other, final long start, final long end)
'''
pass
def getTimeZoneRules():
'''public TimeZoneRule[] getTimeZoneRules()
public TimeZoneRule[] getTimeZoneRules(final long start)
'''
pass
def clone():
'''public Object clone()
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
