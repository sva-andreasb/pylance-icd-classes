def BlockMgrSync():
    '''public BlockMgrSync(final BlockMgr blockMgr)
    '''
def allocateId():
    '''public synchronized int allocateId()
    '''
def allocateBuffer():
    '''public synchronized ByteBuffer allocateBuffer(final int id)
    '''
def blockSize():
    '''public synchronized int blockSize()
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
    '''public synchronized void sync()
    public synchronized void sync(final boolean force)
    '''
def close():
    '''public synchronized void close()
    '''
def isEmpty():
    '''public synchronized boolean isEmpty()
    '''
def startRead():
    '''public synchronized void startRead()
    '''
def finishRead():
    '''public synchronized void finishRead()
    '''
def startUpdate():
    '''public synchronized void startUpdate()
    '''
def finishUpdate():
    '''public synchronized void finishUpdate()
    '''
def valid():
    '''public synchronized boolean valid(final int id)
    '''
def isClosed():
    '''public synchronized boolean isClosed()
    '''
