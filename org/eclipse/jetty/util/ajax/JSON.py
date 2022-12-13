def JSON():
    '''    public JSON()
    '''
def getStringBufferSize():
    '''    public int getStringBufferSize()
    '''
def setStringBufferSize():
    '''    public void setStringBufferSize(final int stringBufferSize)
    '''
def registerConvertor():
    '''    public static void registerConvertor(final Class forClass, final Convertor convertor)
    '''
def getDefault():
    '''    public static JSON getDefault()
    '''
def setDefault():
    '''    public static void setDefault(final JSON json)
    '''
def toString():
    '''    public static String toString(final Object object)
    public static String toString(final Map object)
    public static String toString(final Object[] array)
    public String toString()
    public String toString()
    '''
def parse():
    '''    public static Object parse(final String s)
    public static Object parse(final String s, final boolean stripOuterComment)
    public static Object parse(final Reader in)
    public static Object parse(final Reader in, final boolean stripOuterComment)
    public static Object parse(final InputStream in)
    public static Object parse(final InputStream in, final boolean stripOuterComment)
    public Object parse(final Source source, final boolean stripOuterComment)
    public Object parse(final Source source)
    '''
def toJSON():
    '''    public String toJSON(final Object object)
    public void toJSON(final Output out)
    '''
def fromJSON():
    '''    public Object fromJSON(final String json)
    public void fromJSON(final Map object)
    '''
def append():
    '''    public void append(final StringBuffer buffer, final Object object)
    public void append(final Appendable buffer, final Object object)
    '''
def appendNull():
    '''    public void appendNull(final StringBuffer buffer)
    public void appendNull(final Appendable buffer)
    '''
def appendJSON():
    '''    public void appendJSON(final StringBuffer buffer, final Convertor convertor, final Object object)
    public void appendJSON(final Appendable buffer, final Convertor convertor, final Object object)
    public void appendJSON(final StringBuffer buffer, final Convertible converter)
    public void appendJSON(final Appendable buffer, final Convertible converter)
    public void appendJSON(final StringBuffer buffer, final Generator generator)
    public void appendJSON(final Appendable buffer, final Generator generator)
    '''
def appendMap():
    '''    public void appendMap(final StringBuffer buffer, final Map<?, ?> map)
    public void appendMap(final Appendable buffer, final Map<?, ?> map)
    '''
def appendArray():
    '''    public void appendArray(final StringBuffer buffer, final Collection collection)
    public void appendArray(final Appendable buffer, final Collection collection)
    public void appendArray(final StringBuffer buffer, final Object array)
    public void appendArray(final Appendable buffer, final Object array)
    '''
def appendBoolean():
    '''    public void appendBoolean(final StringBuffer buffer, final Boolean b)
    public void appendBoolean(final Appendable buffer, final Boolean b)
    '''
def appendNumber():
    '''    public void appendNumber(final StringBuffer buffer, final Number number)
    public void appendNumber(final Appendable buffer, final Number number)
    '''
def appendString():
    '''    public void appendString(final StringBuffer buffer, final String string)
    public void appendString(final Appendable buffer, final String string)
    '''
def addConvertor():
    '''    public void addConvertor(final Class forClass, final Convertor convertor)
    '''
def addConvertorFor():
    '''    public void addConvertorFor(final String name, final Convertor convertor)
    '''
def getConvertorFor():
    '''    public Convertor getConvertorFor(final String name)
    '''
def parseNumber():
    '''    public Number parseNumber(final Source source)
    '''
def complete():
    '''    public void complete()
    '''
def add():
    '''    public void add(final Object obj)
    public void add(final String name, final Object value)
    public void add(final String name, final double value)
    public void add(final String name, final long value)
    public void add(final String name, final boolean value)
    '''
def addClass():
    '''    public void addClass(final Class type)
    '''
def StringSource():
    '''    public StringSource(final String s)
    '''
def hasNext():
    '''    public boolean hasNext()
    public boolean hasNext()
    '''
def next():
    '''    public char next()
    public char next()
    '''
def peek():
    '''    public char peek()
    public char peek()
    '''
def scratchBuffer():
    '''    public char[] scratchBuffer()
    public char[] scratchBuffer()
    '''
def ReaderSource():
    '''    public ReaderSource(final Reader r)
    '''
def setReader():
    '''    public void setReader(final Reader reader)
    '''
def Literal():
    '''    public Literal(final String json)
    '''
def addJSON():
    '''    public void addJSON(final Appendable buffer)
    '''
