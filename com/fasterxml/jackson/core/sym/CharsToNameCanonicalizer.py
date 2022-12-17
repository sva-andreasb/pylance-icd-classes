HASH_MULT = "int  33"
def makeChild():
    '''returns CharsToNameCanonicalizer\n\n
    makeChild(final int flags)\n
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
def findSymbol():
    '''returns String\n\n
    findSymbol(final char[] buffer, final int start, final int len, final int h)\n
    '''
def _hashToIndex():
    '''returns int\n\n
    _hashToIndex(int rawHash)\n
    '''
def calcHash():
    '''returns int\n\n
    calcHash(final char[] buffer, final int start, final int len)\n
    calcHash(final String key)\n
    '''
def ():
    '''returns TableInfo\n\n
    (final String s, final Bucket n)\n
    (final int size, final int longestCollisionList, final String[] symbols, final Bucket[] buckets)\n
    (final CharsToNameCanonicalizer src)\n
    '''
def has():
    '''returns String\n\n
    has(final char[] buf, final int start, final int len)\n
    '''
