def now():
'''public static DateTime now()
public static DateTime now(final DateTimeZone dateTimeZone)
public static DateTime now(final Chronology chronology)
'''
pass
def parse():
'''public static DateTime parse(final String s)
public static DateTime parse(final String s, final DateTimeFormatter dateTimeFormatter)
'''
pass
def DateTime():
'''public DateTime()
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
pass
def toDateTime():
'''public DateTime toDateTime()
public DateTime toDateTime(DateTimeZone zone)
public DateTime toDateTime(Chronology chronology)
'''
pass
def toDateTimeISO():
'''public DateTime toDateTimeISO()
'''
pass
def withMillis():
'''public DateTime withMillis(final long n)
'''
pass
def withChronology():
'''public DateTime withChronology(Chronology chronology)
'''
pass
def withZone():
'''public DateTime withZone(final DateTimeZone dateTimeZone)
'''
pass
def withZoneRetainFields():
'''public DateTime withZoneRetainFields(DateTimeZone zone)
'''
pass
def withEarlierOffsetAtOverlap():
'''public DateTime withEarlierOffsetAtOverlap()
'''
pass
def withLaterOffsetAtOverlap():
'''public DateTime withLaterOffsetAtOverlap()
'''
pass
def withDate():
'''public DateTime withDate(final int n, final int n2, final int n3)
public DateTime withDate(final LocalDate localDate)
'''
pass
def withTime():
'''public DateTime withTime(final int n, final int n2, final int n3, final int n4)
public DateTime withTime(final LocalTime localTime)
'''
pass
def withTimeAtStartOfDay():
'''public DateTime withTimeAtStartOfDay()
'''
pass
def withFields():
'''public DateTime withFields(final ReadablePartial readablePartial)
'''
pass
def withField():
'''public DateTime withField(final DateTimeFieldType dateTimeFieldType, final int n)
'''
pass
def withFieldAdded():
'''public DateTime withFieldAdded(final DurationFieldType durationFieldType, final int n)
'''
pass
def withDurationAdded():
'''public DateTime withDurationAdded(final long n, final int n2)
public DateTime withDurationAdded(final ReadableDuration readableDuration, final int n)
'''
pass
def withPeriodAdded():
'''public DateTime withPeriodAdded(final ReadablePeriod readablePeriod, final int n)
'''
pass
def plus():
'''public DateTime plus(final long n)
public DateTime plus(final ReadableDuration readableDuration)
public DateTime plus(final ReadablePeriod readablePeriod)
'''
pass
def plusYears():
'''public DateTime plusYears(final int n)
'''
pass
def plusMonths():
'''public DateTime plusMonths(final int n)
'''
pass
def plusWeeks():
'''public DateTime plusWeeks(final int n)
'''
pass
def plusDays():
'''public DateTime plusDays(final int n)
'''
pass
def plusHours():
'''public DateTime plusHours(final int n)
'''
pass
def plusMinutes():
'''public DateTime plusMinutes(final int n)
'''
pass
def plusSeconds():
'''public DateTime plusSeconds(final int n)
'''
pass
def plusMillis():
'''public DateTime plusMillis(final int n)
'''
pass
def minus():
'''public DateTime minus(final long n)
public DateTime minus(final ReadableDuration readableDuration)
public DateTime minus(final ReadablePeriod readablePeriod)
'''
pass
def minusYears():
'''public DateTime minusYears(final int n)
'''
pass
def minusMonths():
'''public DateTime minusMonths(final int n)
'''
pass
def minusWeeks():
'''public DateTime minusWeeks(final int n)
'''
pass
def minusDays():
'''public DateTime minusDays(final int n)
'''
pass
def minusHours():
'''public DateTime minusHours(final int n)
'''
pass
def minusMinutes():
'''public DateTime minusMinutes(final int n)
'''
pass
def minusSeconds():
'''public DateTime minusSeconds(final int n)
'''
pass
def minusMillis():
'''public DateTime minusMillis(final int n)
'''
pass
def property():
'''public Property property(final DateTimeFieldType obj)
'''
pass
def toDateMidnight():
'''public DateMidnight toDateMidnight()
'''
pass
def toYearMonthDay():
'''public YearMonthDay toYearMonthDay()
'''
pass
def toTimeOfDay():
'''public TimeOfDay toTimeOfDay()
'''
pass
def toLocalDateTime():
'''public LocalDateTime toLocalDateTime()
'''
pass
def toLocalDate():
'''public LocalDate toLocalDate()
'''
pass
def toLocalTime():
'''public LocalTime toLocalTime()
'''
pass
def withEra():
'''public DateTime withEra(final int n)
'''
pass
def withCenturyOfEra():
'''public DateTime withCenturyOfEra(final int n)
'''
pass
def withYearOfEra():
'''public DateTime withYearOfEra(final int n)
'''
pass
def withYearOfCentury():
'''public DateTime withYearOfCentury(final int n)
'''
pass
def withYear():
'''public DateTime withYear(final int n)
'''
pass
def withWeekyear():
'''public DateTime withWeekyear(final int n)
'''
pass
def withMonthOfYear():
'''public DateTime withMonthOfYear(final int n)
'''
pass
def withWeekOfWeekyear():
'''public DateTime withWeekOfWeekyear(final int n)
'''
pass
def withDayOfYear():
'''public DateTime withDayOfYear(final int n)
'''
pass
def withDayOfMonth():
'''public DateTime withDayOfMonth(final int n)
'''
pass
def withDayOfWeek():
'''public DateTime withDayOfWeek(final int n)
'''
pass
def withHourOfDay():
'''public DateTime withHourOfDay(final int n)
'''
pass
def withMinuteOfHour():
'''public DateTime withMinuteOfHour(final int n)
'''
pass
def withSecondOfMinute():
'''public DateTime withSecondOfMinute(final int n)
'''
pass
def withMillisOfSecond():
'''public DateTime withMillisOfSecond(final int n)
'''
pass
def withMillisOfDay():
'''public DateTime withMillisOfDay(final int n)
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
def getField():
'''public DateTimeField getField()
'''
pass
def getDateTime():
'''public DateTime getDateTime()
'''
pass
def addToCopy():
'''public DateTime addToCopy(final int n)
public DateTime addToCopy(final long n)
'''
pass
def addWrapFieldToCopy():
'''public DateTime addWrapFieldToCopy(final int n)
'''
pass
def setCopy():
'''public DateTime setCopy(final int n)
public DateTime setCopy(final String s, final Locale locale)
public DateTime setCopy(final String s)
'''
pass
def withMaximumValue():
'''public DateTime withMaximumValue()
'''
pass
def withMinimumValue():
'''public DateTime withMinimumValue()
'''
pass
def roundFloorCopy():
'''public DateTime roundFloorCopy()
'''
pass
def roundCeilingCopy():
'''public DateTime roundCeilingCopy()
'''
pass
def roundHalfFloorCopy():
'''public DateTime roundHalfFloorCopy()
'''
pass
def roundHalfCeilingCopy():
'''public DateTime roundHalfCeilingCopy()
'''
pass
def roundHalfEvenCopy():
'''public DateTime roundHalfEvenCopy()
'''
pass
