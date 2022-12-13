def now():
    '''    public static DateTime now()
    public static DateTime now(final DateTimeZone dateTimeZone)
    public static DateTime now(final Chronology chronology)
    '''
def parse():
    '''    public static DateTime parse(final String s)
    public static DateTime parse(final String s, final DateTimeFormatter dateTimeFormatter)
    '''
def DateTime():
    '''    public DateTime()
    public DateTime(final DateTimeZone dateTimeZone)
    public DateTime(final Chronology chronology)
    public DateTime(final long n)
    public DateTime(final long n, final DateTimeZone dateTimeZone)
    public DateTime(final long n, final Chronology chronology)
    public DateTime(final Object o)
    public DateTime(final Object o, final DateTimeZone dateTimeZone)
    public DateTime(final Object o, final Chronology chronology)
    public DateTime(final int n, final int n2, final int n3, final int n4, final int n5)
    public DateTime(final int n, final int n2, final int n3, final int n4, final int n5, final DateTimeZone dateTimeZone)
    public DateTime(final int n, final int n2, final int n3, final int n4, final int n5, final Chronology chronology)
    public DateTime(final int n, final int n2, final int n3, final int n4, final int n5, final int n6)
    public DateTime(final int n, final int n2, final int n3, final int n4, final int n5, final int n6, final DateTimeZone dateTimeZone)
    public DateTime(final int n, final int n2, final int n3, final int n4, final int n5, final int n6, final Chronology chronology)
    public DateTime(final int n, final int n2, final int n3, final int n4, final int n5, final int n6, final int n7)
    public DateTime(final int n, final int n2, final int n3, final int n4, final int n5, final int n6, final int n7, final DateTimeZone dateTimeZone)
    public DateTime(final int n, final int n2, final int n3, final int n4, final int n5, final int n6, final int n7, final Chronology chronology)
    '''
def toDateTime():
    '''    public DateTime toDateTime()
    public DateTime toDateTime(DateTimeZone zone)
    public DateTime toDateTime(Chronology chronology)
    '''
def toDateTimeISO():
    '''    public DateTime toDateTimeISO()
    '''
def withMillis():
    '''    public DateTime withMillis(final long n)
    '''
def withChronology():
    '''    public DateTime withChronology(Chronology chronology)
    '''
def withZone():
    '''    public DateTime withZone(final DateTimeZone dateTimeZone)
    '''
def withZoneRetainFields():
    '''    public DateTime withZoneRetainFields(DateTimeZone zone)
    '''
def withEarlierOffsetAtOverlap():
    '''    public DateTime withEarlierOffsetAtOverlap()
    '''
def withLaterOffsetAtOverlap():
    '''    public DateTime withLaterOffsetAtOverlap()
    '''
def withDate():
    '''    public DateTime withDate(final int n, final int n2, final int n3)
    public DateTime withDate(final LocalDate localDate)
    '''
def withTime():
    '''    public DateTime withTime(final int n, final int n2, final int n3, final int n4)
    public DateTime withTime(final LocalTime localTime)
    '''
def withTimeAtStartOfDay():
    '''    public DateTime withTimeAtStartOfDay()
    '''
def withFields():
    '''    public DateTime withFields(final ReadablePartial readablePartial)
    '''
def withField():
    '''    public DateTime withField(final DateTimeFieldType dateTimeFieldType, final int n)
    '''
def withFieldAdded():
    '''    public DateTime withFieldAdded(final DurationFieldType durationFieldType, final int n)
    '''
def withDurationAdded():
    '''    public DateTime withDurationAdded(final long n, final int n2)
    public DateTime withDurationAdded(final ReadableDuration readableDuration, final int n)
    '''
def withPeriodAdded():
    '''    public DateTime withPeriodAdded(final ReadablePeriod readablePeriod, final int n)
    '''
def plus():
    '''    public DateTime plus(final long n)
    public DateTime plus(final ReadableDuration readableDuration)
    public DateTime plus(final ReadablePeriod readablePeriod)
    '''
def plusYears():
    '''    public DateTime plusYears(final int n)
    '''
def plusMonths():
    '''    public DateTime plusMonths(final int n)
    '''
def plusWeeks():
    '''    public DateTime plusWeeks(final int n)
    '''
def plusDays():
    '''    public DateTime plusDays(final int n)
    '''
def plusHours():
    '''    public DateTime plusHours(final int n)
    '''
def plusMinutes():
    '''    public DateTime plusMinutes(final int n)
    '''
def plusSeconds():
    '''    public DateTime plusSeconds(final int n)
    '''
def plusMillis():
    '''    public DateTime plusMillis(final int n)
    '''
def minus():
    '''    public DateTime minus(final long n)
    public DateTime minus(final ReadableDuration readableDuration)
    public DateTime minus(final ReadablePeriod readablePeriod)
    '''
def minusYears():
    '''    public DateTime minusYears(final int n)
    '''
def minusMonths():
    '''    public DateTime minusMonths(final int n)
    '''
def minusWeeks():
    '''    public DateTime minusWeeks(final int n)
    '''
def minusDays():
    '''    public DateTime minusDays(final int n)
    '''
def minusHours():
    '''    public DateTime minusHours(final int n)
    '''
def minusMinutes():
    '''    public DateTime minusMinutes(final int n)
    '''
def minusSeconds():
    '''    public DateTime minusSeconds(final int n)
    '''
def minusMillis():
    '''    public DateTime minusMillis(final int n)
    '''
def property():
    '''    public Property property(final DateTimeFieldType obj)
    '''
def toDateMidnight():
    '''    public DateMidnight toDateMidnight()
    '''
def toYearMonthDay():
    '''    public YearMonthDay toYearMonthDay()
    '''
def toTimeOfDay():
    '''    public TimeOfDay toTimeOfDay()
    '''
def toLocalDateTime():
    '''    public LocalDateTime toLocalDateTime()
    '''
def toLocalDate():
    '''    public LocalDate toLocalDate()
    '''
def toLocalTime():
    '''    public LocalTime toLocalTime()
    '''
def withEra():
    '''    public DateTime withEra(final int n)
    '''
def withCenturyOfEra():
    '''    public DateTime withCenturyOfEra(final int n)
    '''
def withYearOfEra():
    '''    public DateTime withYearOfEra(final int n)
    '''
def withYearOfCentury():
    '''    public DateTime withYearOfCentury(final int n)
    '''
def withYear():
    '''    public DateTime withYear(final int n)
    '''
def withWeekyear():
    '''    public DateTime withWeekyear(final int n)
    '''
def withMonthOfYear():
    '''    public DateTime withMonthOfYear(final int n)
    '''
def withWeekOfWeekyear():
    '''    public DateTime withWeekOfWeekyear(final int n)
    '''
def withDayOfYear():
    '''    public DateTime withDayOfYear(final int n)
    '''
def withDayOfMonth():
    '''    public DateTime withDayOfMonth(final int n)
    '''
def withDayOfWeek():
    '''    public DateTime withDayOfWeek(final int n)
    '''
def withHourOfDay():
    '''    public DateTime withHourOfDay(final int n)
    '''
def withMinuteOfHour():
    '''    public DateTime withMinuteOfHour(final int n)
    '''
def withSecondOfMinute():
    '''    public DateTime withSecondOfMinute(final int n)
    '''
def withMillisOfSecond():
    '''    public DateTime withMillisOfSecond(final int n)
    '''
def withMillisOfDay():
    '''    public DateTime withMillisOfDay(final int n)
    '''
def era():
    '''    public Property era()
    '''
def centuryOfEra():
    '''    public Property centuryOfEra()
    '''
def yearOfCentury():
    '''    public Property yearOfCentury()
    '''
def yearOfEra():
    '''    public Property yearOfEra()
    '''
def year():
    '''    public Property year()
    '''
def weekyear():
    '''    public Property weekyear()
    '''
def monthOfYear():
    '''    public Property monthOfYear()
    '''
def weekOfWeekyear():
    '''    public Property weekOfWeekyear()
    '''
def dayOfYear():
    '''    public Property dayOfYear()
    '''
def dayOfMonth():
    '''    public Property dayOfMonth()
    '''
def dayOfWeek():
    '''    public Property dayOfWeek()
    '''
def hourOfDay():
    '''    public Property hourOfDay()
    '''
def minuteOfDay():
    '''    public Property minuteOfDay()
    '''
def minuteOfHour():
    '''    public Property minuteOfHour()
    '''
def secondOfDay():
    '''    public Property secondOfDay()
    '''
def secondOfMinute():
    '''    public Property secondOfMinute()
    '''
def millisOfDay():
    '''    public Property millisOfDay()
    '''
def millisOfSecond():
    '''    public Property millisOfSecond()
    '''
def getField():
    '''    public DateTimeField getField()
    '''
def getDateTime():
    '''    public DateTime getDateTime()
    '''
def addToCopy():
    '''    public DateTime addToCopy(final int n)
    public DateTime addToCopy(final long n)
    '''
def addWrapFieldToCopy():
    '''    public DateTime addWrapFieldToCopy(final int n)
    '''
def setCopy():
    '''    public DateTime setCopy(final int n)
    public DateTime setCopy(final String s, final Locale locale)
    public DateTime setCopy(final String s)
    '''
def withMaximumValue():
    '''    public DateTime withMaximumValue()
    '''
def withMinimumValue():
    '''    public DateTime withMinimumValue()
    '''
def roundFloorCopy():
    '''    public DateTime roundFloorCopy()
    '''
def roundCeilingCopy():
    '''    public DateTime roundCeilingCopy()
    '''
def roundHalfFloorCopy():
    '''    public DateTime roundHalfFloorCopy()
    '''
def roundHalfCeilingCopy():
    '''    public DateTime roundHalfCeilingCopy()
    '''
def roundHalfEvenCopy():
    '''    public DateTime roundHalfEvenCopy()
    '''
