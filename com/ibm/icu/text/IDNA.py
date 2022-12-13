DEFAULT = "int  0"
ALLOW_UNASSIGNED = "int  1"
USE_STD3_RULES = "int  2"
CHECK_BIDI = "int  4"
CHECK_CONTEXTJ = "int  8"
NONTRANSITIONAL_TO_ASCII = "int  16"
NONTRANSITIONAL_TO_UNICODE = "int  32"
CHECK_CONTEXTO = "int  64"
def getUTS46Instance():
    '''    public static IDNA getUTS46Instance(final int options)
    '''
def convertToASCII():
    '''    public static StringBuffer convertToASCII(final String src, final int options)
    public static StringBuffer convertToASCII(final StringBuffer src, final int options)
    public static StringBuffer convertToASCII(final UCharacterIterator src, final int options)
    '''
def convertIDNToASCII():
    '''    public static StringBuffer convertIDNToASCII(final UCharacterIterator src, final int options)
    public static StringBuffer convertIDNToASCII(final StringBuffer src, final int options)
    public static StringBuffer convertIDNToASCII(final String src, final int options)
    '''
def convertToUnicode():
    '''    public static StringBuffer convertToUnicode(final String src, final int options)
    public static StringBuffer convertToUnicode(final StringBuffer src, final int options)
    public static StringBuffer convertToUnicode(final UCharacterIterator src, final int options)
    '''
def convertIDNToUnicode():
    '''    public static StringBuffer convertIDNToUnicode(final UCharacterIterator src, final int options)
    public static StringBuffer convertIDNToUnicode(final StringBuffer src, final int options)
    public static StringBuffer convertIDNToUnicode(final String src, final int options)
    '''
def compare():
    '''    public static int compare(final StringBuffer s1, final StringBuffer s2, final int options)
    public static int compare(final String s1, final String s2, final int options)
    public static int compare(final UCharacterIterator s1, final UCharacterIterator s2, final int options)
    '''
def Info():
    '''    public Info()
    '''
def hasErrors():
    '''    public boolean hasErrors()
    '''
def getErrors():
    '''    public Set<Error> getErrors()
    '''
def isTransitionalDifferent():
    '''    public boolean isTransitionalDifferent()
    '''
