MILLIS_PER_SECOND = "long  1000L"
MILLIS_PER_MINUTE = "long  60000L"
MILLIS_PER_HOUR = "long  3600000L"
MILLIS_PER_DAY = "long  86400000L"
SEMI_MONTH = "int  1001"
RANGE_WEEK_SUNDAY = "int  1"
RANGE_WEEK_MONDAY = "int  2"
RANGE_WEEK_RELATIVE = "int  3"
RANGE_WEEK_CENTER = "int  4"
RANGE_MONTH_SUNDAY = "int  5"
RANGE_MONTH_MONDAY = "int  6"
def isSameDay():
    '''public static boolean isSameDay(final Date date1, final Date date2)
    public static boolean isSameDay(final Calendar cal1, final Calendar cal2)
    '''
def isSameInstant():
    '''public static boolean isSameInstant(final Date date1, final Date date2)
    public static boolean isSameInstant(final Calendar cal1, final Calendar cal2)
    '''
def isSameLocalTime():
    '''public static boolean isSameLocalTime(final Calendar cal1, final Calendar cal2)
    '''
def parseDate():
    '''public static Date parseDate(final String str, final String... parsePatterns)
    public static Date parseDate(final String str, final Locale locale, final String... parsePatterns)
    '''
def parseDateStrictly():
    '''public static Date parseDateStrictly(final String str, final String... parsePatterns)
    public static Date parseDateStrictly(final String str, final Locale locale, final String... parsePatterns)
    '''
def addYears():
    '''public static Date addYears(final Date date, final int amount)
    '''
def addMonths():
    '''public static Date addMonths(final Date date, final int amount)
    '''
def addWeeks():
    '''public static Date addWeeks(final Date date, final int amount)
    '''
def addDays():
    '''public static Date addDays(final Date date, final int amount)
    '''
def addHours():
    '''public static Date addHours(final Date date, final int amount)
    '''
def addMinutes():
    '''public static Date addMinutes(final Date date, final int amount)
    '''
def addSeconds():
    '''public static Date addSeconds(final Date date, final int amount)
    '''
def addMilliseconds():
    '''public static Date addMilliseconds(final Date date, final int amount)
    '''
def setYears():
    '''public static Date setYears(final Date date, final int amount)
    '''
def setMonths():
    '''public static Date setMonths(final Date date, final int amount)
    '''
def setDays():
    '''public static Date setDays(final Date date, final int amount)
    '''
def setHours():
    '''public static Date setHours(final Date date, final int amount)
    '''
def setMinutes():
    '''public static Date setMinutes(final Date date, final int amount)
    '''
def setSeconds():
    '''public static Date setSeconds(final Date date, final int amount)
    '''
def setMilliseconds():
    '''public static Date setMilliseconds(final Date date, final int amount)
    '''
def toCalendar():
    '''public static Calendar toCalendar(final Date date)
    '''
def round():
    '''public static Date round(final Date date, final int field)
    public static Calendar round(final Calendar date, final int field)
    public static Date round(final Object date, final int field)
    '''
def truncate():
    '''public static Date truncate(final Date date, final int field)
    public static Calendar truncate(final Calendar date, final int field)
    public static Date truncate(final Object date, final int field)
    '''
def ceiling():
    '''public static Date ceiling(final Date date, final int field)
    public static Calendar ceiling(final Calendar date, final int field)
    public static Date ceiling(final Object date, final int field)
    '''
def iterator():
    '''public static Iterator<Calendar> iterator(final Date focus, final int rangeStyle)
    public static Iterator<Calendar> iterator(final Calendar focus, final int rangeStyle)
    '''
def getFragmentInMilliseconds():
    '''public static long getFragmentInMilliseconds(final Date date, final int fragment)
    public static long getFragmentInMilliseconds(final Calendar calendar, final int fragment)
    '''
def getFragmentInSeconds():
    '''public static long getFragmentInSeconds(final Date date, final int fragment)
    public static long getFragmentInSeconds(final Calendar calendar, final int fragment)
    '''
def getFragmentInMinutes():
    '''public static long getFragmentInMinutes(final Date date, final int fragment)
    public static long getFragmentInMinutes(final Calendar calendar, final int fragment)
    '''
def getFragmentInHours():
    '''public static long getFragmentInHours(final Date date, final int fragment)
    public static long getFragmentInHours(final Calendar calendar, final int fragment)
    '''
def getFragmentInDays():
    '''public static long getFragmentInDays(final Date date, final int fragment)
    public static long getFragmentInDays(final Calendar calendar, final int fragment)
    '''
def truncatedEquals():
    '''public static boolean truncatedEquals(final Calendar cal1, final Calendar cal2, final int field)
    public static boolean truncatedEquals(final Date date1, final Date date2, final int field)
    '''
def truncatedCompareTo():
    '''public static int truncatedCompareTo(final Calendar cal1, final Calendar cal2, final int field)
    public static int truncatedCompareTo(final Date date1, final Date date2, final int field)
    '''
def hasNext():
    '''public boolean hasNext()
    '''
def next():
    '''public Calendar next()
    '''
def remove():
    '''public void remove()
    '''
