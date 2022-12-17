def ():
    '''returns BTree\n\n
    (final BTreeParams bTreeParams, final BlockMgr blkMgr)\n
    '''
def getRecordFactory():
    '''returns RecordFactory\n\n
    getRecordFactory()\n
    '''
def find():
    '''returns Record\n\n
    find(final Record record)\n
    '''
def contains():
    '''returns boolean\n\n
    contains(final Record record)\n
    '''
def minKey():
    '''returns Record\n\n
    minKey()\n
    '''
def maxKey():
    '''returns Record\n\n
    maxKey()\n
    '''
def add():
    '''returns boolean\n\n
    add(final Record record)\n
    '''
def addAndReturnOld():
    '''returns Record\n\n
    addAndReturnOld(final Record record)\n
    '''
def delete():
    '''returns boolean\n\n
    delete(final Record record)\n
    '''
def deleteAndReturnOld():
    '''returns Record\n\n
    deleteAndReturnOld(final Record record)\n
    '''
def iterator():
    '''returns Iterator<Record>\n\n
    iterator()\n
    iterator(final Record fromRec, final Record toRec)\n
    '''
def isEmpty():
    '''returns boolean\n\n
    isEmpty()\n
    '''
def clear():
    '''returns None\n\n
    clear()\n
    '''
def sync():
    '''returns None\n\n
    sync()\n
    sync(final boolean force)\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def startRead():
    '''returns None\n\n
    startRead()\n
    '''
def finishRead():
    '''returns None\n\n
    finishRead()\n
    '''
def startUpdate():
    '''returns None\n\n
    startUpdate()\n
    '''
def finishUpdate():
    '''returns None\n\n
    finishUpdate()\n
    '''
def size():
    '''returns long\n\n
    size()\n
    '''
def sessionTripleCount():
    '''returns long\n\n
    sessionTripleCount()\n
    '''
def sizeByCounting():
    '''returns long\n\n
    sizeByCounting()\n
    '''
def check():
    '''returns None\n\n
    check()\n
    '''
def dump():
    '''returns None\n\n
    dump()\n
    '''
