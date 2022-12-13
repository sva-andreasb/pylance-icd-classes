LATIN_CAPITAL_LETTER_I_WITH_DOT_ABOVE_ = "char  '\u0130'"
LATIN_SMALL_LETTER_DOTLESS_I_ = "char  '\u0131'"
LATIN_SMALL_LETTER_I_ = "char  'i'"
TYPE_MASK = "int  31"
SRC_NONE = "int  0"
SRC_CHAR = "int  1"
SRC_PROPSVEC = "int  2"
SRC_NAMES = "int  3"
SRC_CASE = "int  4"
SRC_BIDI = "int  5"
SRC_CHAR_AND_PROPSVEC = "int  6"
SRC_CASE_AND_NORM = "int  7"
SRC_NFC = "int  8"
SRC_NFKC = "int  9"
SRC_NFKC_CF = "int  10"
SRC_NFC_CANON_ITER = "int  11"
SRC_COUNT = "int  12"
def setIndexData():
'''public void setIndexData(final CharTrie.FriendAgent friendagent)
'''
pass
def getProperty():
'''public final int getProperty(final int ch)
'''
pass
def getAdditional():
'''public int getAdditional(final int codepoint, final int column)
'''
pass
def getAge():
'''public VersionInfo getAge(final int codepoint)
'''
pass
def hasBinaryProperty():
'''public boolean hasBinaryProperty(int c, final int which)
'''
pass
def getSource():
'''public final int getSource(final int which)
'''
pass
def getRawSupplementary():
'''public static int getRawSupplementary(final char lead, final char trail)
'''
pass
def isRuleWhiteSpace():
'''public static boolean isRuleWhiteSpace(final int c)
'''
pass
def getMaxValues():
'''public int getMaxValues(final int column)
'''
pass
def getMask():
'''public static final int getMask(final int type)
'''
pass
def addPropertyStarts():
'''public UnicodeSet addPropertyStarts(final UnicodeSet set)
'''
pass
def upropsvec_addPropertyStarts():
'''public void upropsvec_addPropertyStarts(final UnicodeSet set)
'''
pass
def BinaryProperties():
'''public BinaryProperties(final int column, final int mask)
'''
pass
