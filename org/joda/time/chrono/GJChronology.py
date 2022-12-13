def getInstanceUTC():
    '''public static GJChronology getInstanceUTC()
    '''
def getInstance():
    '''public static GJChronology getInstance()
    public static GJChronology getInstance(final DateTimeZone dateTimeZone)
    public static GJChronology getInstance(final DateTimeZone dateTimeZone, final ReadableInstant readableInstant)
    public static GJChronology getInstance(DateTimeZone zone, final ReadableInstant readableInstant, final int n)
    public static GJChronology getInstance(final DateTimeZone dateTimeZone, final long n, final int n2)
    '''
def getZone():
    '''public DateTimeZone getZone()
    '''
def withUTC():
    '''public Chronology withUTC()
    '''
def withZone():
    '''public Chronology withZone(DateTimeZone default1)
    '''
def getDateTimeMillis():
    '''public long getDateTimeMillis(final int n, final int n2, final int n3, final int n4)
    public long getDateTimeMillis(final int n, final int n2, final int n3, final int n4, final int n5, final int n6, final int n7)
    '''
def getGregorianCutover():
    '''public Instant getGregorianCutover()
    '''
def getMinimumDaysInFirstWeek():
    '''public int getMinimumDaysInFirstWeek()
    '''
def equals():
    '''public boolean equals(final Object o)
    '''
def hashCode():
    '''public int hashCode()
    '''
def toString():
    '''public String toString()
    '''
def isLenient():
    '''public boolean isLenient()
    '''
def get():
    '''public int get(final long n)
    '''
def getAsText():
    '''public String getAsText(final long n, final Locale locale)
    public String getAsText(final int n, final Locale locale)
    '''
def getAsShortText():
    '''public String getAsShortText(final long n, final Locale locale)
    public String getAsShortText(final int n, final Locale locale)
    '''
def add():
    '''public long add(final long n, final int n2)
    public long add(final long n, final long n2)
    public int[] add(final ReadablePartial readablePartial, final int n, final int[] array, final int n2)
    public long add(long n, final int n2)
    public long add(long n, final long n2)
    public long add(final long n, final int n2)
    public long add(final long n, final long n2)
    '''
def getDifference():
    '''public int getDifference(final long n, final long n2)
    public int getDifference(long n, final long n2)
    public int getDifference(final long n, final long n2)
    '''
def getDifferenceAsLong():
    '''public long getDifferenceAsLong(final long n, final long n2)
    public long getDifferenceAsLong(long n, final long n2)
    public long getDifferenceAsLong(final long n, final long n2)
    '''
def set():
    '''public long set(long n, final int n2)
    public long set(long n, final String s, final Locale locale)
    '''
def getDurationField():
    '''public DurationField getDurationField()
    '''
def getRangeDurationField():
    '''public DurationField getRangeDurationField()
    '''
def isLeap():
    '''public boolean isLeap(final long n)
    '''
def getLeapAmount():
    '''public int getLeapAmount(final long n)
    '''
def getLeapDurationField():
    '''public DurationField getLeapDurationField()
    '''
def getMinimumValue():
    '''public int getMinimumValue()
    public int getMinimumValue(final ReadablePartial readablePartial)
    public int getMinimumValue(final ReadablePartial readablePartial, final int[] array)
    public int getMinimumValue(long set)
    public int getMinimumValue(final long n)
    '''
def getMaximumValue():
    '''public int getMaximumValue()
    public int getMaximumValue(long set)
    public int getMaximumValue(final ReadablePartial readablePartial)
    public int getMaximumValue(final ReadablePartial readablePartial, final int[] array)
    public int getMaximumValue(final long n)
    '''
def roundFloor():
    '''public long roundFloor(long n)
    '''
def roundCeiling():
    '''public long roundCeiling(long n)
    '''
def getMaximumTextLength():
    '''public int getMaximumTextLength(final Locale locale)
    '''
def getMaximumShortTextLength():
    '''public int getMaximumShortTextLength(final Locale locale)
    '''
