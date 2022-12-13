def create():
    '''public static DatasetPrefixesTDB create(final Location location)
    public static DatasetPrefixesTDB create(final IndexBuilder indexBuilder, final Location location)
    '''
def DatasetPrefixesTDB():
    '''public DatasetPrefixesTDB(final TupleIndex[] indexes, final NodeTable nodes)
    '''
def testing():
    '''public static DatasetPrefixesTDB testing()
    '''
def insertPrefix():
    '''public synchronized void insertPrefix(final String graphName, final String prefix, final String uri)
    '''
def graphNames():
    '''public Set<String> graphNames()
    '''
def readPrefix():
    '''public synchronized String readPrefix(final String graphName, final String prefix)
    '''
def readByURI():
    '''public synchronized String readByURI(final String graphName, final String uriStr)
    '''
def readPrefixMap():
    '''public synchronized Map<String, String> readPrefixMap(final String graphName)
    '''
def loadPrefixMapping():
    '''public synchronized void loadPrefixMapping(final String graphName, final PrefixMapping pmap)
    '''
def removeFromPrefixMap():
    '''public synchronized void removeFromPrefixMap(final String graphName, final String prefix, final String uri)
    '''
def getNodeTupleTable():
    '''public NodeTupleTable getNodeTupleTable()
    '''
def getPrefixMapping():
    '''public PrefixMapping getPrefixMapping()
    public PrefixMapping getPrefixMapping(final String graphName)
    '''
def close():
    '''public void close()
    '''
def sync():
    '''public void sync()
    public void sync(final boolean force)
    '''
