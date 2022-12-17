def ():
    '''returns TupleChange\n\n
    (final SDBConnection connection, final Class<? extends TupleLoader> tupleLoaderClass)\n
    (final boolean toAdd, final TableDesc table, final Node... tuple)\n
    ()\n
    '''
def setStore():
    '''returns None\n\n
    setStore(final Store store)\n
    '''
def startBulkUpdate():
    '''returns None\n\n
    startBulkUpdate()\n
    '''
def finishBulkUpdate():
    '''returns None\n\n
    finishBulkUpdate()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def addTriple():
    '''returns None\n\n
    addTriple(final Triple triple)\n
    '''
def deleteTriple():
    '''returns None\n\n
    deleteTriple(final Triple triple)\n
    '''
def addQuad():
    '''returns None\n\n
    addQuad(final Node g, final Node s, final Node p, final Node o)\n
    '''
def addTuple():
    '''returns None\n\n
    addTuple(final TableDesc t, final Node... nodes)\n
    '''
def deleteQuad():
    '''returns None\n\n
    deleteQuad(final Node g, final Node s, final Node p, final Node o)\n
    '''
def deleteTuple():
    '''returns None\n\n
    deleteTuple(final TableDesc t, final Node... nodes)\n
    '''
def deleteAll():
    '''returns None\n\n
    deleteAll()\n
    deleteAll(final Node graph)\n
    '''
def setChunkSize():
    '''returns None\n\n
    setChunkSize(final int chunkSize)\n
    '''
def getChunkSize():
    '''returns int\n\n
    getChunkSize()\n
    '''
def setUseThreading():
    '''returns None\n\n
    setUseThreading(final boolean useThreading)\n
    '''
def getUseThreading():
    '''returns boolean\n\n
    getUseThreading()\n
    '''
def run():
    '''returns None\n\n
    run()\n
    '''
