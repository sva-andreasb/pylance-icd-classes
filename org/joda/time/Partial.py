def Partial():
    '''    public Partial()
    public Partial(final Chronology chronology)
    public Partial(final DateTimeFieldType dateTimeFieldType, final int n)
    public Partial(final DateTimeFieldType dateTimeFieldType, final int n, Chronology withUTC)
    public Partial(final DateTimeFieldType[] array, final int[] array2)
    public Partial(final DateTimeFieldType[] iTypes, final int[] iValues, Chronology withUTC)
    public Partial(final ReadablePartial readablePartial)
    '''
def size():
    '''    public int size()
    '''
def getChronology():
    '''    public Chronology getChronology()
    '''
def getFieldType():
    '''    public DateTimeFieldType getFieldType(final int n)
    '''
def getFieldTypes():
    '''    public DateTimeFieldType[] getFieldTypes()
    '''
def getValue():
    '''    public int getValue(final int n)
    '''
def getValues():
    '''    public int[] getValues()
    '''
def withChronologyRetainFields():
    '''    public Partial withChronologyRetainFields(Chronology chronology)
    '''
def with():
    '''    public Partial with(final DateTimeFieldType dateTimeFieldType, final int n)
    '''
def without():
    '''    public Partial without(final DateTimeFieldType dateTimeFieldType)
    '''
def withField():
    '''    public Partial withField(final DateTimeFieldType dateTimeFieldType, final int n)
    '''
def withFieldAdded():
    '''    public Partial withFieldAdded(final DurationFieldType durationFieldType, final int n)
    '''
def withFieldAddWrapped():
    '''    public Partial withFieldAddWrapped(final DurationFieldType durationFieldType, final int n)
    '''
def withPeriodAdded():
    '''    public Partial withPeriodAdded(final ReadablePeriod readablePeriod, final int n)
    '''
def plus():
    '''    public Partial plus(final ReadablePeriod readablePeriod)
    '''
def minus():
    '''    public Partial minus(final ReadablePeriod readablePeriod)
    '''
def property():
    '''    public Property property(final DateTimeFieldType dateTimeFieldType)
    '''
def isMatch():
    '''    public boolean isMatch(final ReadableInstant readableInstant)
    public boolean isMatch(final ReadablePartial readablePartial)
    '''
def getFormatter():
    '''    public DateTimeFormatter getFormatter()
    '''
def toString():
    '''    public String toString()
    public String toString(final String s)
    public String toString(final String s, final Locale locale)
    '''
def toStringList():
    '''    public String toStringList()
    '''
def getField():
    '''    public DateTimeField getField()
    '''
def getPartial():
    '''    public Partial getPartial()
    '''
def get():
    '''    public int get()
    '''
def addToCopy():
    '''    public Partial addToCopy(final int n)
    '''
def addWrapFieldToCopy():
    '''    public Partial addWrapFieldToCopy(final int n)
    '''
def setCopy():
    '''    public Partial setCopy(final int n)
    public Partial setCopy(final String s, final Locale locale)
    public Partial setCopy(final String s)
    '''
def withMaximumValue():
    '''    public Partial withMaximumValue()
    '''
def withMinimumValue():
    '''    public Partial withMinimumValue()
    '''
