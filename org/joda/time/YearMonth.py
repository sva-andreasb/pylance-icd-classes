YEAR = "int  0"
MONTH_OF_YEAR = "int  1"
def now():
    '''public static YearMonth now()
    public static YearMonth now(final DateTimeZone dateTimeZone)
    public static YearMonth now(final Chronology chronology)
    '''
def parse():
    '''public static YearMonth parse(final String s)
    public static YearMonth parse(final String s, final DateTimeFormatter dateTimeFormatter)
    '''
def fromCalendarFields():
    '''public static YearMonth fromCalendarFields(final Calendar calendar)
    '''
def fromDateFields():
    '''public static YearMonth fromDateFields(final Date date)
    '''
def YearMonth():
    '''public YearMonth()
    public YearMonth(final DateTimeZone dateTimeZone)
    public YearMonth(final Chronology chronology)
    public YearMonth(final long n)
    public YearMonth(final long n, final Chronology chronology)
    public YearMonth(final Object o)
    public YearMonth(final Object o, final Chronology chronology)
    public YearMonth(final int n, final int n2)
    public YearMonth(final int n, final int n2, final Chronology chronology)
    '''
def size():
    '''public int size()
    '''
def getFieldType():
    '''public DateTimeFieldType getFieldType(final int n)
    '''
def getFieldTypes():
    '''public DateTimeFieldType[] getFieldTypes()
    '''
def withChronologyRetainFields():
    '''public YearMonth withChronologyRetainFields(Chronology chronology)
    '''
def withField():
    '''public YearMonth withField(final DateTimeFieldType dateTimeFieldType, final int n)
    '''
def withFieldAdded():
    '''public YearMonth withFieldAdded(final DurationFieldType durationFieldType, final int n)
    '''
def withPeriodAdded():
    '''public YearMonth withPeriodAdded(final ReadablePeriod readablePeriod, final int n)
    '''
def plus():
    '''public YearMonth plus(final ReadablePeriod readablePeriod)
    '''
def plusYears():
    '''public YearMonth plusYears(final int n)
    '''
def plusMonths():
    '''public YearMonth plusMonths(final int n)
    '''
def minus():
    '''public YearMonth minus(final ReadablePeriod readablePeriod)
    '''
def minusYears():
    '''public YearMonth minusYears(final int n)
    '''
def minusMonths():
    '''public YearMonth minusMonths(final int n)
    '''
def toLocalDate():
    '''public LocalDate toLocalDate(final int n)
    '''
def toInterval():
    '''public Interval toInterval()
    public Interval toInterval(DateTimeZone zone)
    '''
def getYear():
    '''public int getYear()
    '''
def getMonthOfYear():
    '''public int getMonthOfYear()
    '''
def withYear():
    '''public YearMonth withYear(final int n)
    '''
def withMonthOfYear():
    '''public YearMonth withMonthOfYear(final int n)
    '''
def property():
    '''public Property property(final DateTimeFieldType dateTimeFieldType)
    '''
def year():
    '''public Property year()
    '''
def monthOfYear():
    '''public Property monthOfYear()
    '''
def toString():
    '''public String toString()
    public String toString(final String s)
    public String toString(final String s, final Locale locale)
    '''
def getField():
    '''public DateTimeField getField()
    '''
def getYearMonth():
    '''public YearMonth getYearMonth()
    '''
def get():
    '''public int get()
    '''
def addToCopy():
    '''public YearMonth addToCopy(final int n)
    '''
def addWrapFieldToCopy():
    '''public YearMonth addWrapFieldToCopy(final int n)
    '''
def setCopy():
    '''public YearMonth setCopy(final int n)
    public YearMonth setCopy(final String s, final Locale locale)
    public YearMonth setCopy(final String s)
    '''
