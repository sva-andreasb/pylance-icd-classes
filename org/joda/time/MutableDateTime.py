ROUND_NONE = "int  0"
ROUND_FLOOR = "int  1"
ROUND_CEILING = "int  2"
ROUND_HALF_FLOOR = "int  3"
ROUND_HALF_CEILING = "int  4"
ROUND_HALF_EVEN = "int  5"
def ():
    '''returns MutableDateTime\n\n
    ()\n
    (final DateTimeZone dateTimeZone)\n
    (final Chronology chronology)\n
    (final long n)\n
    (final long n, final DateTimeZone dateTimeZone)\n
    (final long n, final Chronology chronology)\n
    (final Object o)\n
    (final Object o, final DateTimeZone dateTimeZone)\n
    (final Object o, final Chronology chronology)\n
    (final int n, final int n2, final int n3, final int n4, final int n5, final int n6, final int n7)\n
    (final int n, final int n2, final int n3, final int n4, final int n5, final int n6, final int n7, final DateTimeZone dateTimeZone)\n
    (final int n, final int n2, final int n3, final int n4, final int n5, final int n6, final int n7, final Chronology chronology)\n
    '''
def getRoundingField():
    '''returns DateTimeField\n\n
    getRoundingField()\n
    '''
def getRoundingMode():
    '''returns int\n\n
    getRoundingMode()\n
    '''
def setRounding():
    '''returns None\n\n
    setRounding(final DateTimeField dateTimeField)\n
    setRounding(final DateTimeField dateTimeField, final int i)\n
    '''
def setMillis():
    '''returns None\n\n
    setMillis(long millis)\n
    setMillis(final ReadableInstant readableInstant)\n
    '''
def add():
    '''returns MutableDateTime\n\n
    add(final long n)\n
    add(final ReadableDuration readableDuration)\n
    add(final ReadableDuration readableDuration, final int n)\n
    add(final ReadablePeriod readablePeriod)\n
    add(final ReadablePeriod readablePeriod, final int n)\n
    add(final DurationFieldType durationFieldType, final int n)\n
    add(final int n)\n
    add(final long n)\n
    '''
def setChronology():
    '''returns None\n\n
    setChronology(final Chronology chronology)\n
    '''
def setZone():
    '''returns None\n\n
    setZone(DateTimeZone zone)\n
    '''
def setZoneRetainFields():
    '''returns None\n\n
    setZoneRetainFields(DateTimeZone zone)\n
    '''
def set():
    '''returns MutableDateTime\n\n
    set(final DateTimeFieldType dateTimeFieldType, final int n)\n
    set(final int n)\n
    set(final String s, final Locale locale)\n
    set(final String s)\n
    '''
def setYear():
    '''returns None\n\n
    setYear(final int n)\n
    '''
def addYears():
    '''returns None\n\n
    addYears(final int n)\n
    '''
def setWeekyear():
    '''returns None\n\n
    setWeekyear(final int n)\n
    '''
def addWeekyears():
    '''returns None\n\n
    addWeekyears(final int n)\n
    '''
def setMonthOfYear():
    '''returns None\n\n
    setMonthOfYear(final int n)\n
    '''
def addMonths():
    '''returns None\n\n
    addMonths(final int n)\n
    '''
def setWeekOfWeekyear():
    '''returns None\n\n
    setWeekOfWeekyear(final int n)\n
    '''
def addWeeks():
    '''returns None\n\n
    addWeeks(final int n)\n
    '''
def setDayOfYear():
    '''returns None\n\n
    setDayOfYear(final int n)\n
    '''
def setDayOfMonth():
    '''returns None\n\n
    setDayOfMonth(final int n)\n
    '''
def setDayOfWeek():
    '''returns None\n\n
    setDayOfWeek(final int n)\n
    '''
def addDays():
    '''returns None\n\n
    addDays(final int n)\n
    '''
def setHourOfDay():
    '''returns None\n\n
    setHourOfDay(final int n)\n
    '''
def addHours():
    '''returns None\n\n
    addHours(final int n)\n
    '''
def setMinuteOfDay():
    '''returns None\n\n
    setMinuteOfDay(final int n)\n
    '''
def setMinuteOfHour():
    '''returns None\n\n
    setMinuteOfHour(final int n)\n
    '''
def addMinutes():
    '''returns None\n\n
    addMinutes(final int n)\n
    '''
def setSecondOfDay():
    '''returns None\n\n
    setSecondOfDay(final int n)\n
    '''
def setSecondOfMinute():
    '''returns None\n\n
    setSecondOfMinute(final int n)\n
    '''
def addSeconds():
    '''returns None\n\n
    addSeconds(final int n)\n
    '''
def setMillisOfDay():
    '''returns None\n\n
    setMillisOfDay(final int n)\n
    '''
def setMillisOfSecond():
    '''returns None\n\n
    setMillisOfSecond(final int n)\n
    '''
def addMillis():
    '''returns None\n\n
    addMillis(final int n)\n
    '''
def setDate():
    '''returns None\n\n
    setDate(final long n)\n
    setDate(final ReadableInstant readableInstant)\n
    setDate(final int n, final int n2, final int n3)\n
    '''
def setTime():
    '''returns None\n\n
    setTime(final long n)\n
    setTime(final ReadableInstant readableInstant)\n
    setTime(final int n, final int n2, final int n3, final int n4)\n
    '''
def setDateTime():
    '''returns None\n\n
    setDateTime(final int n, final int n2, final int n3, final int n4, final int n5, final int n6, final int n7)\n
    '''
def property():
    '''returns Property\n\n
    property(final DateTimeFieldType obj)\n
    '''
def era():
    '''returns Property\n\n
    era()\n
    '''
def centuryOfEra():
    '''returns Property\n\n
    centuryOfEra()\n
    '''
def yearOfCentury():
    '''returns Property\n\n
    yearOfCentury()\n
    '''
def yearOfEra():
    '''returns Property\n\n
    yearOfEra()\n
    '''
def year():
    '''returns Property\n\n
    year()\n
    '''
def weekyear():
    '''returns Property\n\n
    weekyear()\n
    '''
def monthOfYear():
    '''returns Property\n\n
    monthOfYear()\n
    '''
def weekOfWeekyear():
    '''returns Property\n\n
    weekOfWeekyear()\n
    '''
def dayOfYear():
    '''returns Property\n\n
    dayOfYear()\n
    '''
def dayOfMonth():
    '''returns Property\n\n
    dayOfMonth()\n
    '''
def dayOfWeek():
    '''returns Property\n\n
    dayOfWeek()\n
    '''
def hourOfDay():
    '''returns Property\n\n
    hourOfDay()\n
    '''
def minuteOfDay():
    '''returns Property\n\n
    minuteOfDay()\n
    '''
def minuteOfHour():
    '''returns Property\n\n
    minuteOfHour()\n
    '''
def secondOfDay():
    '''returns Property\n\n
    secondOfDay()\n
    '''
def secondOfMinute():
    '''returns Property\n\n
    secondOfMinute()\n
    '''
def millisOfDay():
    '''returns Property\n\n
    millisOfDay()\n
    '''
def millisOfSecond():
    '''returns Property\n\n
    millisOfSecond()\n
    '''
def copy():
    '''returns MutableDateTime\n\n
    copy()\n
    '''
def clone():
    '''returns Object\n\n
    clone()\n
    '''
def getField():
    '''returns DateTimeField\n\n
    getField()\n
    '''
def getMutableDateTime():
    '''returns MutableDateTime\n\n
    getMutableDateTime()\n
    '''
def addWrapField():
    '''returns MutableDateTime\n\n
    addWrapField(final int n)\n
    '''
def roundFloor():
    '''returns MutableDateTime\n\n
    roundFloor()\n
    '''
def roundCeiling():
    '''returns MutableDateTime\n\n
    roundCeiling()\n
    '''
def roundHalfFloor():
    '''returns MutableDateTime\n\n
    roundHalfFloor()\n
    '''
def roundHalfCeiling():
    '''returns MutableDateTime\n\n
    roundHalfCeiling()\n
    '''
def roundHalfEven():
    '''returns MutableDateTime\n\n
    roundHalfEven()\n
    '''
