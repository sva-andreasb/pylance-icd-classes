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
WALLTIME_LAST = "int  0"
WALLTIME_FIRST = "int  1"
WALLTIME_NEXT_VALID = "int  2"
def getInstance():
    '''    public static Calendar getInstance()
    public static Calendar getInstance(final TimeZone zone)
    public static Calendar getInstance(final Locale aLocale)
    public static Calendar getInstance(final ULocale locale)
    public static Calendar getInstance(final TimeZone zone, final Locale aLocale)
    public static Calendar getInstance(final TimeZone zone, final ULocale locale)
    '''
def getAvailableLocales():
    '''    public static Locale[] getAvailableLocales()
    '''
def getAvailableULocales():
    '''    public static ULocale[] getAvailableULocales()
    '''
def getKeywordValuesForLocale():
    '''    public static final String[] getKeywordValuesForLocale(final String key, final ULocale locale, final boolean commonlyUsed)
    '''
def getTime():
    '''    public final Date getTime()
    '''
def setTime():
    '''    public final void setTime(final Date date)
    '''
def getTimeInMillis():
    '''    public long getTimeInMillis()
    '''
def setTimeInMillis():
    '''    public void setTimeInMillis(long millis)
    '''
def get():
    '''    public final int get(final int field)
    '''
def set():
    '''    public final void set(final int field, final int value)
    public final void set(final int year, final int month, final int date)
    public final void set(final int year, final int month, final int date, final int hour, final int minute)
    public final void set(final int year, final int month, final int date, final int hour, final int minute, final int second)
    '''
def getRelatedYear():
    '''    public final int getRelatedYear()
    '''
def setRelatedYear():
    '''    public final void setRelatedYear(int year)
    '''
def clear():
    '''    public final void clear()
    public final void clear(final int field)
    '''
def isSet():
    '''    public final boolean isSet(final int field)
    '''
def equals():
    '''    public boolean equals(final Object obj)
    public boolean equals(final Object other)
    '''
def isEquivalentTo():
    '''    public boolean isEquivalentTo(final Calendar other)
    '''
def hashCode():
    '''    public int hashCode()
    public int hashCode()
    '''
def before():
    '''    public boolean before(final Object when)
    '''
def after():
    '''    public boolean after(final Object when)
    '''
def getActualMaximum():
    '''    public int getActualMaximum(final int field)
    '''
def getActualMinimum():
    '''    public int getActualMinimum(final int field)
    '''
def roll():
    '''    public final void roll(final int field, final boolean up)
    public void roll(final int field, int amount)
    '''
def add():
    '''    public void add(final int field, int amount)
    '''
def getDisplayName():
    '''    public String getDisplayName(final Locale loc)
    public String getDisplayName(final ULocale loc)
    '''
def compareTo():
    '''    public int compareTo(final Calendar that)
    '''
def getDateTimeFormat():
    '''    public DateFormat getDateTimeFormat(final int dateStyle, final int timeStyle, final Locale loc)
    public DateFormat getDateTimeFormat(final int dateStyle, final int timeStyle, final ULocale loc)
    '''
def getDateTimePattern():
    '''    public static String getDateTimePattern(final Calendar cal, final ULocale uLocale, final int dateStyle)
    '''
def fieldDifference():
    '''    public int fieldDifference(final Date when, final int field)
    '''
def setTimeZone():
    '''    public void setTimeZone(final TimeZone value)
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
def setRepeatedWallTimeOption():
    '''    public void setRepeatedWallTimeOption(final int option)
    '''
def getRepeatedWallTimeOption():
    '''    public int getRepeatedWallTimeOption()
    '''
def setSkippedWallTimeOption():
    '''    public void setSkippedWallTimeOption(final int option)
    '''
def getSkippedWallTimeOption():
    '''    public int getSkippedWallTimeOption()
    '''
def setFirstDayOfWeek():
    '''    public void setFirstDayOfWeek(final int value)
    '''
def getFirstDayOfWeek():
    '''    public int getFirstDayOfWeek()
    '''
def setMinimalDaysInFirstWeek():
    '''    public void setMinimalDaysInFirstWeek(int value)
    '''
def getMinimalDaysInFirstWeek():
    '''    public int getMinimalDaysInFirstWeek()
    '''
def getMinimum():
    '''    public final int getMinimum(final int field)
    '''
def getMaximum():
    '''    public final int getMaximum(final int field)
    '''
def getGreatestMinimum():
    '''    public final int getGreatestMinimum(final int field)
    '''
def getLeastMaximum():
    '''    public final int getLeastMaximum(final int field)
    '''
def getDayOfWeekType():
    '''    public int getDayOfWeekType(final int dayOfWeek)
    '''
def getWeekendTransition():
    '''    public int getWeekendTransition(final int dayOfWeek)
    '''
def isWeekend():
    '''    public boolean isWeekend(final Date date)
    public boolean isWeekend()
    '''
def clone():
    '''    public Object clone()
    '''
def toString():
    '''    public String toString()
    public String toString()
    '''
def getWeekDataForRegion():
    '''    public static WeekData getWeekDataForRegion(final String region)
    '''
def getWeekData():
    '''    public WeekData getWeekData()
    '''
def setWeekData():
    '''    public Calendar setWeekData(final WeekData wdata)
    '''
def getFieldCount():
    '''    public final int getFieldCount()
    '''
def getType():
    '''    public String getType()
    '''
def haveDefaultCentury():
    '''    public boolean haveDefaultCentury()
    '''
def getLocale():
    '''    public final ULocale getLocale(final ULocale.Type type)
    public ULocale getLocale()
    '''
def PatternData():
    '''    public PatternData(final String[] patterns, final String[] overrides)
    '''
def getPatternString():
    '''    public String getPatternString()
    '''
def getOverrideString():
    '''    public String getOverrideString()
    '''
def getCalendar():
    '''    public Calendar getCalendar()
    '''
def getDateFormatSymbols():
    '''    public DateFormatSymbols getDateFormatSymbols()
    '''
def WeekData():
    '''    public WeekData(final int fdow, final int mdifw, final int weekendOnset, final int weekendOnsetMillis, final int weekendCease, final int weekendCeaseMillis)
    '''
