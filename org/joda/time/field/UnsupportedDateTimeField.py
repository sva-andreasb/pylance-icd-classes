def getInstance():
'''public static synchronized UnsupportedDateTimeField getInstance(final DateTimeFieldType dateTimeFieldType, final DurationField durationField)
'''
pass
def getType():
'''public DateTimeFieldType getType()
'''
pass
def getName():
'''public String getName()
'''
pass
def isSupported():
'''public boolean isSupported()
'''
pass
def isLenient():
'''public boolean isLenient()
'''
pass
def get():
'''public int get(final long n)
'''
pass
def getAsText():
'''public String getAsText(final long n, final Locale locale)
public String getAsText(final long n)
public String getAsText(final ReadablePartial readablePartial, final int n, final Locale locale)
public String getAsText(final ReadablePartial readablePartial, final Locale locale)
public String getAsText(final int n, final Locale locale)
'''
pass
def getAsShortText():
'''public String getAsShortText(final long n, final Locale locale)
public String getAsShortText(final long n)
public String getAsShortText(final ReadablePartial readablePartial, final int n, final Locale locale)
public String getAsShortText(final ReadablePartial readablePartial, final Locale locale)
public String getAsShortText(final int n, final Locale locale)
'''
pass
def add():
'''public long add(final long n, final int n2)
public long add(final long n, final long n2)
public int[] add(final ReadablePartial readablePartial, final int n, final int[] array, final int n2)
'''
pass
def addWrapPartial():
'''public int[] addWrapPartial(final ReadablePartial readablePartial, final int n, final int[] array, final int n2)
'''
pass
def addWrapField():
'''public long addWrapField(final long n, final int n2)
public int[] addWrapField(final ReadablePartial readablePartial, final int n, final int[] array, final int n2)
'''
pass
def getDifference():
'''public int getDifference(final long n, final long n2)
'''
pass
def getDifferenceAsLong():
'''public long getDifferenceAsLong(final long n, final long n2)
'''
pass
def set():
'''public long set(final long n, final int n2)
public int[] set(final ReadablePartial readablePartial, final int n, final int[] array, final int n2)
public long set(final long n, final String s, final Locale locale)
public long set(final long n, final String s)
public int[] set(final ReadablePartial readablePartial, final int n, final int[] array, final String s, final Locale locale)
'''
pass
def getDurationField():
'''public DurationField getDurationField()
'''
pass
def getRangeDurationField():
'''public DurationField getRangeDurationField()
'''
pass
def isLeap():
'''public boolean isLeap(final long n)
'''
pass
def getLeapAmount():
'''public int getLeapAmount(final long n)
'''
pass
def getLeapDurationField():
'''public DurationField getLeapDurationField()
'''
pass
def getMinimumValue():
'''public int getMinimumValue()
public int getMinimumValue(final long n)
public int getMinimumValue(final ReadablePartial readablePartial)
public int getMinimumValue(final ReadablePartial readablePartial, final int[] array)
'''
pass
def getMaximumValue():
'''public int getMaximumValue()
public int getMaximumValue(final long n)
public int getMaximumValue(final ReadablePartial readablePartial)
public int getMaximumValue(final ReadablePartial readablePartial, final int[] array)
'''
pass
def getMaximumTextLength():
'''public int getMaximumTextLength(final Locale locale)
'''
pass
def getMaximumShortTextLength():
'''public int getMaximumShortTextLength(final Locale locale)
'''
pass
def roundFloor():
'''public long roundFloor(final long n)
'''
pass
def roundCeiling():
'''public long roundCeiling(final long n)
'''
pass
def roundHalfFloor():
'''public long roundHalfFloor(final long n)
'''
pass
def roundHalfCeiling():
'''public long roundHalfCeiling(final long n)
'''
pass
def roundHalfEven():
'''public long roundHalfEven(final long n)
'''
pass
def remainder():
'''public long remainder(final long n)
'''
pass
def toString():
'''public String toString()
'''
pass
