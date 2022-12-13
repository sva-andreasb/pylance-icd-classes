TRIE = "int  4"
BITLEN = "int  8"
FIELD_LENGTH = "int  8"
def HashBucket():
    '''    public HashBucket(final int id, final int hashValue, final int bucketBitLen, final ByteBuffer byteBuffer, final RecordFactory factory, final HashBucketMgr hashBucketPageMgr, final int count)
    '''
def findIndex():
    '''    public final int findIndex(final Record key)
    '''
def find():
    '''    public final Record find(final Record key)
    '''
def put():
    '''    public final boolean put(final Record record)
    '''
def set():
    '''    public void set(final int x, final Record record)
    '''
def removeByKey():
    '''    public final boolean removeByKey(final Record key)
    '''
def isFull():
    '''    public final boolean isFull()
    '''
def isEmpty():
    '''    public final boolean isEmpty()
    '''
def get():
    '''    public final Record get(final int idx)
    '''
def getTrieValue():
    '''    public final int getTrieValue()
    '''
def getTrieBitLen():
    '''    public final int getTrieBitLen()
    '''
def setTrieLength():
    '''    public void setTrieLength(final int trieBitLen)
    '''
def setPageMgr():
    '''    public void setPageMgr(final HashBucketMgr pageMgr)
    '''
def getPageMgr():
    '''    public HashBucketMgr getPageMgr()
    '''
def toString():
    '''    public String toString()
    '''
