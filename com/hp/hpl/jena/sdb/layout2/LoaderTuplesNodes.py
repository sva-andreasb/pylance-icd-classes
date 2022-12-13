def LoaderTuplesNodes():
    '''public LoaderTuplesNodes(final SDBConnection connection, final Class<? extends TupleLoader> tupleLoaderClass)
    '''
def setStore():
    '''public void setStore(final Store store)
    '''
def startBulkUpdate():
    '''public void startBulkUpdate()
    '''
def finishBulkUpdate():
    '''public void finishBulkUpdate()
    '''
def close():
    '''public void close()
    '''
def addTriple():
    '''public void addTriple(final Triple triple)
    '''
def deleteTriple():
    '''public void deleteTriple(final Triple triple)
    '''
def addQuad():
    '''public void addQuad(final Node g, final Node s, final Node p, final Node o)
    '''
def addTuple():
    '''public void addTuple(final TableDesc t, final Node... nodes)
    '''
def deleteQuad():
    '''public void deleteQuad(final Node g, final Node s, final Node p, final Node o)
    '''
def deleteTuple():
    '''public void deleteTuple(final TableDesc t, final Node... nodes)
    '''
def deleteAll():
    '''public void deleteAll()
    public void deleteAll(final Node graph)
    '''
def setChunkSize():
    '''public void setChunkSize(final int chunkSize)
    '''
def getChunkSize():
    '''public int getChunkSize()
    '''
def setUseThreading():
    '''public void setUseThreading(final boolean useThreading)
    '''
def getUseThreading():
    '''public boolean getUseThreading()
    '''
def TupleChange():
    '''public TupleChange(final boolean toAdd, final TableDesc table, final Node... tuple)
    public TupleChange()
    '''
def run():
    '''public void run()
    '''
