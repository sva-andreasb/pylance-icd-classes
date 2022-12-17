ERA_FIELD = "int  0"
YEAR_FIELD = "int  1"
MONTH_FIELD = "int  2"
DATE_FIELD = "int  3"
HOUR_OF_DAY1_FIELD = "int  4"
HOUR_OF_DAY0_FIELD = "int  5"
MINUTE_FIELD = "int  6"
SECOND_FIELD = "int  7"
FRACTIONAL_SECOND_FIELD = "int  8"
MILLISECOND_FIELD = "int  8"
DAY_OF_WEEK_FIELD = "int  9"
DAY_OF_YEAR_FIELD = "int  10"
DAY_OF_WEEK_IN_MONTH_FIELD = "int  11"
WEEK_OF_YEAR_FIELD = "int  12"
WEEK_OF_MONTH_FIELD = "int  13"
AM_PM_FIELD = "int  14"
HOUR1_FIELD = "int  15"
HOUR0_FIELD = "int  16"
TIMEZONE_FIELD = "int  17"
YEAR_WOY_FIELD = "int  18"
DOW_LOCAL_FIELD = "int  19"
EXTENDED_YEAR_FIELD = "int  20"
JULIAN_DAY_FIELD = "int  21"
MILLISECONDS_IN_DAY_FIELD = "int  22"
TIMEZONE_RFC_FIELD = "int  23"
TIMEZONE_GENERIC_FIELD = "int  24"
STANDALONE_DAY_FIELD = "int  25"
STANDALONE_MONTH_FIELD = "int  26"
QUARTER_FIELD = "int  27"
STANDALONE_QUARTER_FIELD = "int  28"
TIMEZONE_SPECIAL_FIELD = "int  29"
FIELD_COUNT = "int  30"
NONE = "int  -1"
FULL = "int  0"
LONG = "int  1"
MEDIUM = "int  2"
SHORT = "int  3"
DEFAULT = "int  2"
RELATIVE = "int  128"
RELATIVE_FULL = "int  128"
RELATIVE_LONG = "int  129"
RELATIVE_MEDIUM = "int  130"
RELATIVE_SHORT = "int  131"
RELATIVE_DEFAULT = "int  130"
MINUTE_SECOND = "String  \"ms\""
HOUR24_MINUTE = "String  \"Hm\""
HOUR24_MINUTE_SECOND = "String  \"Hms\""
HOUR_MINUTE_SECOND = "String  \"hms\""
STANDALONE_MONTH = "String  \"LLLL\""
ABBR_STANDALONE_MONTH = "String  \"LLL\""
YEAR_QUARTER = "String  \"yQQQ\""
YEAR_ABBR_QUARTER = "String  \"yQ\""
HOUR_MINUTE = "String  \"hm\""
YEAR = "String  \"y\""
DAY = "String  \"d\""
NUM_MONTH_WEEKDAY_DAY = "String  \"MEd\""
YEAR_NUM_MONTH = "String  \"yM\""
NUM_MONTH_DAY = "String  \"Md\""
YEAR_NUM_MONTH_WEEKDAY_DAY = "String  \"yMEd\""
ABBR_MONTH_WEEKDAY_DAY = "String  \"MMMEd\""
YEAR_MONTH = "String  \"yMMMM\""
YEAR_ABBR_MONTH = "String  \"yMMM\""
MONTH_DAY = "String  \"MMMMd\""
ABBR_MONTH_DAY = "String  \"MMMd\""
MONTH_WEEKDAY_DAY = "String  \"MMMMEEEEd\""
YEAR_ABBR_MONTH_WEEKDAY_DAY = "String  \"yMMMEd\""
YEAR_MONTH_WEEKDAY_DAY = "String  \"yMMMMEEEEd\""
YEAR_MONTH_DAY = "String  \"yMMMMd\""
YEAR_ABBR_MONTH_DAY = "String  \"yMMMd\""
YEAR_NUM_MONTH_DAY = "String  \"yMd\""
NUM_MONTH = "String  \"M\""
ABBR_MONTH = "String  \"MMM\""
MONTH = "String  \"MMMM\""
HOUR_MINUTE_GENERIC_TZ = "String  \"hmv\""
HOUR_MINUTE_TZ = "String  \"hmz\""
HOUR = "String  \"h\""
HOUR_GENERIC_TZ = "String  \"hv\""
HOUR_TZ = "String  \"hz\""
def format():
    '''returns StringBuffer\n\n
    format(final Date date, final StringBuffer toAppendTo, final FieldPosition fieldPosition)\n
    '''
def parse():
    '''returns Date\n\n
    parse(final String text)\n
    parse(final String text, final ParsePosition pos)\n
    '''
def parseObject():
    '''returns Object\n\n
    parseObject(final String source, final ParsePosition pos)\n
    '''
def setCalendar():
    '''returns None\n\n
    setCalendar(final Calendar newCalendar)\n
    '''
def getCalendar():
    '''returns Calendar\n\n
    getCalendar()\n
    '''
def setNumberFormat():
    '''returns None\n\n
    setNumberFormat(final NumberFormat newNumberFormat)\n
    '''
def getNumberFormat():
    '''returns NumberFormat\n\n
    getNumberFormat()\n
    '''
def setTimeZone():
    '''returns None\n\n
    setTimeZone(final TimeZone zone)\n
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
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object obj)\n
    '''
def clone():
    '''returns Object\n\n
    clone()\n
    '''
def getCalendarField():
    '''returns int\n\n
    getCalendarField()\n
    '''
