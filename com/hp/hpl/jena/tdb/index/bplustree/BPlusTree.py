def attach():
    '''public static BPlusTree attach(final BPlusTreeParams params, final BlockMgr blkMgrNodes, final BlockMgr blkMgrLeaves)
    '''
def makeMem():
    '''public static BPlusTree makeMem(final int order, final int minRecords, final int keyLength, final int valueLength)
    public static BPlusTree makeMem(final String name, final int order, final int minRecords, final int keyLength, final int valueLength)
    '''
def dummy():
    '''public static BPlusTree dummy(final BPlusTreeParams params, final BlockMgr blkMgrNodes, final BlockMgr blkMgrLeaves)
    '''
def getParams():
    '''public BPlusTreeParams getParams()
    '''
def getNodeManager():
    '''public BPTreeNodeMgr getNodeManager()
    '''
def getRecordsMgr():
    '''public BPTreeRecordsMgr getRecordsMgr()
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
def finishRead():
    '''public void finishRead()
    '''
def finishUpdate():
    '''public void finishUpdate()
    '''
def startRead():
    '''public void startRead()
    '''
def startUpdate():
    '''public void startUpdate()
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
def sessionTripleCount():
    '''public long sessionTripleCount()
    '''
def size():
    '''public long size()
    '''
def check():
    '''public void check()
    '''
def dump():
    '''public void dump()
    public void dump(final IndentedWriter out)
    '''
