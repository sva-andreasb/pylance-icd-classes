def ():
    '''returns StrBuilder\n\n
    ()\n
    (int initialCapacity)\n
    (final String str)\n
    '''
def getNewLineText():
    '''returns String\n\n
    getNewLineText()\n
    '''
def setNewLineText():
    '''returns StrBuilder\n\n
    setNewLineText(final String newLine)\n
    '''
def getNullText():
    '''returns String\n\n
    getNullText()\n
    '''
def setNullText():
    '''returns StrBuilder\n\n
    setNullText(String nullText)\n
    '''
def length():
    '''returns int\n\n
    length()\n
    '''
def setLength():
    '''returns StrBuilder\n\n
    setLength(final int length)\n
    '''
def capacity():
    '''returns int\n\n
    capacity()\n
    '''
def ensureCapacity():
    '''returns StrBuilder\n\n
    ensureCapacity(final int capacity)\n
    '''
def minimizeCapacity():
    '''returns StrBuilder\n\n
    minimizeCapacity()\n
    '''
def size():
    '''returns int\n\n
    size()\n
    '''
def isEmpty():
    '''returns boolean\n\n
    isEmpty()\n
    '''
def clear():
    '''returns StrBuilder\n\n
    clear()\n
    '''
def charAt():
    '''returns char\n\n
    charAt(final int index)\n
    '''
def setCharAt():
    '''returns StrBuilder\n\n
    setCharAt(final int index, final char ch)\n
    '''
def deleteCharAt():
    '''returns StrBuilder\n\n
    deleteCharAt(final int index)\n
    '''
def toCharArray():
    '''returns char[]\n\n
    toCharArray()\n
    toCharArray(final int startIndex, int endIndex)\n
    '''
def getChars():
    '''returns None\n\n
    getChars(char[] destination)\n
    getChars(final int startIndex, final int endIndex, final char[] destination, final int destinationIndex)\n
    '''
def readFrom():
    '''returns int\n\n
    readFrom(final Readable readable)\n
    '''
def appendNewLine():
    '''returns StrBuilder\n\n
    appendNewLine()\n
    '''
def appendNull():
    '''returns StrBuilder\n\n
    appendNull()\n
    '''
def append():
    '''returns StrBuilder\n\n
    append(final Object obj)\n
    append(final CharSequence seq)\n
    append(final CharSequence seq, final int startIndex, final int length)\n
    append(final String str)\n
    append(final String str, final int startIndex, final int length)\n
    append(final String format, final Object... objs)\n
    append(final CharBuffer buf)\n
    append(final CharBuffer buf, final int startIndex, final int length)\n
    append(final StringBuffer str)\n
    append(final StringBuffer str, final int startIndex, final int length)\n
    append(final StringBuilder str)\n
    append(final StringBuilder str, final int startIndex, final int length)\n
    append(final StrBuilder str)\n
    append(final StrBuilder str, final int startIndex, final int length)\n
    append(final char[] chars)\n
    append(final char[] chars, final int startIndex, final int length)\n
    append(final boolean value)\n
    append(final char ch)\n
    append(final int value)\n
    append(final long value)\n
    append(final float value)\n
    append(final double value)\n
    '''
def appendln():
    '''returns StrBuilder\n\n
    appendln(final Object obj)\n
    appendln(final String str)\n
    appendln(final String str, final int startIndex, final int length)\n
    appendln(final String format, final Object... objs)\n
    appendln(final StringBuffer str)\n
    appendln(final StringBuilder str)\n
    appendln(final StringBuilder str, final int startIndex, final int length)\n
    appendln(final StringBuffer str, final int startIndex, final int length)\n
    appendln(final StrBuilder str)\n
    appendln(final StrBuilder str, final int startIndex, final int length)\n
    appendln(final char[] chars)\n
    appendln(final char[] chars, final int startIndex, final int length)\n
    appendln(final boolean value)\n
    appendln(final char ch)\n
    appendln(final int value)\n
    appendln(final long value)\n
    appendln(final float value)\n
    appendln(final double value)\n
    '''
def appendAll():
    '''returns StrBuilder\n\n
    appendAll(final Iterable<?> iterable)\n
    appendAll(final Iterator<?> it)\n
    '''
def appendWithSeparators():
    '''returns StrBuilder\n\n
    appendWithSeparators(final Object[] array, final String separator)\n
    appendWithSeparators(final Iterable<?> iterable, final String separator)\n
    appendWithSeparators(final Iterator<?> it, final String separator)\n
    '''
def appendSeparator():
    '''returns StrBuilder\n\n
    appendSeparator(final String separator)\n
    appendSeparator(final String standard, final String defaultIfEmpty)\n
    appendSeparator(final char separator)\n
    appendSeparator(final char standard, final char defaultIfEmpty)\n
    appendSeparator(final String separator, final int loopIndex)\n
    appendSeparator(final char separator, final int loopIndex)\n
    '''
def appendPadding():
    '''returns StrBuilder\n\n
    appendPadding(final int length, final char padChar)\n
    '''
def appendFixedWidthPadLeft():
    '''returns StrBuilder\n\n
    appendFixedWidthPadLeft(final Object obj, final int width, final char padChar)\n
    appendFixedWidthPadLeft(final int value, final int width, final char padChar)\n
    '''
def appendFixedWidthPadRight():
    '''returns StrBuilder\n\n
    appendFixedWidthPadRight(final Object obj, final int width, final char padChar)\n
    appendFixedWidthPadRight(final int value, final int width, final char padChar)\n
    '''
def insert():
    '''returns StrBuilder\n\n
    insert(final int index, final Object obj)\n
    insert(final int index, String str)\n
    insert(final int index, final char[] chars)\n
    insert(final int index, final char[] chars, final int offset, final int length)\n
    insert(int index, final boolean value)\n
    insert(final int index, final char value)\n
    insert(final int index, final int value)\n
    insert(final int index, final long value)\n
    insert(final int index, final float value)\n
    insert(final int index, final double value)\n
    '''
def delete():
    '''returns StrBuilder\n\n
    delete(final int startIndex, int endIndex)\n
    '''
def deleteAll():
    '''returns StrBuilder\n\n
    deleteAll(final char ch)\n
    deleteAll(final String str)\n
    deleteAll(final StrMatcher matcher)\n
    '''
def deleteFirst():
    '''returns StrBuilder\n\n
    deleteFirst(final char ch)\n
    deleteFirst(final String str)\n
    deleteFirst(final StrMatcher matcher)\n
    '''
def replace():
    '''returns StrBuilder\n\n
    replace(final int startIndex, int endIndex, final String replaceStr)\n
    replace(final StrMatcher matcher, final String replaceStr, final int startIndex, int endIndex, final int replaceCount)\n
    '''
def replaceAll():
    '''returns StrBuilder\n\n
    replaceAll(final char search, final char replace)\n
    replaceAll(final String searchStr, final String replaceStr)\n
    replaceAll(final StrMatcher matcher, final String replaceStr)\n
    '''
def replaceFirst():
    '''returns StrBuilder\n\n
    replaceFirst(final char search, final char replace)\n
    replaceFirst(final String searchStr, final String replaceStr)\n
    replaceFirst(final StrMatcher matcher, final String replaceStr)\n
    '''
def reverse():
    '''returns StrBuilder\n\n
    reverse()\n
    '''
def trim():
    '''returns StrBuilder\n\n
    trim()\n
    '''
def startsWith():
    '''returns boolean\n\n
    startsWith(final String str)\n
    '''
def endsWith():
    '''returns boolean\n\n
    endsWith(final String str)\n
    '''
def subSequence():
    '''returns CharSequence\n\n
    subSequence(final int startIndex, final int endIndex)\n
    '''
def substring():
    '''returns String\n\n
    substring(final int start)\n
    substring(final int startIndex, int endIndex)\n
    '''
def leftString():
    '''returns String\n\n
    leftString(final int length)\n
    '''
def rightString():
    '''returns String\n\n
    rightString(final int length)\n
    '''
def midString():
    '''returns String\n\n
    midString(int index, final int length)\n
    '''
def contains():
    '''returns boolean\n\n
    contains(final char ch)\n
    contains(final String str)\n
    contains(final StrMatcher matcher)\n
    '''
def indexOf():
    '''returns int\n\n
    indexOf(final char ch)\n
    indexOf(final char ch, int startIndex)\n
    indexOf(final String str)\n
    indexOf(final String str, int startIndex)\n
    indexOf(final StrMatcher matcher)\n
    indexOf(final StrMatcher matcher, int startIndex)\n
    '''
def lastIndexOf():
    '''returns int\n\n
    lastIndexOf(final char ch)\n
    lastIndexOf(final char ch, int startIndex)\n
    lastIndexOf(final String str)\n
    lastIndexOf(final String str, int startIndex)\n
    lastIndexOf(final StrMatcher matcher)\n
    lastIndexOf(final StrMatcher matcher, int startIndex)\n
    '''
def asTokenizer():
    '''returns StrTokenizer\n\n
    asTokenizer()\n
    '''
def asReader():
    '''returns Reader\n\n
    asReader()\n
    '''
def asWriter():
    '''returns Writer\n\n
    asWriter()\n
    '''
def appendTo():
    '''returns None\n\n
    appendTo(final Appendable appendable)\n
    '''
def equalsIgnoreCase():
    '''returns boolean\n\n
    equalsIgnoreCase(final StrBuilder other)\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final StrBuilder other)\n
    equals(final Object obj)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def toStringBuffer():
    '''returns StringBuffer\n\n
    toStringBuffer()\n
    '''
def toStringBuilder():
    '''returns StringBuilder\n\n
    toStringBuilder()\n
    '''
def build():
    '''returns String\n\n
    build()\n
    '''
def getContent():
    '''returns String\n\n
    getContent()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    close()\n
    '''
def read():
    '''returns int\n\n
    read()\n
    read(final char[] b, final int off, int len)\n
    '''
def skip():
    '''returns long\n\n
    skip(long n)\n
    '''
def ready():
    '''returns boolean\n\n
    ready()\n
    '''
def markSupported():
    '''returns boolean\n\n
    markSupported()\n
    '''
def mark():
    '''returns None\n\n
    mark(final int readAheadLimit)\n
    '''
def reset():
    '''returns None\n\n
    reset()\n
    '''
def flush():
    '''returns None\n\n
    flush()\n
    '''
def write():
    '''returns None\n\n
    write(final int c)\n
    write(final char[] cbuf)\n
    write(final char[] cbuf, final int off, final int len)\n
    write(final String str)\n
    write(final String str, final int off, final int len)\n
    '''
