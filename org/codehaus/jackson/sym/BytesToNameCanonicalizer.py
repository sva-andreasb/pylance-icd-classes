def createRoot():
'''public static BytesToNameCanonicalizer createRoot()
'''
pass
def makeChild():
'''public BytesToNameCanonicalizer makeChild(final boolean canonicalize, final boolean intern)
'''
pass
def release():
'''public void release()
'''
pass
def size():
'''public int size()
'''
pass
def bucketCount():
'''public int bucketCount()
'''
pass
def maybeDirty():
'''public boolean maybeDirty()
'''
pass
def hashSeed():
'''public int hashSeed()
'''
pass
def collisionCount():
'''public int collisionCount()
'''
pass
def maxCollisionLength():
'''public int maxCollisionLength()
'''
pass
def getEmptyName():
'''public static Name getEmptyName()
'''
pass
def findName():
'''public Name findName(final int firstQuad)
public Name findName(final int firstQuad, final int secondQuad)
public Name findName(final int[] quads, final int qlen)
'''
pass
def addName():
'''public Name addName(String symbolStr, final int q1, final int q2)
public Name addName(String symbolStr, final int[] quads, final int qlen)
'''
pass
def calcHash():
'''public final int calcHash(final int firstQuad)
public final int calcHash(final int firstQuad, final int secondQuad)
public final int calcHash(final int[] quads, final int qlen)
'''
pass
def TableInfo():
'''public TableInfo(final int count, final int mainHashMask, final int[] mainHash, final Name[] mainNames, final Bucket[] collList, final int collCount, final int collEnd, final int longestCollisionList)
public TableInfo(final BytesToNameCanonicalizer src)
'''
pass
def length():
'''public int length()
'''
pass
def find():
'''public Name find(final int hash, final int firstQuad, final int secondQuad)
public Name find(final int hash, final int[] quads, final int qlen)
'''
pass
