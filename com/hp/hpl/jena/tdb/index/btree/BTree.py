def makeMem():
    '''public static BTree makeMem(final int N, final int keyLength, final int valueLength)
    public static BTree makeMem(final String name, final int N, final int keyLength, final int valueLength)
    '''
def BTree():
    '''public BTree(final BTreeParams bTreeParams, final BlockMgr blkMgr)
    '''
def getRecordFactory():
    '''public RecordFactory getRecordFactory()
    '''
def find():
    '''public Record find(final Record record)
    '''
def contains():
    '''public boolean contains(final Record record)
    '''
def minKey():
    '''public Record minKey()
    '''
def maxKey():
    '''public Record maxKey()
    '''
def add():
    '''public boolean add(final Record record)
    '''
def addAndReturnOld():
    '''public Record addAndReturnOld(final Record record)
    '''
def delete():
    '''public boolean delete(final Record record)
    '''
def deleteAndReturnOld():
    '''public Record deleteAndReturnOld(final Record record)
    '''
def iterator():
    '''public Iterator<Record> iterator()
    public Iterator<Record> iterator(final Record fromRec, final Record toRec)
    '''
def isEmpty():
    '''public boolean isEmpty()
    '''
def clear():
    '''public void clear()
    '''
def sync():
    '''public void sync()
    public void sync(final boolean force)
    '''
def close():
    '''public void close()
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
def size():
    '''public long size()
    '''
def sessionTripleCount():
    '''public long sessionTripleCount()
    '''
def sizeByCounting():
    '''public long sizeByCounting()
    '''
def check():
    '''public void check()
    '''
def dump():
    '''public void dump()
    '''
