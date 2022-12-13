def StrBuilder():
    '''    public StrBuilder()
    public StrBuilder(int initialCapacity)
    public StrBuilder(final String str)
    '''
def getNewLineText():
    '''    public String getNewLineText()
    '''
def setNewLineText():
    '''    public StrBuilder setNewLineText(final String newLine)
    '''
def getNullText():
    '''    public String getNullText()
    '''
def setNullText():
    '''    public StrBuilder setNullText(String nullText)
    '''
def length():
    '''    public int length()
    '''
def setLength():
    '''    public StrBuilder setLength(final int length)
    '''
def capacity():
    '''    public int capacity()
    '''
def ensureCapacity():
    '''    public StrBuilder ensureCapacity(final int capacity)
    '''
def minimizeCapacity():
    '''    public StrBuilder minimizeCapacity()
    '''
def size():
    '''    public int size()
    '''
def isEmpty():
    '''    public boolean isEmpty()
    '''
def clear():
    '''    public StrBuilder clear()
    '''
def charAt():
    '''    public char charAt(final int index)
    '''
def setCharAt():
    '''    public StrBuilder setCharAt(final int index, final char ch)
    '''
def deleteCharAt():
    '''    public StrBuilder deleteCharAt(final int index)
    '''
def toCharArray():
    '''    public char[] toCharArray()
    public char[] toCharArray(final int startIndex, int endIndex)
    '''
def getChars():
    '''    public char[] getChars(char[] destination)
    public void getChars(final int startIndex, final int endIndex, final char[] destination, final int destinationIndex)
    '''
def readFrom():
    '''    public int readFrom(final Readable readable)
    '''
def appendNewLine():
    '''    public StrBuilder appendNewLine()
    '''
def appendNull():
    '''    public StrBuilder appendNull()
    '''
def append():
    '''    public StrBuilder append(final Object obj)
    public StrBuilder append(final CharSequence seq)
    public StrBuilder append(final CharSequence seq, final int startIndex, final int length)
    public StrBuilder append(final String str)
    public StrBuilder append(final String str, final int startIndex, final int length)
    public StrBuilder append(final String format, final Object... objs)
    public StrBuilder append(final CharBuffer buf)
    public StrBuilder append(final CharBuffer buf, final int startIndex, final int length)
    public StrBuilder append(final StringBuffer str)
    public StrBuilder append(final StringBuffer str, final int startIndex, final int length)
    public StrBuilder append(final StringBuilder str)
    public StrBuilder append(final StringBuilder str, final int startIndex, final int length)
    public StrBuilder append(final StrBuilder str)
    public StrBuilder append(final StrBuilder str, final int startIndex, final int length)
    public StrBuilder append(final char[] chars)
    public StrBuilder append(final char[] chars, final int startIndex, final int length)
    public StrBuilder append(final boolean value)
    public StrBuilder append(final char ch)
    public StrBuilder append(final int value)
    public StrBuilder append(final long value)
    public StrBuilder append(final float value)
    public StrBuilder append(final double value)
    '''
def appendln():
    '''    public StrBuilder appendln(final Object obj)
    public StrBuilder appendln(final String str)
    public StrBuilder appendln(final String str, final int startIndex, final int length)
    public StrBuilder appendln(final String format, final Object... objs)
    public StrBuilder appendln(final StringBuffer str)
    public StrBuilder appendln(final StringBuilder str)
    public StrBuilder appendln(final StringBuilder str, final int startIndex, final int length)
    public StrBuilder appendln(final StringBuffer str, final int startIndex, final int length)
    public StrBuilder appendln(final StrBuilder str)
    public StrBuilder appendln(final StrBuilder str, final int startIndex, final int length)
    public StrBuilder appendln(final char[] chars)
    public StrBuilder appendln(final char[] chars, final int startIndex, final int length)
    public StrBuilder appendln(final boolean value)
    public StrBuilder appendln(final char ch)
    public StrBuilder appendln(final int value)
    public StrBuilder appendln(final long value)
    public StrBuilder appendln(final float value)
    public StrBuilder appendln(final double value)
    '''
def appendAll():
    '''    public <T> StrBuilder appendAll(final T... array)
    public StrBuilder appendAll(final Iterable<?> iterable)
    public StrBuilder appendAll(final Iterator<?> it)
    '''
def appendWithSeparators():
    '''    public StrBuilder appendWithSeparators(final Object[] array, final String separator)
    public StrBuilder appendWithSeparators(final Iterable<?> iterable, final String separator)
    public StrBuilder appendWithSeparators(final Iterator<?> it, final String separator)
    '''
def appendSeparator():
    '''    public StrBuilder appendSeparator(final String separator)
    public StrBuilder appendSeparator(final String standard, final String defaultIfEmpty)
    public StrBuilder appendSeparator(final char separator)
    public StrBuilder appendSeparator(final char standard, final char defaultIfEmpty)
    public StrBuilder appendSeparator(final String separator, final int loopIndex)
    public StrBuilder appendSeparator(final char separator, final int loopIndex)
    '''
def appendPadding():
    '''    public StrBuilder appendPadding(final int length, final char padChar)
    '''
def appendFixedWidthPadLeft():
    '''    public StrBuilder appendFixedWidthPadLeft(final Object obj, final int width, final char padChar)
    public StrBuilder appendFixedWidthPadLeft(final int value, final int width, final char padChar)
    '''
def appendFixedWidthPadRight():
    '''    public StrBuilder appendFixedWidthPadRight(final Object obj, final int width, final char padChar)
    public StrBuilder appendFixedWidthPadRight(final int value, final int width, final char padChar)
    '''
def insert():
    '''    public StrBuilder insert(final int index, final Object obj)
    public StrBuilder insert(final int index, String str)
    public StrBuilder insert(final int index, final char[] chars)
    public StrBuilder insert(final int index, final char[] chars, final int offset, final int length)
    public StrBuilder insert(int index, final boolean value)
    public StrBuilder insert(final int index, final char value)
    public StrBuilder insert(final int index, final int value)
    public StrBuilder insert(final int index, final long value)
    public StrBuilder insert(final int index, final float value)
    public StrBuilder insert(final int index, final double value)
    '''
def delete():
    '''    public StrBuilder delete(final int startIndex, int endIndex)
    '''
def deleteAll():
    '''    public StrBuilder deleteAll(final char ch)
    public StrBuilder deleteAll(final String str)
    public StrBuilder deleteAll(final StrMatcher matcher)
    '''
def deleteFirst():
    '''    public StrBuilder deleteFirst(final char ch)
    public StrBuilder deleteFirst(final String str)
    public StrBuilder deleteFirst(final StrMatcher matcher)
    '''
def replace():
    '''    public StrBuilder replace(final int startIndex, int endIndex, final String replaceStr)
    public StrBuilder replace(final StrMatcher matcher, final String replaceStr, final int startIndex, int endIndex, final int replaceCount)
    '''
def replaceAll():
    '''    public StrBuilder replaceAll(final char search, final char replace)
    public StrBuilder replaceAll(final String searchStr, final String replaceStr)
    public StrBuilder replaceAll(final StrMatcher matcher, final String replaceStr)
    '''
def replaceFirst():
    '''    public StrBuilder replaceFirst(final char search, final char replace)
    public StrBuilder replaceFirst(final String searchStr, final String replaceStr)
    public StrBuilder replaceFirst(final StrMatcher matcher, final String replaceStr)
    '''
def reverse():
    '''    public StrBuilder reverse()
    '''
def trim():
    '''    public StrBuilder trim()
    '''
def startsWith():
    '''    public boolean startsWith(final String str)
    '''
def endsWith():
    '''    public boolean endsWith(final String str)
    '''
def subSequence():
    '''    public CharSequence subSequence(final int startIndex, final int endIndex)
    '''
def substring():
    '''    public String substring(final int start)
    public String substring(final int startIndex, int endIndex)
    '''
def leftString():
    '''    public String leftString(final int length)
    '''
def rightString():
    '''    public String rightString(final int length)
    '''
def midString():
    '''    public String midString(int index, final int length)
    '''
def contains():
    '''    public boolean contains(final char ch)
    public boolean contains(final String str)
    public boolean contains(final StrMatcher matcher)
    '''
def indexOf():
    '''    public int indexOf(final char ch)
    public int indexOf(final char ch, int startIndex)
    public int indexOf(final String str)
    public int indexOf(final String str, int startIndex)
    public int indexOf(final StrMatcher matcher)
    public int indexOf(final StrMatcher matcher, int startIndex)
    '''
def lastIndexOf():
    '''    public int lastIndexOf(final char ch)
    public int lastIndexOf(final char ch, int startIndex)
    public int lastIndexOf(final String str)
    public int lastIndexOf(final String str, int startIndex)
    public int lastIndexOf(final StrMatcher matcher)
    public int lastIndexOf(final StrMatcher matcher, int startIndex)
    '''
def asTokenizer():
    '''    public StrTokenizer asTokenizer()
    '''
def asReader():
    '''    public Reader asReader()
    '''
def asWriter():
    '''    public Writer asWriter()
    '''
def appendTo():
    '''    public void appendTo(final Appendable appendable)
    '''
def equalsIgnoreCase():
    '''    public boolean equalsIgnoreCase(final StrBuilder other)
    '''
def equals():
    '''    public boolean equals(final StrBuilder other)
    public boolean equals(final Object obj)
    '''
def hashCode():
    '''    public int hashCode()
    '''
def toString():
    '''    public String toString()
    '''
def toStringBuffer():
    '''    public StringBuffer toStringBuffer()
    '''
def toStringBuilder():
    '''    public StringBuilder toStringBuilder()
    '''
def build():
    '''    public String build()
    '''
def getContent():
    '''    public String getContent()
    '''
def close():
    '''    public void close()
    public void close()
    '''
def read():
    '''    public int read()
    public int read(final char[] b, final int off, int len)
    '''
def skip():
    '''    public long skip(long n)
    '''
def ready():
    '''    public boolean ready()
    '''
def markSupported():
    '''    public boolean markSupported()
    '''
def mark():
    '''    public void mark(final int readAheadLimit)
    '''
def reset():
    '''    public void reset()
    '''
def flush():
    '''    public void flush()
    '''
def write():
    '''    public void write(final int c)
    public void write(final char[] cbuf)
    public void write(final char[] cbuf, final int off, final int len)
    public void write(final String str)
    public void write(final String str, final int off, final int len)
    '''
