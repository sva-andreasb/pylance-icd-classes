def createRoot():
    '''    public static ByteQuadsCanonicalizer createRoot()
    '''
def makeChild():
    '''    public ByteQuadsCanonicalizer makeChild(final int flags)
    '''
def release():
    '''    public void release()
    '''
def size():
    '''    public int size()
    '''
def bucketCount():
    '''    public int bucketCount()
    '''
def maybeDirty():
    '''    public boolean maybeDirty()
    '''
def hashSeed():
    '''    public int hashSeed()
    '''
def primaryCount():
    '''    public int primaryCount()
    '''
def secondaryCount():
    '''    public int secondaryCount()
    '''
def tertiaryCount():
    '''    public int tertiaryCount()
    '''
def spilloverCount():
    '''    public int spilloverCount()
    '''
def totalCount():
    '''    public int totalCount()
    '''
def toString():
    '''    public String toString()
    '''
def findName():
    '''    public String findName(final int q1)
    public String findName(final int q1, final int q2)
    public String findName(final int q1, final int q2, final int q3)
    public String findName(final int[] q, final int qlen)
    '''
def addName():
    '''    public String addName(String name, final int q1)
    public String addName(String name, final int q1, final int q2)
    public String addName(String name, final int q1, final int q2, final int q3)
    public String addName(String name, final int[] q, final int qlen)
    '''
def calcHash():
    '''    public int calcHash(final int q1)
    public int calcHash(final int q1, final int q2)
    public int calcHash(final int q1, final int q2, final int q3)
    public int calcHash(final int[] q, final int qlen)
    '''
def TableInfo():
    '''    public TableInfo(final int size, final int count, final int tertiaryShift, final int[] mainHash, final String[] names, final int spilloverEnd, final int longNameOffset)
    public TableInfo(final ByteQuadsCanonicalizer src)
    '''
def createInitial():
    '''    public static TableInfo createInitial(final int sz)
    '''
