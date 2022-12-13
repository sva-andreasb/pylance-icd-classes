def create():
'''public static DatasetPrefixesTDB create(final Location location)
public static DatasetPrefixesTDB create(final IndexBuilder indexBuilder, final Location location)
'''
pass
def DatasetPrefixesTDB():
'''public DatasetPrefixesTDB(final TupleIndex[] indexes, final NodeTable nodes)
'''
pass
def testing():
'''public static DatasetPrefixesTDB testing()
'''
pass
def insertPrefix():
'''public synchronized void insertPrefix(final String graphName, final String prefix, final String uri)
'''
pass
def graphNames():
'''public Set<String> graphNames()
'''
pass
def readPrefix():
'''public synchronized String readPrefix(final String graphName, final String prefix)
'''
pass
def readByURI():
'''public synchronized String readByURI(final String graphName, final String uriStr)
'''
pass
def readPrefixMap():
'''public synchronized Map<String, String> readPrefixMap(final String graphName)
'''
pass
def loadPrefixMapping():
'''public synchronized void loadPrefixMapping(final String graphName, final PrefixMapping pmap)
'''
pass
def removeFromPrefixMap():
'''public synchronized void removeFromPrefixMap(final String graphName, final String prefix, final String uri)
'''
pass
def getNodeTupleTable():
'''public NodeTupleTable getNodeTupleTable()
'''
pass
def getPrefixMapping():
'''public PrefixMapping getPrefixMapping()
public PrefixMapping getPrefixMapping(final String graphName)
'''
pass
def close():
'''public void close()
'''
pass
def sync():
'''public void sync()
public void sync(final boolean force)
'''
pass
