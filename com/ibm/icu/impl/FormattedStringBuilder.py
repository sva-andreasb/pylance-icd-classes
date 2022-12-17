def ():
    '''returns FormattedStringBuilder\n\n
    ()\n
    (final int capacity)\n
    (final FormattedStringBuilder source)\n
    '''
def copyFrom():
    '''returns None\n\n
    copyFrom(final FormattedStringBuilder source)\n
    '''
def length():
    '''returns int\n\n
    length()\n
    '''
def codePointCount():
    '''returns int\n\n
    codePointCount()\n
    '''
def charAt():
    '''returns char\n\n
    charAt(final int index)\n
    '''
def fieldAt():
    '''returns Object\n\n
    fieldAt(final int index)\n
    '''
def getFirstCodePoint():
    '''returns int\n\n
    getFirstCodePoint()\n
    '''
def getLastCodePoint():
    '''returns int\n\n
    getLastCodePoint()\n
    '''
def codePointAt():
    '''returns int\n\n
    codePointAt(final int index)\n
    '''
def codePointBefore():
    '''returns int\n\n
    codePointBefore(final int index)\n
    '''
def clear():
    '''returns FormattedStringBuilder\n\n
    clear()\n
    '''
def setAppendIndex():
    '''returns None\n\n
    setAppendIndex(final int index)\n
    '''
def appendChar16():
    '''returns int\n\n
    appendChar16(final char codeUnit, final Object field)\n
    '''
def insertChar16():
    '''returns int\n\n
    insertChar16(final int index, final char codeUnit, final Object field)\n
    '''
def appendCodePoint():
    '''returns int\n\n
    appendCodePoint(final int codePoint, final Object field)\n
    '''
def insertCodePoint():
    '''returns int\n\n
    insertCodePoint(final int index, final int codePoint, final Object field)\n
    '''
def append():
    '''returns Appendable\n\n
    append(final CharSequence sequence, final Object field)\n
    append(final char[] chars, final Object[] fields)\n
    append(final FormattedStringBuilder other)\n
    append(final CharSequence csq)\n
    append(final CharSequence csq, final int start, final int end)\n
    append(final char c)\n
    '''
def insert():
    '''returns int\n\n
    insert(final int index, final CharSequence sequence, final Object field)\n
    insert(final int index, final CharSequence sequence, final int start, final int end, final Object field)\n
    insert(final int index, final char[] chars, final Object[] fields)\n
    insert(final int index, final FormattedStringBuilder other)\n
    '''
def splice():
    '''returns int\n\n
    splice(final int startThis, final int endThis, final CharSequence sequence, final int startOther, final int endOther, final Object field)\n
    '''
def subSequence():
    '''returns CharSequence\n\n
    subSequence(final int start, final int end)\n
    '''
def subString():
    '''returns String\n\n
    subString(final int start, final int end)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def toDebugString():
    '''returns String\n\n
    toDebugString()\n
    '''
def toCharArray():
    '''returns char[]\n\n
    toCharArray()\n
    '''
def toFieldArray():
    '''returns Object[]\n\n
    toFieldArray()\n
    '''
def setAppendableField():
    '''returns None\n\n
    setAppendableField(final Object field)\n
    '''
def contentEquals():
    '''returns boolean\n\n
    contentEquals(final char[] chars, final Object[] fields)\n
    contentEquals(final FormattedStringBuilder other)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object other)\n
    '''
