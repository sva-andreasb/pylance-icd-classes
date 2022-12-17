def ():
    '''returns Builder\n\n
    (final Struct struct, final short version)\n
    (final String groupId, final List<TopicPartition> partitions)\n
    '''
def getErrorResponse():
    '''returns OffsetFetchResponse\n\n
    getErrorResponse(final Errors error)\n
    getErrorResponse(final int throttleTimeMs, final Errors error)\n
    getErrorResponse(final int throttleTimeMs, final Throwable e)\n
    '''
def groupId():
    '''returns String\n\n
    groupId()\n
    '''
def partitions():
    '''returns List<TopicPartition>\n\n
    partitions()\n
    '''
def isAllPartitions():
    '''returns boolean\n\n
    isAllPartitions()\n
    '''
def isAllTopicPartitions():
    '''returns boolean\n\n
    isAllTopicPartitions()\n
    '''
def build():
    '''returns OffsetFetchRequest\n\n
    build(final short version)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
