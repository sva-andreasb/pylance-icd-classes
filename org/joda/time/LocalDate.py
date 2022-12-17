def ():
    '''returns LocalDate\n\n
    ()\n
    (final DateTimeZone dateTimeZone)\n
    (final Chronology chronology)\n
    (final long n)\n
    (final long n, final DateTimeZone dateTimeZone)\n
    (final long n, Chronology iChronology)\n
    (final Object o)\n
    (final Object o, final DateTimeZone dateTimeZone)\n
    (final Object o, Chronology chronology)\n
    (final int n, final int n2, final int n3)\n
    (final int n, final int n2, final int n3, Chronology withUTC)\n
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
    get(final DateTimeFieldType obj)\n
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
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def compareTo():
    '''returns int\n\n
    compareTo(final ReadablePartial readablePartial)\n
    '''
def toDateTimeAtStartOfDay():
    '''returns DateTime\n\n
    toDateTimeAtStartOfDay()\n
    toDateTimeAtStartOfDay(DateTimeZone zone)\n
    '''
def toDateTimeAtMidnight():
    '''returns DateTime\n\n
    toDateTimeAtMidnight()\n
    toDateTimeAtMidnight(DateTimeZone zone)\n
    '''
def toDateTimeAtCurrentTime():
    '''returns DateTime\n\n
    toDateTimeAtCurrentTime()\n
    toDateTimeAtCurrentTime(DateTimeZone zone)\n
    '''
def toDateMidnight():
    '''returns DateMidnight\n\n
    toDateMidnight()\n
    toDateMidnight(DateTimeZone zone)\n
    '''
def toLocalDateTime():
    '''returns LocalDateTime\n\n
    toLocalDateTime(final LocalTime localTime)\n
    '''
def toDateTime():
    '''returns DateTime\n\n
    toDateTime(final LocalTime localTime)\n
    toDateTime(final LocalTime localTime, final DateTimeZone dateTimeZone)\n
    '''
def toInterval():
    '''returns Interval\n\n
    toInterval()\n
    toInterval(DateTimeZone zone)\n
    '''
def toDate():
    '''returns Date\n\n
    toDate()\n
    '''
def withFields():
    '''returns LocalDate\n\n
    withFields(final ReadablePartial readablePartial)\n
    '''
def withField():
    '''returns LocalDate\n\n
    withField(final DateTimeFieldType obj, final int n)\n
    '''
def withFieldAdded():
    '''returns LocalDate\n\n
    withFieldAdded(final DurationFieldType obj, final int n)\n
    '''
def withPeriodAdded():
    '''returns LocalDate\n\n
    withPeriodAdded(final ReadablePeriod readablePeriod, final int n)\n
    '''
def plus():
    '''returns LocalDate\n\n
    plus(final ReadablePeriod readablePeriod)\n
    '''
def plusYears():
    '''returns LocalDate\n\n
    plusYears(final int n)\n
    '''
def plusMonths():
    '''returns LocalDate\n\n
    plusMonths(final int n)\n
    '''
def plusWeeks():
    '''returns LocalDate\n\n
    plusWeeks(final int n)\n
    '''
def plusDays():
    '''returns LocalDate\n\n
    plusDays(final int n)\n
    '''
def minus():
    '''returns LocalDate\n\n
    minus(final ReadablePeriod readablePeriod)\n
    '''
def minusYears():
    '''returns LocalDate\n\n
    minusYears(final int n)\n
    '''
def minusMonths():
    '''returns LocalDate\n\n
    minusMonths(final int n)\n
    '''
def minusWeeks():
    '''returns LocalDate\n\n
    minusWeeks(final int n)\n
    '''
def minusDays():
    '''returns LocalDate\n\n
    minusDays(final int n)\n
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
def withEra():
    '''returns LocalDate\n\n
    withEra(final int n)\n
    '''
def withCenturyOfEra():
    '''returns LocalDate\n\n
    withCenturyOfEra(final int n)\n
    '''
def withYearOfEra():
    '''returns LocalDate\n\n
    withYearOfEra(final int n)\n
    '''
def withYearOfCentury():
    '''returns LocalDate\n\n
    withYearOfCentury(final int n)\n
    '''
def withYear():
    '''returns LocalDate\n\n
    withYear(final int n)\n
    '''
def withWeekyear():
    '''returns LocalDate\n\n
    withWeekyear(final int n)\n
    '''
def withMonthOfYear():
    '''returns LocalDate\n\n
    withMonthOfYear(final int n)\n
    '''
def withWeekOfWeekyear():
    '''returns LocalDate\n\n
    withWeekOfWeekyear(final int n)\n
    '''
def withDayOfYear():
    '''returns LocalDate\n\n
    withDayOfYear(final int n)\n
    '''
def withDayOfMonth():
    '''returns LocalDate\n\n
    withDayOfMonth(final int n)\n
    '''
def withDayOfWeek():
    '''returns LocalDate\n\n
    withDayOfWeek(final int n)\n
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
def getLocalDate():
    '''returns LocalDate\n\n
    getLocalDate()\n
    '''
def addToCopy():
    '''returns LocalDate\n\n
    addToCopy(final int n)\n
    '''
def addWrapFieldToCopy():
    '''returns LocalDate\n\n
    addWrapFieldToCopy(final int n)\n
    '''
def setCopy():
    '''returns LocalDate\n\n
    setCopy(final int n)\n
    setCopy(final String s, final Locale locale)\n
    setCopy(final String s)\n
    '''
def withMaximumValue():
    '''returns LocalDate\n\n
    withMaximumValue()\n
    '''
def withMinimumValue():
    '''returns LocalDate\n\n
    withMinimumValue()\n
    '''
def roundFloorCopy():
    '''returns LocalDate\n\n
    roundFloorCopy()\n
    '''
def roundCeilingCopy():
    '''returns LocalDate\n\n
    roundCeilingCopy()\n
    '''
def roundHalfFloorCopy():
    '''returns LocalDate\n\n
    roundHalfFloorCopy()\n
    '''
def roundHalfCeilingCopy():
    '''returns LocalDate\n\n
    roundHalfCeilingCopy()\n
    '''
def roundHalfEvenCopy():
    '''returns LocalDate\n\n
    roundHalfEvenCopy()\n
    '''
