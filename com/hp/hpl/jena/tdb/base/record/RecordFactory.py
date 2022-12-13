def RecordFactory():
    '''public RecordFactory(final int keyLength, final int valueLength)
    '''
def keyFactory():
    '''public RecordFactory keyFactory()
    '''
def createKeyOnly():
    '''public Record createKeyOnly()
    public Record createKeyOnly(final Record record)
    '''
def create():
    '''public Record create(final byte[] key)
    public Record create()
    public Record create(final byte[] key, final byte[] value)
    '''
def insertInto():
    '''public void insertInto(final Record record, final ByteBuffer bb, final int idx)
    '''
def buildFrom():
    '''public Record buildFrom(final ByteBuffer bb, final int idx)
    '''
def hasValue():
    '''public boolean hasValue()
    '''
def recordLength():
    '''public int recordLength()
    '''
def keyLength():
    '''public int keyLength()
    '''
def valueLength():
    '''public int valueLength()
    '''
def toString():
    '''public String toString()
    '''
