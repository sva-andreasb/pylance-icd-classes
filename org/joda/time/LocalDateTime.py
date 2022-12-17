def ():
    '''returns LocalDateTime\n\n
    ()\n
    (final DateTimeZone dateTimeZone)\n
    (final Chronology chronology)\n
    (final long n)\n
    (final long n, final DateTimeZone dateTimeZone)\n
    (final long n, Chronology chronology)\n
    (final Object o)\n
    (final Object o, final DateTimeZone dateTimeZone)\n
    (final Object o, Chronology chronology)\n
    (final int n, final int n2, final int n3, final int n4, final int n5)\n
    (final int n, final int n2, final int n3, final int n4, final int n5, final int n6)\n
    (final int n, final int n2, final int n3, final int n4, final int n5, final int n6, final int n7)\n
    (final int n, final int n2, final int n3, final int n4, final int n5, final int n6, final int n7, Chronology withUTC)\n
    '''
def size():
    '''returns int\n\n
    size()\n
    '''
def getValue():
    '''returns int\n\n
    getValue(final int i)\n
    '''
def get():
    '''returns int\n\n
    get(final DateTimeFieldType dateTimeFieldType)\n
    '''
def isSupported():
    '''returns boolean\n\n
    isSupported(final DateTimeFieldType dateTimeFieldType)\n
    isSupported(final DurationFieldType durationFieldType)\n
    '''
def getChronology():
    '''returns Chronology\n\n
    getChronology()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object o)\n
    '''
def compareTo():
    '''returns int\n\n
    compareTo(final ReadablePartial readablePartial)\n
    '''
def toDateTime():
    '''returns DateTime\n\n
    toDateTime()\n
    toDateTime(DateTimeZone zone)\n
    '''
def toLocalDate():
    '''returns LocalDate\n\n
    toLocalDate()\n
    '''
def toLocalTime():
    '''returns LocalTime\n\n
    toLocalTime()\n
    '''
def toDate():
    '''returns Date\n\n
    toDate()\n
    toDate(final TimeZone zone)\n
    '''
def withDate():
    '''returns LocalDateTime\n\n
    withDate(final int n, final int n2, final int n3)\n
    '''
def withTime():
    '''returns LocalDateTime\n\n
    withTime(final int n, final int n2, final int n3, final int n4)\n
    '''
def withFields():
    '''returns LocalDateTime\n\n
    withFields(final ReadablePartial readablePartial)\n
    '''
def withField():
    '''returns LocalDateTime\n\n
    withField(final DateTimeFieldType dateTimeFieldType, final int n)\n
    '''
def withFieldAdded():
    '''returns LocalDateTime\n\n
    withFieldAdded(final DurationFieldType durationFieldType, final int n)\n
    '''
def withDurationAdded():
    '''returns LocalDateTime\n\n
    withDurationAdded(final ReadableDuration readableDuration, final int n)\n
    '''
def withPeriodAdded():
    '''returns LocalDateTime\n\n
    withPeriodAdded(final ReadablePeriod readablePeriod, final int n)\n
    '''
def plus():
    '''returns LocalDateTime\n\n
    plus(final ReadableDuration readableDuration)\n
    plus(final ReadablePeriod readablePeriod)\n
    '''
def plusYears():
    '''returns LocalDateTime\n\n
    plusYears(final int n)\n
    '''
def plusMonths():
    '''returns LocalDateTime\n\n
    plusMonths(final int n)\n
    '''
def plusWeeks():
    '''returns LocalDateTime\n\n
    plusWeeks(final int n)\n
    '''
def plusDays():
    '''returns LocalDateTime\n\n
    plusDays(final int n)\n
    '''
def plusHours():
    '''returns LocalDateTime\n\n
    plusHours(final int n)\n
    '''
def plusMinutes():
    '''returns LocalDateTime\n\n
    plusMinutes(final int n)\n
    '''
def plusSeconds():
    '''returns LocalDateTime\n\n
    plusSeconds(final int n)\n
    '''
def plusMillis():
    '''returns LocalDateTime\n\n
    plusMillis(final int n)\n
    '''
def minus():
    '''returns LocalDateTime\n\n
    minus(final ReadableDuration readableDuration)\n
    minus(final ReadablePeriod readablePeriod)\n
    '''
def minusYears():
    '''returns LocalDateTime\n\n
    minusYears(final int n)\n
    '''
def minusMonths():
    '''returns LocalDateTime\n\n
    minusMonths(final int n)\n
    '''
def minusWeeks():
    '''returns LocalDateTime\n\n
    minusWeeks(final int n)\n
    '''
def minusDays():
    '''returns LocalDateTime\n\n
    minusDays(final int n)\n
    '''
def minusHours():
    '''returns LocalDateTime\n\n
    minusHours(final int n)\n
    '''
def minusMinutes():
    '''returns LocalDateTime\n\n
    minusMinutes(final int n)\n
    '''
def minusSeconds():
    '''returns LocalDateTime\n\n
    minusSeconds(final int n)\n
    '''
def minusMillis():
    '''returns LocalDateTime\n\n
    minusMillis(final int n)\n
    '''
def property():
    '''returns Property\n\n
    property(final DateTimeFieldType obj)\n
    '''
def getEra():
    '''returns int\n\n
    getEra()\n
    '''
def getCenturyOfEra():
    '''returns int\n\n
    getCenturyOfEra()\n
    '''
def getYearOfEra():
    '''returns int\n\n
    getYearOfEra()\n
    '''
def getYearOfCentury():
    '''returns int\n\n
    getYearOfCentury()\n
    '''
def getYear():
    '''returns int\n\n
    getYear()\n
    '''
def getWeekyear():
    '''returns int\n\n
    getWeekyear()\n
    '''
def getMonthOfYear():
    '''returns int\n\n
    getMonthOfYear()\n
    '''
def getWeekOfWeekyear():
    '''returns int\n\n
    getWeekOfWeekyear()\n
    '''
def getDayOfYear():
    '''returns int\n\n
    getDayOfYear()\n
    '''
def getDayOfMonth():
    '''returns int\n\n
    getDayOfMonth()\n
    '''
def getDayOfWeek():
    '''returns int\n\n
    getDayOfWeek()\n
    '''
def getHourOfDay():
    '''returns int\n\n
    getHourOfDay()\n
    '''
def getMinuteOfHour():
    '''returns int\n\n
    getMinuteOfHour()\n
    '''
def getSecondOfMinute():
    '''returns int\n\n
    getSecondOfMinute()\n
    '''
def getMillisOfSecond():
    '''returns int\n\n
    getMillisOfSecond()\n
    '''
def getMillisOfDay():
    '''returns int\n\n
    getMillisOfDay()\n
    '''
def withEra():
    '''returns LocalDateTime\n\n
    withEra(final int n)\n
    '''
def withCenturyOfEra():
    '''returns LocalDateTime\n\n
    withCenturyOfEra(final int n)\n
    '''
def withYearOfEra():
    '''returns LocalDateTime\n\n
    withYearOfEra(final int n)\n
    '''
def withYearOfCentury():
    '''returns LocalDateTime\n\n
    withYearOfCentury(final int n)\n
    '''
def withYear():
    '''returns LocalDateTime\n\n
    withYear(final int n)\n
    '''
def withWeekyear():
    '''returns LocalDateTime\n\n
    withWeekyear(final int n)\n
    '''
def withMonthOfYear():
    '''returns LocalDateTime\n\n
    withMonthOfYear(final int n)\n
    '''
def withWeekOfWeekyear():
    '''returns LocalDateTime\n\n
    withWeekOfWeekyear(final int n)\n
    '''
def withDayOfYear():
    '''returns LocalDateTime\n\n
    withDayOfYear(final int n)\n
    '''
def withDayOfMonth():
    '''returns LocalDateTime\n\n
    withDayOfMonth(final int n)\n
    '''
def withDayOfWeek():
    '''returns LocalDateTime\n\n
    withDayOfWeek(final int n)\n
    '''
def withHourOfDay():
    '''returns LocalDateTime\n\n
    withHourOfDay(final int n)\n
    '''
def withMinuteOfHour():
    '''returns LocalDateTime\n\n
    withMinuteOfHour(final int n)\n
    '''
def withSecondOfMinute():
    '''returns LocalDateTime\n\n
    withSecondOfMinute(final int n)\n
    '''
def withMillisOfSecond():
    '''returns LocalDateTime\n\n
    withMillisOfSecond(final int n)\n
    '''
def withMillisOfDay():
    '''returns LocalDateTime\n\n
    withMillisOfDay(final int n)\n
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
def minuteOfHour():
    '''returns Property\n\n
    minuteOfHour()\n
    '''
def secondOfMinute():
    '''returns Property\n\n
    secondOfMinute()\n
    '''
def millisOfSecond():
    '''returns Property\n\n
    millisOfSecond()\n
    '''
def millisOfDay():
    '''returns Property\n\n
    millisOfDay()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString(final String s)\n
    toString(final String s, final Locale locale)\n
    '''
def getField():
    '''returns DateTimeField\n\n
    getField()\n
    '''
def getLocalDateTime():
    '''returns LocalDateTime\n\n
    getLocalDateTime()\n
    '''
def addToCopy():
    '''returns LocalDateTime\n\n
    addToCopy(final int n)\n
    addToCopy(final long n)\n
    '''
def addWrapFieldToCopy():
    '''returns LocalDateTime\n\n
    addWrapFieldToCopy(final int n)\n
    '''
def setCopy():
    '''returns LocalDateTime\n\n
    setCopy(final int n)\n
    setCopy(final String s, final Locale locale)\n
    setCopy(final String s)\n
    '''
def withMaximumValue():
    '''returns LocalDateTime\n\n
    withMaximumValue()\n
    '''
def withMinimumValue():
    '''returns LocalDateTime\n\n
    withMinimumValue()\n
    '''
def roundFloorCopy():
    '''returns LocalDateTime\n\n
    roundFloorCopy()\n
    '''
def roundCeilingCopy():
    '''returns LocalDateTime\n\n
    roundCeilingCopy()\n
    '''
def roundHalfFloorCopy():
    '''returns LocalDateTime\n\n
    roundHalfFloorCopy()\n
    '''
def roundHalfCeilingCopy():
    '''returns LocalDateTime\n\n
    roundHalfCeilingCopy()\n
    '''
def roundHalfEvenCopy():
    '''returns LocalDateTime\n\n
    roundHalfEvenCopy()\n
    '''
