def getOffset():
    '''returns None\n\n
    getOffset(final int era, final int year, final int month, final int day, final int dayOfWeek, final int milliseconds)\n
    getOffset(final long date, final boolean local, final int[] offsets)\n
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
def getTZURL():
    '''returns String\n\n
    getTZURL()\n
    '''
def setTZURL():
    '''returns None\n\n
    setTZURL(final String url)\n
    '''
def getLastModified():
    '''returns Date\n\n
    getLastModified()\n
    '''
def setLastModified():
    '''returns None\n\n
    setLastModified(final Date date)\n
    '''
def write():
    '''returns None\n\n
    write(final Writer writer)\n
    write(final Writer writer, final long start)\n
    '''
def writeSimple():
    '''returns None\n\n
    writeSimple(final Writer writer, final long time)\n
    '''
def getNextTransition():
    '''returns TimeZoneTransition\n\n
    getNextTransition(final long base, final boolean inclusive)\n
    '''
def getPreviousTransition():
    '''returns TimeZoneTransition\n\n
    getPreviousTransition(final long base, final boolean inclusive)\n
    '''
def hasEquivalentTransitions():
    '''returns boolean\n\n
    hasEquivalentTransitions(final TimeZone other, final long start, final long end)\n
    '''
def getTimeZoneRules():
    '''returns TimeZoneRule[]\n\n
    getTimeZoneRules()\n
    getTimeZoneRules(final long start)\n
    '''
def clone():
    '''returns Object\n\n
    clone()\n
    '''
