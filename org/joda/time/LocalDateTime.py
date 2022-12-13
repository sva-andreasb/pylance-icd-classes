def now():
    '''public static LocalDateTime now()
    public static LocalDateTime now(final DateTimeZone dateTimeZone)
    public static LocalDateTime now(final Chronology chronology)
    '''
def parse():
    '''public static LocalDateTime parse(final String s)
    public static LocalDateTime parse(final String s, final DateTimeFormatter dateTimeFormatter)
    '''
def fromCalendarFields():
    '''public static LocalDateTime fromCalendarFields(final Calendar calendar)
    '''
def fromDateFields():
    '''public static LocalDateTime fromDateFields(final Date time)
    '''
def LocalDateTime():
    '''public LocalDateTime()
    public LocalDateTime(final DateTimeZone dateTimeZone)
    public LocalDateTime(final Chronology chronology)
    public LocalDateTime(final long n)
    public LocalDateTime(final long n, final DateTimeZone dateTimeZone)
    public LocalDateTime(final long n, Chronology chronology)
    public LocalDateTime(final Object o)
    public LocalDateTime(final Object o, final DateTimeZone dateTimeZone)
    public LocalDateTime(final Object o, Chronology chronology)
    public LocalDateTime(final int n, final int n2, final int n3, final int n4, final int n5)
    public LocalDateTime(final int n, final int n2, final int n3, final int n4, final int n5, final int n6)
    public LocalDateTime(final int n, final int n2, final int n3, final int n4, final int n5, final int n6, final int n7)
    public LocalDateTime(final int n, final int n2, final int n3, final int n4, final int n5, final int n6, final int n7, Chronology withUTC)
    '''
def size():
    '''public int size()
    '''
def getValue():
    '''public int getValue(final int i)
    '''
def get():
    '''public int get(final DateTimeFieldType dateTimeFieldType)
    '''
def isSupported():
    '''public boolean isSupported(final DateTimeFieldType dateTimeFieldType)
    public boolean isSupported(final DurationFieldType durationFieldType)
    '''
def getChronology():
    '''public Chronology getChronology()
    '''
def equals():
    '''public boolean equals(final Object o)
    '''
def compareTo():
    '''public int compareTo(final ReadablePartial readablePartial)
    '''
def toDateTime():
    '''public DateTime toDateTime()
    public DateTime toDateTime(DateTimeZone zone)
    '''
def toLocalDate():
    '''public LocalDate toLocalDate()
    '''
def toLocalTime():
    '''public LocalTime toLocalTime()
    '''
def toDate():
    '''public Date toDate()
    public Date toDate(final TimeZone zone)
    '''
def withDate():
    '''public LocalDateTime withDate(final int n, final int n2, final int n3)
    '''
def withTime():
    '''public LocalDateTime withTime(final int n, final int n2, final int n3, final int n4)
    '''
def withFields():
    '''public LocalDateTime withFields(final ReadablePartial readablePartial)
    '''
def withField():
    '''public LocalDateTime withField(final DateTimeFieldType dateTimeFieldType, final int n)
    '''
def withFieldAdded():
    '''public LocalDateTime withFieldAdded(final DurationFieldType durationFieldType, final int n)
    '''
def withDurationAdded():
    '''public LocalDateTime withDurationAdded(final ReadableDuration readableDuration, final int n)
    '''
def withPeriodAdded():
    '''public LocalDateTime withPeriodAdded(final ReadablePeriod readablePeriod, final int n)
    '''
def plus():
    '''public LocalDateTime plus(final ReadableDuration readableDuration)
    public LocalDateTime plus(final ReadablePeriod readablePeriod)
    '''
def plusYears():
    '''public LocalDateTime plusYears(final int n)
    '''
def plusMonths():
    '''public LocalDateTime plusMonths(final int n)
    '''
def plusWeeks():
    '''public LocalDateTime plusWeeks(final int n)
    '''
def plusDays():
    '''public LocalDateTime plusDays(final int n)
    '''
def plusHours():
    '''public LocalDateTime plusHours(final int n)
    '''
def plusMinutes():
    '''public LocalDateTime plusMinutes(final int n)
    '''
def plusSeconds():
    '''public LocalDateTime plusSeconds(final int n)
    '''
def plusMillis():
    '''public LocalDateTime plusMillis(final int n)
    '''
def minus():
    '''public LocalDateTime minus(final ReadableDuration readableDuration)
    public LocalDateTime minus(final ReadablePeriod readablePeriod)
    '''
def minusYears():
    '''public LocalDateTime minusYears(final int n)
    '''
def minusMonths():
    '''public LocalDateTime minusMonths(final int n)
    '''
def minusWeeks():
    '''public LocalDateTime minusWeeks(final int n)
    '''
def minusDays():
    '''public LocalDateTime minusDays(final int n)
    '''
def minusHours():
    '''public LocalDateTime minusHours(final int n)
    '''
def minusMinutes():
    '''public LocalDateTime minusMinutes(final int n)
    '''
def minusSeconds():
    '''public LocalDateTime minusSeconds(final int n)
    '''
def minusMillis():
    '''public LocalDateTime minusMillis(final int n)
    '''
def property():
    '''public Property property(final DateTimeFieldType obj)
    '''
def getEra():
    '''public int getEra()
    '''
def getCenturyOfEra():
    '''public int getCenturyOfEra()
    '''
def getYearOfEra():
    '''public int getYearOfEra()
    '''
def getYearOfCentury():
    '''public int getYearOfCentury()
    '''
def getYear():
    '''public int getYear()
    '''
def getWeekyear():
    '''public int getWeekyear()
    '''
def getMonthOfYear():
    '''public int getMonthOfYear()
    '''
def getWeekOfWeekyear():
    '''public int getWeekOfWeekyear()
    '''
def getDayOfYear():
    '''public int getDayOfYear()
    '''
def getDayOfMonth():
    '''public int getDayOfMonth()
    '''
def getDayOfWeek():
    '''public int getDayOfWeek()
    '''
def getHourOfDay():
    '''public int getHourOfDay()
    '''
def getMinuteOfHour():
    '''public int getMinuteOfHour()
    '''
def getSecondOfMinute():
    '''public int getSecondOfMinute()
    '''
def getMillisOfSecond():
    '''public int getMillisOfSecond()
    '''
def getMillisOfDay():
    '''public int getMillisOfDay()
    '''
def withEra():
    '''public LocalDateTime withEra(final int n)
    '''
def withCenturyOfEra():
    '''public LocalDateTime withCenturyOfEra(final int n)
    '''
def withYearOfEra():
    '''public LocalDateTime withYearOfEra(final int n)
    '''
def withYearOfCentury():
    '''public LocalDateTime withYearOfCentury(final int n)
    '''
def withYear():
    '''public LocalDateTime withYear(final int n)
    '''
def withWeekyear():
    '''public LocalDateTime withWeekyear(final int n)
    '''
def withMonthOfYear():
    '''public LocalDateTime withMonthOfYear(final int n)
    '''
def withWeekOfWeekyear():
    '''public LocalDateTime withWeekOfWeekyear(final int n)
    '''
def withDayOfYear():
    '''public LocalDateTime withDayOfYear(final int n)
    '''
def withDayOfMonth():
    '''public LocalDateTime withDayOfMonth(final int n)
    '''
def withDayOfWeek():
    '''public LocalDateTime withDayOfWeek(final int n)
    '''
def withHourOfDay():
    '''public LocalDateTime withHourOfDay(final int n)
    '''
def withMinuteOfHour():
    '''public LocalDateTime withMinuteOfHour(final int n)
    '''
def withSecondOfMinute():
    '''public LocalDateTime withSecondOfMinute(final int n)
    '''
def withMillisOfSecond():
    '''public LocalDateTime withMillisOfSecond(final int n)
    '''
def withMillisOfDay():
    '''public LocalDateTime withMillisOfDay(final int n)
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
def minuteOfHour():
    '''public Property minuteOfHour()
    '''
def secondOfMinute():
    '''public Property secondOfMinute()
    '''
def millisOfSecond():
    '''public Property millisOfSecond()
    '''
def millisOfDay():
    '''public Property millisOfDay()
    '''
def toString():
    '''public String toString()
    public String toString(final String s)
    public String toString(final String s, final Locale locale)
    '''
def getField():
    '''public DateTimeField getField()
    '''
def getLocalDateTime():
    '''public LocalDateTime getLocalDateTime()
    '''
def addToCopy():
    '''public LocalDateTime addToCopy(final int n)
    public LocalDateTime addToCopy(final long n)
    '''
def addWrapFieldToCopy():
    '''public LocalDateTime addWrapFieldToCopy(final int n)
    '''
def setCopy():
    '''public LocalDateTime setCopy(final int n)
    public LocalDateTime setCopy(final String s, final Locale locale)
    public LocalDateTime setCopy(final String s)
    '''
def withMaximumValue():
    '''public LocalDateTime withMaximumValue()
    '''
def withMinimumValue():
    '''public LocalDateTime withMinimumValue()
    '''
def roundFloorCopy():
    '''public LocalDateTime roundFloorCopy()
    '''
def roundCeilingCopy():
    '''public LocalDateTime roundCeilingCopy()
    '''
def roundHalfFloorCopy():
    '''public LocalDateTime roundHalfFloorCopy()
    '''
def roundHalfCeilingCopy():
    '''public LocalDateTime roundHalfCeilingCopy()
    '''
def roundHalfEvenCopy():
    '''public LocalDateTime roundHalfEvenCopy()
    '''
