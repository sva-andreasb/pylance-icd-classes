def createRoot():
    '''public static BytesToNameCanonicalizer createRoot()
    '''
def makeChild():
    '''public BytesToNameCanonicalizer makeChild(final boolean canonicalize, final boolean intern)
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
def getEmptyName():
    '''public static Name getEmptyName()
    '''
def findName():
    '''public Name findName(final int firstQuad)
    public Name findName(final int firstQuad, final int secondQuad)
    public Name findName(final int[] quads, final int qlen)
    '''
def addName():
    '''public Name addName(String symbolStr, final int q1, final int q2)
    public Name addName(String symbolStr, final int[] quads, final int qlen)
    '''
def calcHash():
    '''public final int calcHash(final int firstQuad)
    public final int calcHash(final int firstQuad, final int secondQuad)
    public final int calcHash(final int[] quads, final int qlen)
    '''
def TableInfo():
    '''public TableInfo(final int count, final int mainHashMask, final int[] mainHash, final Name[] mainNames, final Bucket[] collList, final int collCount, final int collEnd, final int longestCollisionList)
    public TableInfo(final BytesToNameCanonicalizer src)
    '''
def length():
    '''public int length()
    '''
def find():
    '''public Name find(final int hash, final int firstQuad, final int secondQuad)
    public Name find(final int hash, final int[] quads, final int qlen)
    '''
