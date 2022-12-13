def now():
    '''    public static LocalTime now()
    public static LocalTime now(final DateTimeZone dateTimeZone)
    public static LocalTime now(final Chronology chronology)
    '''
def parse():
    '''    public static LocalTime parse(final String s)
    public static LocalTime parse(final String s, final DateTimeFormatter dateTimeFormatter)
    '''
def fromMillisOfDay():
    '''    public static LocalTime fromMillisOfDay(final long n)
    public static LocalTime fromMillisOfDay(final long n, Chronology withUTC)
    '''
def fromCalendarFields():
    '''    public static LocalTime fromCalendarFields(final Calendar calendar)
    '''
def fromDateFields():
    '''    public static LocalTime fromDateFields(final Date date)
    '''
def LocalTime():
    '''    public LocalTime()
    public LocalTime(final DateTimeZone dateTimeZone)
    public LocalTime(final Chronology chronology)
    public LocalTime(final long n)
    public LocalTime(final long n, final DateTimeZone dateTimeZone)
    public LocalTime(final long n, Chronology iChronology)
    public LocalTime(final Object o)
    public LocalTime(final Object o, final DateTimeZone dateTimeZone)
    public LocalTime(final Object o, Chronology chronology)
    public LocalTime(final int n, final int n2)
    public LocalTime(final int n, final int n2, final int n3)
    public LocalTime(final int n, final int n2, final int n3, final int n4)
    public LocalTime(final int n, final int n2, final int n3, final int n4, Chronology withUTC)
    '''
def size():
    '''    public int size()
    '''
def getValue():
    '''    public int getValue(final int i)
    '''
def get():
    '''    public int get(final DateTimeFieldType obj)
    '''
def isSupported():
    '''    public boolean isSupported(final DateTimeFieldType dateTimeFieldType)
    public boolean isSupported(final DurationFieldType durationFieldType)
    '''
def getChronology():
    '''    public Chronology getChronology()
    '''
def equals():
    '''    public boolean equals(final Object o)
    '''
def compareTo():
    '''    public int compareTo(final ReadablePartial readablePartial)
    '''
def withFields():
    '''    public LocalTime withFields(final ReadablePartial readablePartial)
    '''
def withField():
    '''    public LocalTime withField(final DateTimeFieldType obj, final int n)
    '''
def withFieldAdded():
    '''    public LocalTime withFieldAdded(final DurationFieldType obj, final int n)
    '''
def withPeriodAdded():
    '''    public LocalTime withPeriodAdded(final ReadablePeriod readablePeriod, final int n)
    '''
def plus():
    '''    public LocalTime plus(final ReadablePeriod readablePeriod)
    '''
def plusHours():
    '''    public LocalTime plusHours(final int n)
    '''
def plusMinutes():
    '''    public LocalTime plusMinutes(final int n)
    '''
def plusSeconds():
    '''    public LocalTime plusSeconds(final int n)
    '''
def plusMillis():
    '''    public LocalTime plusMillis(final int n)
    '''
def minus():
    '''    public LocalTime minus(final ReadablePeriod readablePeriod)
    '''
def minusHours():
    '''    public LocalTime minusHours(final int n)
    '''
def minusMinutes():
    '''    public LocalTime minusMinutes(final int n)
    '''
def minusSeconds():
    '''    public LocalTime minusSeconds(final int n)
    '''
def minusMillis():
    '''    public LocalTime minusMillis(final int n)
    '''
def property():
    '''    public Property property(final DateTimeFieldType obj)
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
def getMillisOfDay():
    '''    public int getMillisOfDay()
    '''
def withHourOfDay():
    '''    public LocalTime withHourOfDay(final int n)
    '''
def withMinuteOfHour():
    '''    public LocalTime withMinuteOfHour(final int n)
    '''
def withSecondOfMinute():
    '''    public LocalTime withSecondOfMinute(final int n)
    '''
def withMillisOfSecond():
    '''    public LocalTime withMillisOfSecond(final int n)
    '''
def withMillisOfDay():
    '''    public LocalTime withMillisOfDay(final int n)
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
def millisOfDay():
    '''    public Property millisOfDay()
    '''
def toDateTimeToday():
    '''    public DateTime toDateTimeToday()
    public DateTime toDateTimeToday(final DateTimeZone dateTimeZone)
    '''
def toString():
    '''    public String toString()
    public String toString(final String s)
    public String toString(final String s, final Locale locale)
    '''
def getField():
    '''    public DateTimeField getField()
    '''
def getLocalTime():
    '''    public LocalTime getLocalTime()
    '''
def addCopy():
    '''    public LocalTime addCopy(final int n)
    public LocalTime addCopy(final long n)
    '''
def addNoWrapToCopy():
    '''    public LocalTime addNoWrapToCopy(final int n)
    '''
def addWrapFieldToCopy():
    '''    public LocalTime addWrapFieldToCopy(final int n)
    '''
def setCopy():
    '''    public LocalTime setCopy(final int n)
    public LocalTime setCopy(final String s, final Locale locale)
    public LocalTime setCopy(final String s)
    '''
def withMaximumValue():
    '''    public LocalTime withMaximumValue()
    '''
def withMinimumValue():
    '''    public LocalTime withMinimumValue()
    '''
def roundFloorCopy():
    '''    public LocalTime roundFloorCopy()
    '''
def roundCeilingCopy():
    '''    public LocalTime roundCeilingCopy()
    '''
def roundHalfFloorCopy():
    '''    public LocalTime roundHalfFloorCopy()
    '''
def roundHalfCeilingCopy():
    '''    public LocalTime roundHalfCeilingCopy()
    '''
def roundHalfEvenCopy():
    '''    public LocalTime roundHalfEvenCopy()
    '''
