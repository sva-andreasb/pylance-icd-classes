RootParent = "int  -2"
NoParent = "int  -99"
def toString():
'''public String toString()
'''
pass
def BTreeParams():
'''public BTreeParams(final int order, final int keyLen, final int valLen)
public BTreeParams(final int order, final RecordFactory factory)
'''
pass
def getOrder():
'''public int getOrder()
'''
pass
def getPtrLength():
'''public static int getPtrLength()
'''
pass
def getRecordLength():
'''public int getRecordLength()
'''
pass
def getRecordFactory():
'''public RecordFactory getRecordFactory()
'''
pass
def getBlockSize():
'''public int getBlockSize()
'''
pass
def calcOrder():
'''public static int calcOrder(final int blockSize, final RecordFactory factory)
public static int calcOrder(int blockSize, final int recordLength)
'''
pass
def calcBlockSize():
'''public static int calcBlockSize(final int bTreeOrder, final RecordFactory factory)
'''
pass
def getMaxRecNonLeaf():
'''public int getMaxRecNonLeaf()
'''
pass
def getMaxRecLeaf():
'''public int getMaxRecLeaf()
'''
pass
def getMaxPtr():
'''public int getMaxPtr()
'''
pass
def getMinRec():
'''public int getMinRec()
'''
pass
def getMinPtr():
'''public int getMinPtr()
'''
pass
