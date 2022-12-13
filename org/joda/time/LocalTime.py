def now():
'''public static LocalTime now()
public static LocalTime now(final DateTimeZone dateTimeZone)
public static LocalTime now(final Chronology chronology)
'''
pass
def parse():
'''public static LocalTime parse(final String s)
public static LocalTime parse(final String s, final DateTimeFormatter dateTimeFormatter)
'''
pass
def fromMillisOfDay():
'''public static LocalTime fromMillisOfDay(final long n)
public static LocalTime fromMillisOfDay(final long n, Chronology withUTC)
'''
pass
def fromCalendarFields():
'''public static LocalTime fromCalendarFields(final Calendar calendar)
'''
pass
def fromDateFields():
'''public static LocalTime fromDateFields(final Date date)
'''
pass
def LocalTime():
'''public LocalTime()
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
pass
def size():
'''public int size()
'''
pass
def getValue():
'''public int getValue(final int i)
'''
pass
def get():
'''public int get(final DateTimeFieldType obj)
'''
pass
def isSupported():
'''public boolean isSupported(final DateTimeFieldType dateTimeFieldType)
public boolean isSupported(final DurationFieldType durationFieldType)
'''
pass
def getChronology():
'''public Chronology getChronology()
'''
pass
def equals():
'''public boolean equals(final Object o)
'''
pass
def compareTo():
'''public int compareTo(final ReadablePartial readablePartial)
'''
pass
def withFields():
'''public LocalTime withFields(final ReadablePartial readablePartial)
'''
pass
def withField():
'''public LocalTime withField(final DateTimeFieldType obj, final int n)
'''
pass
def withFieldAdded():
'''public LocalTime withFieldAdded(final DurationFieldType obj, final int n)
'''
pass
def withPeriodAdded():
'''public LocalTime withPeriodAdded(final ReadablePeriod readablePeriod, final int n)
'''
pass
def plus():
'''public LocalTime plus(final ReadablePeriod readablePeriod)
'''
pass
def plusHours():
'''public LocalTime plusHours(final int n)
'''
pass
def plusMinutes():
'''public LocalTime plusMinutes(final int n)
'''
pass
def plusSeconds():
'''public LocalTime plusSeconds(final int n)
'''
pass
def plusMillis():
'''public LocalTime plusMillis(final int n)
'''
pass
def minus():
'''public LocalTime minus(final ReadablePeriod readablePeriod)
'''
pass
def minusHours():
'''public LocalTime minusHours(final int n)
'''
pass
def minusMinutes():
'''public LocalTime minusMinutes(final int n)
'''
pass
def minusSeconds():
'''public LocalTime minusSeconds(final int n)
'''
pass
def minusMillis():
'''public LocalTime minusMillis(final int n)
'''
pass
def property():
'''public Property property(final DateTimeFieldType obj)
'''
pass
def getHourOfDay():
'''public int getHourOfDay()
'''
pass
def getMinuteOfHour():
'''public int getMinuteOfHour()
'''
pass
def getSecondOfMinute():
'''public int getSecondOfMinute()
'''
pass
def getMillisOfSecond():
'''public int getMillisOfSecond()
'''
pass
def getMillisOfDay():
'''public int getMillisOfDay()
'''
pass
def withHourOfDay():
'''public LocalTime withHourOfDay(final int n)
'''
pass
def withMinuteOfHour():
'''public LocalTime withMinuteOfHour(final int n)
'''
pass
def withSecondOfMinute():
'''public LocalTime withSecondOfMinute(final int n)
'''
pass
def withMillisOfSecond():
'''public LocalTime withMillisOfSecond(final int n)
'''
pass
def withMillisOfDay():
'''public LocalTime withMillisOfDay(final int n)
'''
pass
def hourOfDay():
'''public Property hourOfDay()
'''
pass
def minuteOfHour():
'''public Property minuteOfHour()
'''
pass
def secondOfMinute():
'''public Property secondOfMinute()
'''
pass
def millisOfSecond():
'''public Property millisOfSecond()
'''
pass
def millisOfDay():
'''public Property millisOfDay()
'''
pass
def toDateTimeToday():
'''public DateTime toDateTimeToday()
public DateTime toDateTimeToday(final DateTimeZone dateTimeZone)
'''
pass
def toString():
'''public String toString()
public String toString(final String s)
public String toString(final String s, final Locale locale)
'''
pass
def getField():
'''public DateTimeField getField()
'''
pass
def getLocalTime():
'''public LocalTime getLocalTime()
'''
pass
def addCopy():
'''public LocalTime addCopy(final int n)
public LocalTime addCopy(final long n)
'''
pass
def addNoWrapToCopy():
'''public LocalTime addNoWrapToCopy(final int n)
'''
pass
def addWrapFieldToCopy():
'''public LocalTime addWrapFieldToCopy(final int n)
'''
pass
def setCopy():
'''public LocalTime setCopy(final int n)
public LocalTime setCopy(final String s, final Locale locale)
public LocalTime setCopy(final String s)
'''
pass
def withMaximumValue():
'''public LocalTime withMaximumValue()
'''
pass
def withMinimumValue():
'''public LocalTime withMinimumValue()
'''
pass
def roundFloorCopy():
'''public LocalTime roundFloorCopy()
'''
pass
def roundCeilingCopy():
'''public LocalTime roundCeilingCopy()
'''
pass
def roundHalfFloorCopy():
'''public LocalTime roundHalfFloorCopy()
'''
pass
def roundHalfCeilingCopy():
'''public LocalTime roundHalfCeilingCopy()
'''
pass
def roundHalfEvenCopy():
'''public LocalTime roundHalfEvenCopy()
'''
pass
