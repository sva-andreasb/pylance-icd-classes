HOUR_OF_DAY = "int  0"
MINUTE_OF_HOUR = "int  1"
SECOND_OF_MINUTE = "int  2"
MILLIS_OF_SECOND = "int  3"
def fromCalendarFields():
    '''    public static TimeOfDay fromCalendarFields(final Calendar calendar)
    '''
def fromDateFields():
    '''    public static TimeOfDay fromDateFields(final Date date)
    '''
def fromMillisOfDay():
    '''    public static TimeOfDay fromMillisOfDay(final long n)
    public static TimeOfDay fromMillisOfDay(final long n, Chronology chronology)
    '''
def TimeOfDay():
    '''    public TimeOfDay()
    public TimeOfDay(final DateTimeZone dateTimeZone)
    public TimeOfDay(final Chronology chronology)
    public TimeOfDay(final long n)
    public TimeOfDay(final long n, final Chronology chronology)
    public TimeOfDay(final Object o)
    public TimeOfDay(final Object o, final Chronology chronology)
    public TimeOfDay(final int n, final int n2)
    public TimeOfDay(final int n, final int n2, final Chronology chronology)
    public TimeOfDay(final int n, final int n2, final int n3)
    public TimeOfDay(final int n, final int n2, final int n3, final Chronology chronology)
    public TimeOfDay(final int n, final int n2, final int n3, final int n4)
    public TimeOfDay(final int n, final int n2, final int n3, final int n4, final Chronology chronology)
    '''
def size():
    '''    public int size()
    '''
def getFieldType():
    '''    public DateTimeFieldType getFieldType(final int n)
    '''
def getFieldTypes():
    '''    public DateTimeFieldType[] getFieldTypes()
    '''
def withChronologyRetainFields():
    '''    public TimeOfDay withChronologyRetainFields(Chronology chronology)
    '''
def withField():
    '''    public TimeOfDay withField(final DateTimeFieldType dateTimeFieldType, final int n)
    '''
def withFieldAdded():
    '''    public TimeOfDay withFieldAdded(final DurationFieldType durationFieldType, final int n)
    '''
def withPeriodAdded():
    '''    public TimeOfDay withPeriodAdded(final ReadablePeriod readablePeriod, final int n)
    '''
def plus():
    '''    public TimeOfDay plus(final ReadablePeriod readablePeriod)
    '''
def plusHours():
    '''    public TimeOfDay plusHours(final int n)
    '''
def plusMinutes():
    '''    public TimeOfDay plusMinutes(final int n)
    '''
def plusSeconds():
    '''    public TimeOfDay plusSeconds(final int n)
    '''
def plusMillis():
    '''    public TimeOfDay plusMillis(final int n)
    '''
def minus():
    '''    public TimeOfDay minus(final ReadablePeriod readablePeriod)
    '''
def minusHours():
    '''    public TimeOfDay minusHours(final int n)
    '''
def minusMinutes():
    '''    public TimeOfDay minusMinutes(final int n)
    '''
def minusSeconds():
    '''    public TimeOfDay minusSeconds(final int n)
    '''
def minusMillis():
    '''    public TimeOfDay minusMillis(final int n)
    '''
def property():
    '''    public Property property(final DateTimeFieldType dateTimeFieldType)
    '''
def toLocalTime():
    '''    public LocalTime toLocalTime()
    '''
def toDateTimeToday():
    '''    public DateTime toDateTimeToday()
    public DateTime toDateTimeToday(final DateTimeZone dateTimeZone)
    '''
def getHourOfDay():
    '''    public int getHourOfDay()
    '''
def getMinuteOfHour():
    '''    public int getMinuteOfHour()
    '''
def getSecondOfMinute():
    '''    public int getSecondOfMinute()
    '''
def getMillisOfSecond():
    '''    public int getMillisOfSecond()
    '''
def withHourOfDay():
    '''    public TimeOfDay withHourOfDay(final int n)
    '''
def withMinuteOfHour():
    '''    public TimeOfDay withMinuteOfHour(final int n)
    '''
def withSecondOfMinute():
    '''    public TimeOfDay withSecondOfMinute(final int n)
    '''
def withMillisOfSecond():
    '''    public TimeOfDay withMillisOfSecond(final int n)
    '''
def hourOfDay():
    '''    public Property hourOfDay()
    '''
def minuteOfHour():
    '''    public Property minuteOfHour()
    '''
def secondOfMinute():
    '''    public Property secondOfMinute()
    '''
def millisOfSecond():
    '''    public Property millisOfSecond()
    '''
def toString():
    '''    public String toString()
    '''
def getField():
    '''    public DateTimeField getField()
    '''
def getTimeOfDay():
    '''    public TimeOfDay getTimeOfDay()
    '''
def get():
    '''    public int get()
    '''
def addToCopy():
    '''    public TimeOfDay addToCopy(final int n)
    '''
def addNoWrapToCopy():
    '''    public TimeOfDay addNoWrapToCopy(final int n)
    '''
def addWrapFieldToCopy():
    '''    public TimeOfDay addWrapFieldToCopy(final int n)
    '''
def setCopy():
    '''    public TimeOfDay setCopy(final int n)
    public TimeOfDay setCopy(final String s, final Locale locale)
    public TimeOfDay setCopy(final String s)
    '''
def withMaximumValue():
    '''    public TimeOfDay withMaximumValue()
    '''
def withMinimumValue():
    '''    public TimeOfDay withMinimumValue()
    '''
