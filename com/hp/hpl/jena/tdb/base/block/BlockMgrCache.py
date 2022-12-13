def BlockMgrCache():
'''public BlockMgrCache(final String indexName, final int readSlots, final int writeSlots, final BlockMgr blockMgr)
'''
pass
def apply():
'''public void apply(final Integer id, final ByteBuffer bb)
'''
pass
def get():
'''public synchronized ByteBuffer get(final int id)
'''
pass
def put():
'''public synchronized void put(final int id, final ByteBuffer block)
'''
pass
def freeBlock():
'''public synchronized void freeBlock(final int id)
'''
pass
def sync():
'''public synchronized void sync(final boolean force)
'''
pass
def close():
'''public synchronized void close()
'''
pass
