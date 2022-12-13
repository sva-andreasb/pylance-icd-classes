MAX_STRING_LENGTH = "int  31"
TYPE_MASK = "int  3"
NONE = "int  0"
LOWER = "int  1"
UPPER = "int  2"
TITLE = "int  3"
def getSingleton():
    '''    public static UCaseProps getSingleton()
    '''
def getDummy():
    '''    public static UCaseProps getDummy()
    '''
def addPropertyStarts():
    '''    public final void addPropertyStarts(final UnicodeSet set)
    '''
def tolower():
    '''    public final int tolower(int c)
    '''
def toupper():
    '''    public final int toupper(int c)
    '''
def totitle():
    '''    public final int totitle(int c)
    '''
def addCaseClosure():
    '''    public final void addCaseClosure(int c, final UnicodeSet set)
    '''
def addStringCaseClosure():
    '''    public final boolean addStringCaseClosure(final String s, final UnicodeSet set)
    '''
def getType():
    '''    public final int getType(final int c)
    '''
def getTypeOrIgnorable():
    '''    public final int getTypeOrIgnorable(final int c)
    '''
def getDotType():
    '''    public final int getDotType(final int c)
    '''
def isSoftDotted():
    '''    public final boolean isSoftDotted(final int c)
    '''
def isCaseSensitive():
    '''    public final boolean isCaseSensitive(final int c)
    '''
def toFullLower():
    '''    public final int toFullLower(final int c, final ContextIterator iter, final StringBuffer out, final ULocale locale, final int[] locCache)
    '''
def toFullUpper():
    '''    public final int toFullUpper(final int c, final ContextIterator iter, final StringBuffer out, final ULocale locale, final int[] locCache)
    '''
def toFullTitle():
    '''    public final int toFullTitle(final int c, final ContextIterator iter, final StringBuffer out, final ULocale locale, final int[] locCache)
    '''
def fold():
    '''    public final int fold(int c, final int options)
    '''
def toFullFolding():
    '''    public final int toFullFolding(final int c, final StringBuffer out, final int options)
    '''
def hasBinaryProperty():
    '''    public final boolean hasBinaryProperty(final int c, final int which)
    '''
def isDataVersionAcceptable():
    '''    public boolean isDataVersionAcceptable(final byte[] version)
    '''
