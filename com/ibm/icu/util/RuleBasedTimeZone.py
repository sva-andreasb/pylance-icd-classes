def ():
    '''returns RuleBasedTimeZone\n\n
    (final String id, final InitialTimeZoneRule initialRule)\n
    '''
def addTransitionRule():
    '''returns None\n\n
    addTransitionRule(final TimeZoneRule rule)\n
    '''
def getOffset():
    '''returns None\n\n
    getOffset(final int era, int year, final int month, final int day, final int dayOfWeek, final int milliseconds)\n
    getOffset(final long time, final boolean local, final int[] offsets)\n
    '''
def getOffsetFromLocal():
    '''returns None\n\n
    getOffsetFromLocal(final long date, final int nonExistingTimeOpt, final int duplicatedTimeOpt, final int[] offsets)\n
    '''
def getRawOffset():
    '''returns int\n\n
    getRawOffset()\n
    '''
def inDaylightTime():
    '''returns boolean\n\n
    inDaylightTime(final Date date)\n
    '''
def setRawOffset():
    '''returns None\n\n
    setRawOffset(final int offsetMillis)\n
    '''
def useDaylightTime():
    '''returns boolean\n\n
    useDaylightTime()\n
    '''
def hasSameRules():
    '''returns boolean\n\n
    hasSameRules(final TimeZone other)\n
    '''
def getTimeZoneRules():
    '''returns TimeZoneRule[]\n\n
    getTimeZoneRules()\n
    '''
def getNextTransition():
    '''returns TimeZoneTransition\n\n
    getNextTransition(final long base, final boolean inclusive)\n
    '''
def getPreviousTransition():
    '''returns TimeZoneTransition\n\n
    getPreviousTransition(final long base, final boolean inclusive)\n
    '''
def clone():
    '''returns Object\n\n
    clone()\n
    '''
