def BlockMgrWrapper():
    '''public BlockMgrWrapper(final BlockMgr blockMgr)
    '''
def allocateId():
    '''public int allocateId()
    '''
def allocateBuffer():
    '''public ByteBuffer allocateBuffer(final int id)
    '''
def blockSize():
    '''public int blockSize()
    '''
def get():
    '''public ByteBuffer get(final int id)
    '''
def put():
    '''public void put(final int id, final ByteBuffer block)
    '''
def freeBlock():
    '''public void freeBlock(final int id)
    '''
def sync():
    '''public void sync()
    public void sync(final boolean force)
    '''
def close():
    '''public void close()
    '''
def isEmpty():
    '''public boolean isEmpty()
    '''
def startRead():
    '''public void startRead()
    '''
def finishRead():
    '''public void finishRead()
    '''
def startUpdate():
    '''public void startUpdate()
    '''
def finishUpdate():
    '''public void finishUpdate()
    '''
def valid():
    '''public boolean valid(final int id)
    '''
def isClosed():
    '''public boolean isClosed()
    '''
