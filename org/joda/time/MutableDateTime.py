ROUND_NONE = "int  0"
ROUND_FLOOR = "int  1"
ROUND_CEILING = "int  2"
ROUND_HALF_FLOOR = "int  3"
ROUND_HALF_CEILING = "int  4"
ROUND_HALF_EVEN = "int  5"
def now():
'''public static MutableDateTime now()
public static MutableDateTime now(final DateTimeZone dateTimeZone)
public static MutableDateTime now(final Chronology chronology)
'''
pass
def parse():
'''public static MutableDateTime parse(final String s)
public static MutableDateTime parse(final String s, final DateTimeFormatter dateTimeFormatter)
'''
pass
def MutableDateTime():
'''public MutableDateTime()
public MutableDateTime(final DateTimeZone dateTimeZone)
public MutableDateTime(final Chronology chronology)
public MutableDateTime(final long n)
public MutableDateTime(final long n, final DateTimeZone dateTimeZone)
public MutableDateTime(final long n, final Chronology chronology)
public MutableDateTime(final Object o)
public MutableDateTime(final Object o, final DateTimeZone dateTimeZone)
public MutableDateTime(final Object o, final Chronology chronology)
public MutableDateTime(final int n, final int n2, final int n3, final int n4, final int n5, final int n6, final int n7)
public MutableDateTime(final int n, final int n2, final int n3, final int n4, final int n5, final int n6, final int n7, final DateTimeZone dateTimeZone)
public MutableDateTime(final int n, final int n2, final int n3, final int n4, final int n5, final int n6, final int n7, final Chronology chronology)
'''
pass
def getRoundingField():
'''public DateTimeField getRoundingField()
'''
pass
def getRoundingMode():
'''public int getRoundingMode()
'''
pass
def setRounding():
'''public void setRounding(final DateTimeField dateTimeField)
public void setRounding(final DateTimeField dateTimeField, final int i)
'''
pass
def setMillis():
'''public void setMillis(long millis)
public void setMillis(final ReadableInstant readableInstant)
'''
pass
def add():
'''public void add(final long n)
public void add(final ReadableDuration readableDuration)
public void add(final ReadableDuration readableDuration, final int n)
public void add(final ReadablePeriod readablePeriod)
public void add(final ReadablePeriod readablePeriod, final int n)
public void add(final DurationFieldType durationFieldType, final int n)
public MutableDateTime add(final int n)
public MutableDateTime add(final long n)
'''
pass
def setChronology():
'''public void setChronology(final Chronology chronology)
'''
pass
def setZone():
'''public void setZone(DateTimeZone zone)
'''
pass
def setZoneRetainFields():
'''public void setZoneRetainFields(DateTimeZone zone)
'''
pass
def set():
'''public void set(final DateTimeFieldType dateTimeFieldType, final int n)
public MutableDateTime set(final int n)
public MutableDateTime set(final String s, final Locale locale)
public MutableDateTime set(final String s)
'''
pass
def setYear():
'''public void setYear(final int n)
'''
pass
def addYears():
'''public void addYears(final int n)
'''
pass
def setWeekyear():
'''public void setWeekyear(final int n)
'''
pass
def addWeekyears():
'''public void addWeekyears(final int n)
'''
pass
def setMonthOfYear():
'''public void setMonthOfYear(final int n)
'''
pass
def addMonths():
'''public void addMonths(final int n)
'''
pass
def setWeekOfWeekyear():
'''public void setWeekOfWeekyear(final int n)
'''
pass
def addWeeks():
'''public void addWeeks(final int n)
'''
pass
def setDayOfYear():
'''public void setDayOfYear(final int n)
'''
pass
def setDayOfMonth():
'''public void setDayOfMonth(final int n)
'''
pass
def setDayOfWeek():
'''public void setDayOfWeek(final int n)
'''
pass
def addDays():
'''public void addDays(final int n)
'''
pass
def setHourOfDay():
'''public void setHourOfDay(final int n)
'''
pass
def addHours():
'''public void addHours(final int n)
'''
pass
def setMinuteOfDay():
'''public void setMinuteOfDay(final int n)
'''
pass
def setMinuteOfHour():
'''public void setMinuteOfHour(final int n)
'''
pass
def addMinutes():
'''public void addMinutes(final int n)
'''
pass
def setSecondOfDay():
'''public void setSecondOfDay(final int n)
'''
pass
def setSecondOfMinute():
'''public void setSecondOfMinute(final int n)
'''
pass
def addSeconds():
'''public void addSeconds(final int n)
'''
pass
def setMillisOfDay():
'''public void setMillisOfDay(final int n)
'''
pass
def setMillisOfSecond():
'''public void setMillisOfSecond(final int n)
'''
pass
def addMillis():
'''public void addMillis(final int n)
'''
pass
def setDate():
'''public void setDate(final long n)
public void setDate(final ReadableInstant readableInstant)
public void setDate(final int n, final int n2, final int n3)
'''
pass
def setTime():
'''public void setTime(final long n)
public void setTime(final ReadableInstant readableInstant)
public void setTime(final int n, final int n2, final int n3, final int n4)
'''
pass
def setDateTime():
'''public void setDateTime(final int n, final int n2, final int n3, final int n4, final int n5, final int n6, final int n7)
'''
pass
def property():
'''public Property property(final DateTimeFieldType obj)
'''
pass
def era():
'''public Property era()
'''
pass
def centuryOfEra():
'''public Property centuryOfEra()
'''
pass
def yearOfCentury():
'''public Property yearOfCentury()
'''
pass
def yearOfEra():
'''public Property yearOfEra()
'''
pass
def year():
'''public Property year()
'''
pass
def weekyear():
'''public Property weekyear()
'''
pass
def monthOfYear():
'''public Property monthOfYear()
'''
pass
def weekOfWeekyear():
'''public Property weekOfWeekyear()
'''
pass
def dayOfYear():
'''public Property dayOfYear()
'''
pass
def dayOfMonth():
'''public Property dayOfMonth()
'''
pass
def dayOfWeek():
'''public Property dayOfWeek()
'''
pass
def hourOfDay():
'''public Property hourOfDay()
'''
pass
def minuteOfDay():
'''public Property minuteOfDay()
'''
pass
def minuteOfHour():
'''public Property minuteOfHour()
'''
pass
def secondOfDay():
'''public Property secondOfDay()
'''
pass
def secondOfMinute():
'''public Property secondOfMinute()
'''
pass
def millisOfDay():
'''public Property millisOfDay()
'''
pass
def millisOfSecond():
'''public Property millisOfSecond()
'''
pass
def copy():
'''public MutableDateTime copy()
'''
pass
def clone():
'''public Object clone()
'''
pass
def getField():
'''public DateTimeField getField()
'''
pass
def getMutableDateTime():
'''public MutableDateTime getMutableDateTime()
'''
pass
def addWrapField():
'''public MutableDateTime addWrapField(final int n)
'''
pass
def roundFloor():
'''public MutableDateTime roundFloor()
'''
pass
def roundCeiling():
'''public MutableDateTime roundCeiling()
'''
pass
def roundHalfFloor():
'''public MutableDateTime roundHalfFloor()
'''
pass
def roundHalfCeiling():
'''public MutableDateTime roundHalfCeiling()
'''
pass
def roundHalfEven():
'''public MutableDateTime roundHalfEven()
'''
pass
