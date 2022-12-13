NodeTableType = "String  dat""
NodeTableLayout = "String  1""
def buildDataset():
'''public static DatasetGraphTDB buildDataset(final Location location)
'''
pass
def makeTripleTable():
'''public static TripleTable makeTripleTable(final Location location, final Properties config, final NodeTable nodeTable, final String dftPrimary, final String[] dftIndexes)
'''
pass
def makeQuadTable():
'''public static QuadTable makeQuadTable(final Location location, final Properties config, final NodeTable nodeTable, final String dftPrimary, final String[] dftIndexes)
'''
pass
def makePrefixes():
'''public static DatasetPrefixStorage makePrefixes(final Location location, final Properties config)
'''
pass
def makeTupleIndexes():
'''public static TupleIndex[] makeTupleIndexes(final Location location, final Properties config, final String primary, final String[] descs, final String[] filenames)
'''
pass
def makeTupleIndex():
'''public static TupleIndex makeTupleIndex(final Location location, final Properties config, final String primary, final String indexOrder, final String indexName, final int keyLength)
'''
pass
def makeIndex():
'''public static Index makeIndex(final Location location, final String indexName, final int dftKeyLength, final int dftValueLength, final int readCacheSize, final int writeCacheSize)
'''
pass
def makeRangeIndex():
'''public static RangeIndex makeRangeIndex(final Location location, final String indexName, final int dftKeyLength, final int dftValueLength, final int readCacheSize, final int writeCacheSize)
'''
pass
def makeBPlusTree():
'''public static RangeIndex makeBPlusTree(final FileSet fs, final int readCacheSize, final int writeCacheSize, final int dftKeyLength, final int dftValueLength)
'''
pass
def makeRecordFactory():
'''public static RecordFactory makeRecordFactory(final MetaFile metafile, final String keyName, final int keyLenDft, final int valLenDft)
'''
pass
def makeNodeTableBase():
'''public static NodeTable makeNodeTableBase(final Location location, final String indexNode2Id, final String indexId2Node)
'''
pass
def makeNodeTable():
'''public static NodeTable makeNodeTable(final Location location, final String indexNode2Id, final int nodeToIdCacheSize, final String indexId2Node, final int idToNodeCacheSize)
'''
pass
def makeObjectFile():
'''public static ObjectFile makeObjectFile(final FileSet fsIdToNode)
'''
pass
def locationMetadata():
'''public static MetaFile locationMetadata(final Location location)
'''
pass
def createBPTree():
'''public static RangeIndex createBPTree(final FileSet fileset, int order, int blockSize, final int readCacheSize, final int writeCacheSize, final RecordFactory factory)
'''
pass
def setOptimizerWarningFlag():
'''public static void setOptimizerWarningFlag(final boolean b)
'''
pass
def chooseOptimizer():
'''public static ReorderTransformation chooseOptimizer(final Location location)
'''
pass
def error():
'''public static void error(final Logger log, final String msg)
'''
pass
def parseInt():
'''public static int parseInt(final String str, final String messageBase)
'''
pass
def getSyncTick():
'''public int getSyncTick()
'''
pass
def getSegmentSize():
'''public int getSegmentSize()
'''
pass
def getNodeId2NodeCacheSize():
'''public int getNodeId2NodeCacheSize()
'''
pass
def getNode2NodeIdCacheSize():
'''public int getNode2NodeIdCacheSize()
'''
pass
def getBlockWriteCacheSize():
'''public int getBlockWriteCacheSize()
'''
pass
def getBlockSize():
'''public int getBlockSize()
'''
pass
def getBlockReadCacheSize():
'''public int getBlockReadCacheSize()
'''
pass
