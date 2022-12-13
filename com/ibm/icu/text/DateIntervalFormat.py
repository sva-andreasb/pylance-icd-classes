def DateIntervalFormat():
    '''    public DateIntervalFormat(final String skeleton, final DateIntervalInfo dtItvInfo, final SimpleDateFormat simpleDateFormat)
    '''
def getInstance():
    '''    public static final DateIntervalFormat getInstance(final String skeleton)
    public static final DateIntervalFormat getInstance(final String skeleton, final Locale locale)
    public static final DateIntervalFormat getInstance(final String skeleton, final ULocale locale)
    public static final DateIntervalFormat getInstance(final String skeleton, final DateIntervalInfo dtitvinf)
    public static final DateIntervalFormat getInstance(final String skeleton, final Locale locale, final DateIntervalInfo dtitvinf)
    public static final DateIntervalFormat getInstance(final String skeleton, final ULocale locale, DateIntervalInfo dtitvinf)
    '''
def clone():
    '''    public synchronized Object clone()
    '''
def format():
    '''    public final StringBuffer format(final Object obj, final StringBuffer appendTo, final FieldPosition fieldPosition)
    public final StringBuffer format(final DateInterval dtInterval, final StringBuffer appendTo, final FieldPosition fieldPosition)
    public final StringBuffer format(final Calendar fromCalendar, final Calendar toCalendar, final StringBuffer appendTo, final FieldPosition pos)
    '''
def formatToValue():
    '''    public FormattedDateInterval formatToValue(final DateInterval dtInterval)
    public FormattedDateInterval formatToValue(final Calendar fromCalendar, final Calendar toCalendar)
    '''
def getPatterns():
    '''    public String getPatterns(final Calendar fromCalendar, final Calendar toCalendar, final Output<String> part2)
    '''
def parseObject():
    '''    public Object parseObject(final String source, final ParsePosition parse_pos)
    '''
def getDateIntervalInfo():
    '''    public DateIntervalInfo getDateIntervalInfo()
    '''
def setDateIntervalInfo():
    '''    public void setDateIntervalInfo(final DateIntervalInfo newItvPattern)
    '''
def getTimeZone():
    '''    public TimeZone getTimeZone()
    '''
def setTimeZone():
    '''    public void setTimeZone(final TimeZone zone)
    '''
def getDateFormat():
    '''    public synchronized DateFormat getDateFormat()
    '''
def toString():
    '''    public String toString()
    '''
def length():
    '''    public int length()
    '''
def charAt():
    '''    public char charAt(final int index)
    '''
def subSequence():
    '''    public CharSequence subSequence(final int start, final int end)
    '''
def appendTo():
    '''    public <A extends Appendable> A appendTo(final A appendable)
    '''
def nextPosition():
    '''    public boolean nextPosition(final ConstrainedFieldPosition cfpos)
    '''
def toCharacterIterator():
    '''    public AttributedCharacterIterator toCharacterIterator()
    '''
def register():
    '''    public void register(final int i)
    '''
