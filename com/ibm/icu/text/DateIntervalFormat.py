def DateIntervalFormat():
'''public DateIntervalFormat(final String skeleton, final DateIntervalInfo dtItvInfo, final SimpleDateFormat simpleDateFormat)
'''
pass
def getInstance():
'''public static final DateIntervalFormat getInstance(final String skeleton)
public static final DateIntervalFormat getInstance(final String skeleton, final Locale locale)
public static final DateIntervalFormat getInstance(final String skeleton, final ULocale locale)
public static final DateIntervalFormat getInstance(final String skeleton, final DateIntervalInfo dtitvinf)
public static final DateIntervalFormat getInstance(final String skeleton, final Locale locale, final DateIntervalInfo dtitvinf)
public static final DateIntervalFormat getInstance(final String skeleton, final ULocale locale, DateIntervalInfo dtitvinf)
'''
pass
def clone():
'''public synchronized Object clone()
'''
pass
def format():
'''public final StringBuffer format(final Object obj, final StringBuffer appendTo, final FieldPosition fieldPosition)
public final StringBuffer format(final DateInterval dtInterval, final StringBuffer appendTo, final FieldPosition fieldPosition)
public final StringBuffer format(final Calendar fromCalendar, final Calendar toCalendar, final StringBuffer appendTo, final FieldPosition pos)
'''
pass
def formatToValue():
'''public FormattedDateInterval formatToValue(final DateInterval dtInterval)
public FormattedDateInterval formatToValue(final Calendar fromCalendar, final Calendar toCalendar)
'''
pass
def getPatterns():
'''public String getPatterns(final Calendar fromCalendar, final Calendar toCalendar, final Output<String> part2)
'''
pass
def parseObject():
'''public Object parseObject(final String source, final ParsePosition parse_pos)
'''
pass
def getDateIntervalInfo():
'''public DateIntervalInfo getDateIntervalInfo()
'''
pass
def setDateIntervalInfo():
'''public void setDateIntervalInfo(final DateIntervalInfo newItvPattern)
'''
pass
def getTimeZone():
'''public TimeZone getTimeZone()
'''
pass
def setTimeZone():
'''public void setTimeZone(final TimeZone zone)
'''
pass
def getDateFormat():
'''public synchronized DateFormat getDateFormat()
'''
pass
def toString():
'''public String toString()
'''
pass
def length():
'''public int length()
'''
pass
def charAt():
'''public char charAt(final int index)
'''
pass
def subSequence():
'''public CharSequence subSequence(final int start, final int end)
'''
pass
def appendTo():
'''public <A extends Appendable> A appendTo(final A appendable)
'''
pass
def nextPosition():
'''public boolean nextPosition(final ConstrainedFieldPosition cfpos)
'''
pass
def toCharacterIterator():
'''public AttributedCharacterIterator toCharacterIterator()
'''
pass
def register():
'''public void register(final int i)
'''
pass
