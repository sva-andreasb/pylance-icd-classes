def GDateBuilder():
    '''    public GDateBuilder()
    public GDateBuilder(final GDateSpecification gdate)
    public GDateBuilder(final CharSequence string)
    public GDateBuilder(final Calendar calendar)
    public GDateBuilder(final int year, final int month, final int day, final int hour, final int minute, final int second, final BigDecimal fraction)
    public GDateBuilder(final int year, final int month, final int day, final int hour, final int minute, final int second, final BigDecimal fraction, final int tzSign, final int tzHour, final int tzMinute)
    public GDateBuilder(final Date date)
    '''
def clone():
    '''    public Object clone()
    '''
def toGDate():
    '''    public GDate toGDate()
    '''
def isImmutable():
    '''    public boolean isImmutable()
    '''
def getFlags():
    '''    public int getFlags()
    '''
def hasTimeZone():
    '''    public final boolean hasTimeZone()
    '''
def hasYear():
    '''    public final boolean hasYear()
    '''
def hasMonth():
    '''    public final boolean hasMonth()
    '''
def hasDay():
    '''    public final boolean hasDay()
    '''
def hasTime():
    '''    public final boolean hasTime()
    '''
def hasDate():
    '''    public final boolean hasDate()
    '''
def getYear():
    '''    public final int getYear()
    '''
def getMonth():
    '''    public final int getMonth()
    '''
def getDay():
    '''    public final int getDay()
    '''
def getHour():
    '''    public final int getHour()
    '''
def getMinute():
    '''    public final int getMinute()
    '''
def getSecond():
    '''    public final int getSecond()
    '''
def getFraction():
    '''    public final BigDecimal getFraction()
    '''
def getMillisecond():
    '''    public final int getMillisecond()
    '''
def getTimeZoneSign():
    '''    public final int getTimeZoneSign()
    '''
def getTimeZoneHour():
    '''    public final int getTimeZoneHour()
    '''
def getTimeZoneMinute():
    '''    public final int getTimeZoneMinute()
    '''
def setYear():
    '''    public void setYear(final int year)
    '''
def setMonth():
    '''    public void setMonth(final int month)
    '''
def setDay():
    '''    public void setDay(final int day)
    '''
def setTime():
    '''    public void setTime(final int hour, final int minute, final int second, final BigDecimal fraction)
    '''
def setTimeZone():
    '''    public void setTimeZone(final int tzSign, final int tzHour, final int tzMinute)
    public void setTimeZone(int tzTotalMinutes)
    '''
def clearYear():
    '''    public void clearYear()
    '''
def clearMonth():
    '''    public void clearMonth()
    '''
def clearDay():
    '''    public void clearDay()
    '''
def clearTime():
    '''    public void clearTime()
    '''
def clearTimeZone():
    '''    public void clearTimeZone()
    '''
def isValid():
    '''    public boolean isValid()
    '''
def normalize():
    '''    public void normalize()
    '''
def normalizeToTimeZone():
    '''    public void normalizeToTimeZone(final int tzSign, final int tzHour, final int tzMinute)
    public void normalizeToTimeZone(int tzTotalMinutes)
    '''
def addGDuration():
    '''    public void addGDuration(final GDurationSpecification duration)
    '''
def subtractGDuration():
    '''    public void subtractGDuration(final GDurationSpecification duration)
    '''
def addDuration():
    '''    public void addDuration(final int sign, final int year, final int month, final int day, final int hour, final int minute, final int second, final BigDecimal fraction)
    '''
def getJulianDate():
    '''    public final int getJulianDate()
    '''
def setJulianDate():
    '''    public void setJulianDate(final int julianday)
    '''
def setDate():
    '''    public void setDate(final Date date)
    '''
def setGDate():
    '''    public void setGDate(final GDateSpecification gdate)
    '''
def getCalendar():
    '''    public XmlCalendar getCalendar()
    '''
def getDate():
    '''    public Date getDate()
    '''
def compareToGDate():
    '''    public final int compareToGDate(final GDateSpecification datespec)
    '''
def getBuiltinTypeCode():
    '''    public final int getBuiltinTypeCode()
    '''
def setBuiltinTypeCode():
    '''    public void setBuiltinTypeCode(final int typeCode)
    '''
def canonicalString():
    '''    public String canonicalString()
    '''
def toString():
    '''    public final String toString()
    '''
