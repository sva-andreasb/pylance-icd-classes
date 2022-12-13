END_OF_SUBTAG = "int 128"
DISTANCE_SKIP_SCRIPT = "int 128"
IX_DEF_LANG_DISTANCE = "int 0"
IX_DEF_SCRIPT_DISTANCE = "int 1"
IX_DEF_REGION_DISTANCE = "int 2"
IX_MIN_REGION_DISTANCE = "int 3"
IX_LIMIT = "int 4"
def shiftDistance():
'''public static final int shiftDistance(final int distance)
'''
pass
def getShiftedDistance():
'''public static final int getShiftedDistance(final int indexAndDistance)
'''
pass
def getDistanceDouble():
'''public static final double getDistanceDouble(final int indexAndDistance)
'''
pass
def getIndex():
'''public static final int getIndex(final int indexAndDistance)
'''
pass
def testOnlyDistance():
'''public int testOnlyDistance(final ULocale desired, final ULocale supported, final int threshold, final LocaleMatcher.FavorSubtag favorSubtag)
'''
pass
def getBestIndexAndDistance():
'''public int getBestIndexAndDistance(final LSR desired, final LSR[] supportedLSRs, final int supportedLSRsLength, int shiftedThreshold, final LocaleMatcher.FavorSubtag favorSubtag, final LocaleMatcher.Direction direction)
'''
pass
def toString():
'''public String toString()
'''
pass
def isParadigmLSR():
'''public boolean isParadigmLSR(final LSR lsr)
'''
pass
def getDefaultScriptDistance():
'''public int getDefaultScriptDistance()
'''
pass
def getDefaultDemotionPerDesiredLocale():
'''public int getDefaultDemotionPerDesiredLocale()
'''
pass
def testOnlyGetDistanceTable():
'''public Map<String, Integer> testOnlyGetDistanceTable()
'''
pass
def testOnlyPrintDistanceTable():
'''public void testOnlyPrintDistanceTable()
'''
pass
def Data():
'''public Data(final byte[] trie, final byte[] regionToPartitionsIndex, final String[] partitionArrays, final Set<LSR> paradigmLSRs, final int[] distances)
'''
pass
def load():
'''public static Data load()
'''
pass
def equals():
'''public boolean equals(final Object other)
'''
pass
def hashCode():
'''public int hashCode()
'''
pass
