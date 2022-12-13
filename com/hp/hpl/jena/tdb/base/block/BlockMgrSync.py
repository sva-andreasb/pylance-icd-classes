def BlockMgrSync():
'''public BlockMgrSync(final BlockMgr blockMgr)
'''
pass
def allocateId():
'''public synchronized int allocateId()
'''
pass
def allocateBuffer():
'''public synchronized ByteBuffer allocateBuffer(final int id)
'''
pass
def blockSize():
'''public synchronized int blockSize()
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
'''public synchronized void sync()
public synchronized void sync(final boolean force)
'''
pass
def close():
'''public synchronized void close()
'''
pass
def isEmpty():
'''public synchronized boolean isEmpty()
'''
pass
def startRead():
'''public synchronized void startRead()
'''
pass
def finishRead():
'''public synchronized void finishRead()
'''
pass
def startUpdate():
'''public synchronized void startUpdate()
'''
pass
def finishUpdate():
'''public synchronized void finishUpdate()
'''
pass
def valid():
'''public synchronized boolean valid(final int id)
'''
pass
def isClosed():
'''public synchronized boolean isClosed()
'''
pass
