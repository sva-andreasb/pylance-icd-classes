def BlockMgrWeakRefCache():
    '''public BlockMgrWeakRefCache(final String indexName, final int readSlots, final int writeSlots, final BlockMgr blockMgr)
    '''
def get():
    '''public synchronized ByteBuffer get(final int id)
    '''
def put():
    '''public synchronized void put(final int id, final ByteBuffer block)
    '''
def freeBlock():
    '''public synchronized void freeBlock(final int id)
    '''
def sync():
    '''public synchronized void sync(final boolean force)
    '''
def close():
    '''public synchronized void close()
    '''
