RootParent = "int  -2"
NoParent = "int  -99"
def toString():
    '''    public String toString()
    '''
def BTreeParams():
    '''    public BTreeParams(final int order, final int keyLen, final int valLen)
    public BTreeParams(final int order, final RecordFactory factory)
    '''
def getOrder():
    '''    public int getOrder()
    '''
def getPtrLength():
    '''    public static int getPtrLength()
    '''
def getRecordLength():
    '''    public int getRecordLength()
    '''
def getRecordFactory():
    '''    public RecordFactory getRecordFactory()
    '''
def getBlockSize():
    '''    public int getBlockSize()
    '''
def calcOrder():
    '''    public static int calcOrder(final int blockSize, final RecordFactory factory)
    public static int calcOrder(int blockSize, final int recordLength)
    '''
def calcBlockSize():
    '''    public static int calcBlockSize(final int bTreeOrder, final RecordFactory factory)
    '''
def getMaxRecNonLeaf():
    '''    public int getMaxRecNonLeaf()
    '''
def getMaxRecLeaf():
    '''    public int getMaxRecLeaf()
    '''
def getMaxPtr():
    '''    public int getMaxPtr()
    '''
def getMinRec():
    '''    public int getMinRec()
    '''
def getMinPtr():
    '''    public int getMinPtr()
    '''
