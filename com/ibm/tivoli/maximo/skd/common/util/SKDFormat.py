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
def SKDFormat():
    '''    public SKDFormat(final SKDUserLocaleData skdLocale)
    '''
def stringToDate():
    '''    public Date stringToDate(final String s, final Locale l, final TimeZone tz)
    '''
def parseDateTime():
    '''    public int[] parseDateTime(final String s, final Locale l, final String pattern)
    '''
def stringToInt():
    '''    public int stringToInt(final String s, final Locale l)
    '''
def stringToDateTime():
    '''    public Date stringToDateTime(final String s, final Locale l, final TimeZone tz)
    '''
def getDateOnly():
    '''    public static Date getDateOnly(final Date date)
    '''
def stringToTime():
    '''    public Date stringToTime(final String s, final Locale l, final TimeZone tz)
    '''
def dateTimeToDisplayString():
    '''    public String dateTimeToDisplayString(final Date d, final Locale l, final TimeZone tz)
    public String dateTimeToDisplayString(final Date d, final Locale l)
    '''
def dateTimeToParseString():
    '''    public String dateTimeToParseString(final Date d, final Locale l, final TimeZone tz)
    '''
def dateToString():
    '''    public String dateToString(final Date d, final Locale l, final TimeZone tz)
    '''
def timeToDisplayString():
    '''    public String timeToDisplayString(final Date d, final Locale l, final TimeZone tz)
    '''
def timeToParseString():
    '''    public String timeToParseString(final Date d, final Locale l, final TimeZone tz)
    '''
def stringToBoolean():
    '''    public boolean stringToBoolean(final String s, final Locale l)
    '''
def convertToStoreYNValue():
    '''    public String convertToStoreYNValue(final String val, final Locale l)
    '''
def booleanToString():
    '''    public String booleanToString(final boolean b, final Locale l)
    '''
def doubleToDuration():
    '''    public String doubleToDuration(double d)
    '''
def durationToDouble():
    '''    public double durationToDouble(String s, final Locale l)
    '''
def stringToDouble():
    '''    public double stringToDouble(final String s, final Locale l)
    '''
def getDatePattern():
    '''    public String getDatePattern()
    '''
def getTimePattern():
    '''    public String getTimePattern()
    '''
def dateTimeToString():
    '''    public String dateTimeToString(final Date d, final Locale l, final TimeZone tz)
    '''
def doubleToString():
    '''    public String doubleToString(final double d, final int places, final Locale l, final boolean groupingInFormat)
    '''
