def RuleBasedTimeZone():
'''public RuleBasedTimeZone(final String id, final InitialTimeZoneRule initialRule)
'''
pass
def addTransitionRule():
'''public void addTransitionRule(final TimeZoneRule rule)
'''
pass
def getOffset():
'''public int getOffset(final int era, int year, final int month, final int day, final int dayOfWeek, final int milliseconds)
public void getOffset(final long time, final boolean local, final int[] offsets)
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
def getTimeZoneRules():
'''public TimeZoneRule[] getTimeZoneRules()
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
