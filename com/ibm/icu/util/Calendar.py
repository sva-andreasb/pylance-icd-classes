ERA = "int  0"
YEAR = "int  1"
MONTH = "int  2"
WEEK_OF_YEAR = "int  3"
WEEK_OF_MONTH = "int  4"
DATE = "int  5"
DAY_OF_MONTH = "int  5"
DAY_OF_YEAR = "int  6"
DAY_OF_WEEK = "int  7"
DAY_OF_WEEK_IN_MONTH = "int  8"
AM_PM = "int  9"
HOUR = "int  10"
HOUR_OF_DAY = "int  11"
MINUTE = "int  12"
SECOND = "int  13"
MILLISECOND = "int  14"
ZONE_OFFSET = "int  15"
DST_OFFSET = "int  16"
YEAR_WOY = "int  17"
DOW_LOCAL = "int  18"
EXTENDED_YEAR = "int  19"
JULIAN_DAY = "int  20"
MILLISECONDS_IN_DAY = "int  21"
IS_LEAP_MONTH = "int  22"
SUNDAY = "int  1"
MONDAY = "int  2"
TUESDAY = "int  3"
WEDNESDAY = "int  4"
THURSDAY = "int  5"
FRIDAY = "int  6"
SATURDAY = "int  7"
JANUARY = "int  0"
FEBRUARY = "int  1"
MARCH = "int  2"
APRIL = "int  3"
MAY = "int  4"
JUNE = "int  5"
JULY = "int  6"
AUGUST = "int  7"
SEPTEMBER = "int  8"
OCTOBER = "int  9"
NOVEMBER = "int  10"
DECEMBER = "int  11"
UNDECIMBER = "int  12"
AM = "int  0"
PM = "int  1"
WEEKDAY = "int  0"
WEEKEND = "int  1"
WEEKEND_ONSET = "int  2"
WEEKEND_CEASE = "int  3"
def getTimeInMillis():
    '''returns long\n\n
    getTimeInMillis()\n
    '''
def setTimeInMillis():
    '''returns None\n\n
    setTimeInMillis(long millis)\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object obj)\n
    '''
def isEquivalentTo():
    '''returns boolean\n\n
    isEquivalentTo(final Calendar other)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def before():
    '''returns boolean\n\n
    before(final Object when)\n
    '''
def after():
    '''returns boolean\n\n
    after(final Object when)\n
    '''
def getActualMaximum():
    '''returns int\n\n
    getActualMaximum(final int field)\n
    '''
def getActualMinimum():
    '''returns int\n\n
    getActualMinimum(final int field)\n
    '''
def roll():
    '''returns None\n\n
    roll(final int field, final int amount)\n
    '''
def add():
    '''returns None\n\n
    add(final int field, final int amount)\n
    '''
def getDisplayName():
    '''returns String\n\n
    getDisplayName(final Locale loc)\n
    getDisplayName(final ULocale loc)\n
    '''
def compareTo():
    '''returns int\n\n
    compareTo(final Calendar that)\n
    '''
def getDateTimeFormat():
    '''returns DateFormat\n\n
    getDateTimeFormat(final int dateStyle, final int timeStyle, final Locale loc)\n
    getDateTimeFormat(final int dateStyle, final int timeStyle, final ULocale loc)\n
    '''
def fieldDifference():
    '''returns int\n\n
    fieldDifference(final Date when, final int field)\n
    '''
def setTimeZone():
    '''returns None\n\n
    setTimeZone(final TimeZone value)\n
    '''
def getTimeZone():
    '''returns TimeZone\n\n
    getTimeZone()\n
    '''
def setLenient():
    '''returns None\n\n
    setLenient(final boolean lenient)\n
    '''
def isLenient():
    '''returns boolean\n\n
    isLenient()\n
    '''
def setFirstDayOfWeek():
    '''returns None\n\n
    setFirstDayOfWeek(final int value)\n
    '''
def getFirstDayOfWeek():
    '''returns int\n\n
    getFirstDayOfWeek()\n
    '''
def setMinimalDaysInFirstWeek():
    '''returns None\n\n
    setMinimalDaysInFirstWeek(int value)\n
    '''
def getMinimalDaysInFirstWeek():
    '''returns int\n\n
    getMinimalDaysInFirstWeek()\n
    '''
def getDayOfWeekType():
    '''returns int\n\n
    getDayOfWeekType(final int dayOfWeek)\n
    '''
def getWeekendTransition():
    '''returns int\n\n
    getWeekendTransition(final int dayOfWeek)\n
    '''
def isWeekend():
    '''returns boolean\n\n
    isWeekend(final Date date)\n
    isWeekend()\n
    '''
def clone():
    '''returns Object\n\n
    clone()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def getType():
    '''returns String\n\n
    getType()\n
    '''
def visible():
    '''returns boolean\n\n
    visible()\n
    '''
def createCalendar():
    '''returns Calendar\n\n
    createCalendar(final ULocale loc)\n
    '''
def ():
    '''returns WeekData\n\n
    (final String[] patterns, final String[] overrides)\n
    (final int fdow, final int mdifw, final int weekendOnset, final int weekendOnsetMillis, final int weekendCease, final int weekendCeaseMillis, final ULocale actualLoc)\n
    '''
def getPatternString():
    '''returns String\n\n
    getPatternString()\n
    '''
def getOverrideString():
    '''returns String\n\n
    getOverrideString()\n
    '''
def getCalendar():
    '''returns Calendar\n\n
    getCalendar()\n
    '''
def getLocale():
    '''returns ULocale\n\n
    getLocale()\n
    '''
def getDateFormatSymbols():
    '''returns DateFormatSymbols\n\n
    getDateFormatSymbols()\n
    '''
