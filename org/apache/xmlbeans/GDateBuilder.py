def GDateBuilder():
'''public GDateBuilder()
public GDateBuilder(final GDateSpecification gdate)
public GDateBuilder(final CharSequence string)
public GDateBuilder(final Calendar calendar)
public GDateBuilder(final int year, final int month, final int day, final int hour, final int minute, final int second, final BigDecimal fraction)
public GDateBuilder(final int year, final int month, final int day, final int hour, final int minute, final int second, final BigDecimal fraction, final int tzSign, final int tzHour, final int tzMinute)
public GDateBuilder(final Date date)
'''
pass
def clone():
'''public Object clone()
'''
pass
def toGDate():
'''public GDate toGDate()
'''
pass
def isImmutable():
'''public boolean isImmutable()
'''
pass
def getFlags():
'''public int getFlags()
'''
pass
def hasTimeZone():
'''public final boolean hasTimeZone()
'''
pass
def hasYear():
'''public final boolean hasYear()
'''
pass
def hasMonth():
'''public final boolean hasMonth()
'''
pass
def hasDay():
'''public final boolean hasDay()
'''
pass
def hasTime():
'''public final boolean hasTime()
'''
pass
def hasDate():
'''public final boolean hasDate()
'''
pass
def getYear():
'''public final int getYear()
'''
pass
def getMonth():
'''public final int getMonth()
'''
pass
def getDay():
'''public final int getDay()
'''
pass
def getHour():
'''public final int getHour()
'''
pass
def getMinute():
'''public final int getMinute()
'''
pass
def getSecond():
'''public final int getSecond()
'''
pass
def getFraction():
'''public final BigDecimal getFraction()
'''
pass
def getMillisecond():
'''public final int getMillisecond()
'''
pass
def getTimeZoneSign():
'''public final int getTimeZoneSign()
'''
pass
def getTimeZoneHour():
'''public final int getTimeZoneHour()
'''
pass
def getTimeZoneMinute():
'''public final int getTimeZoneMinute()
'''
pass
def setYear():
'''public void setYear(final int year)
'''
pass
def setMonth():
'''public void setMonth(final int month)
'''
pass
def setDay():
'''public void setDay(final int day)
'''
pass
def setTime():
'''public void setTime(final int hour, final int minute, final int second, final BigDecimal fraction)
'''
pass
def setTimeZone():
'''public void setTimeZone(final int tzSign, final int tzHour, final int tzMinute)
public void setTimeZone(int tzTotalMinutes)
'''
pass
def clearYear():
'''public void clearYear()
'''
pass
def clearMonth():
'''public void clearMonth()
'''
pass
def clearDay():
'''public void clearDay()
'''
pass
def clearTime():
'''public void clearTime()
'''
pass
def clearTimeZone():
'''public void clearTimeZone()
'''
pass
def isValid():
'''public boolean isValid()
'''
pass
def normalize():
'''public void normalize()
'''
pass
def normalizeToTimeZone():
'''public void normalizeToTimeZone(final int tzSign, final int tzHour, final int tzMinute)
public void normalizeToTimeZone(int tzTotalMinutes)
'''
pass
def addGDuration():
'''public void addGDuration(final GDurationSpecification duration)
'''
pass
def subtractGDuration():
'''public void subtractGDuration(final GDurationSpecification duration)
'''
pass
def addDuration():
'''public void addDuration(final int sign, final int year, final int month, final int day, final int hour, final int minute, final int second, final BigDecimal fraction)
'''
pass
def getJulianDate():
'''public final int getJulianDate()
'''
pass
def setJulianDate():
'''public void setJulianDate(final int julianday)
'''
pass
def setDate():
'''public void setDate(final Date date)
'''
pass
def setGDate():
'''public void setGDate(final GDateSpecification gdate)
'''
pass
def getCalendar():
'''public XmlCalendar getCalendar()
'''
pass
def getDate():
'''public Date getDate()
'''
pass
def compareToGDate():
'''public final int compareToGDate(final GDateSpecification datespec)
'''
pass
def getBuiltinTypeCode():
'''public final int getBuiltinTypeCode()
'''
pass
def setBuiltinTypeCode():
'''public void setBuiltinTypeCode(final int typeCode)
'''
pass
def canonicalString():
'''public String canonicalString()
'''
pass
def toString():
'''public final String toString()
'''
pass
