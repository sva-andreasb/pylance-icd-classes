FWD = "int  32"
BACK = "int  16"
UTF16 = "int  8"
CONTAINED = "int  2"
NOT_CONTAINED = "int  1"
ALL = "int  63"
FWD_UTF16_CONTAINED = "int  42"
FWD_UTF16_NOT_CONTAINED = "int  41"
BACK_UTF16_CONTAINED = "int  26"
BACK_UTF16_NOT_CONTAINED = "int  25"
def UnicodeSetStringSpan():
'''public UnicodeSetStringSpan(final UnicodeSet set, final ArrayList<String> setStrings, final int which)
public UnicodeSetStringSpan(final UnicodeSetStringSpan otherStringSpan, final ArrayList<String> newParentSetStrings)
'''
pass
def needsStringSpanUTF16():
'''public boolean needsStringSpanUTF16()
'''
pass
def contains():
'''public boolean contains(final int c)
'''
pass
def span():
'''public synchronized int span(final CharSequence s, final int start, final int length, final UnicodeSet.SpanCondition spanCondition)
'''
pass
def spanBack():
'''public synchronized int spanBack(final CharSequence s, final int length, final UnicodeSet.SpanCondition spanCondition)
'''
pass
def OffsetList():
'''public OffsetList()
'''
pass
def setMaxLength():
'''public void setMaxLength(final int maxLength)
'''
pass
def clear():
'''public void clear()
'''
pass
def isEmpty():
'''public boolean isEmpty()
'''
pass
def shift():
'''public void shift(final int delta)
'''
pass
def addOffset():
'''public void addOffset(final int offset)
'''
pass
def containsOffset():
'''public boolean containsOffset(final int offset)
'''
pass
def popMinimum():
'''public int popMinimum()
'''
pass
