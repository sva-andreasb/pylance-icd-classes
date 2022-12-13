JAVA_TIME = "int 0"
UNIX_TIME = "int 1"
ICU4C_TIME = "int 2"
WINDOWS_FILE_TIME = "int 3"
DOTNET_DATE_TIME = "int 4"
MAC_OLD_TIME = "int 5"
MAC_TIME = "int 6"
EXCEL_TIME = "int 7"
DB2_TIME = "int 8"
UNIX_MICROSECONDS_TIME = "int 9"
MAX_SCALE = "int 10"
UNITS_VALUE = "int 0"
EPOCH_OFFSET_VALUE = "int 1"
FROM_MIN_VALUE = "int 2"
FROM_MAX_VALUE = "int 3"
TO_MIN_VALUE = "int 4"
TO_MAX_VALUE = "int 5"
EPOCH_OFFSET_PLUS_1_VALUE = "int 6"
EPOCH_OFFSET_MINUS_1_VALUE = "int 7"
UNITS_ROUND_VALUE = "int 8"
MIN_ROUND_VALUE = "int 9"
MAX_ROUND_VALUE = "int 10"
MAX_SCALE_VALUE = "int 11"
def from():
'''public static long from(final long otherTime, final int timeScale)
'''
pass
def bigDecimalFrom():
'''public static BigDecimal bigDecimalFrom(final double otherTime, final int timeScale)
public static BigDecimal bigDecimalFrom(final long otherTime, final int timeScale)
public static BigDecimal bigDecimalFrom(final BigDecimal otherTime, final int timeScale)
'''
pass
def toLong():
'''public static long toLong(final long universalTime, final int timeScale)
'''
pass
def toBigDecimal():
'''public static BigDecimal toBigDecimal(final long universalTime, final int timeScale)
public static BigDecimal toBigDecimal(final BigDecimal universalTime, final int timeScale)
'''
pass
def getTimeScaleValue():
'''public static long getTimeScaleValue(final int scale, final int value)
'''
pass
def toBigDecimalTrunc():
'''public static BigDecimal toBigDecimalTrunc(final BigDecimal universalTime, final int timeScale)
'''
pass
