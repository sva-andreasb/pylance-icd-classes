ALN = "int  0"
UPPER = "int  1"
LOWER = "int  2"
DATE = "int  3"
DATETIME = "int  4"
TIME = "int  5"
INTEGER = "int  6"
SMALLINT = "int  7"
FLOAT = "int  8"
DECIMAL = "int  9"
DURATION = "int  10"
AMOUNT = "int  11"
YORN = "int  12"
GL = "int  13"
LONGALN = "int  14"
CRYPTO = "int  15"
CRYPTOX = "int  16"
CLOB = "int  17"
BLOB = "int  18"
UDTYPE = "int  99"
UNLIMITEDPLACES = "int  8"
TIMESEP = "String  \":\""
DATESEP = "String  \"/\""
YEARCHAR = "char  'y'"
MONTHCHAR = "char  'M'"
DAYCHAR = "char  'd'"
AMCHAR = "char  'a'"
MINCHAR = "char  'm'"
HOUR24CHAR = "char  'H'"
HOUR12CHAR = "char  'h'"
SECONDCHAR = "char  's'"
SEPERATORS = "String  \" /-.:\""
MINSPERHOUR = "double  60.0"
def ():
    '''returns SKDFormat\n\n
    (final SKDUserLocaleData skdLocale)\n
    '''
def stringToDate():
    '''returns Date\n\n
    stringToDate(final String s, final Locale l, final TimeZone tz)\n
    '''
def parseDateTime():
    '''returns int[]\n\n
    parseDateTime(final String s, final Locale l, final String pattern)\n
    '''
def stringToInt():
    '''returns int\n\n
    stringToInt(final String s, final Locale l)\n
    '''
def stringToDateTime():
    '''returns Date\n\n
    stringToDateTime(final String s, final Locale l, final TimeZone tz)\n
    '''
def stringToTime():
    '''returns Date\n\n
    stringToTime(final String s, final Locale l, final TimeZone tz)\n
    '''
def dateTimeToDisplayString():
    '''returns String\n\n
    dateTimeToDisplayString(final Date d, final Locale l, final TimeZone tz)\n
    dateTimeToDisplayString(final Date d, final Locale l)\n
    '''
def dateTimeToParseString():
    '''returns String\n\n
    dateTimeToParseString(final Date d, final Locale l, final TimeZone tz)\n
    '''
def dateToString():
    '''returns String\n\n
    dateToString(final Date d, final Locale l, final TimeZone tz)\n
    '''
def timeToDisplayString():
    '''returns String\n\n
    timeToDisplayString(final Date d, final Locale l, final TimeZone tz)\n
    '''
def timeToParseString():
    '''returns String\n\n
    timeToParseString(final Date d, final Locale l, final TimeZone tz)\n
    '''
def stringToBoolean():
    '''returns boolean\n\n
    stringToBoolean(final String s, final Locale l)\n
    '''
def convertToStoreYNValue():
    '''returns String\n\n
    convertToStoreYNValue(final String val, final Locale l)\n
    '''
def booleanToString():
    '''returns String\n\n
    booleanToString(final boolean b, final Locale l)\n
    '''
def doubleToDuration():
    '''returns String\n\n
    doubleToDuration(double d)\n
    '''
def durationToDouble():
    '''returns double\n\n
    durationToDouble(String s, final Locale l)\n
    '''
def stringToDouble():
    '''returns double\n\n
    stringToDouble(final String s, final Locale l)\n
    '''
def getDatePattern():
    '''returns String\n\n
    getDatePattern()\n
    '''
def getTimePattern():
    '''returns String\n\n
    getTimePattern()\n
    '''
def dateTimeToString():
    '''returns String\n\n
    dateTimeToString(final Date d, final Locale l, final TimeZone tz)\n
    '''
def doubleToString():
    '''returns String\n\n
    doubleToString(final double d, final int places, final Locale l, final boolean groupingInFormat)\n
    '''
