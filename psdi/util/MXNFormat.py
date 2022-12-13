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
BIGINT = "int  19"
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
SPECIALSAVECHARS = "String  \"=: \t\r\n\f#!\""
def stringToDate():
    '''    public static Date stringToDate(final String s)
    public static Date stringToDate(final String s, final ULocale l)
    public static Date stringToDate(final String s, final ULocale l, final TimeZone tz)
    public static Date stringToDate(final String strDate, final String strFormat)
    '''
def dateToString():
    '''    public static String dateToString(final Date d)
    public static String dateToString(final Date d, final ULocale l)
    public static String dateToString(final Date d, final ULocale l, final TimeZone tz)
    '''
def stringToDateTime():
    '''    public static Date stringToDateTime(final String s)
    public static Date stringToDateTime(final String s, final ULocale l)
    public static Date stringToDateTime(final String s, final ULocale l, final TimeZone tz)
    '''
def dateTimeToParseString():
    '''    public static String dateTimeToParseString(final Date d)
    public static String dateTimeToParseString(final Date d, final ULocale l)
    public static String dateTimeToParseString(final Date d, final ULocale l, final com.ibm.icu.util.TimeZone tz)
    '''
def dateTimeToString():
    '''    public static String dateTimeToString(final Date d)
    public static String dateTimeToString(final Date d, final ULocale l)
    public static String dateTimeToString(final Date d, final ULocale l, final TimeZone tz)
    '''
def dateTimeToSQLString():
    '''    public static String dateTimeToSQLString(final Date d)
    '''
def dateToSQLString():
    '''    public static String dateToSQLString(final Date d)
    '''
def getDateOnly():
    '''    public static Date getDateOnly(final Date date)
    '''
def parseDateTime():
    '''    public static int[] parseDateTime(final String s, final ULocale l, final String pattern)
    '''
def setSettingProp():
    '''    public static synchronized void setSettingProp(final String propName, final String propValue)
    '''
