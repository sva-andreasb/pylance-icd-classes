def makeMem():
'''public static BTree makeMem(final int N, final int keyLength, final int valueLength)
public static BTree makeMem(final String name, final int N, final int keyLength, final int valueLength)
'''
pass
def BTree():
'''public BTree(final BTreeParams bTreeParams, final BlockMgr blkMgr)
'''
pass
def getRecordFactory():
'''public RecordFactory getRecordFactory()
'''
pass
def find():
'''public Record find(final Record record)
'''
pass
def contains():
'''public boolean contains(final Record record)
'''
pass
def minKey():
'''public Record minKey()
'''
pass
def maxKey():
'''public Record maxKey()
'''
pass
def add():
'''public boolean add(final Record record)
'''
pass
def addAndReturnOld():
'''public Record addAndReturnOld(final Record record)
'''
pass
def delete():
'''public boolean delete(final Record record)
'''
pass
def deleteAndReturnOld():
'''public Record deleteAndReturnOld(final Record record)
'''
pass
def iterator():
'''public Iterator<Record> iterator()
public Iterator<Record> iterator(final Record fromRec, final Record toRec)
'''
pass
def isEmpty():
'''public boolean isEmpty()
'''
pass
def clear():
'''public void clear()
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
def size():
'''public long size()
'''
pass
def sessionTripleCount():
'''public long sessionTripleCount()
'''
pass
def sizeByCounting():
'''public long sizeByCounting()
'''
pass
def check():
'''public void check()
'''
pass
def dump():
'''public void dump()
'''
pass
