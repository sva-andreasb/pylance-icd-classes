def BPTreeNodeMgr():
'''public BPTreeNodeMgr(final BPlusTree bpTree, final BlockMgr blockMgr)
'''
pass
def getBlockMgr():
'''public BlockMgr getBlockMgr()
'''
pass
def allocateId():
'''public int allocateId()
'''
pass
def createRoot():
'''public BPTreeNode createRoot()
'''
pass
def createNode():
'''public BPTreeNode createNode(final int parent)
'''
pass
def getRoot():
'''public BPTreeNode getRoot(final int id)
'''
pass
def get():
'''public BPTreeNode get(final int id, final int parent)
'''
pass
def put():
'''public void put(final BPTreeNode node)
'''
pass
def release():
'''public void release(final int id)
'''
pass
def valid():
'''public boolean valid(final int id)
'''
pass
def dump():
'''public void dump()
'''
pass
def startRead():
'''public void startRead()
'''
pass
def finishRead():
'''public void finishRead()
'''
pass
def startUpdate():
'''public void startUpdate()
'''
pass
def finishUpdate():
'''public void finishUpdate()
'''
pass
def createFromByteBuffer():
'''public BPTreeNode createFromByteBuffer(final ByteBuffer bb, final BlockType bType)
'''
pass
def fromByteBuffer():
'''public BPTreeNode fromByteBuffer(final ByteBuffer byteBuffer)
'''
pass
def toByteBuffer():
'''public ByteBuffer toByteBuffer(final BPTreeNode node)
'''
pass
