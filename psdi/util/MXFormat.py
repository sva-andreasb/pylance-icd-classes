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
GENTIMEZONECHAR = "char  'z'"
RFCTIMEZONECHAR = "char  'Z'"
ISOTIMEZONECHAR = "char  'X'"
SEPERATORS = "String  \" /-.:\""
SEPERATORS_FR = "String  \" /-:\""
MINSPERHOUR = "double  60.0"
SPECIALSAVECHARS = "String  \"=: \t\r\n\f#!\""
def validateDoubleAgainstLocaleFormat():
    '''    public static boolean validateDoubleAgainstLocaleFormat(final String s, final Locale l)
    '''
def validateAmountAgainstLocaleFormat():
    '''    public static boolean validateAmountAgainstLocaleFormat(final String s, final Locale l)
    '''
def validateFloatAgainstLocaleFormat():
    '''    public static boolean validateFloatAgainstLocaleFormat(final String s, final Locale l)
    '''
def validateEnteredValueAgainstLocaleFormat():
    '''    public static boolean validateEnteredValueAgainstLocaleFormat(final String s, final Locale l, final String regEx)
    '''
def getAmountRegex():
    '''    public static String getAmountRegex(final Locale locale)
    '''
def stringToInt():
    '''    public static int stringToInt(final String s)
    public static int stringToInt(String s, final Locale l)
    '''
def stringToIntAsBindNumber():
    '''    public static int stringToIntAsBindNumber(String s)
    '''
def stringToLong():
    '''    public static long stringToLong(final String s)
    public static long stringToLong(String s, final Locale l)
    '''
def intToString():
    '''    public static String intToString(final int i)
    public static String intToString(final int i, final Locale l)
    '''
def longToString():
    '''    public static String longToString(final long i)
    public static String longToString(final long i, final Locale l)
    '''
def stringToAmount():
    '''    public static double stringToAmount(final String s)
    public static double stringToAmount(final String s, final Locale l)
    '''
def amountToString():
    '''    public static String amountToString(final double d)
    public static String amountToString(final double d, final int places)
    public static String amountToString(final double d, final int places, final Locale l)
    '''
def stringToDouble():
    '''    public static double stringToDouble(final String s, Locale l)
    public static double stringToDouble(final String s)
    public static double stringToDouble(String s, final Locale l, final boolean userUIMod)
    '''
def doubleToString():
    '''    public static String doubleToString(final double d)
    public static String doubleToString(final double d, final Locale l)
    public static String doubleToString(final double d, final int places)
    public static String doubleToString(final double d, final int places, final Locale l)
    public static String doubleToString(final double d, final int places, final Locale l, final boolean groupingInFormat)
    '''
def durationToDouble():
    '''    public static double durationToDouble(final String s)
    public static double durationToDouble(String s, final Locale l)
    '''
def doubleToDuration():
    '''    public static String doubleToDuration(final double d)
    public static String doubleToDuration(double d, final Locale l)
    '''
def stringToBoolean():
    '''    public static boolean stringToBoolean(final String s)
    public static boolean stringToBoolean(final String s, final Locale l)
    '''
def booleanToString():
    '''    public static String booleanToString(final boolean b)
    public static String booleanToString(final boolean b, final Locale l)
    '''
def booleanToInt():
    '''    public static int booleanToInt(final boolean b)
    '''
def booleanToDouble():
    '''    public static double booleanToDouble(final boolean b)
    '''
def booleanToLong():
    '''    public static long booleanToLong(final boolean b)
    '''
def stringToDate():
    '''    public static Date stringToDate(final String s)
    public static Date stringToDate(final String s, final Locale l)
    public static Date stringToDate(final String s, final Locale l, TimeZone tz)
    public static Date stringToDate(final String strDate, final String strFormat)
    '''
def dateTimeToString():
    '''    public static String dateTimeToString(final Date date, final String dateFormat, final Locale l, final TimeZone tz)
    public static String dateTimeToString(final Date d)
    public static String dateTimeToString(final Date d, final Locale l)
    public static String dateTimeToString(final Date d, final Locale l, final TimeZone tz)
    '''
def sqlWindowsStringToDateTime():
    '''    public static Date sqlWindowsStringToDateTime(final String s)
    '''
def jmigStringToDateTime():
    '''    public static Date jmigStringToDateTime(final String s)
    '''
def dateToString():
    '''    public static String dateToString(final Date d)
    public static String dateToString(final Date d, final Locale l)
    public static String dateToString(final Date d, final Locale l, final TimeZone tz)
    '''
def stringToDateTime():
    '''    public static Date stringToDateTime(final String s)
    public static Date stringToDateTime(final String s, final Locale l)
    public static Date stringToDateTime(final String s, final Locale l, TimeZone tz)
    '''
def dateTimeToParseString():
    '''    public static String dateTimeToParseString(final Date d)
    public static String dateTimeToParseString(final Date d, final Locale l)
    public static String dateTimeToParseString(final Date d, final Locale l, final TimeZone tz)
    '''
def dateTimeToSQLString():
    '''    public static String dateTimeToSQLString(final Date d)
    '''
def dateToSQLString():
    '''    public static String dateToSQLString(final Date d)
    '''
def timeToSQLString():
    '''    public static String timeToSQLString(final Date d)
    '''
def stringToTime():
    '''    public static Date stringToTime(final String s)
    public static Date stringToTime(final String s, final Locale l)
    public static Date stringToTime(final String s, final Locale l, TimeZone tz)
    '''
def timeToParsetring():
    '''    public static String timeToParsetring(final Date d)
    '''
def timeToParseString():
    '''    public static String timeToParseString(final Date d, final Locale l)
    public static String timeToParseString(final Date d, final Locale l, final TimeZone tz)
    '''
def timeToString():
    '''    public static String timeToString(final Date d)
    public static String timeToString(final Date d, final Locale l)
    public static String timeToString(final Date d, final Locale l, final TimeZone tz)
    '''
def getDateOnly():
    '''    public static Date getDateOnly(final Date date)
    '''
def getDateTimeHHMMOnly():
    '''    public static Date getDateTimeHHMMOnly(final Date date)
    '''
def getMaxTypeAsInt():
    '''    public static int getMaxTypeAsInt(final String type)
    '''
def parseDateTime():
    '''    public static int[] parseDateTime(String s, final Locale l, String pattern)
    '''
def isTimePartEntered():
    '''    public static boolean isTimePartEntered(final String s, final Locale l)
    '''
def getStoreYesValue():
    '''    public static String getStoreYesValue()
    '''
def getStoreNoValue():
    '''    public static String getStoreNoValue()
    '''
def getDisplayYesValue():
    '''    public static String getDisplayYesValue(final Locale l)
    '''
def getDisplayNoValue():
    '''    public static String getDisplayNoValue(final Locale l)
    '''
def convertToStoreYNValue():
    '''    public static String convertToStoreYNValue(final String val, final Locale l)
    '''
def clobToString():
    '''    public static String clobToString(final Clob c)
    '''
def blobToBytes():
    '''    public static byte[] blobToBytes(final Blob b)
    '''
def getDatePattern():
    '''    public static String getDatePattern(final Locale l)
    '''
def getTimePattern():
    '''    public static String getTimePattern(final Locale l)
    '''
def getDisplayTimePattern():
    '''    public static String getDisplayTimePattern(final Locale l)
    '''
def getDateTimePattern():
    '''    public static String getDateTimePattern(final Locale l)
    '''
def supports24Hours():
    '''    public static boolean supports24Hours(final Locale l)
    '''
def dateTimePartToPosition():
    '''    public static int dateTimePartToPosition(final int tokennum, final String pattern)
    '''
def stringToCodepoints():
    '''    public static String stringToCodepoints(final String theString, final boolean escapeSpace, final boolean escapeUnicode)
    '''
def setSettingProp():
    '''    public static synchronized void setSettingProp(final String propName, final String propValue)
    '''
def toHex():
    '''    public static char toHex(final int nibble)
    '''
def isValidChar():
    '''    public static boolean isValidChar(final String checkString)
    '''
def getConvertedTypes():
    '''    public static Map<String, String[]> getConvertedTypes()
    '''
def getRepresentedTypes():
    '''    public static Map<String, String[]> getRepresentedTypes()
    '''
def formatHasTimeZone():
    '''    public static boolean formatHasTimeZone(final String format)
    '''
def formatRemoveTimeZone():
    '''    public static String formatRemoveTimeZone(final String format)
    '''
def stringToTimeZone():
    '''    public static TimeZone stringToTimeZone(final String d, final Locale l, final String timeFormat, final TimeZone defaultTZ)
    '''
