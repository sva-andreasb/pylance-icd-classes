YEAR = "int  0"
MONTH_OF_YEAR = "int  1"
DAY_OF_MONTH = "int  2"
def fromCalendarFields():
    '''    public static YearMonthDay fromCalendarFields(final Calendar calendar)
    '''
def fromDateFields():
    '''    public static YearMonthDay fromDateFields(final Date date)
    '''
def YearMonthDay():
    '''    public YearMonthDay()
    public YearMonthDay(final DateTimeZone dateTimeZone)
    public YearMonthDay(final Chronology chronology)
    public YearMonthDay(final long n)
    public YearMonthDay(final long n, final Chronology chronology)
    public YearMonthDay(final Object o)
    public YearMonthDay(final Object o, final Chronology chronology)
    public YearMonthDay(final int n, final int n2, final int n3)
    public YearMonthDay(final int n, final int n2, final int n3, final Chronology chronology)
    '''
def size():
    '''    public int size()
    '''
def getFieldType():
    '''    public DateTimeFieldType getFieldType(final int n)
    '''
def getFieldTypes():
    '''    public DateTimeFieldType[] getFieldTypes()
    '''
def withChronologyRetainFields():
    '''    public YearMonthDay withChronologyRetainFields(Chronology chronology)
    '''
def withField():
    '''    public YearMonthDay withField(final DateTimeFieldType dateTimeFieldType, final int n)
    '''
def withFieldAdded():
    '''    public YearMonthDay withFieldAdded(final DurationFieldType durationFieldType, final int n)
    '''
def withPeriodAdded():
    '''    public YearMonthDay withPeriodAdded(final ReadablePeriod readablePeriod, final int n)
    '''
def plus():
    '''    public YearMonthDay plus(final ReadablePeriod readablePeriod)
    '''
def plusYears():
    '''    public YearMonthDay plusYears(final int n)
    '''
def plusMonths():
    '''    public YearMonthDay plusMonths(final int n)
    '''
def plusDays():
    '''    public YearMonthDay plusDays(final int n)
    '''
def minus():
    '''    public YearMonthDay minus(final ReadablePeriod readablePeriod)
    '''
def minusYears():
    '''    public YearMonthDay minusYears(final int n)
    '''
def minusMonths():
    '''    public YearMonthDay minusMonths(final int n)
    '''
def minusDays():
    '''    public YearMonthDay minusDays(final int n)
    '''
def property():
    '''    public Property property(final DateTimeFieldType dateTimeFieldType)
    '''
def toLocalDate():
    '''    public LocalDate toLocalDate()
    '''
def toDateTimeAtMidnight():
    '''    public DateTime toDateTimeAtMidnight()
    public DateTime toDateTimeAtMidnight(final DateTimeZone dateTimeZone)
    '''
def toDateTimeAtCurrentTime():
    '''    public DateTime toDateTimeAtCurrentTime()
    public DateTime toDateTimeAtCurrentTime(final DateTimeZone dateTimeZone)
    '''
def toDateMidnight():
    '''    public DateMidnight toDateMidnight()
    public DateMidnight toDateMidnight(final DateTimeZone dateTimeZone)
    '''
def toDateTime():
    '''    public DateTime toDateTime(final TimeOfDay timeOfDay)
    public DateTime toDateTime(final TimeOfDay timeOfDay, final DateTimeZone dateTimeZone)
    '''
def toInterval():
    '''    public Interval toInterval()
    public Interval toInterval(DateTimeZone zone)
    '''
def getYear():
    '''    public int getYear()
    '''
def getMonthOfYear():
    '''    public int getMonthOfYear()
    '''
def getDayOfMonth():
    '''    public int getDayOfMonth()
    '''
def withYear():
    '''    public YearMonthDay withYear(final int n)
    '''
def withMonthOfYear():
    '''    public YearMonthDay withMonthOfYear(final int n)
    '''
def withDayOfMonth():
    '''    public YearMonthDay withDayOfMonth(final int n)
    '''
def year():
    '''    public Property year()
    '''
def monthOfYear():
    '''    public Property monthOfYear()
    '''
def dayOfMonth():
    '''    public Property dayOfMonth()
    '''
def toString():
    '''    public String toString()
    '''
def getField():
    '''    public DateTimeField getField()
    '''
def getYearMonthDay():
    '''    public YearMonthDay getYearMonthDay()
    '''
def get():
    '''    public int get()
    '''
def addToCopy():
    '''    public YearMonthDay addToCopy(final int n)
    '''
def addWrapFieldToCopy():
    '''    public YearMonthDay addWrapFieldToCopy(final int n)
    '''
def setCopy():
    '''    public YearMonthDay setCopy(final int n)
    public YearMonthDay setCopy(final String s, final Locale locale)
    public YearMonthDay setCopy(final String s)
    '''
def withMaximumValue():
    '''    public YearMonthDay withMaximumValue()
    '''
def withMinimumValue():
    '''    public YearMonthDay withMinimumValue()
    '''
