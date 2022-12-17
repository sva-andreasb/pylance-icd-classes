def makeChild():
    '''returns BytesToNameCanonicalizer\n\n
    makeChild(final boolean canonicalize, final boolean intern)\n
    '''
def release():
    '''returns None\n\n
    release()\n
    '''
def size():
    '''returns int\n\n
    size()\n
    '''
def bucketCount():
    '''returns int\n\n
    bucketCount()\n
    '''
def maybeDirty():
    '''returns boolean\n\n
    maybeDirty()\n
    '''
def hashSeed():
    '''returns int\n\n
    hashSeed()\n
    '''
def collisionCount():
    '''returns int\n\n
    collisionCount()\n
    '''
def maxCollisionLength():
    '''returns int\n\n
    maxCollisionLength()\n
    '''
def findName():
    '''returns Name\n\n
    findName(final int firstQuad)\n
    findName(final int firstQuad, final int secondQuad)\n
    findName(final int[] quads, final int qlen)\n
    '''
def addName():
    '''returns Name\n\n
    addName(String symbolStr, final int q1, final int q2)\n
    addName(String symbolStr, final int[] quads, final int qlen)\n
    '''
def ():
    '''returns TableInfo\n\n
    (final int count, final int mainHashMask, final int[] mainHash, final Name[] mainNames, final Bucket[] collList, final int collCount, final int collEnd, final int longestCollisionList)\n
    (final BytesToNameCanonicalizer src)\n
    '''
def length():
    '''returns int\n\n
    length()\n
    '''
def find():
    '''returns Name\n\n
    find(final int hash, final int firstQuad, final int secondQuad)\n
    find(final int hash, final int[] quads, final int qlen)\n
    '''
