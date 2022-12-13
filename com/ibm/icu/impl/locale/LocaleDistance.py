END_OF_SUBTAG = "int  128"
DISTANCE_SKIP_SCRIPT = "int  128"
IX_DEF_LANG_DISTANCE = "int  0"
IX_DEF_SCRIPT_DISTANCE = "int  1"
IX_DEF_REGION_DISTANCE = "int  2"
IX_MIN_REGION_DISTANCE = "int  3"
IX_LIMIT = "int  4"
def shiftDistance():
    '''    public static final int shiftDistance(final int distance)
    '''
def getShiftedDistance():
    '''    public static final int getShiftedDistance(final int indexAndDistance)
    '''
def getDistanceDouble():
    '''    public static final double getDistanceDouble(final int indexAndDistance)
    '''
def getIndex():
    '''    public static final int getIndex(final int indexAndDistance)
    '''
def testOnlyDistance():
    '''    public int testOnlyDistance(final ULocale desired, final ULocale supported, final int threshold, final LocaleMatcher.FavorSubtag favorSubtag)
    '''
def getBestIndexAndDistance():
    '''    public int getBestIndexAndDistance(final LSR desired, final LSR[] supportedLSRs, final int supportedLSRsLength, int shiftedThreshold, final LocaleMatcher.FavorSubtag favorSubtag, final LocaleMatcher.Direction direction)
    '''
def toString():
    '''    public String toString()
    '''
def isParadigmLSR():
    '''    public boolean isParadigmLSR(final LSR lsr)
    '''
def getDefaultScriptDistance():
    '''    public int getDefaultScriptDistance()
    '''
def getDefaultDemotionPerDesiredLocale():
    '''    public int getDefaultDemotionPerDesiredLocale()
    '''
def testOnlyGetDistanceTable():
    '''    public Map<String, Integer> testOnlyGetDistanceTable()
    '''
def testOnlyPrintDistanceTable():
    '''    public void testOnlyPrintDistanceTable()
    '''
def Data():
    '''    public Data(final byte[] trie, final byte[] regionToPartitionsIndex, final String[] partitionArrays, final Set<LSR> paradigmLSRs, final int[] distances)
    '''
def load():
    '''    public static Data load()
    '''
def equals():
    '''    public boolean equals(final Object other)
    '''
def hashCode():
    '''    public int hashCode()
    '''
