MASK_VALID = "int  1"
MASK_SPACE = "int  2"
MASK_NAME_START = "int  4"
MASK_NAME = "int  8"
MASK_PUBID = "int  16"
MASK_CONTENT = "int  32"
MASK_NCNAME_START = "int  64"
MASK_NCNAME = "int  128"
def isSupplemental():
    '''    public static boolean isSupplemental(final int c)
    '''
def supplemental():
    '''    public static int supplemental(final char h, final char l)
    '''
def highSurrogate():
    '''    public static char highSurrogate(final int c)
    '''
def lowSurrogate():
    '''    public static char lowSurrogate(final int c)
    '''
def isHighSurrogate():
    '''    public static boolean isHighSurrogate(final int c)
    '''
def isLowSurrogate():
    '''    public static boolean isLowSurrogate(final int c)
    '''
def isValid():
    '''    public static boolean isValid(final int c)
    '''
def isInvalid():
    '''    public static boolean isInvalid(final int c)
    '''
def isContent():
    '''    public static boolean isContent(final int c)
    '''
def isMarkup():
    '''    public static boolean isMarkup(final int c)
    '''
def isSpace():
    '''    public static boolean isSpace(final int c)
    '''
def isNameStart():
    '''    public static boolean isNameStart(final int c)
    '''
def isName():
    '''    public static boolean isName(final int c)
    '''
def isNCNameStart():
    '''    public static boolean isNCNameStart(final int c)
    '''
def isNCName():
    '''    public static boolean isNCName(final int c)
    '''
def isPubid():
    '''    public static boolean isPubid(final int c)
    '''
def isValidName():
    '''    public static boolean isValidName(final String name)
    '''
def isValidNCName():
    '''    public static boolean isValidNCName(final String ncName)
    '''
def isValidNmtoken():
    '''    public static boolean isValidNmtoken(final String nmtoken)
    '''
def isValidIANAEncoding():
    '''    public static boolean isValidIANAEncoding(final String ianaEncoding)
    '''
def isValidJavaEncoding():
    '''    public static boolean isValidJavaEncoding(final String javaEncoding)
    '''
