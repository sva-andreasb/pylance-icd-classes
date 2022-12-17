def getOffset():
    '''returns None\n\n
    getOffset(final int era, final int year, final int month, final int day, final int dayOfWeek, final int milliseconds)\n
    getOffset(final int era, int year, final int month, final int dom, final int dow, final int millis, final int monthLength)\n
    getOffset(final long date, final boolean local, final int[] offsets)\n
    '''
def setRawOffset():
    '''returns None\n\n
    setRawOffset(final int offsetMillis)\n
    '''
def clone():
    '''returns Object\n\n
    clone()\n
    '''
def getOffsetFromLocal():
    '''returns None\n\n
    getOffsetFromLocal(final long date, final int nonExistingTimeOpt, final int duplicatedTimeOpt, final int[] offsets)\n
    '''
def getRawOffset():
    '''returns int\n\n
    getRawOffset()\n
    '''
def useDaylightTime():
    '''returns boolean\n\n
    useDaylightTime()\n
    '''
def getDSTSavings():
    '''returns int\n\n
    getDSTSavings()\n
    '''
def inDaylightTime():
    '''returns boolean\n\n
    inDaylightTime(final Date date)\n
    '''
def hasSameRules():
    '''returns boolean\n\n
    hasSameRules(final TimeZone other)\n
    '''
def ():
    '''returns OlsonTimeZone\n\n
    (final UResourceBundle top, final UResourceBundle res)\n
    (final String id)\n
    '''
def setID():
    '''returns None\n\n
    setID(final String id)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object obj)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
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
