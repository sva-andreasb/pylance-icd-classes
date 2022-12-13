def FormattedStringBuilder():
    '''    public FormattedStringBuilder()
    public FormattedStringBuilder(final int capacity)
    public FormattedStringBuilder(final FormattedStringBuilder source)
    '''
def copyFrom():
    '''    public void copyFrom(final FormattedStringBuilder source)
    '''
def length():
    '''    public int length()
    '''
def codePointCount():
    '''    public int codePointCount()
    '''
def charAt():
    '''    public char charAt(final int index)
    '''
def fieldAt():
    '''    public Object fieldAt(final int index)
    '''
def getFirstCodePoint():
    '''    public int getFirstCodePoint()
    '''
def getLastCodePoint():
    '''    public int getLastCodePoint()
    '''
def codePointAt():
    '''    public int codePointAt(final int index)
    '''
def codePointBefore():
    '''    public int codePointBefore(final int index)
    '''
def clear():
    '''    public FormattedStringBuilder clear()
    '''
def setAppendIndex():
    '''    public void setAppendIndex(final int index)
    '''
def appendChar16():
    '''    public int appendChar16(final char codeUnit, final Object field)
    '''
def insertChar16():
    '''    public int insertChar16(final int index, final char codeUnit, final Object field)
    '''
def appendCodePoint():
    '''    public int appendCodePoint(final int codePoint, final Object field)
    '''
def insertCodePoint():
    '''    public int insertCodePoint(final int index, final int codePoint, final Object field)
    '''
def append():
    '''    public int append(final CharSequence sequence, final Object field)
    public int append(final char[] chars, final Object[] fields)
    public int append(final FormattedStringBuilder other)
    public Appendable append(final CharSequence csq)
    public Appendable append(final CharSequence csq, final int start, final int end)
    public Appendable append(final char c)
    '''
def insert():
    '''    public int insert(final int index, final CharSequence sequence, final Object field)
    public int insert(final int index, final CharSequence sequence, final int start, final int end, final Object field)
    public int insert(final int index, final char[] chars, final Object[] fields)
    public int insert(final int index, final FormattedStringBuilder other)
    '''
def splice():
    '''    public int splice(final int startThis, final int endThis, final CharSequence sequence, final int startOther, final int endOther, final Object field)
    '''
def subSequence():
    '''    public CharSequence subSequence(final int start, final int end)
    '''
def subString():
    '''    public String subString(final int start, final int end)
    '''
def toString():
    '''    public String toString()
    '''
def toDebugString():
    '''    public String toDebugString()
    '''
def toCharArray():
    '''    public char[] toCharArray()
    '''
def toFieldArray():
    '''    public Object[] toFieldArray()
    '''
def setAppendableField():
    '''    public void setAppendableField(final Object field)
    '''
def contentEquals():
    '''    public boolean contentEquals(final char[] chars, final Object[] fields)
    public boolean contentEquals(final FormattedStringBuilder other)
    '''
def hashCode():
    '''    public int hashCode()
    '''
def equals():
    '''    public boolean equals(final Object other)
    '''
