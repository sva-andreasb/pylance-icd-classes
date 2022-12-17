def ():
    '''returns BlockMgrWrapper\n\n
    (final BlockMgr blockMgr)\n
    '''
def allocateId():
    '''returns int\n\n
    allocateId()\n
    '''
def allocateBuffer():
    '''returns ByteBuffer\n\n
    allocateBuffer(final int id)\n
    '''
def blockSize():
    '''returns int\n\n
    blockSize()\n
    '''
def get():
    '''returns ByteBuffer\n\n
    get(final int id)\n
    '''
def put():
    '''returns None\n\n
    put(final int id, final ByteBuffer block)\n
    '''
def freeBlock():
    '''returns None\n\n
    freeBlock(final int id)\n
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
def isEmpty():
    '''returns boolean\n\n
    isEmpty()\n
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
def valid():
    '''returns boolean\n\n
    valid(final int id)\n
    '''
def isClosed():
    '''returns boolean\n\n
    isClosed()\n
    '''
