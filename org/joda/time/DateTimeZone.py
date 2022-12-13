def getDefault():
    '''    public static DateTimeZone getDefault()
    '''
def setDefault():
    '''    public static void setDefault(final DateTimeZone newValue)
    '''
def forID():
    '''    public static DateTimeZone forID(String printOffset)
    '''
def forOffsetHours():
    '''    public static DateTimeZone forOffsetHours(final int n)
    '''
def forOffsetHoursMinutes():
    '''    public static DateTimeZone forOffsetHoursMinutes(final int i, int a)
    '''
def forOffsetMillis():
    '''    public static DateTimeZone forOffsetMillis(final int i)
    '''
def forTimeZone():
    '''    public static DateTimeZone forTimeZone(final TimeZone timeZone)
    '''
def getAvailableIDs():
    '''    public static Set<String> getAvailableIDs()
    '''
def getProvider():
    '''    public static Provider getProvider()
    '''
def setProvider():
    '''    public static void setProvider(Provider defaultProvider)
    '''
def getNameProvider():
    '''    public static NameProvider getNameProvider()
    '''
def setNameProvider():
    '''    public static void setNameProvider(NameProvider defaultNameProvider)
    '''
def getID():
    '''    public final String getID()
    '''
def getShortName():
    '''    public final String getShortName(final long n)
    public String getShortName(final long n, Locale default1)
    '''
def getName():
    '''    public final String getName(final long n)
    public String getName(final long n, Locale default1)
    '''
def getOffset():
    '''    public final int getOffset(final ReadableInstant readableInstant)
    '''
def isStandardOffset():
    '''    public boolean isStandardOffset(final long n)
    '''
def getOffsetFromLocal():
    '''    public int getOffsetFromLocal(final long n)
    '''
def convertUTCToLocal():
    '''    public long convertUTCToLocal(final long n)
    '''
def convertLocalToUTC():
    '''    public long convertLocalToUTC(final long n, final boolean b, final long n2)
    public long convertLocalToUTC(final long n, final boolean b)
    '''
def getMillisKeepLocal():
    '''    public long getMillisKeepLocal(DateTimeZone default1, final long n)
    '''
def isLocalDateTimeGap():
    '''    public boolean isLocalDateTimeGap(final LocalDateTime localDateTime)
    '''
def adjustOffset():
    '''    public long adjustOffset(final long n, final boolean b)
    '''
def toTimeZone():
    '''    public TimeZone toTimeZone()
    '''
def hashCode():
    '''    public int hashCode()
    '''
def toString():
    '''    public String toString()
    public String toString()
    '''
def getZone():
    '''    public DateTimeZone getZone()
    '''
def withUTC():
    '''    public Chronology withUTC()
    '''
def withZone():
    '''    public Chronology withZone(final DateTimeZone dateTimeZone)
    '''
