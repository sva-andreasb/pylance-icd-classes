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
    '''returns Normalizer2Impl\n\n
    load(final InputStream data)\n
    load(final String name)\n
    '''
def addPropertyStarts():
    '''returns None\n\n
    addPropertyStarts(final UnicodeSet set)\n
    '''
def addCanonIterPropertyStarts():
    '''returns None\n\n
    addCanonIterPropertyStarts(final UnicodeSet set)\n
    '''
def getNormTrie():
    '''returns Trie2_16\n\n
    getNormTrie()\n
    '''
def getNorm16():
    '''returns int\n\n
    getNorm16(final int c)\n
    '''
def getCompQuickCheck():
    '''returns int\n\n
    getCompQuickCheck(final int norm16)\n
    '''
def isCompNo():
    '''returns boolean\n\n
    isCompNo(final int norm16)\n
    '''
def isDecompYes():
    '''returns boolean\n\n
    isDecompYes(final int norm16)\n
    '''
def getCC():
    '''returns int\n\n
    getCC(final int norm16)\n
    '''
def getFCD16():
    '''returns int\n\n
    getFCD16(final int c)\n
    '''
def getFCD16FromSingleLead():
    '''returns int\n\n
    getFCD16FromSingleLead(final char c)\n
    '''
def getDecomposition():
    '''returns String\n\n
    getDecomposition(int c)\n
    '''
def isCanonSegmentStarter():
    '''returns boolean\n\n
    isCanonSegmentStarter(final int c)\n
    '''
def getCanonStartSet():
    '''returns boolean\n\n
    getCanonStartSet(final int c, final UnicodeSet set)\n
    '''
def decompose():
    '''returns int\n\n
    decompose(final CharSequence s, int src, final int limit, final ReorderingBuffer buffer)\n
    '''
def decomposeAndAppend():
    '''returns None\n\n
    decomposeAndAppend(final CharSequence s, final boolean doDecompose, final ReorderingBuffer buffer)\n
    '''
def compose():
    '''returns boolean\n\n
    compose(final CharSequence s, int src, final int limit, final boolean onlyContiguous, final boolean doCompose, final ReorderingBuffer buffer)\n
    '''
def composeQuickCheck():
    '''returns int\n\n
    composeQuickCheck(final CharSequence s, int src, final int limit, final boolean onlyContiguous, final boolean doSpan)\n
    '''
def composeAndAppend():
    '''returns None\n\n
    composeAndAppend(final CharSequence s, final boolean doCompose, final boolean onlyContiguous, final ReorderingBuffer buffer)\n
    '''
def makeFCD():
    '''returns int\n\n
    makeFCD(final CharSequence s, int src, final int limit, final ReorderingBuffer buffer)\n
    '''
def makeFCDAndAppend():
    '''returns None\n\n
    makeFCDAndAppend(final CharSequence s, final boolean doMakeFCD, final ReorderingBuffer buffer)\n
    '''
def hasDecompBoundary():
    '''returns boolean\n\n
    hasDecompBoundary(int c, final boolean before)\n
    '''
def isDecompInert():
    '''returns boolean\n\n
    isDecompInert(final int c)\n
    '''
def hasCompBoundaryBefore():
    '''returns boolean\n\n
    hasCompBoundaryBefore(final int c)\n
    '''
def hasCompBoundaryAfter():
    '''returns boolean\n\n
    hasCompBoundaryAfter(int c, final boolean onlyContiguous, final boolean testInert)\n
    '''
def hasFCDBoundaryBefore():
    '''returns boolean\n\n
    hasFCDBoundaryBefore(final int c)\n
    '''
def hasFCDBoundaryAfter():
    '''returns boolean\n\n
    hasFCDBoundaryAfter(final int c)\n
    '''
def isFCDInert():
    '''returns boolean\n\n
    isFCDInert(final int c)\n
    '''
def decomposeShort():
    '''returns None\n\n
    decomposeShort(final CharSequence s, int src, final int limit, final ReorderingBuffer buffer)\n
    '''
def map():
    '''returns int\n\n
    map(final int in)\n
    '''
def ():
    '''returns ReorderingBuffer\n\n
    (final Normalizer2Impl ni, final Appendable dest, final int destCapacity)\n
    '''
def isEmpty():
    '''returns boolean\n\n
    isEmpty()\n
    '''
def length():
    '''returns int\n\n
    length()\n
    '''
def getLastCC():
    '''returns int\n\n
    getLastCC()\n
    '''
def getStringBuilder():
    '''returns StringBuilder\n\n
    getStringBuilder()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final CharSequence s, final int start, final int limit)\n
    '''
def setLastChar():
    '''returns None\n\n
    setLastChar(final char c)\n
    '''
def append():
    '''returns ReorderingBuffer\n\n
    append(final int c, final int cc)\n
    append(final CharSequence s, int start, final int limit, int leadCC, final int trailCC)\n
    append(final char c)\n
    append(final CharSequence s)\n
    append(final CharSequence s, final int start, final int limit)\n
    '''
def appendZeroCC():
    '''returns None\n\n
    appendZeroCC(final int c)\n
    '''
def flush():
    '''returns None\n\n
    flush()\n
    '''
def flushAndAppendZeroCC():
    '''returns ReorderingBuffer\n\n
    flushAndAppendZeroCC(final CharSequence s, final int start, final int limit)\n
    '''
def remove():
    '''returns None\n\n
    remove()\n
    '''
def removeSuffix():
    '''returns None\n\n
    removeSuffix(final int suffixLength)\n
    '''
def isDataVersionAcceptable():
    '''returns boolean\n\n
    isDataVersionAcceptable(final byte[] version)\n
    '''
def readHeader():
    '''returns VersionInfo\n\n
    readHeader(final InputStream data)\n
    '''
