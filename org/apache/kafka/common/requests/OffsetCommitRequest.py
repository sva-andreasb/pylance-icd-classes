DEFAULT_GENERATION_ID = "int  -1"
DEFAULT_MEMBER_ID = "String  "
DEFAULT_RETENTION_TIME = "long  -1L"
DEFAULT_TIMESTAMP = "long  -1L"
def schemaVersions():
'''public static Schema[] schemaVersions()
'''
pass
def OffsetCommitRequest():
'''public OffsetCommitRequest(final Struct struct, final short versionId)
'''
pass
def toStruct():
'''public Struct toStruct()
'''
pass
def getErrorResponse():
'''public AbstractResponse getErrorResponse(final int throttleTimeMs, final Throwable e)
'''
pass
def groupId():
'''public String groupId()
'''
pass
def generationId():
'''public int generationId()
'''
pass
def memberId():
'''public String memberId()
'''
pass
def retentionTime():
'''public long retentionTime()
'''
pass
def offsetData():
'''public Map<TopicPartition, PartitionData> offsetData()
'''
pass
def parse():
'''public static OffsetCommitRequest parse(final ByteBuffer buffer, final short version)
'''
pass
def PartitionData():
'''public PartitionData(final long offset, final long timestamp, final String metadata)
public PartitionData(final long offset, final String metadata)
'''
pass
def toString():
'''public String toString()
public String toString()
'''
pass
def Builder():
'''public Builder(final String groupId, final Map<TopicPartition, PartitionData> offsetData)
'''
pass
def setMemberId():
'''public Builder setMemberId(final String memberId)
'''
pass
def setGenerationId():
'''public Builder setGenerationId(final int generationId)
'''
pass
def setRetentionTime():
'''public Builder setRetentionTime(final long retentionTime)
'''
pass
def build():
'''public OffsetCommitRequest build(final short version)
'''
pass
