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
def parse():
    '''public static MutableDateTime parse(final String s)
    public static MutableDateTime parse(final String s, final DateTimeFormatter dateTimeFormatter)
    '''
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
def getRoundingField():
    '''public DateTimeField getRoundingField()
    '''
def getRoundingMode():
    '''public int getRoundingMode()
    '''
def setRounding():
    '''public void setRounding(final DateTimeField dateTimeField)
    public void setRounding(final DateTimeField dateTimeField, final int i)
    '''
def setMillis():
    '''public void setMillis(long millis)
    public void setMillis(final ReadableInstant readableInstant)
    '''
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
def setChronology():
    '''public void setChronology(final Chronology chronology)
    '''
def setZone():
    '''public void setZone(DateTimeZone zone)
    '''
def setZoneRetainFields():
    '''public void setZoneRetainFields(DateTimeZone zone)
    '''
def set():
    '''public void set(final DateTimeFieldType dateTimeFieldType, final int n)
    public MutableDateTime set(final int n)
    public MutableDateTime set(final String s, final Locale locale)
    public MutableDateTime set(final String s)
    '''
def setYear():
    '''public void setYear(final int n)
    '''
def addYears():
    '''public void addYears(final int n)
    '''
def setWeekyear():
    '''public void setWeekyear(final int n)
    '''
def addWeekyears():
    '''public void addWeekyears(final int n)
    '''
def setMonthOfYear():
    '''public void setMonthOfYear(final int n)
    '''
def addMonths():
    '''public void addMonths(final int n)
    '''
def setWeekOfWeekyear():
    '''public void setWeekOfWeekyear(final int n)
    '''
def addWeeks():
    '''public void addWeeks(final int n)
    '''
def setDayOfYear():
    '''public void setDayOfYear(final int n)
    '''
def setDayOfMonth():
    '''public void setDayOfMonth(final int n)
    '''
def setDayOfWeek():
    '''public void setDayOfWeek(final int n)
    '''
def addDays():
    '''public void addDays(final int n)
    '''
def setHourOfDay():
    '''public void setHourOfDay(final int n)
    '''
def addHours():
    '''public void addHours(final int n)
    '''
def setMinuteOfDay():
    '''public void setMinuteOfDay(final int n)
    '''
def setMinuteOfHour():
    '''public void setMinuteOfHour(final int n)
    '''
def addMinutes():
    '''public void addMinutes(final int n)
    '''
def setSecondOfDay():
    '''public void setSecondOfDay(final int n)
    '''
def setSecondOfMinute():
    '''public void setSecondOfMinute(final int n)
    '''
def addSeconds():
    '''public void addSeconds(final int n)
    '''
def setMillisOfDay():
    '''public void setMillisOfDay(final int n)
    '''
def setMillisOfSecond():
    '''public void setMillisOfSecond(final int n)
    '''
def addMillis():
    '''public void addMillis(final int n)
    '''
def setDate():
    '''public void setDate(final long n)
    public void setDate(final ReadableInstant readableInstant)
    public void setDate(final int n, final int n2, final int n3)
    '''
def setTime():
    '''public void setTime(final long n)
    public void setTime(final ReadableInstant readableInstant)
    public void setTime(final int n, final int n2, final int n3, final int n4)
    '''
def setDateTime():
    '''public void setDateTime(final int n, final int n2, final int n3, final int n4, final int n5, final int n6, final int n7)
    '''
def property():
    '''public Property property(final DateTimeFieldType obj)
    '''
def era():
    '''public Property era()
    '''
def centuryOfEra():
    '''public Property centuryOfEra()
    '''
def yearOfCentury():
    '''public Property yearOfCentury()
    '''
def yearOfEra():
    '''public Property yearOfEra()
    '''
def year():
    '''public Property year()
    '''
def weekyear():
    '''public Property weekyear()
    '''
def monthOfYear():
    '''public Property monthOfYear()
    '''
def weekOfWeekyear():
    '''public Property weekOfWeekyear()
    '''
def dayOfYear():
    '''public Property dayOfYear()
    '''
def dayOfMonth():
    '''public Property dayOfMonth()
    '''
def dayOfWeek():
    '''public Property dayOfWeek()
    '''
def hourOfDay():
    '''public Property hourOfDay()
    '''
def minuteOfDay():
    '''public Property minuteOfDay()
    '''
def minuteOfHour():
    '''public Property minuteOfHour()
    '''
def secondOfDay():
    '''public Property secondOfDay()
    '''
def secondOfMinute():
    '''public Property secondOfMinute()
    '''
def millisOfDay():
    '''public Property millisOfDay()
    '''
def millisOfSecond():
    '''public Property millisOfSecond()
    '''
def copy():
    '''public MutableDateTime copy()
    '''
def clone():
    '''public Object clone()
    '''
def getField():
    '''public DateTimeField getField()
    '''
def getMutableDateTime():
    '''public MutableDateTime getMutableDateTime()
    '''
def addWrapField():
    '''public MutableDateTime addWrapField(final int n)
    '''
def roundFloor():
    '''public MutableDateTime roundFloor()
    '''
def roundCeiling():
    '''public MutableDateTime roundCeiling()
    '''
def roundHalfFloor():
    '''public MutableDateTime roundHalfFloor()
    '''
def roundHalfCeiling():
    '''public MutableDateTime roundHalfCeiling()
    '''
def roundHalfEven():
    '''public MutableDateTime roundHalfEven()
    '''
