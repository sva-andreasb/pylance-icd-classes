def ():
    '''returns DateTime\n\n
    ()\n
    (final DateTimeZone dateTimeZone)\n
    (final Chronology chronology)\n
    (final long n)\n
    (final long n, final DateTimeZone dateTimeZone)\n
    (final long n, final Chronology chronology)\n
    (final Object o)\n
    (final Object o, final DateTimeZone dateTimeZone)\n
    (final Object o, final Chronology chronology)\n
    (final int n, final int n2, final int n3, final int n4, final int n5)\n
    (final int n, final int n2, final int n3, final int n4, final int n5, final DateTimeZone dateTimeZone)\n
    (final int n, final int n2, final int n3, final int n4, final int n5, final Chronology chronology)\n
    (final int n, final int n2, final int n3, final int n4, final int n5, final int n6)\n
    (final int n, final int n2, final int n3, final int n4, final int n5, final int n6, final DateTimeZone dateTimeZone)\n
    (final int n, final int n2, final int n3, final int n4, final int n5, final int n6, final Chronology chronology)\n
    (final int n, final int n2, final int n3, final int n4, final int n5, final int n6, final int n7)\n
    (final int n, final int n2, final int n3, final int n4, final int n5, final int n6, final int n7, final DateTimeZone dateTimeZone)\n
    (final int n, final int n2, final int n3, final int n4, final int n5, final int n6, final int n7, final Chronology chronology)\n
    '''
def toDateTime():
    '''returns DateTime\n\n
    toDateTime()\n
    toDateTime(DateTimeZone zone)\n
    toDateTime(Chronology chronology)\n
    '''
def toDateTimeISO():
    '''returns DateTime\n\n
    toDateTimeISO()\n
    '''
def withMillis():
    '''returns DateTime\n\n
    withMillis(final long n)\n
    '''
def withChronology():
    '''returns DateTime\n\n
    withChronology(Chronology chronology)\n
    '''
def withZone():
    '''returns DateTime\n\n
    withZone(final DateTimeZone dateTimeZone)\n
    '''
def withZoneRetainFields():
    '''returns DateTime\n\n
    withZoneRetainFields(DateTimeZone zone)\n
    '''
def withEarlierOffsetAtOverlap():
    '''returns DateTime\n\n
    withEarlierOffsetAtOverlap()\n
    '''
def withLaterOffsetAtOverlap():
    '''returns DateTime\n\n
    withLaterOffsetAtOverlap()\n
    '''
def withDate():
    '''returns DateTime\n\n
    withDate(final int n, final int n2, final int n3)\n
    withDate(final LocalDate localDate)\n
    '''
def withTime():
    '''returns DateTime\n\n
    withTime(final int n, final int n2, final int n3, final int n4)\n
    withTime(final LocalTime localTime)\n
    '''
def withTimeAtStartOfDay():
    '''returns DateTime\n\n
    withTimeAtStartOfDay()\n
    '''
def withFields():
    '''returns DateTime\n\n
    withFields(final ReadablePartial readablePartial)\n
    '''
def withField():
    '''returns DateTime\n\n
    withField(final DateTimeFieldType dateTimeFieldType, final int n)\n
    '''
def withFieldAdded():
    '''returns DateTime\n\n
    withFieldAdded(final DurationFieldType durationFieldType, final int n)\n
    '''
def withDurationAdded():
    '''returns DateTime\n\n
    withDurationAdded(final long n, final int n2)\n
    withDurationAdded(final ReadableDuration readableDuration, final int n)\n
    '''
def withPeriodAdded():
    '''returns DateTime\n\n
    withPeriodAdded(final ReadablePeriod readablePeriod, final int n)\n
    '''
def plus():
    '''returns DateTime\n\n
    plus(final long n)\n
    plus(final ReadableDuration readableDuration)\n
    plus(final ReadablePeriod readablePeriod)\n
    '''
def plusYears():
    '''returns DateTime\n\n
    plusYears(final int n)\n
    '''
def plusMonths():
    '''returns DateTime\n\n
    plusMonths(final int n)\n
    '''
def plusWeeks():
    '''returns DateTime\n\n
    plusWeeks(final int n)\n
    '''
def plusDays():
    '''returns DateTime\n\n
    plusDays(final int n)\n
    '''
def plusHours():
    '''returns DateTime\n\n
    plusHours(final int n)\n
    '''
def plusMinutes():
    '''returns DateTime\n\n
    plusMinutes(final int n)\n
    '''
def plusSeconds():
    '''returns DateTime\n\n
    plusSeconds(final int n)\n
    '''
def plusMillis():
    '''returns DateTime\n\n
    plusMillis(final int n)\n
    '''
def minus():
    '''returns DateTime\n\n
    minus(final long n)\n
    minus(final ReadableDuration readableDuration)\n
    minus(final ReadablePeriod readablePeriod)\n
    '''
def minusYears():
    '''returns DateTime\n\n
    minusYears(final int n)\n
    '''
def minusMonths():
    '''returns DateTime\n\n
    minusMonths(final int n)\n
    '''
def minusWeeks():
    '''returns DateTime\n\n
    minusWeeks(final int n)\n
    '''
def minusDays():
    '''returns DateTime\n\n
    minusDays(final int n)\n
    '''
def minusHours():
    '''returns DateTime\n\n
    minusHours(final int n)\n
    '''
def minusMinutes():
    '''returns DateTime\n\n
    minusMinutes(final int n)\n
    '''
def minusSeconds():
    '''returns DateTime\n\n
    minusSeconds(final int n)\n
    '''
def minusMillis():
    '''returns DateTime\n\n
    minusMillis(final int n)\n
    '''
def property():
    '''returns Property\n\n
    property(final DateTimeFieldType obj)\n
    '''
def toDateMidnight():
    '''returns DateMidnight\n\n
    toDateMidnight()\n
    '''
def toYearMonthDay():
    '''returns YearMonthDay\n\n
    toYearMonthDay()\n
    '''
def toTimeOfDay():
    '''returns TimeOfDay\n\n
    toTimeOfDay()\n
    '''
def toLocalDateTime():
    '''returns LocalDateTime\n\n
    toLocalDateTime()\n
    '''
def toLocalDate():
    '''returns LocalDate\n\n
    toLocalDate()\n
    '''
def toLocalTime():
    '''returns LocalTime\n\n
    toLocalTime()\n
    '''
def withEra():
    '''returns DateTime\n\n
    withEra(final int n)\n
    '''
def withCenturyOfEra():
    '''returns DateTime\n\n
    withCenturyOfEra(final int n)\n
    '''
def withYearOfEra():
    '''returns DateTime\n\n
    withYearOfEra(final int n)\n
    '''
def withYearOfCentury():
    '''returns DateTime\n\n
    withYearOfCentury(final int n)\n
    '''
def withYear():
    '''returns DateTime\n\n
    withYear(final int n)\n
    '''
def withWeekyear():
    '''returns DateTime\n\n
    withWeekyear(final int n)\n
    '''
def withMonthOfYear():
    '''returns DateTime\n\n
    withMonthOfYear(final int n)\n
    '''
def withWeekOfWeekyear():
    '''returns DateTime\n\n
    withWeekOfWeekyear(final int n)\n
    '''
def withDayOfYear():
    '''returns DateTime\n\n
    withDayOfYear(final int n)\n
    '''
def withDayOfMonth():
    '''returns DateTime\n\n
    withDayOfMonth(final int n)\n
    '''
def withDayOfWeek():
    '''returns DateTime\n\n
    withDayOfWeek(final int n)\n
    '''
def withHourOfDay():
    '''returns DateTime\n\n
    withHourOfDay(final int n)\n
    '''
def withMinuteOfHour():
    '''returns DateTime\n\n
    withMinuteOfHour(final int n)\n
    '''
def withSecondOfMinute():
    '''returns DateTime\n\n
    withSecondOfMinute(final int n)\n
    '''
def withMillisOfSecond():
    '''returns DateTime\n\n
    withMillisOfSecond(final int n)\n
    '''
def withMillisOfDay():
    '''returns DateTime\n\n
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
def getField():
    '''returns DateTimeField\n\n
    getField()\n
    '''
def getDateTime():
    '''returns DateTime\n\n
    getDateTime()\n
    '''
def addToCopy():
    '''returns DateTime\n\n
    addToCopy(final int n)\n
    addToCopy(final long n)\n
    '''
def addWrapFieldToCopy():
    '''returns DateTime\n\n
    addWrapFieldToCopy(final int n)\n
    '''
def setCopy():
    '''returns DateTime\n\n
    setCopy(final int n)\n
    setCopy(final String s, final Locale locale)\n
    setCopy(final String s)\n
    '''
def withMaximumValue():
    '''returns DateTime\n\n
    withMaximumValue()\n
    '''
def withMinimumValue():
    '''returns DateTime\n\n
    withMinimumValue()\n
    '''
def roundFloorCopy():
    '''returns DateTime\n\n
    roundFloorCopy()\n
    '''
def roundCeilingCopy():
    '''returns DateTime\n\n
    roundCeilingCopy()\n
    '''
def roundHalfFloorCopy():
    '''returns DateTime\n\n
    roundHalfFloorCopy()\n
    '''
def roundHalfCeilingCopy():
    '''returns DateTime\n\n
    roundHalfCeilingCopy()\n
    '''
def roundHalfEvenCopy():
    '''returns DateTime\n\n
    roundHalfEvenCopy()\n
    '''
