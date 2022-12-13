ERA = "int 0"
YEAR = "int 1"
MONTH = "int 2"
WEEK_OF_YEAR = "int 3"
WEEK_OF_MONTH = "int 4"
DATE = "int 5"
DAY_OF_MONTH = "int 5"
DAY_OF_YEAR = "int 6"
DAY_OF_WEEK = "int 7"
DAY_OF_WEEK_IN_MONTH = "int 8"
AM_PM = "int 9"
HOUR = "int 10"
HOUR_OF_DAY = "int 11"
MINUTE = "int 12"
SECOND = "int 13"
MILLISECOND = "int 14"
ZONE_OFFSET = "int 15"
DST_OFFSET = "int 16"
YEAR_WOY = "int 17"
DOW_LOCAL = "int 18"
EXTENDED_YEAR = "int 19"
JULIAN_DAY = "int 20"
MILLISECONDS_IN_DAY = "int 21"
IS_LEAP_MONTH = "int 22"
SUNDAY = "int 1"
MONDAY = "int 2"
TUESDAY = "int 3"
WEDNESDAY = "int 4"
THURSDAY = "int 5"
FRIDAY = "int 6"
SATURDAY = "int 7"
JANUARY = "int 0"
FEBRUARY = "int 1"
MARCH = "int 2"
APRIL = "int 3"
MAY = "int 4"
JUNE = "int 5"
JULY = "int 6"
AUGUST = "int 7"
SEPTEMBER = "int 8"
OCTOBER = "int 9"
NOVEMBER = "int 10"
DECEMBER = "int 11"
UNDECIMBER = "int 12"
AM = "int 0"
PM = "int 1"
WEEKDAY = "int 0"
WEEKEND = "int 1"
WEEKEND_ONSET = "int 2"
WEEKEND_CEASE = "int 3"
WALLTIME_LAST = "int 0"
WALLTIME_FIRST = "int 1"
WALLTIME_NEXT_VALID = "int 2"
def getInstance():
'''public static Calendar getInstance()
public static Calendar getInstance(final TimeZone zone)
public static Calendar getInstance(final Locale aLocale)
public static Calendar getInstance(final ULocale locale)
public static Calendar getInstance(final TimeZone zone, final Locale aLocale)
public static Calendar getInstance(final TimeZone zone, final ULocale locale)
'''
pass
def getAvailableLocales():
'''public static Locale[] getAvailableLocales()
'''
pass
def getAvailableULocales():
'''public static ULocale[] getAvailableULocales()
'''
pass
def getKeywordValuesForLocale():
'''public static final String[] getKeywordValuesForLocale(final String key, final ULocale locale, final boolean commonlyUsed)
'''
pass
def getTime():
'''public final Date getTime()
'''
pass
def setTime():
'''public final void setTime(final Date date)
'''
pass
def getTimeInMillis():
'''public long getTimeInMillis()
'''
pass
def setTimeInMillis():
'''public void setTimeInMillis(long millis)
'''
pass
def get():
'''public final int get(final int field)
'''
pass
def set():
'''public final void set(final int field, final int value)
public final void set(final int year, final int month, final int date)
public final void set(final int year, final int month, final int date, final int hour, final int minute)
public final void set(final int year, final int month, final int date, final int hour, final int minute, final int second)
'''
pass
def getRelatedYear():
'''public final int getRelatedYear()
'''
pass
def setRelatedYear():
'''public final void setRelatedYear(int year)
'''
pass
def clear():
'''public final void clear()
public final void clear(final int field)
'''
pass
def isSet():
'''public final boolean isSet(final int field)
'''
pass
def equals():
'''public boolean equals(final Object obj)
public boolean equals(final Object other)
'''
pass
def isEquivalentTo():
'''public boolean isEquivalentTo(final Calendar other)
'''
pass
def hashCode():
'''public int hashCode()
public int hashCode()
'''
pass
def before():
'''public boolean before(final Object when)
'''
pass
def after():
'''public boolean after(final Object when)
'''
pass
def getActualMaximum():
'''public int getActualMaximum(final int field)
'''
pass
def getActualMinimum():
'''public int getActualMinimum(final int field)
'''
pass
def roll():
'''public final void roll(final int field, final boolean up)
public void roll(final int field, int amount)
'''
pass
def add():
'''public void add(final int field, int amount)
'''
pass
def getDisplayName():
'''public String getDisplayName(final Locale loc)
public String getDisplayName(final ULocale loc)
'''
pass
def compareTo():
'''public int compareTo(final Calendar that)
'''
pass
def getDateTimeFormat():
'''public DateFormat getDateTimeFormat(final int dateStyle, final int timeStyle, final Locale loc)
public DateFormat getDateTimeFormat(final int dateStyle, final int timeStyle, final ULocale loc)
'''
pass
def getDateTimePattern():
'''public static String getDateTimePattern(final Calendar cal, final ULocale uLocale, final int dateStyle)
'''
pass
def fieldDifference():
'''public int fieldDifference(final Date when, final int field)
'''
pass
def setTimeZone():
'''public void setTimeZone(final TimeZone value)
'''
pass
def getTimeZone():
'''public TimeZone getTimeZone()
'''
pass
def setLenient():
'''public void setLenient(final boolean lenient)
'''
pass
def isLenient():
'''public boolean isLenient()
'''
pass
def setRepeatedWallTimeOption():
'''public void setRepeatedWallTimeOption(final int option)
'''
pass
def getRepeatedWallTimeOption():
'''public int getRepeatedWallTimeOption()
'''
pass
def setSkippedWallTimeOption():
'''public void setSkippedWallTimeOption(final int option)
'''
pass
def getSkippedWallTimeOption():
'''public int getSkippedWallTimeOption()
'''
pass
def setFirstDayOfWeek():
'''public void setFirstDayOfWeek(final int value)
'''
pass
def getFirstDayOfWeek():
'''public int getFirstDayOfWeek()
'''
pass
def setMinimalDaysInFirstWeek():
'''public void setMinimalDaysInFirstWeek(int value)
'''
pass
def getMinimalDaysInFirstWeek():
'''public int getMinimalDaysInFirstWeek()
'''
pass
def getMinimum():
'''public final int getMinimum(final int field)
'''
pass
def getMaximum():
'''public final int getMaximum(final int field)
'''
pass
def getGreatestMinimum():
'''public final int getGreatestMinimum(final int field)
'''
pass
def getLeastMaximum():
'''public final int getLeastMaximum(final int field)
'''
pass
def getDayOfWeekType():
'''public int getDayOfWeekType(final int dayOfWeek)
'''
pass
def getWeekendTransition():
'''public int getWeekendTransition(final int dayOfWeek)
'''
pass
def isWeekend():
'''public boolean isWeekend(final Date date)
public boolean isWeekend()
'''
pass
def clone():
'''public Object clone()
'''
pass
def toString():
'''public String toString()
public String toString()
'''
pass
def getWeekDataForRegion():
'''public static WeekData getWeekDataForRegion(final String region)
'''
pass
def getWeekData():
'''public WeekData getWeekData()
'''
pass
def setWeekData():
'''public Calendar setWeekData(final WeekData wdata)
'''
pass
def getFieldCount():
'''public final int getFieldCount()
'''
pass
def getType():
'''public String getType()
'''
pass
def haveDefaultCentury():
'''public boolean haveDefaultCentury()
'''
pass
def getLocale():
'''public final ULocale getLocale(final ULocale.Type type)
public ULocale getLocale()
'''
pass
def PatternData():
'''public PatternData(final String[] patterns, final String[] overrides)
'''
pass
def getPatternString():
'''public String getPatternString()
'''
pass
def getOverrideString():
'''public String getOverrideString()
'''
pass
def getCalendar():
'''public Calendar getCalendar()
'''
pass
def getDateFormatSymbols():
'''public DateFormatSymbols getDateFormatSymbols()
'''
pass
def WeekData():
'''public WeekData(final int fdow, final int mdifw, final int weekendOnset, final int weekendOnsetMillis, final int weekendCease, final int weekendCeaseMillis)
'''
pass
