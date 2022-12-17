def ():
    '''returns TupleLoaderBase\n\n
    (final SDBConnection connection, final TableDesc tableDesc, final int chunkSize)\n
    '''
def getArity():
    '''returns int\n\n
    getArity()\n
    '''
def load():
    '''returns None\n\n
    load(final Node... row)\n
    '''
def unload():
    '''returns None\n\n
    unload(final Node... row)\n
    '''
def finish():
    '''returns None\n\n
    finish()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def getNodeLoader():
    '''returns String\n\n
    getNodeLoader()\n
    '''
def getTupleLoader():
    '''returns String\n\n
    getTupleLoader()\n
    '''
def getCreateTempNodes():
    '''returns String\n\n
    getCreateTempNodes()\n
    '''
def getCreateTempTuples():
    '''returns String\n\n
    getCreateTempTuples()\n
    '''
def getInsertTempNodes():
    '''returns String\n\n
    getInsertTempNodes()\n
    '''
def getInsertTempTuples():
    '''returns String\n\n
    getInsertTempTuples()\n
    '''
def getLoadNodes():
    '''returns String\n\n
    getLoadNodes()\n
    '''
def getClearTempNodes():
    '''returns String\n\n
    getClearTempNodes()\n
    '''
def getClearTempTuples():
    '''returns String\n\n
    getClearTempTuples()\n
    '''
def clearsOnCommit():
    '''returns boolean\n\n
    clearsOnCommit()\n
    '''
def addToStatement():
    '''returns None\n\n
    addToStatement(final PreparedStatement s)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object other)\n
    '''
