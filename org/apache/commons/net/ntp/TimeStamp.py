NTP_DATE_FORMAT = "String  \"EEE, MMM dd yyyy HH:mm:ss.SSS\""
def TimeStamp():
    '''public TimeStamp(final long ntpTime)
    public TimeStamp(final String s)
    public TimeStamp(final Date d)
    '''
def ntpValue():
    '''public long ntpValue()
    '''
def getSeconds():
    '''public long getSeconds()
    '''
def getFraction():
    '''public long getFraction()
    '''
def getTime():
    '''public long getTime()
    public static long getTime(final long ntpTimeValue)
    '''
def getDate():
    '''public Date getDate()
    '''
def getNtpTime():
    '''public static TimeStamp getNtpTime(final long date)
    '''
def getCurrentTime():
    '''public static TimeStamp getCurrentTime()
    '''
def parseNtpString():
    '''public static TimeStamp parseNtpString(final String s)
    '''
def hashCode():
    '''public int hashCode()
    '''
def equals():
    '''public boolean equals(final Object obj)
    '''
def toString():
    '''public String toString()
    public static String toString(final long ntpTime)
    '''
def toDateString():
    '''public String toDateString()
    '''
def toUTCString():
    '''public String toUTCString()
    '''
def compareTo():
    '''public int compareTo(final TimeStamp anotherTimeStamp)
    public int compareTo(final Object o)
    '''
