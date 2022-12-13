RootParent = "int  -2"
NoParent = "int  -99"
def checkAll():
    '''    public static void checkAll()
    '''
def infoAll():
    '''    public static void infoAll()
    '''
def toString():
    '''    public String toString()
    '''
def readMeta():
    '''    public static BPlusTreeParams readMeta(final MetaFile mf)
    '''
def addToMetaData():
    '''    public void addToMetaData(final MetaFile mf)
    '''
def BPlusTreeParams():
    '''    public BPlusTreeParams(final int order, final int keyLen, final int valLen)
    public BPlusTreeParams(final int order, final RecordFactory factory)
    '''
def getOrder():
    '''    public int getOrder()
    '''
def getPtrLength():
    '''    public int getPtrLength()
    '''
def getRecordLength():
    '''    public int getRecordLength()
    '''
def getRecordFactory():
    '''    public RecordFactory getRecordFactory()
    '''
def getKeyLength():
    '''    public int getKeyLength()
    '''
def getKeyFactory():
    '''    public RecordFactory getKeyFactory()
    '''
def getBlockSize():
    '''    public int getBlockSize()
    '''
def calcOrder():
    '''    public static int calcOrder(final int blockSize, final RecordFactory factory)
    public static int calcOrder(int blockSize, final int recordLength)
    '''
def calcBlockSize():
    '''    public static int calcBlockSize(final int bpTreeOrder, final RecordFactory factory)
    '''
def getMaxRec():
    '''    public int getMaxRec()
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
