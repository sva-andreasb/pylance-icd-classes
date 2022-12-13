def getType():
    '''    public final DateTimeFieldType getType()
    '''
def getName():
    '''    public final String getName()
    '''
def isSupported():
    '''    public final boolean isSupported()
    '''
def getAsText():
    '''    public String getAsText(final long n, final Locale locale)
    public final String getAsText(final long n)
    public String getAsText(final ReadablePartial readablePartial, final int n, final Locale locale)
    public final String getAsText(final ReadablePartial readablePartial, final Locale locale)
    public String getAsText(final int i, final Locale locale)
    '''
def getAsShortText():
    '''    public String getAsShortText(final long n, final Locale locale)
    public final String getAsShortText(final long n)
    public String getAsShortText(final ReadablePartial readablePartial, final int n, final Locale locale)
    public final String getAsShortText(final ReadablePartial readablePartial, final Locale locale)
    public String getAsShortText(final int n, final Locale locale)
    '''
def add():
    '''    public long add(final long n, final int n2)
    public long add(final long n, final long n2)
    public int[] add(final ReadablePartial readablePartial, final int n, int[] array, int i)
    '''
def addWrapPartial():
    '''    public int[] addWrapPartial(final ReadablePartial readablePartial, final int n, int[] array, int i)
    '''
def addWrapField():
    '''    public long addWrapField(final long n, final int n2)
    public int[] addWrapField(final ReadablePartial readablePartial, final int n, final int[] array, final int n2)
    '''
def getDifference():
    '''    public int getDifference(final long n, final long n2)
    '''
def getDifferenceAsLong():
    '''    public long getDifferenceAsLong(final long n, final long n2)
    '''
def set():
    '''    public int[] set(final ReadablePartial readablePartial, final int n, final int[] array, final int n2)
    public long set(final long n, final String s, final Locale locale)
    public final long set(final long n, final String s)
    public int[] set(final ReadablePartial readablePartial, final int n, final int[] array, final String s, final Locale locale)
    '''
def isLeap():
    '''    public boolean isLeap(final long n)
    '''
def getLeapAmount():
    '''    public int getLeapAmount(final long n)
    '''
def getLeapDurationField():
    '''    public DurationField getLeapDurationField()
    '''
def getMinimumValue():
    '''    public int getMinimumValue(final long n)
    public int getMinimumValue(final ReadablePartial readablePartial)
    public int getMinimumValue(final ReadablePartial readablePartial, final int[] array)
    '''
def getMaximumValue():
    '''    public int getMaximumValue(final long n)
    public int getMaximumValue(final ReadablePartial readablePartial)
    public int getMaximumValue(final ReadablePartial readablePartial, final int[] array)
    '''
def getMaximumTextLength():
    '''    public int getMaximumTextLength(final Locale locale)
    '''
def getMaximumShortTextLength():
    '''    public int getMaximumShortTextLength(final Locale locale)
    '''
def roundCeiling():
    '''    public long roundCeiling(long add)
    '''
def roundHalfFloor():
    '''    public long roundHalfFloor(final long n)
    '''
def roundHalfCeiling():
    '''    public long roundHalfCeiling(final long n)
    '''
def roundHalfEven():
    '''    public long roundHalfEven(final long n)
    '''
def remainder():
    '''    public long remainder(final long n)
    '''
def toString():
    '''    public String toString()
    '''
