END_OF_SUBTAG = "int  128"
DISTANCE_SKIP_SCRIPT = "int  128"
IX_DEF_LANG_DISTANCE = "int  0"
IX_DEF_SCRIPT_DISTANCE = "int  1"
IX_DEF_REGION_DISTANCE = "int  2"
IX_MIN_REGION_DISTANCE = "int  3"
IX_LIMIT = "int  4"
def testOnlyDistance():
    '''returns int\n\n
    testOnlyDistance(final ULocale desired, final ULocale supported, final int threshold, final LocaleMatcher.FavorSubtag favorSubtag)\n
    '''
def getBestIndexAndDistance():
    '''returns int\n\n
    getBestIndexAndDistance(final LSR desired, final LSR[] supportedLSRs, final int supportedLSRsLength, int shiftedThreshold, final LocaleMatcher.FavorSubtag favorSubtag, final LocaleMatcher.Direction direction)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def isParadigmLSR():
    '''returns boolean\n\n
    isParadigmLSR(final LSR lsr)\n
    '''
def getDefaultScriptDistance():
    '''returns int\n\n
    getDefaultScriptDistance()\n
    '''
def getDefaultDemotionPerDesiredLocale():
    '''returns int\n\n
    getDefaultDemotionPerDesiredLocale()\n
    '''
def testOnlyPrintDistanceTable():
    '''returns None\n\n
    testOnlyPrintDistanceTable()\n
    '''
def ():
    '''returns Data\n\n
    (final byte[] trie, final byte[] regionToPartitionsIndex, final String[] partitionArrays, final Set<LSR> paradigmLSRs, final int[] distances)\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object other)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
