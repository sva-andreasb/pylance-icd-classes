DAY = "int  0"
WEEK = "int  1"
DAYOFMONTH = "int  2"
MONTH = "int  3"
def DateSelectorUtil():
    '''    public DateSelectorUtil()
    '''
def getPreviewDates():
    '''    public static Vector getPreviewDates(final Date startDate, final Date endDate, final String pattern)
    public static Vector<Date> getPreviewDates(final Locale l, final TimeZone tz, final Date startDate, final Date endDate, final String pattern)
    '''
def getPreviewDatesAfterTodayInServerTimeZone():
    '''    public static Vector<Date> getPreviewDatesAfterTodayInServerTimeZone(Date startDate, final String pattern)
    '''
def getPreviewDatesInServerTimeZone():
    '''    public static Vector<Date> getPreviewDatesInServerTimeZone(Date startDate, final Date endDate, final String pattern)
    '''
def getPreviewDatesInClientPattern():
    '''    public static Vector<Date> getPreviewDatesInClientPattern(final Locale l, final TimeZone tz, Date startDate, final Date endDate, final String pattern)
    '''
def getCalAfterSetPattern():
    '''    public static Calendar getCalAfterSetPattern(final Locale l, final TimeZone tz, final Date d, final String[] str, final int repeatValue, final String timeUnit)
    '''
def getIndividualString():
    '''    public static String[] getIndividualString(String pattern)
    '''
def getNextCalendar():
    '''    public static Calendar getNextCalendar(final Calendar c, final String[] str, final int repeatValue, final String timeUnit)
    '''
def getSleepingTimeInObject():
    '''    public static DateSelectorUtil getSleepingTimeInObject(final String pattern)
    public static DateSelectorUtil getSleepingTimeInObject(final Date d, final String pattern)
    public static DateSelectorUtil getSleepingTimeInObject(final Locale l, final TimeZone tz, final Date d, final String pattern)
    '''
def getDifference():
    '''    public long getDifference()
    '''
def getSleepingTimeInMilliSecond():
    '''    public static long getSleepingTimeInMilliSecond(final DateSelectorUtil ds)
    public static long getSleepingTimeInMilliSecond(final Locale l, final TimeZone tz, final Date d, final DateSelectorUtil ds)
    public static long getSleepingTimeInMilliSecond(final Date nextScheduled, final Date d)
    public static long getSleepingTimeInMilliSecond(final String pattern)
    public static long getSleepingTimeInMilliSecond(final Date d, final String pattern)
    public static long getSleepingTimeInMilliSecond(final Locale l, final TimeZone tz, final Date d, final String pattern)
    '''
def getNextPreviewDate():
    '''    public static Date getNextPreviewDate(final Locale l, final TimeZone tz, final Date d, final DateSelectorUtil ds)
    '''
def getWeekDayAsInt():
    '''    public static int getWeekDayAsInt(final Locale l, final String weekDay)
    '''
def getMonthAsInt():
    '''    public static int getMonthAsInt(final Locale l, final String month)
    '''
def getDOMAsInt():
    '''    public static int getDOMAsInt(final String domStr)
    '''
def convertDateToClientDate():
    '''    public static Date convertDateToClientDate(final Date d, final Locale l, final TimeZone tz)
    '''
def getCalendarForPattern():
    '''    public static Calendar getCalendarForPattern(final String d, int day, final int month, final Locale l, TimeZone tz, final int type)
    public static Calendar getCalendarForPattern(final String d, int day, final int month, final Locale l, TimeZone tz, final Locale clientl, final TimeZone clienttz, final int type)
    '''
