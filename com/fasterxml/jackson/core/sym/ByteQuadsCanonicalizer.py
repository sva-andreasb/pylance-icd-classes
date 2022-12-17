def makeChild():
    '''returns ByteQuadsCanonicalizer\n\n
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
def primaryCount():
    '''returns int\n\n
    primaryCount()\n
    '''
def secondaryCount():
    '''returns int\n\n
    secondaryCount()\n
    '''
def tertiaryCount():
    '''returns int\n\n
    tertiaryCount()\n
    '''
def spilloverCount():
    '''returns int\n\n
    spilloverCount()\n
    '''
def totalCount():
    '''returns int\n\n
    totalCount()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def findName():
    '''returns String\n\n
    findName(final int q1)\n
    findName(final int q1, final int q2)\n
    findName(final int q1, final int q2, final int q3)\n
    findName(final int[] q, final int qlen)\n
    '''
def addName():
    '''returns String\n\n
    addName(String name, final int q1)\n
    addName(String name, final int q1, final int q2)\n
    addName(String name, final int q1, final int q2, final int q3)\n
    addName(String name, final int[] q, final int qlen)\n
    '''
def calcHash():
    '''returns int\n\n
    calcHash(final int q1)\n
    calcHash(final int q1, final int q2)\n
    calcHash(final int q1, final int q2, final int q3)\n
    calcHash(final int[] q, final int qlen)\n
    '''
def ():
    '''returns TableInfo\n\n
    (final int size, final int count, final int tertiaryShift, final int[] mainHash, final String[] names, final int spilloverEnd, final int longNameOffset)\n
    (final ByteQuadsCanonicalizer src)\n
    '''
