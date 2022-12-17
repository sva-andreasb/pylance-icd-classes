TRIE = "int  4"
BITLEN = "int  8"
FIELD_LENGTH = "int  8"
def ():
    '''returns HashBucket\n\n
    (final int id, final int hashValue, final int bucketBitLen, final ByteBuffer byteBuffer, final RecordFactory factory, final HashBucketMgr hashBucketPageMgr, final int count)\n
    '''
def set():
    '''returns None\n\n
    set(final int x, final Record record)\n
    '''
def setTrieLength():
    '''returns None\n\n
    setTrieLength(final int trieBitLen)\n
    '''
def setPageMgr():
    '''returns None\n\n
    setPageMgr(final HashBucketMgr pageMgr)\n
    '''
def getPageMgr():
    '''returns HashBucketMgr\n\n
    getPageMgr()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
