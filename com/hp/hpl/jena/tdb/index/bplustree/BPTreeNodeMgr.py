def BPTreeNodeMgr():
    '''    public BPTreeNodeMgr(final BPlusTree bpTree, final BlockMgr blockMgr)
    '''
def getBlockMgr():
    '''    public BlockMgr getBlockMgr()
    '''
def allocateId():
    '''    public int allocateId()
    '''
def createRoot():
    '''    public BPTreeNode createRoot()
    '''
def createNode():
    '''    public BPTreeNode createNode(final int parent)
    '''
def getRoot():
    '''    public BPTreeNode getRoot(final int id)
    '''
def get():
    '''    public BPTreeNode get(final int id, final int parent)
    '''
def put():
    '''    public void put(final BPTreeNode node)
    '''
def release():
    '''    public void release(final int id)
    '''
def valid():
    '''    public boolean valid(final int id)
    '''
def dump():
    '''    public void dump()
    '''
def startRead():
    '''    public void startRead()
    '''
def finishRead():
    '''    public void finishRead()
    '''
def startUpdate():
    '''    public void startUpdate()
    '''
def finishUpdate():
    '''    public void finishUpdate()
    '''
def createFromByteBuffer():
    '''    public BPTreeNode createFromByteBuffer(final ByteBuffer bb, final BlockType bType)
    '''
def fromByteBuffer():
    '''    public BPTreeNode fromByteBuffer(final ByteBuffer byteBuffer)
    '''
def toByteBuffer():
    '''    public ByteBuffer toByteBuffer(final BPTreeNode node)
    '''
