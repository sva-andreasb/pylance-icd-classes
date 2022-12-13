def DateTimeParserBucket():
    '''public DateTimeParserBucket(final long n, final Chronology chronology, final Locale locale)
    public DateTimeParserBucket(final long n, final Chronology chronology, final Locale locale, final Integer n2)
    public DateTimeParserBucket(final long iMillis, Chronology chronology, final Locale locale, final Integer iDefaultPivotYear, final int iDefaultYear)
    '''
def reset():
    '''public void reset()
    '''
def parseMillis():
    '''public long parseMillis(final DateTimeParser dateTimeParser, final CharSequence charSequence)
    '''
def getChronology():
    '''public Chronology getChronology()
    '''
def getLocale():
    '''public Locale getLocale()
    '''
def getZone():
    '''public DateTimeZone getZone()
    '''
def setZone():
    '''public void setZone(final DateTimeZone iZone)
    '''
def getOffset():
    '''public int getOffset()
    '''
def getOffsetInteger():
    '''public Integer getOffsetInteger()
    '''
def setOffset():
    '''public void setOffset(final int i)
    public void setOffset(final Integer iOffset)
    '''
def getPivotYear():
    '''public Integer getPivotYear()
    '''
def setPivotYear():
    '''public void setPivotYear(final Integer iPivotYear)
    '''
def saveField():
    '''public void saveField(final DateTimeField dateTimeField, final int n)
    public void saveField(final DateTimeFieldType dateTimeFieldType, final int n)
    public void saveField(final DateTimeFieldType dateTimeFieldType, final String s, final Locale locale)
    '''
def saveState():
    '''public Object saveState()
    '''
def restoreState():
    '''public boolean restoreState(final Object iSavedState)
    '''
def computeMillis():
    '''public long computeMillis()
    public long computeMillis(final boolean b)
    public long computeMillis(final boolean b, final String s)
    public long computeMillis(final boolean b, final CharSequence charSequence)
    '''
def compareTo():
    '''public int compareTo(final SavedField savedField)
    '''
