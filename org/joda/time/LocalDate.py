def now():
    '''    public static LocalDate now()
    public static LocalDate now(final DateTimeZone dateTimeZone)
    public static LocalDate now(final Chronology chronology)
    '''
def parse():
    '''    public static LocalDate parse(final String s)
    public static LocalDate parse(final String s, final DateTimeFormatter dateTimeFormatter)
    '''
def fromCalendarFields():
    '''    public static LocalDate fromCalendarFields(final Calendar calendar)
    '''
def fromDateFields():
    '''    public static LocalDate fromDateFields(final Date time)
    '''
def LocalDate():
    '''    public LocalDate()
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
def hashCode():
    '''    public int hashCode()
    '''
def compareTo():
    '''    public int compareTo(final ReadablePartial readablePartial)
    '''
def toDateTimeAtStartOfDay():
    '''    public DateTime toDateTimeAtStartOfDay()
    public DateTime toDateTimeAtStartOfDay(DateTimeZone zone)
    '''
def toDateTimeAtMidnight():
    '''    public DateTime toDateTimeAtMidnight()
    public DateTime toDateTimeAtMidnight(DateTimeZone zone)
    '''
def toDateTimeAtCurrentTime():
    '''    public DateTime toDateTimeAtCurrentTime()
    public DateTime toDateTimeAtCurrentTime(DateTimeZone zone)
    '''
def toDateMidnight():
    '''    public DateMidnight toDateMidnight()
    public DateMidnight toDateMidnight(DateTimeZone zone)
    '''
def toLocalDateTime():
    '''    public LocalDateTime toLocalDateTime(final LocalTime localTime)
    '''
def toDateTime():
    '''    public DateTime toDateTime(final LocalTime localTime)
    public DateTime toDateTime(final LocalTime localTime, final DateTimeZone dateTimeZone)
    '''
def toInterval():
    '''    public Interval toInterval()
    public Interval toInterval(DateTimeZone zone)
    '''
def toDate():
    '''    public Date toDate()
    '''
def withFields():
    '''    public LocalDate withFields(final ReadablePartial readablePartial)
    '''
def withField():
    '''    public LocalDate withField(final DateTimeFieldType obj, final int n)
    '''
def withFieldAdded():
    '''    public LocalDate withFieldAdded(final DurationFieldType obj, final int n)
    '''
def withPeriodAdded():
    '''    public LocalDate withPeriodAdded(final ReadablePeriod readablePeriod, final int n)
    '''
def plus():
    '''    public LocalDate plus(final ReadablePeriod readablePeriod)
    '''
def plusYears():
    '''    public LocalDate plusYears(final int n)
    '''
def plusMonths():
    '''    public LocalDate plusMonths(final int n)
    '''
def plusWeeks():
    '''    public LocalDate plusWeeks(final int n)
    '''
def plusDays():
    '''    public LocalDate plusDays(final int n)
    '''
def minus():
    '''    public LocalDate minus(final ReadablePeriod readablePeriod)
    '''
def minusYears():
    '''    public LocalDate minusYears(final int n)
    '''
def minusMonths():
    '''    public LocalDate minusMonths(final int n)
    '''
def minusWeeks():
    '''    public LocalDate minusWeeks(final int n)
    '''
def minusDays():
    '''    public LocalDate minusDays(final int n)
    '''
def property():
    '''    public Property property(final DateTimeFieldType obj)
    '''
def getEra():
    '''    public int getEra()
    '''
def getCenturyOfEra():
    '''    public int getCenturyOfEra()
    '''
def getYearOfEra():
    '''    public int getYearOfEra()
    '''
def getYearOfCentury():
    '''    public int getYearOfCentury()
    '''
def getYear():
    '''    public int getYear()
    '''
def getWeekyear():
    '''    public int getWeekyear()
    '''
def getMonthOfYear():
    '''    public int getMonthOfYear()
    '''
def getWeekOfWeekyear():
    '''    public int getWeekOfWeekyear()
    '''
def getDayOfYear():
    '''    public int getDayOfYear()
    '''
def getDayOfMonth():
    '''    public int getDayOfMonth()
    '''
def getDayOfWeek():
    '''    public int getDayOfWeek()
    '''
def withEra():
    '''    public LocalDate withEra(final int n)
    '''
def withCenturyOfEra():
    '''    public LocalDate withCenturyOfEra(final int n)
    '''
def withYearOfEra():
    '''    public LocalDate withYearOfEra(final int n)
    '''
def withYearOfCentury():
    '''    public LocalDate withYearOfCentury(final int n)
    '''
def withYear():
    '''    public LocalDate withYear(final int n)
    '''
def withWeekyear():
    '''    public LocalDate withWeekyear(final int n)
    '''
def withMonthOfYear():
    '''    public LocalDate withMonthOfYear(final int n)
    '''
def withWeekOfWeekyear():
    '''    public LocalDate withWeekOfWeekyear(final int n)
    '''
def withDayOfYear():
    '''    public LocalDate withDayOfYear(final int n)
    '''
def withDayOfMonth():
    '''    public LocalDate withDayOfMonth(final int n)
    '''
def withDayOfWeek():
    '''    public LocalDate withDayOfWeek(final int n)
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
def toString():
    '''    public String toString()
    public String toString(final String s)
    public String toString(final String s, final Locale locale)
    '''
def getField():
    '''    public DateTimeField getField()
    '''
def getLocalDate():
    '''    public LocalDate getLocalDate()
    '''
def addToCopy():
    '''    public LocalDate addToCopy(final int n)
    '''
def addWrapFieldToCopy():
    '''    public LocalDate addWrapFieldToCopy(final int n)
    '''
def setCopy():
    '''    public LocalDate setCopy(final int n)
    public LocalDate setCopy(final String s, final Locale locale)
    public LocalDate setCopy(final String s)
    '''
def withMaximumValue():
    '''    public LocalDate withMaximumValue()
    '''
def withMinimumValue():
    '''    public LocalDate withMinimumValue()
    '''
def roundFloorCopy():
    '''    public LocalDate roundFloorCopy()
    '''
def roundCeilingCopy():
    '''    public LocalDate roundCeilingCopy()
    '''
def roundHalfFloorCopy():
    '''    public LocalDate roundHalfFloorCopy()
    '''
def roundHalfCeilingCopy():
    '''    public LocalDate roundHalfCeilingCopy()
    '''
def roundHalfEvenCopy():
    '''    public LocalDate roundHalfEvenCopy()
    '''
