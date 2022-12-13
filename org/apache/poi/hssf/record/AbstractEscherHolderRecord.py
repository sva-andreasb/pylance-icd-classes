def AbstractEscherHolderRecord():
    '''public AbstractEscherHolderRecord()
    public AbstractEscherHolderRecord(final RecordInputStream in)
    '''
def toString():
    '''public String toString()
    '''
def serialize():
    '''public int serialize(final int offset, final byte[] data)
    '''
def getRecordSize():
    '''public int getRecordSize()
    '''
def clone():
    '''public AbstractEscherHolderRecord clone()
    '''
def addEscherRecord():
    '''public void addEscherRecord(final int index, final EscherRecord element)
    public boolean addEscherRecord(final EscherRecord element)
    '''
def getEscherRecords():
    '''public List<EscherRecord> getEscherRecords()
    '''
def clearEscherRecords():
    '''public void clearEscherRecords()
    '''
def getEscherContainer():
    '''public EscherContainerRecord getEscherContainer()
    '''
def findFirstWithId():
    '''public EscherRecord findFirstWithId(final short id)
    '''
def getEscherRecord():
    '''public EscherRecord getEscherRecord(final int index)
    '''
def join():
    '''public void join(final AbstractEscherHolderRecord record)
    '''
def processContinueRecord():
    '''public void processContinueRecord(final byte[] record)
    '''
def getRawData():
    '''public byte[] getRawData()
    '''
def setRawData():
    '''public void setRawData(final byte[] rawData)
    '''
def decode():
    '''public void decode()
    '''
