NodeTableType = "String  \"dat\""
NodeTableLayout = "String  \"1\""
def buildDataset():
    '''    public static DatasetGraphTDB buildDataset(final Location location)
    '''
def makeTripleTable():
    '''    public static TripleTable makeTripleTable(final Location location, final Properties config, final NodeTable nodeTable, final String dftPrimary, final String[] dftIndexes)
    '''
def makeQuadTable():
    '''    public static QuadTable makeQuadTable(final Location location, final Properties config, final NodeTable nodeTable, final String dftPrimary, final String[] dftIndexes)
    '''
def makePrefixes():
    '''    public static DatasetPrefixStorage makePrefixes(final Location location, final Properties config)
    '''
def makeTupleIndexes():
    '''    public static TupleIndex[] makeTupleIndexes(final Location location, final Properties config, final String primary, final String[] descs, final String[] filenames)
    '''
def makeTupleIndex():
    '''    public static TupleIndex makeTupleIndex(final Location location, final Properties config, final String primary, final String indexOrder, final String indexName, final int keyLength)
    '''
def makeIndex():
    '''    public static Index makeIndex(final Location location, final String indexName, final int dftKeyLength, final int dftValueLength, final int readCacheSize, final int writeCacheSize)
    '''
def makeRangeIndex():
    '''    public static RangeIndex makeRangeIndex(final Location location, final String indexName, final int dftKeyLength, final int dftValueLength, final int readCacheSize, final int writeCacheSize)
    '''
def makeBPlusTree():
    '''    public static RangeIndex makeBPlusTree(final FileSet fs, final int readCacheSize, final int writeCacheSize, final int dftKeyLength, final int dftValueLength)
    '''
def makeRecordFactory():
    '''    public static RecordFactory makeRecordFactory(final MetaFile metafile, final String keyName, final int keyLenDft, final int valLenDft)
    '''
def makeNodeTableBase():
    '''    public static NodeTable makeNodeTableBase(final Location location, final String indexNode2Id, final String indexId2Node)
    '''
def makeNodeTable():
    '''    public static NodeTable makeNodeTable(final Location location, final String indexNode2Id, final int nodeToIdCacheSize, final String indexId2Node, final int idToNodeCacheSize)
    '''
def makeObjectFile():
    '''    public static ObjectFile makeObjectFile(final FileSet fsIdToNode)
    '''
def locationMetadata():
    '''    public static MetaFile locationMetadata(final Location location)
    '''
def createBPTree():
    '''    public static RangeIndex createBPTree(final FileSet fileset, int order, int blockSize, final int readCacheSize, final int writeCacheSize, final RecordFactory factory)
    '''
def setOptimizerWarningFlag():
    '''    public static void setOptimizerWarningFlag(final boolean b)
    '''
def chooseOptimizer():
    '''    public static ReorderTransformation chooseOptimizer(final Location location)
    '''
def error():
    '''    public static void error(final Logger log, final String msg)
    '''
def parseInt():
    '''    public static int parseInt(final String str, final String messageBase)
    '''
def getSyncTick():
    '''    public int getSyncTick()
    '''
def getSegmentSize():
    '''    public int getSegmentSize()
    '''
def getNodeId2NodeCacheSize():
    '''    public int getNodeId2NodeCacheSize()
    '''
def getNode2NodeIdCacheSize():
    '''    public int getNode2NodeIdCacheSize()
    '''
def getBlockWriteCacheSize():
    '''    public int getBlockWriteCacheSize()
    '''
def getBlockSize():
    '''    public int getBlockSize()
    '''
def getBlockReadCacheSize():
    '''    public int getBlockReadCacheSize()
    '''
