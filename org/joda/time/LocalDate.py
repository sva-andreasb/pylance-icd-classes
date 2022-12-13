def now():
'''public static LocalDate now()
public static LocalDate now(final DateTimeZone dateTimeZone)
public static LocalDate now(final Chronology chronology)
'''
pass
def parse():
'''public static LocalDate parse(final String s)
public static LocalDate parse(final String s, final DateTimeFormatter dateTimeFormatter)
'''
pass
def fromCalendarFields():
'''public static LocalDate fromCalendarFields(final Calendar calendar)
'''
pass
def fromDateFields():
'''public static LocalDate fromDateFields(final Date time)
'''
pass
def LocalDate():
'''public LocalDate()
public LocalDate(final DateTimeZone dateTimeZone)
public LocalDate(final Chronology chronology)
public LocalDate(final long n)
public LocalDate(final long n, final DateTimeZone dateTimeZone)
public LocalDate(final long n, Chronology iChronology)
public LocalDate(final Object o)
public LocalDate(final Object o, final DateTimeZone dateTimeZone)
public LocalDate(final Object o, Chronology chronology)
public LocalDate(final int n, final int n2, final int n3)
public LocalDate(final int n, final int n2, final int n3, Chronology withUTC)
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
def hashCode():
'''public int hashCode()
'''
pass
def compareTo():
'''public int compareTo(final ReadablePartial readablePartial)
'''
pass
def toDateTimeAtStartOfDay():
'''public DateTime toDateTimeAtStartOfDay()
public DateTime toDateTimeAtStartOfDay(DateTimeZone zone)
'''
pass
def toDateTimeAtMidnight():
'''public DateTime toDateTimeAtMidnight()
public DateTime toDateTimeAtMidnight(DateTimeZone zone)
'''
pass
def toDateTimeAtCurrentTime():
'''public DateTime toDateTimeAtCurrentTime()
public DateTime toDateTimeAtCurrentTime(DateTimeZone zone)
'''
pass
def toDateMidnight():
'''public DateMidnight toDateMidnight()
public DateMidnight toDateMidnight(DateTimeZone zone)
'''
pass
def toLocalDateTime():
'''public LocalDateTime toLocalDateTime(final LocalTime localTime)
'''
pass
def toDateTime():
'''public DateTime toDateTime(final LocalTime localTime)
public DateTime toDateTime(final LocalTime localTime, final DateTimeZone dateTimeZone)
'''
pass
def toInterval():
'''public Interval toInterval()
public Interval toInterval(DateTimeZone zone)
'''
pass
def toDate():
'''public Date toDate()
'''
pass
def withFields():
'''public LocalDate withFields(final ReadablePartial readablePartial)
'''
pass
def withField():
'''public LocalDate withField(final DateTimeFieldType obj, final int n)
'''
pass
def withFieldAdded():
'''public LocalDate withFieldAdded(final DurationFieldType obj, final int n)
'''
pass
def withPeriodAdded():
'''public LocalDate withPeriodAdded(final ReadablePeriod readablePeriod, final int n)
'''
pass
def plus():
'''public LocalDate plus(final ReadablePeriod readablePeriod)
'''
pass
def plusYears():
'''public LocalDate plusYears(final int n)
'''
pass
def plusMonths():
'''public LocalDate plusMonths(final int n)
'''
pass
def plusWeeks():
'''public LocalDate plusWeeks(final int n)
'''
pass
def plusDays():
'''public LocalDate plusDays(final int n)
'''
pass
def minus():
'''public LocalDate minus(final ReadablePeriod readablePeriod)
'''
pass
def minusYears():
'''public LocalDate minusYears(final int n)
'''
pass
def minusMonths():
'''public LocalDate minusMonths(final int n)
'''
pass
def minusWeeks():
'''public LocalDate minusWeeks(final int n)
'''
pass
def minusDays():
'''public LocalDate minusDays(final int n)
'''
pass
def property():
'''public Property property(final DateTimeFieldType obj)
'''
pass
def getEra():
'''public int getEra()
'''
pass
def getCenturyOfEra():
'''public int getCenturyOfEra()
'''
pass
def getYearOfEra():
'''public int getYearOfEra()
'''
pass
def getYearOfCentury():
'''public int getYearOfCentury()
'''
pass
def getYear():
'''public int getYear()
'''
pass
def getWeekyear():
'''public int getWeekyear()
'''
pass
def getMonthOfYear():
'''public int getMonthOfYear()
'''
pass
def getWeekOfWeekyear():
'''public int getWeekOfWeekyear()
'''
pass
def getDayOfYear():
'''public int getDayOfYear()
'''
pass
def getDayOfMonth():
'''public int getDayOfMonth()
'''
pass
def getDayOfWeek():
'''public int getDayOfWeek()
'''
pass
def withEra():
'''public LocalDate withEra(final int n)
'''
pass
def withCenturyOfEra():
'''public LocalDate withCenturyOfEra(final int n)
'''
pass
def withYearOfEra():
'''public LocalDate withYearOfEra(final int n)
'''
pass
def withYearOfCentury():
'''public LocalDate withYearOfCentury(final int n)
'''
pass
def withYear():
'''public LocalDate withYear(final int n)
'''
pass
def withWeekyear():
'''public LocalDate withWeekyear(final int n)
'''
pass
def withMonthOfYear():
'''public LocalDate withMonthOfYear(final int n)
'''
pass
def withWeekOfWeekyear():
'''public LocalDate withWeekOfWeekyear(final int n)
'''
pass
def withDayOfYear():
'''public LocalDate withDayOfYear(final int n)
'''
pass
def withDayOfMonth():
'''public LocalDate withDayOfMonth(final int n)
'''
pass
def withDayOfWeek():
'''public LocalDate withDayOfWeek(final int n)
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
def getLocalDate():
'''public LocalDate getLocalDate()
'''
pass
def addToCopy():
'''public LocalDate addToCopy(final int n)
'''
pass
def addWrapFieldToCopy():
'''public LocalDate addWrapFieldToCopy(final int n)
'''
pass
def setCopy():
'''public LocalDate setCopy(final int n)
public LocalDate setCopy(final String s, final Locale locale)
public LocalDate setCopy(final String s)
'''
pass
def withMaximumValue():
'''public LocalDate withMaximumValue()
'''
pass
def withMinimumValue():
'''public LocalDate withMinimumValue()
'''
pass
def roundFloorCopy():
'''public LocalDate roundFloorCopy()
'''
pass
def roundCeilingCopy():
'''public LocalDate roundCeilingCopy()
'''
pass
def roundHalfFloorCopy():
'''public LocalDate roundHalfFloorCopy()
'''
pass
def roundHalfCeilingCopy():
'''public LocalDate roundHalfCeilingCopy()
'''
pass
def roundHalfEvenCopy():
'''public LocalDate roundHalfEvenCopy()
'''
pass
