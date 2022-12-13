MONTH_OF_YEAR = "int  0"
DAY_OF_MONTH = "int  1"
def now():
    '''public static MonthDay now()
    public static MonthDay now(final DateTimeZone dateTimeZone)
    public static MonthDay now(final Chronology chronology)
    '''
def parse():
    '''public static MonthDay parse(final String s)
    public static MonthDay parse(final String s, final DateTimeFormatter dateTimeFormatter)
    '''
def fromCalendarFields():
    '''public static MonthDay fromCalendarFields(final Calendar calendar)
    '''
def fromDateFields():
    '''public static MonthDay fromDateFields(final Date date)
    '''
def MonthDay():
    '''public MonthDay()
    public MonthDay(final DateTimeZone dateTimeZone)
    public MonthDay(final Chronology chronology)
    public MonthDay(final long n)
    public MonthDay(final long n, final Chronology chronology)
    public MonthDay(final Object o)
    public MonthDay(final Object o, final Chronology chronology)
    public MonthDay(final int n, final int n2)
    public MonthDay(final int n, final int n2, final Chronology chronology)
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
    '''public MonthDay withChronologyRetainFields(Chronology chronology)
    '''
def withField():
    '''public MonthDay withField(final DateTimeFieldType dateTimeFieldType, final int n)
    '''
def withFieldAdded():
    '''public MonthDay withFieldAdded(final DurationFieldType durationFieldType, final int n)
    '''
def withPeriodAdded():
    '''public MonthDay withPeriodAdded(final ReadablePeriod readablePeriod, final int n)
    '''
def plus():
    '''public MonthDay plus(final ReadablePeriod readablePeriod)
    '''
def plusMonths():
    '''public MonthDay plusMonths(final int n)
    '''
def plusDays():
    '''public MonthDay plusDays(final int n)
    '''
def minus():
    '''public MonthDay minus(final ReadablePeriod readablePeriod)
    '''
def minusMonths():
    '''public MonthDay minusMonths(final int n)
    '''
def minusDays():
    '''public MonthDay minusDays(final int n)
    '''
def toLocalDate():
    '''public LocalDate toLocalDate(final int n)
    '''
def getMonthOfYear():
    '''public int getMonthOfYear()
    '''
def getDayOfMonth():
    '''public int getDayOfMonth()
    '''
def withMonthOfYear():
    '''public MonthDay withMonthOfYear(final int n)
    '''
def withDayOfMonth():
    '''public MonthDay withDayOfMonth(final int n)
    '''
def property():
    '''public Property property(final DateTimeFieldType dateTimeFieldType)
    '''
def monthOfYear():
    '''public Property monthOfYear()
    '''
def dayOfMonth():
    '''public Property dayOfMonth()
    '''
def toString():
    '''public String toString()
    public String toString(final String s)
    public String toString(final String s, final Locale locale)
    '''
def getField():
    '''public DateTimeField getField()
    '''
def getMonthDay():
    '''public MonthDay getMonthDay()
    '''
def get():
    '''public int get()
    '''
def addToCopy():
    '''public MonthDay addToCopy(final int n)
    '''
def addWrapFieldToCopy():
    '''public MonthDay addWrapFieldToCopy(final int n)
    '''
def setCopy():
    '''public MonthDay setCopy(final int n)
    public MonthDay setCopy(final String s, final Locale locale)
    public MonthDay setCopy(final String s)
    '''
