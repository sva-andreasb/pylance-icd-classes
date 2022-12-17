def ():
    '''returns Partial\n\n
    ()\n
    (final Chronology chronology)\n
    (final DateTimeFieldType dateTimeFieldType, final int n)\n
    (final DateTimeFieldType dateTimeFieldType, final int n, Chronology withUTC)\n
    (final DateTimeFieldType[] array, final int[] array2)\n
    (final DateTimeFieldType[] iTypes, final int[] iValues, Chronology withUTC)\n
    (final ReadablePartial readablePartial)\n
    '''
def size():
    '''returns int\n\n
    size()\n
    '''
def getChronology():
    '''returns Chronology\n\n
    getChronology()\n
    '''
def getFieldType():
    '''returns DateTimeFieldType\n\n
    getFieldType(final int n)\n
    '''
def getFieldTypes():
    '''returns DateTimeFieldType[]\n\n
    getFieldTypes()\n
    '''
def getValue():
    '''returns int\n\n
    getValue(final int n)\n
    '''
def getValues():
    '''returns int[]\n\n
    getValues()\n
    '''
def withChronologyRetainFields():
    '''returns Partial\n\n
    withChronologyRetainFields(Chronology chronology)\n
    '''
def with():
    '''returns Partial\n\n
    with(final DateTimeFieldType dateTimeFieldType, final int n)\n
    '''
def without():
    '''returns Partial\n\n
    without(final DateTimeFieldType dateTimeFieldType)\n
    '''
def withField():
    '''returns Partial\n\n
    withField(final DateTimeFieldType dateTimeFieldType, final int n)\n
    '''
def withFieldAdded():
    '''returns Partial\n\n
    withFieldAdded(final DurationFieldType durationFieldType, final int n)\n
    '''
def withFieldAddWrapped():
    '''returns Partial\n\n
    withFieldAddWrapped(final DurationFieldType durationFieldType, final int n)\n
    '''
def withPeriodAdded():
    '''returns Partial\n\n
    withPeriodAdded(final ReadablePeriod readablePeriod, final int n)\n
    '''
def plus():
    '''returns Partial\n\n
    plus(final ReadablePeriod readablePeriod)\n
    '''
def minus():
    '''returns Partial\n\n
    minus(final ReadablePeriod readablePeriod)\n
    '''
def property():
    '''returns Property\n\n
    property(final DateTimeFieldType dateTimeFieldType)\n
    '''
def isMatch():
    '''returns boolean\n\n
    isMatch(final ReadableInstant readableInstant)\n
    isMatch(final ReadablePartial readablePartial)\n
    '''
def getFormatter():
    '''returns DateTimeFormatter\n\n
    getFormatter()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString(final String s)\n
    toString(final String s, final Locale locale)\n
    '''
def toStringList():
    '''returns String\n\n
    toStringList()\n
    '''
def getField():
    '''returns DateTimeField\n\n
    getField()\n
    '''
def getPartial():
    '''returns Partial\n\n
    getPartial()\n
    '''
def get():
    '''returns int\n\n
    get()\n
    '''
def addToCopy():
    '''returns Partial\n\n
    addToCopy(final int n)\n
    '''
def addWrapFieldToCopy():
    '''returns Partial\n\n
    addWrapFieldToCopy(final int n)\n
    '''
def setCopy():
    '''returns Partial\n\n
    setCopy(final int n)\n
    setCopy(final String s, final Locale locale)\n
    setCopy(final String s)\n
    '''
def withMaximumValue():
    '''returns Partial\n\n
    withMaximumValue()\n
    '''
def withMinimumValue():
    '''returns Partial\n\n
    withMinimumValue()\n
    '''
