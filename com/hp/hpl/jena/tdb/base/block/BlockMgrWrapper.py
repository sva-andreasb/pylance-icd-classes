def BlockMgrWrapper():
'''public BlockMgrWrapper(final BlockMgr blockMgr)
'''
pass
def allocateId():
'''public int allocateId()
'''
pass
def allocateBuffer():
'''public ByteBuffer allocateBuffer(final int id)
'''
pass
def blockSize():
'''public int blockSize()
'''
pass
def get():
'''public ByteBuffer get(final int id)
'''
pass
def put():
'''public void put(final int id, final ByteBuffer block)
'''
pass
def freeBlock():
'''public void freeBlock(final int id)
'''
pass
def sync():
'''public void sync()
public void sync(final boolean force)
'''
pass
def close():
'''public void close()
'''
pass
def isEmpty():
'''public boolean isEmpty()
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
def valid():
'''public boolean valid(final int id)
'''
pass
def isClosed():
'''public boolean isClosed()
'''
pass
