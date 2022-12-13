QC_NFC = "int  17"
QC_NFKC = "int  34"
QC_NFD = "int  4"
QC_NFKD = "int  8"
QC_ANY_NO = "int  15"
QC_MAYBE = "int  16"
QC_ANY_MAYBE = "int  48"
QC_MASK = "int  63"
COMBINES_ANY = "int  192"
CC_MASK = "int  65280"
INDEX_MIN_NFC_NO_MAYBE = "int  6"
INDEX_MIN_NFKC_NO_MAYBE = "int  7"
INDEX_MIN_NFD_NO_MAYBE = "int  8"
INDEX_MIN_NFKD_NO_MAYBE = "int  9"
COMPARE_EQUIV = "int  524288"
MIN_WITH_LEAD_CC = "int  768"
JAMO_L_BASE = "int  4352"
JAMO_V_BASE = "int  4449"
JAMO_T_BASE = "int  4519"
HANGUL_BASE = "int  44032"
JAMO_L_COUNT = "int  19"
JAMO_V_COUNT = "int  21"
JAMO_T_COUNT = "int  28"
HANGUL_COUNT = "int  11172"
OPTIONS_SETS_MASK = "int  255"
BEFORE_PRI_29 = "int  256"
OPTIONS_COMPAT = "int  4096"
OPTIONS_COMPOSE_CONTIGUOUS = "int  8192"
def getFromIndexesArr():
    '''public static int getFromIndexesArr(final int index)
    '''
def getNorm32():
    '''public static long getNorm32(final char c)
    '''
def getNorm32FromSurrogatePair():
    '''public static long getNorm32FromSurrogatePair(final long norm32, final char c2)
    '''
def getUnicodeVersion():
    '''public static VersionInfo getUnicodeVersion()
    '''
def getFCD16():
    '''public static char getFCD16(final char c)
    public static int getFCD16(final int c)
    '''
def getFCD16FromSurrogatePair():
    '''public static char getFCD16FromSurrogatePair(final char fcd16, final char c2)
    '''
def isNFDSafe():
    '''public static boolean isNFDSafe(final long norm32, final int ccOrQCMask, final int decompQCMask)
    '''
def isTrueStarter():
    '''public static boolean isTrueStarter(final long norm32, final int ccOrQCMask, final int decompQCMask)
    '''
def checkFCD():
    '''public static boolean checkFCD(final char[] src, final int srcStart, final int srcLimit, final UnicodeSet nx)
    '''
def getDecomposition():
    '''public static int getDecomposition(int c, final boolean compat, final char[] dest, int destStart, final int destCapacity)
    '''
def decompose():
    '''public static int decompose(final char[] src, final int srcStart, final int srcLimit, final char[] dest, final int destStart, final int destLimit, final boolean compat, final int[] outTrailCC, final UnicodeSet nx)
    '''
def compose():
    '''public static int compose(final char[] src, final int srcStart, final int srcLimit, final char[] dest, final int destStart, final int destLimit, final int options, final UnicodeSet nx)
    '''
def makeFCD():
    '''public static int makeFCD(final char[] src, int srcStart, final int srcLimit, final char[] dest, final int destStart, final int destLimit, final UnicodeSet nx)
    '''
def getCombiningClass():
    '''public static int getCombiningClass(final int c)
    '''
def isFullCompositionExclusion():
    '''public static boolean isFullCompositionExclusion(final int c)
    '''
def isCanonSafeStart():
    '''public static boolean isCanonSafeStart(final int c)
    '''
def getCanonStartSet():
    '''public static boolean getCanonStartSet(final int c, final USerializedSet fillSet)
    '''
def getFC_NFKC_Closure():
    '''public static int getFC_NFKC_Closure(final int c, final char[] dest)
    '''
def isNFSkippable():
    '''public static boolean isNFSkippable(final int c, final Normalizer.Mode mode, long mask)
    '''
def addPropertyStarts():
    '''public static UnicodeSet addPropertyStarts(final UnicodeSet set)
    '''
def quickCheck():
    '''public static final int quickCheck(final int c, final int modeValue)
    '''
def getFCDTrie():
    '''public CharTrie getFCDTrie()
    '''
def cmpEquivFold():
    '''public static int cmpEquivFold(final String s1, final String s2, final int options)
    public static int cmpEquivFold(final char[] s1, int s1Start, final int s1Limit, final char[] s2, int s2Start, final int s2Limit, final int options)
    '''
def getNX():
    '''public static final UnicodeSet getNX(int options)
    '''
def getFoldingOffset():
    '''public int getFoldingOffset(final int value)
    public int getFoldingOffset(final int value)
    public int getFoldingOffset(final int value)
    '''
