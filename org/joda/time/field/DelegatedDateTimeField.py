def ():
    '''returns DelegatedDateTimeField\n\n
    (final DateTimeField dateTimeField)\n
    (final DateTimeField dateTimeField, final DateTimeFieldType dateTimeFieldType)\n
    (final DateTimeField iField, final DurationField iRangeDurationField, final DateTimeFieldType dateTimeFieldType)\n
    '''
def getType():
    '''returns DateTimeFieldType\n\n
    getType()\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def isSupported():
    '''returns boolean\n\n
    isSupported()\n
    '''
def isLenient():
    '''returns boolean\n\n
    isLenient()\n
    '''
def get():
    '''returns int\n\n
    get(final long n)\n
    '''
def getAsText():
    '''returns String\n\n
    getAsText(final long n, final Locale locale)\n
    getAsText(final long n)\n
    getAsText(final ReadablePartial readablePartial, final int n, final Locale locale)\n
    getAsText(final ReadablePartial readablePartial, final Locale locale)\n
    getAsText(final int n, final Locale locale)\n
    '''
def getAsShortText():
    '''returns String\n\n
    getAsShortText(final long n, final Locale locale)\n
    getAsShortText(final long n)\n
    getAsShortText(final ReadablePartial readablePartial, final int n, final Locale locale)\n
    getAsShortText(final ReadablePartial readablePartial, final Locale locale)\n
    getAsShortText(final int n, final Locale locale)\n
    '''
def add():
    '''returns int[]\n\n
    add(final long n, final int n2)\n
    add(final long n, final long n2)\n
    add(final ReadablePartial readablePartial, final int n, final int[] array, final int n2)\n
    '''
def addWrapPartial():
    '''returns int[]\n\n
    addWrapPartial(final ReadablePartial readablePartial, final int n, final int[] array, final int n2)\n
    '''
def addWrapField():
    '''returns int[]\n\n
    addWrapField(final long n, final int n2)\n
    addWrapField(final ReadablePartial readablePartial, final int n, final int[] array, final int n2)\n
    '''
def getDifference():
    '''returns int\n\n
    getDifference(final long n, final long n2)\n
    '''
def getDifferenceAsLong():
    '''returns long\n\n
    getDifferenceAsLong(final long n, final long n2)\n
    '''
def set():
    '''returns int[]\n\n
    set(final long n, final int n2)\n
    set(final long n, final String s, final Locale locale)\n
    set(final long n, final String s)\n
    set(final ReadablePartial readablePartial, final int n, final int[] array, final int n2)\n
    set(final ReadablePartial readablePartial, final int n, final int[] array, final String s, final Locale locale)\n
    '''
def getDurationField():
    '''returns DurationField\n\n
    getDurationField()\n
    '''
def getRangeDurationField():
    '''returns DurationField\n\n
    getRangeDurationField()\n
    '''
def isLeap():
    '''returns boolean\n\n
    isLeap(final long n)\n
    '''
def getLeapAmount():
    '''returns int\n\n
    getLeapAmount(final long n)\n
    '''
def getLeapDurationField():
    '''returns DurationField\n\n
    getLeapDurationField()\n
    '''
def getMinimumValue():
    '''returns int\n\n
    getMinimumValue()\n
    getMinimumValue(final long n)\n
    getMinimumValue(final ReadablePartial readablePartial)\n
    getMinimumValue(final ReadablePartial readablePartial, final int[] array)\n
    '''
def getMaximumValue():
    '''returns int\n\n
    getMaximumValue()\n
    getMaximumValue(final long n)\n
    getMaximumValue(final ReadablePartial readablePartial)\n
    getMaximumValue(final ReadablePartial readablePartial, final int[] array)\n
    '''
def getMaximumTextLength():
    '''returns int\n\n
    getMaximumTextLength(final Locale locale)\n
    '''
def getMaximumShortTextLength():
    '''returns int\n\n
    getMaximumShortTextLength(final Locale locale)\n
    '''
def roundFloor():
    '''returns long\n\n
    roundFloor(final long n)\n
    '''
def roundCeiling():
    '''returns long\n\n
    roundCeiling(final long n)\n
    '''
def roundHalfFloor():
    '''returns long\n\n
    roundHalfFloor(final long n)\n
    '''
def roundHalfCeiling():
    '''returns long\n\n
    roundHalfCeiling(final long n)\n
    '''
def roundHalfEven():
    '''returns long\n\n
    roundHalfEven(final long n)\n
    '''
def remainder():
    '''returns long\n\n
    remainder(final long n)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
