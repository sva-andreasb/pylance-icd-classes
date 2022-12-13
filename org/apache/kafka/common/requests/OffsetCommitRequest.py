DEFAULT_GENERATION_ID = "int  -1"
DEFAULT_MEMBER_ID = "String  \"\""
DEFAULT_RETENTION_TIME = "long  -1L"
DEFAULT_TIMESTAMP = "long  -1L"
def schemaVersions():
    '''    public static Schema[] schemaVersions()
    '''
def OffsetCommitRequest():
    '''    public OffsetCommitRequest(final Struct struct, final short versionId)
    '''
def toStruct():
    '''    public Struct toStruct()
    '''
def getErrorResponse():
    '''    public AbstractResponse getErrorResponse(final int throttleTimeMs, final Throwable e)
    '''
def groupId():
    '''    public String groupId()
    '''
def generationId():
    '''    public int generationId()
    '''
def memberId():
    '''    public String memberId()
    '''
def retentionTime():
    '''    public long retentionTime()
    '''
def offsetData():
    '''    public Map<TopicPartition, PartitionData> offsetData()
    '''
def parse():
    '''    public static OffsetCommitRequest parse(final ByteBuffer buffer, final short version)
    '''
def PartitionData():
    '''    public PartitionData(final long offset, final long timestamp, final String metadata)
    public PartitionData(final long offset, final String metadata)
    '''
def toString():
    '''    public String toString()
    public String toString()
    '''
def Builder():
    '''    public Builder(final String groupId, final Map<TopicPartition, PartitionData> offsetData)
    '''
def setMemberId():
    '''    public Builder setMemberId(final String memberId)
    '''
def setGenerationId():
    '''    public Builder setGenerationId(final int generationId)
    '''
def setRetentionTime():
    '''    public Builder setRetentionTime(final long retentionTime)
    '''
def build():
    '''    public OffsetCommitRequest build(final short version)
    '''
