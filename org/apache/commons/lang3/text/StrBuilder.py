def StrBuilder():
'''public StrBuilder()
public StrBuilder(int initialCapacity)
public StrBuilder(final String str)
'''
pass
def getNewLineText():
'''public String getNewLineText()
'''
pass
def setNewLineText():
'''public StrBuilder setNewLineText(final String newLine)
'''
pass
def getNullText():
'''public String getNullText()
'''
pass
def setNullText():
'''public StrBuilder setNullText(String nullText)
'''
pass
def length():
'''public int length()
'''
pass
def setLength():
'''public StrBuilder setLength(final int length)
'''
pass
def capacity():
'''public int capacity()
'''
pass
def ensureCapacity():
'''public StrBuilder ensureCapacity(final int capacity)
'''
pass
def minimizeCapacity():
'''public StrBuilder minimizeCapacity()
'''
pass
def size():
'''public int size()
'''
pass
def isEmpty():
'''public boolean isEmpty()
'''
pass
def clear():
'''public StrBuilder clear()
'''
pass
def charAt():
'''public char charAt(final int index)
'''
pass
def setCharAt():
'''public StrBuilder setCharAt(final int index, final char ch)
'''
pass
def deleteCharAt():
'''public StrBuilder deleteCharAt(final int index)
'''
pass
def toCharArray():
'''public char[] toCharArray()
public char[] toCharArray(final int startIndex, int endIndex)
'''
pass
def getChars():
'''public char[] getChars(char[] destination)
public void getChars(final int startIndex, final int endIndex, final char[] destination, final int destinationIndex)
'''
pass
def readFrom():
'''public int readFrom(final Readable readable)
'''
pass
def appendNewLine():
'''public StrBuilder appendNewLine()
'''
pass
def appendNull():
'''public StrBuilder appendNull()
'''
pass
def append():
'''public StrBuilder append(final Object obj)
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
pass
def appendln():
'''public StrBuilder appendln(final Object obj)
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
pass
def appendAll():
'''public <T> StrBuilder appendAll(final T... array)
public StrBuilder appendAll(final Iterable<?> iterable)
public StrBuilder appendAll(final Iterator<?> it)
'''
pass
def appendWithSeparators():
'''public StrBuilder appendWithSeparators(final Object[] array, final String separator)
public StrBuilder appendWithSeparators(final Iterable<?> iterable, final String separator)
public StrBuilder appendWithSeparators(final Iterator<?> it, final String separator)
'''
pass
def appendSeparator():
'''public StrBuilder appendSeparator(final String separator)
public StrBuilder appendSeparator(final String standard, final String defaultIfEmpty)
public StrBuilder appendSeparator(final char separator)
public StrBuilder appendSeparator(final char standard, final char defaultIfEmpty)
public StrBuilder appendSeparator(final String separator, final int loopIndex)
public StrBuilder appendSeparator(final char separator, final int loopIndex)
'''
pass
def appendPadding():
'''public StrBuilder appendPadding(final int length, final char padChar)
'''
pass
def appendFixedWidthPadLeft():
'''public StrBuilder appendFixedWidthPadLeft(final Object obj, final int width, final char padChar)
public StrBuilder appendFixedWidthPadLeft(final int value, final int width, final char padChar)
'''
pass
def appendFixedWidthPadRight():
'''public StrBuilder appendFixedWidthPadRight(final Object obj, final int width, final char padChar)
public StrBuilder appendFixedWidthPadRight(final int value, final int width, final char padChar)
'''
pass
def insert():
'''public StrBuilder insert(final int index, final Object obj)
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
pass
def delete():
'''public StrBuilder delete(final int startIndex, int endIndex)
'''
pass
def deleteAll():
'''public StrBuilder deleteAll(final char ch)
public StrBuilder deleteAll(final String str)
public StrBuilder deleteAll(final StrMatcher matcher)
'''
pass
def deleteFirst():
'''public StrBuilder deleteFirst(final char ch)
public StrBuilder deleteFirst(final String str)
public StrBuilder deleteFirst(final StrMatcher matcher)
'''
pass
def replace():
'''public StrBuilder replace(final int startIndex, int endIndex, final String replaceStr)
public StrBuilder replace(final StrMatcher matcher, final String replaceStr, final int startIndex, int endIndex, final int replaceCount)
'''
pass
def replaceAll():
'''public StrBuilder replaceAll(final char search, final char replace)
public StrBuilder replaceAll(final String searchStr, final String replaceStr)
public StrBuilder replaceAll(final StrMatcher matcher, final String replaceStr)
'''
pass
def replaceFirst():
'''public StrBuilder replaceFirst(final char search, final char replace)
public StrBuilder replaceFirst(final String searchStr, final String replaceStr)
public StrBuilder replaceFirst(final StrMatcher matcher, final String replaceStr)
'''
pass
def reverse():
'''public StrBuilder reverse()
'''
pass
def trim():
'''public StrBuilder trim()
'''
pass
def startsWith():
'''public boolean startsWith(final String str)
'''
pass
def endsWith():
'''public boolean endsWith(final String str)
'''
pass
def subSequence():
'''public CharSequence subSequence(final int startIndex, final int endIndex)
'''
pass
def substring():
'''public String substring(final int start)
public String substring(final int startIndex, int endIndex)
'''
pass
def leftString():
'''public String leftString(final int length)
'''
pass
def rightString():
'''public String rightString(final int length)
'''
pass
def midString():
'''public String midString(int index, final int length)
'''
pass
def contains():
'''public boolean contains(final char ch)
public boolean contains(final String str)
public boolean contains(final StrMatcher matcher)
'''
pass
def indexOf():
'''public int indexOf(final char ch)
public int indexOf(final char ch, int startIndex)
public int indexOf(final String str)
public int indexOf(final String str, int startIndex)
public int indexOf(final StrMatcher matcher)
public int indexOf(final StrMatcher matcher, int startIndex)
'''
pass
def lastIndexOf():
'''public int lastIndexOf(final char ch)
public int lastIndexOf(final char ch, int startIndex)
public int lastIndexOf(final String str)
public int lastIndexOf(final String str, int startIndex)
public int lastIndexOf(final StrMatcher matcher)
public int lastIndexOf(final StrMatcher matcher, int startIndex)
'''
pass
def asTokenizer():
'''public StrTokenizer asTokenizer()
'''
pass
def asReader():
'''public Reader asReader()
'''
pass
def asWriter():
'''public Writer asWriter()
'''
pass
def appendTo():
'''public void appendTo(final Appendable appendable)
'''
pass
def equalsIgnoreCase():
'''public boolean equalsIgnoreCase(final StrBuilder other)
'''
pass
def equals():
'''public boolean equals(final StrBuilder other)
public boolean equals(final Object obj)
'''
pass
def hashCode():
'''public int hashCode()
'''
pass
def toString():
'''public String toString()
'''
pass
def toStringBuffer():
'''public StringBuffer toStringBuffer()
'''
pass
def toStringBuilder():
'''public StringBuilder toStringBuilder()
'''
pass
def build():
'''public String build()
'''
pass
def getContent():
'''public String getContent()
'''
pass
def close():
'''public void close()
public void close()
'''
pass
def read():
'''public int read()
public int read(final char[] b, final int off, int len)
'''
pass
def skip():
'''public long skip(long n)
'''
pass
def ready():
'''public boolean ready()
'''
pass
def markSupported():
'''public boolean markSupported()
'''
pass
def mark():
'''public void mark(final int readAheadLimit)
'''
pass
def reset():
'''public void reset()
'''
pass
def flush():
'''public void flush()
'''
pass
def write():
'''public void write(final int c)
public void write(final char[] cbuf)
public void write(final char[] cbuf, final int off, final int len)
public void write(final String str)
public void write(final String str, final int off, final int len)
'''
pass
