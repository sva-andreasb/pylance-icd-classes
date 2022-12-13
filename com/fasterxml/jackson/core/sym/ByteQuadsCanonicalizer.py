def createRoot():
'''public static ByteQuadsCanonicalizer createRoot()
'''
pass
def makeChild():
'''public ByteQuadsCanonicalizer makeChild(final int flags)
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
def primaryCount():
'''public int primaryCount()
'''
pass
def secondaryCount():
'''public int secondaryCount()
'''
pass
def tertiaryCount():
'''public int tertiaryCount()
'''
pass
def spilloverCount():
'''public int spilloverCount()
'''
pass
def totalCount():
'''public int totalCount()
'''
pass
def toString():
'''public String toString()
'''
pass
def findName():
'''public String findName(final int q1)
public String findName(final int q1, final int q2)
public String findName(final int q1, final int q2, final int q3)
public String findName(final int[] q, final int qlen)
'''
pass
def addName():
'''public String addName(String name, final int q1)
public String addName(String name, final int q1, final int q2)
public String addName(String name, final int q1, final int q2, final int q3)
public String addName(String name, final int[] q, final int qlen)
'''
pass
def calcHash():
'''public int calcHash(final int q1)
public int calcHash(final int q1, final int q2)
public int calcHash(final int q1, final int q2, final int q3)
public int calcHash(final int[] q, final int qlen)
'''
pass
def TableInfo():
'''public TableInfo(final int size, final int count, final int tertiaryShift, final int[] mainHash, final String[] names, final int spilloverEnd, final int longNameOffset)
public TableInfo(final ByteQuadsCanonicalizer src)
'''
pass
def createInitial():
'''public static TableInfo createInitial(final int sz)
'''
pass
