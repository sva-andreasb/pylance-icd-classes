DEFAULT_GENERATION_ID = "int  -1"
DEFAULT_MEMBER_ID = "String  \"\""
DEFAULT_RETENTION_TIME = "long  -1L"
DEFAULT_TIMESTAMP = "long  -1L"
def ():
    '''returns Builder\n\n
    (final Struct struct, final short versionId)\n
    (final long offset, final long timestamp, final String metadata)\n
    (final long offset, final String metadata)\n
    (final String groupId, final Map<TopicPartition, PartitionData> offsetData)\n
    '''
def toStruct():
    '''returns Struct\n\n
    toStruct()\n
    '''
def getErrorResponse():
    '''returns AbstractResponse\n\n
    getErrorResponse(final int throttleTimeMs, final Throwable e)\n
    '''
def groupId():
    '''returns String\n\n
    groupId()\n
    '''
def generationId():
    '''returns int\n\n
    generationId()\n
    '''
def memberId():
    '''returns String\n\n
    memberId()\n
    '''
def retentionTime():
    '''returns long\n\n
    retentionTime()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString()\n
    '''
def setMemberId():
    '''returns Builder\n\n
    setMemberId(final String memberId)\n
    '''
def setGenerationId():
    '''returns Builder\n\n
    setGenerationId(final int generationId)\n
    '''
def setRetentionTime():
    '''returns Builder\n\n
    setRetentionTime(final long retentionTime)\n
    '''
def build():
    '''returns OffsetCommitRequest\n\n
    build(final short version)\n
    '''
