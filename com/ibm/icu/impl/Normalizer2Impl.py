MIN_CCC_LCCC_CP = "int  768"
MIN_YES_YES_WITH_CC = "int  65281"
JAMO_VT = "int  65280"
MIN_NORMAL_MAYBE_YES = "int  65024"
JAMO_L = "int  1"
MAX_DELTA = "int  64"
IX_NORM_TRIE_OFFSET = "int  0"
IX_EXTRA_DATA_OFFSET = "int  1"
IX_RESERVED2_OFFSET = "int  2"
IX_TOTAL_SIZE = "int  7"
IX_MIN_DECOMP_NO_CP = "int  8"
IX_MIN_COMP_NO_MAYBE_CP = "int  9"
IX_MIN_YES_NO = "int  10"
IX_MIN_NO_NO = "int  11"
IX_LIMIT_NO_NO = "int  12"
IX_MIN_MAYBE_YES = "int  13"
IX_COUNT = "int  16"
MAPPING_HAS_CCC_LCCC_WORD = "int  128"
MAPPING_PLUS_COMPOSITION_LIST = "int  64"
MAPPING_NO_COMP_BOUNDARY_AFTER = "int  32"
MAPPING_LENGTH_MASK = "int  31"
COMP_1_LAST_TUPLE = "int  32768"
COMP_1_TRIPLE = "int  1"
COMP_1_TRAIL_LIMIT = "int  13312"
COMP_1_TRAIL_MASK = "int  32766"
COMP_1_TRAIL_SHIFT = "int  9"
COMP_2_TRAIL_SHIFT = "int  6"
COMP_2_TRAIL_MASK = "int  65472"
JAMO_L_BASE = "int  4352"
JAMO_V_BASE = "int  4449"
JAMO_T_BASE = "int  4519"
HANGUL_BASE = "int  44032"
JAMO_L_COUNT = "int  19"
JAMO_V_COUNT = "int  21"
JAMO_T_COUNT = "int  28"
JAMO_L_LIMIT = "int  4371"
JAMO_V_LIMIT = "int  4470"
JAMO_VT_COUNT = "int  588"
HANGUL_COUNT = "int  11172"
HANGUL_LIMIT = "int  55204"
def load():
'''public Normalizer2Impl load(final InputStream data)
public Normalizer2Impl load(final String name)
'''
pass
def addPropertyStarts():
'''public void addPropertyStarts(final UnicodeSet set)
'''
pass
def addCanonIterPropertyStarts():
'''public void addCanonIterPropertyStarts(final UnicodeSet set)
'''
pass
def getNormTrie():
'''public Trie2_16 getNormTrie()
'''
pass
def getFCDTrie():
'''public synchronized Trie2_16 getFCDTrie()
'''
pass
def ensureCanonIterData():
'''public synchronized Normalizer2Impl ensureCanonIterData()
'''
pass
def getNorm16():
'''public int getNorm16(final int c)
'''
pass
def getCompQuickCheck():
'''public int getCompQuickCheck(final int norm16)
'''
pass
def isCompNo():
'''public boolean isCompNo(final int norm16)
'''
pass
def isDecompYes():
'''public boolean isDecompYes(final int norm16)
'''
pass
def getCC():
'''public int getCC(final int norm16)
'''
pass
def getCCFromYesOrMaybe():
'''public static int getCCFromYesOrMaybe(final int norm16)
'''
pass
def getFCD16():
'''public int getFCD16(final int c)
'''
pass
def getFCD16FromSingleLead():
'''public int getFCD16FromSingleLead(final char c)
'''
pass
def getDecomposition():
'''public String getDecomposition(int c)
'''
pass
def isCanonSegmentStarter():
'''public boolean isCanonSegmentStarter(final int c)
'''
pass
def getCanonStartSet():
'''public boolean getCanonStartSet(final int c, final UnicodeSet set)
'''
pass
def decompose():
'''public int decompose(final CharSequence s, int src, final int limit, final ReorderingBuffer buffer)
public static int decompose(int c, final Appendable buffer)
'''
pass
def decomposeAndAppend():
'''public void decomposeAndAppend(final CharSequence s, final boolean doDecompose, final ReorderingBuffer buffer)
'''
pass
def compose():
'''public boolean compose(final CharSequence s, int src, final int limit, final boolean onlyContiguous, final boolean doCompose, final ReorderingBuffer buffer)
'''
pass
def composeQuickCheck():
'''public int composeQuickCheck(final CharSequence s, int src, final int limit, final boolean onlyContiguous, final boolean doSpan)
'''
pass
def composeAndAppend():
'''public void composeAndAppend(final CharSequence s, final boolean doCompose, final boolean onlyContiguous, final ReorderingBuffer buffer)
'''
pass
def makeFCD():
'''public int makeFCD(final CharSequence s, int src, final int limit, final ReorderingBuffer buffer)
'''
pass
def makeFCDAndAppend():
'''public void makeFCDAndAppend(final CharSequence s, final boolean doMakeFCD, final ReorderingBuffer buffer)
'''
pass
def hasDecompBoundary():
'''public boolean hasDecompBoundary(int c, final boolean before)
'''
pass
def isDecompInert():
'''public boolean isDecompInert(final int c)
'''
pass
def hasCompBoundaryBefore():
'''public boolean hasCompBoundaryBefore(final int c)
'''
pass
def hasCompBoundaryAfter():
'''public boolean hasCompBoundaryAfter(int c, final boolean onlyContiguous, final boolean testInert)
'''
pass
def hasFCDBoundaryBefore():
'''public boolean hasFCDBoundaryBefore(final int c)
'''
pass
def hasFCDBoundaryAfter():
'''public boolean hasFCDBoundaryAfter(final int c)
'''
pass
def isFCDInert():
'''public boolean isFCDInert(final int c)
'''
pass
def decomposeShort():
'''public void decomposeShort(final CharSequence s, int src, final int limit, final ReorderingBuffer buffer)
'''
pass
def map():
'''public int map(final int in)
'''
pass
def isHangul():
'''public static boolean isHangul(final int c)
'''
pass
def isHangulWithoutJamoT():
'''public static boolean isHangulWithoutJamoT(char c)
'''
pass
def isJamoL():
'''public static boolean isJamoL(final int c)
'''
pass
def isJamoV():
'''public static boolean isJamoV(final int c)
'''
pass
def ReorderingBuffer():
'''public ReorderingBuffer(final Normalizer2Impl ni, final Appendable dest, final int destCapacity)
'''
pass
def isEmpty():
'''public boolean isEmpty()
'''
pass
def length():
'''public int length()
'''
pass
def getLastCC():
'''public int getLastCC()
'''
pass
def getStringBuilder():
'''public StringBuilder getStringBuilder()
'''
pass
def equals():
'''public boolean equals(final CharSequence s, final int start, final int limit)
'''
pass
def setLastChar():
'''public void setLastChar(final char c)
'''
pass
def append():
'''public void append(final int c, final int cc)
public void append(final CharSequence s, int start, final int limit, int leadCC, final int trailCC)
public ReorderingBuffer append(final char c)
public ReorderingBuffer append(final CharSequence s)
public ReorderingBuffer append(final CharSequence s, final int start, final int limit)
'''
pass
def appendZeroCC():
'''public void appendZeroCC(final int c)
'''
pass
def flush():
'''public void flush()
'''
pass
def flushAndAppendZeroCC():
'''public ReorderingBuffer flushAndAppendZeroCC(final CharSequence s, final int start, final int limit)
'''
pass
def remove():
'''public void remove()
'''
pass
def removeSuffix():
'''public void removeSuffix(final int suffixLength)
'''
pass
def isSurrogateLead():
'''public static boolean isSurrogateLead(final int c)
'''
pass
def equal():
'''public static boolean equal(final CharSequence s1, final CharSequence s2)
public static boolean equal(final CharSequence s1, int start1, final int limit1, final CharSequence s2, int start2, final int limit2)
'''
pass
def isDataVersionAcceptable():
'''public boolean isDataVersionAcceptable(final byte[] version)
'''
pass
def readHeader():
'''public VersionInfo readHeader(final InputStream data)
'''
pass