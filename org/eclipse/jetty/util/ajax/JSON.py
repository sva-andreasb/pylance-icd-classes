def JSON():
'''public JSON()
'''
pass
def getStringBufferSize():
'''public int getStringBufferSize()
'''
pass
def setStringBufferSize():
'''public void setStringBufferSize(final int stringBufferSize)
'''
pass
def registerConvertor():
'''public static void registerConvertor(final Class forClass, final Convertor convertor)
'''
pass
def getDefault():
'''public static JSON getDefault()
'''
pass
def setDefault():
'''public static void setDefault(final JSON json)
'''
pass
def toString():
'''public static String toString(final Object object)
public static String toString(final Map object)
public static String toString(final Object[] array)
public String toString()
public String toString()
'''
pass
def parse():
'''public static Object parse(final String s)
public static Object parse(final String s, final boolean stripOuterComment)
public static Object parse(final Reader in)
public static Object parse(final Reader in, final boolean stripOuterComment)
public static Object parse(final InputStream in)
public static Object parse(final InputStream in, final boolean stripOuterComment)
public Object parse(final Source source, final boolean stripOuterComment)
public Object parse(final Source source)
'''
pass
def toJSON():
'''public String toJSON(final Object object)
public void toJSON(final Output out)
'''
pass
def fromJSON():
'''public Object fromJSON(final String json)
public void fromJSON(final Map object)
'''
pass
def append():
'''public void append(final StringBuffer buffer, final Object object)
public void append(final Appendable buffer, final Object object)
'''
pass
def appendNull():
'''public void appendNull(final StringBuffer buffer)
public void appendNull(final Appendable buffer)
'''
pass
def appendJSON():
'''public void appendJSON(final StringBuffer buffer, final Convertor convertor, final Object object)
public void appendJSON(final Appendable buffer, final Convertor convertor, final Object object)
public void appendJSON(final StringBuffer buffer, final Convertible converter)
public void appendJSON(final Appendable buffer, final Convertible converter)
public void appendJSON(final StringBuffer buffer, final Generator generator)
public void appendJSON(final Appendable buffer, final Generator generator)
'''
pass
def appendMap():
'''public void appendMap(final StringBuffer buffer, final Map<?, ?> map)
public void appendMap(final Appendable buffer, final Map<?, ?> map)
'''
pass
def appendArray():
'''public void appendArray(final StringBuffer buffer, final Collection collection)
public void appendArray(final Appendable buffer, final Collection collection)
public void appendArray(final StringBuffer buffer, final Object array)
public void appendArray(final Appendable buffer, final Object array)
'''
pass
def appendBoolean():
'''public void appendBoolean(final StringBuffer buffer, final Boolean b)
public void appendBoolean(final Appendable buffer, final Boolean b)
'''
pass
def appendNumber():
'''public void appendNumber(final StringBuffer buffer, final Number number)
public void appendNumber(final Appendable buffer, final Number number)
'''
pass
def appendString():
'''public void appendString(final StringBuffer buffer, final String string)
public void appendString(final Appendable buffer, final String string)
'''
pass
def addConvertor():
'''public void addConvertor(final Class forClass, final Convertor convertor)
'''
pass
def addConvertorFor():
'''public void addConvertorFor(final String name, final Convertor convertor)
'''
pass
def getConvertorFor():
'''public Convertor getConvertorFor(final String name)
'''
pass
def parseNumber():
'''public Number parseNumber(final Source source)
'''
pass
def complete():
'''public void complete()
'''
pass
def add():
'''public void add(final Object obj)
public void add(final String name, final Object value)
public void add(final String name, final double value)
public void add(final String name, final long value)
public void add(final String name, final boolean value)
'''
pass
def addClass():
'''public void addClass(final Class type)
'''
pass
def StringSource():
'''public StringSource(final String s)
'''
pass
def hasNext():
'''public boolean hasNext()
public boolean hasNext()
'''
pass
def next():
'''public char next()
public char next()
'''
pass
def peek():
'''public char peek()
public char peek()
'''
pass
def scratchBuffer():
'''public char[] scratchBuffer()
public char[] scratchBuffer()
'''
pass
def ReaderSource():
'''public ReaderSource(final Reader r)
'''
pass
def setReader():
'''public void setReader(final Reader reader)
'''
pass
def Literal():
'''public Literal(final String json)
'''
pass
def addJSON():
'''public void addJSON(final Appendable buffer)
'''
pass
