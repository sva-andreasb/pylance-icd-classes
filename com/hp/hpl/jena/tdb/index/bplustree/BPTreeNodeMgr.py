def ():
    '''returns BPTreeNodeMgr\n\n
    (final BPlusTree bpTree, final BlockMgr blockMgr)\n
    '''
def getBlockMgr():
    '''returns BlockMgr\n\n
    getBlockMgr()\n
    '''
def allocateId():
    '''returns int\n\n
    allocateId()\n
    '''
def createRoot():
    '''returns BPTreeNode\n\n
    createRoot()\n
    '''
def createNode():
    '''returns BPTreeNode\n\n
    createNode(final int parent)\n
    '''
def getRoot():
    '''returns BPTreeNode\n\n
    getRoot(final int id)\n
    '''
def get():
    '''returns BPTreeNode\n\n
    get(final int id, final int parent)\n
    '''
def put():
    '''returns None\n\n
    put(final BPTreeNode node)\n
    '''
def release():
    '''returns None\n\n
    release(final int id)\n
    '''
def valid():
    '''returns boolean\n\n
    valid(final int id)\n
    '''
def dump():
    '''returns None\n\n
    dump()\n
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
def createFromByteBuffer():
    '''returns BPTreeNode\n\n
    createFromByteBuffer(final ByteBuffer bb, final BlockType bType)\n
    '''
def fromByteBuffer():
    '''returns BPTreeNode\n\n
    fromByteBuffer(final ByteBuffer byteBuffer)\n
    '''
def toByteBuffer():
    '''returns ByteBuffer\n\n
    toByteBuffer(final BPTreeNode node)\n
    '''
