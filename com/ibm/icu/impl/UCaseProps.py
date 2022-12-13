MAX_STRING_LENGTH = "int  31"
TYPE_MASK = "int  3"
NONE = "int  0"
LOWER = "int  1"
UPPER = "int  2"
TITLE = "int  3"
def getSingleton():
'''public static UCaseProps getSingleton()
'''
pass
def getDummy():
'''public static UCaseProps getDummy()
'''
pass
def addPropertyStarts():
'''public final void addPropertyStarts(final UnicodeSet set)
'''
pass
def tolower():
'''public final int tolower(int c)
'''
pass
def toupper():
'''public final int toupper(int c)
'''
pass
def totitle():
'''public final int totitle(int c)
'''
pass
def addCaseClosure():
'''public final void addCaseClosure(int c, final UnicodeSet set)
'''
pass
def addStringCaseClosure():
'''public final boolean addStringCaseClosure(final String s, final UnicodeSet set)
'''
pass
def getType():
'''public final int getType(final int c)
'''
pass
def getTypeOrIgnorable():
'''public final int getTypeOrIgnorable(final int c)
'''
pass
def getDotType():
'''public final int getDotType(final int c)
'''
pass
def isSoftDotted():
'''public final boolean isSoftDotted(final int c)
'''
pass
def isCaseSensitive():
'''public final boolean isCaseSensitive(final int c)
'''
pass
def toFullLower():
'''public final int toFullLower(final int c, final ContextIterator iter, final StringBuffer out, final ULocale locale, final int[] locCache)
'''
pass
def toFullUpper():
'''public final int toFullUpper(final int c, final ContextIterator iter, final StringBuffer out, final ULocale locale, final int[] locCache)
'''
pass
def toFullTitle():
'''public final int toFullTitle(final int c, final ContextIterator iter, final StringBuffer out, final ULocale locale, final int[] locCache)
'''
pass
def fold():
'''public final int fold(int c, final int options)
'''
pass
def toFullFolding():
'''public final int toFullFolding(final int c, final StringBuffer out, final int options)
'''
pass
def hasBinaryProperty():
'''public final boolean hasBinaryProperty(final int c, final int which)
'''
pass
def isDataVersionAcceptable():
'''public boolean isDataVersionAcceptable(final byte[] version)
'''
pass
