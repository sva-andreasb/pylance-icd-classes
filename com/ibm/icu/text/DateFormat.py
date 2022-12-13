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
YEAR_NAME_FIELD = "int  30"
TIMEZONE_LOCALIZED_GMT_OFFSET_FIELD = "int  31"
TIMEZONE_ISO_FIELD = "int  32"
TIMEZONE_ISO_LOCAL_FIELD = "int  33"
AM_PM_MIDNIGHT_NOON_FIELD = "int  35"
FLEXIBLE_DAY_PERIOD_FIELD = "int  36"
TIME_SEPARATOR = "int  37"
FIELD_COUNT = "int  38"
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
YEAR = "String  \"y\""
QUARTER = "String  \"QQQQ\""
ABBR_QUARTER = "String  \"QQQ\""
YEAR_QUARTER = "String  \"yQQQQ\""
YEAR_ABBR_QUARTER = "String  \"yQQQ\""
MONTH = "String  \"MMMM\""
ABBR_MONTH = "String  \"MMM\""
NUM_MONTH = "String  \"M\""
YEAR_MONTH = "String  \"yMMMM\""
YEAR_ABBR_MONTH = "String  \"yMMM\""
YEAR_NUM_MONTH = "String  \"yM\""
DAY = "String  \"d\""
YEAR_MONTH_DAY = "String  \"yMMMMd\""
YEAR_ABBR_MONTH_DAY = "String  \"yMMMd\""
YEAR_NUM_MONTH_DAY = "String  \"yMd\""
WEEKDAY = "String  \"EEEE\""
ABBR_WEEKDAY = "String  \"E\""
YEAR_MONTH_WEEKDAY_DAY = "String  \"yMMMMEEEEd\""
YEAR_ABBR_MONTH_WEEKDAY_DAY = "String  \"yMMMEd\""
YEAR_NUM_MONTH_WEEKDAY_DAY = "String  \"yMEd\""
MONTH_DAY = "String  \"MMMMd\""
ABBR_MONTH_DAY = "String  \"MMMd\""
NUM_MONTH_DAY = "String  \"Md\""
MONTH_WEEKDAY_DAY = "String  \"MMMMEEEEd\""
ABBR_MONTH_WEEKDAY_DAY = "String  \"MMMEd\""
NUM_MONTH_WEEKDAY_DAY = "String  \"MEd\""
HOUR = "String  \"j\""
HOUR24 = "String  \"H\""
MINUTE = "String  \"m\""
HOUR_MINUTE = "String  \"jm\""
HOUR24_MINUTE = "String  \"Hm\""
SECOND = "String  \"s\""
HOUR_MINUTE_SECOND = "String  \"jms\""
HOUR24_MINUTE_SECOND = "String  \"Hms\""
MINUTE_SECOND = "String  \"ms\""
LOCATION_TZ = "String  \"VVVV\""
GENERIC_TZ = "String  \"vvvv\""
ABBR_GENERIC_TZ = "String  \"v\""
SPECIFIC_TZ = "String  \"zzzz\""
ABBR_SPECIFIC_TZ = "String  \"z\""
ABBR_UTC_TZ = "String  \"ZZZZ\""
STANDALONE_MONTH = "String  \"LLLL\""
ABBR_STANDALONE_MONTH = "String  \"LLL\""
HOUR_MINUTE_GENERIC_TZ = "String  \"jmv\""
HOUR_MINUTE_TZ = "String  \"jmz\""
HOUR_GENERIC_TZ = "String  \"jv\""
HOUR_TZ = "String  \"jz\""
JP_ERA_2019_ROOT = "String  \"Reiwa\""
JP_ERA_2019_JA = "String  \"\u4ee4\u548c\""
JP_ERA_2019_NARROW = "String  \"R\""
def format():
    '''    public final StringBuffer format(final Object obj, final StringBuffer toAppendTo, final FieldPosition fieldPosition)
    public StringBuffer format(final Date date, final StringBuffer toAppendTo, final FieldPosition fieldPosition)
    public final String format(final Date date)
    '''
def parse():
    '''    public Date parse(final String text)
    public Date parse(final String text, final ParsePosition pos)
    '''
def parseObject():
    '''    public Object parseObject(final String source, final ParsePosition pos)
    '''
def getTimeInstance():
    '''    public static final DateFormat getTimeInstance()
    public static final DateFormat getTimeInstance(final int style)
    public static final DateFormat getTimeInstance(final int style, final Locale aLocale)
    public static final DateFormat getTimeInstance(final int style, final ULocale locale)
    public static final DateFormat getTimeInstance(final Calendar cal, final int timeStyle, final Locale locale)
    public static final DateFormat getTimeInstance(final Calendar cal, final int timeStyle, final ULocale locale)
    public static final DateFormat getTimeInstance(final Calendar cal, final int timeStyle)
    '''
def getDateInstance():
    '''    public static final DateFormat getDateInstance()
    public static final DateFormat getDateInstance(final int style)
    public static final DateFormat getDateInstance(final int style, final Locale aLocale)
    public static final DateFormat getDateInstance(final int style, final ULocale locale)
    public static final DateFormat getDateInstance(final Calendar cal, final int dateStyle, final Locale locale)
    public static final DateFormat getDateInstance(final Calendar cal, final int dateStyle, final ULocale locale)
    public static final DateFormat getDateInstance(final Calendar cal, final int dateStyle)
    '''
def getDateTimeInstance():
    '''    public static final DateFormat getDateTimeInstance()
    public static final DateFormat getDateTimeInstance(final int dateStyle, final int timeStyle)
    public static final DateFormat getDateTimeInstance(final int dateStyle, final int timeStyle, final Locale aLocale)
    public static final DateFormat getDateTimeInstance(final int dateStyle, final int timeStyle, final ULocale locale)
    public static final DateFormat getDateTimeInstance(final Calendar cal, final int dateStyle, final int timeStyle, final Locale locale)
    public static final DateFormat getDateTimeInstance(final Calendar cal, final int dateStyle, final int timeStyle, final ULocale locale)
    public static final DateFormat getDateTimeInstance(final Calendar cal, final int dateStyle, final int timeStyle)
    '''
def getInstance():
    '''    public static final DateFormat getInstance()
    public static final DateFormat getInstance(final Calendar cal, final Locale locale)
    public static final DateFormat getInstance(final Calendar cal, final ULocale locale)
    public static final DateFormat getInstance(final Calendar cal)
    '''
def getAvailableLocales():
    '''    public static Locale[] getAvailableLocales()
    '''
def getAvailableULocales():
    '''    public static ULocale[] getAvailableULocales()
    '''
def setCalendar():
    '''    public void setCalendar(final Calendar newCalendar)
    '''
def getCalendar():
    '''    public Calendar getCalendar()
    '''
def setNumberFormat():
    '''    public void setNumberFormat(final NumberFormat newNumberFormat)
    '''
def getNumberFormat():
    '''    public NumberFormat getNumberFormat()
    '''
def setTimeZone():
    '''    public void setTimeZone(final TimeZone zone)
    '''
def getTimeZone():
    '''    public TimeZone getTimeZone()
    '''
def setLenient():
    '''    public void setLenient(final boolean lenient)
    '''
def isLenient():
    '''    public boolean isLenient()
    '''
def setCalendarLenient():
    '''    public void setCalendarLenient(final boolean lenient)
    '''
def isCalendarLenient():
    '''    public boolean isCalendarLenient()
    '''
def setBooleanAttribute():
    '''    public DateFormat setBooleanAttribute(BooleanAttribute key, final boolean value)
    '''
def getBooleanAttribute():
    '''    public boolean getBooleanAttribute(BooleanAttribute key)
    '''
def setContext():
    '''    public void setContext(final DisplayContext context)
    '''
def getContext():
    '''    public DisplayContext getContext(final DisplayContext.Type type)
    '''
def hashCode():
    '''    public int hashCode()
    '''
def equals():
    '''    public boolean equals(final Object obj)
    '''
def clone():
    '''    public Object clone()
    '''
def getInstanceForSkeleton():
    '''    public static final DateFormat getInstanceForSkeleton(final String skeleton)
    public static final DateFormat getInstanceForSkeleton(final String skeleton, final Locale locale)
    public static final DateFormat getInstanceForSkeleton(final String skeleton, final ULocale locale)
    public static final DateFormat getInstanceForSkeleton(final Calendar cal, final String skeleton, final Locale locale)
    public static final DateFormat getInstanceForSkeleton(final Calendar cal, final String skeleton, ULocale locale)
    '''
def getPatternInstance():
    '''    public static final DateFormat getPatternInstance(final String skeleton)
    public static final DateFormat getPatternInstance(final String skeleton, final Locale locale)
    public static final DateFormat getPatternInstance(final String skeleton, final ULocale locale)
    public static final DateFormat getPatternInstance(final Calendar cal, final String skeleton, final Locale locale)
    public static final DateFormat getPatternInstance(final Calendar cal, final String skeleton, final ULocale locale)
    '''
def ofCalendarField():
    '''    public static Field ofCalendarField(final int calendarField)
    '''
def getCalendarField():
    '''    public int getCalendarField()
    '''
