HASH_MULT = "int  33"
def createRoot():
    '''public static CharsToNameCanonicalizer createRoot()
    '''
def makeChild():
    '''public CharsToNameCanonicalizer makeChild(final int flags)
    '''
def release():
    '''public void release()
    '''
def size():
    '''public int size()
    '''
def bucketCount():
    '''public int bucketCount()
    '''
def maybeDirty():
    '''public boolean maybeDirty()
    '''
def hashSeed():
    '''public int hashSeed()
    '''
def collisionCount():
    '''public int collisionCount()
    '''
def maxCollisionLength():
    '''public int maxCollisionLength()
    '''
def findSymbol():
    '''public String findSymbol(final char[] buffer, final int start, final int len, final int h)
    '''
def _hashToIndex():
    '''public int _hashToIndex(int rawHash)
    '''
def calcHash():
    '''public int calcHash(final char[] buffer, final int start, final int len)
    public int calcHash(final String key)
    '''
def Bucket():
    '''public Bucket(final String s, final Bucket n)
    '''
def has():
    '''public String has(final char[] buf, final int start, final int len)
    '''
def TableInfo():
    '''public TableInfo(final int size, final int longestCollisionList, final String[] symbols, final Bucket[] buckets)
    public TableInfo(final CharsToNameCanonicalizer src)
    '''
def createInitial():
    '''public static TableInfo createInitial(final int sz)
    '''
