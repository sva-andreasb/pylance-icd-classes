def schemaVersions():
    '''    public static Schema[] schemaVersions()
    '''
def ProduceRequest():
    '''    public ProduceRequest(final Struct struct, final short version)
    '''
def toStruct():
    '''    public Struct toStruct()
    '''
def toString():
    '''    public String toString(final boolean verbose)
    public String toString()
    '''
def getErrorResponse():
    '''    public ProduceResponse getErrorResponse(final int throttleTimeMs, final Throwable e)
    '''
def errorCounts():
    '''    public Map<Errors, Integer> errorCounts(final Throwable e)
    '''
def acks():
    '''    public short acks()
    '''
def timeout():
    '''    public int timeout()
    '''
def transactionalId():
    '''    public String transactionalId()
    '''
def isTransactional():
    '''    public boolean isTransactional()
    '''
def isIdempotent():
    '''    public boolean isIdempotent()
    '''
def partitionRecordsOrFail():
    '''    public Map<TopicPartition, MemoryRecords> partitionRecordsOrFail()
    '''
def clearPartitionRecords():
    '''    public void clearPartitionRecords()
    '''
def parse():
    '''    public static ProduceRequest parse(final ByteBuffer buffer, final short version)
    '''
def requiredMagicForVersion():
    '''    public static byte requiredMagicForVersion(final short produceRequestVersion)
    '''
def forCurrentMagic():
    '''    public static Builder forCurrentMagic(final short acks, final int timeout, final Map<TopicPartition, MemoryRecords> partitionRecords)
    '''
def forMagic():
    '''    public static Builder forMagic(final byte magic, final short acks, final int timeout, final Map<TopicPartition, MemoryRecords> partitionRecords, final String transactionalId)
    '''
def build():
    '''    public ProduceRequest build(final short version)
    '''
