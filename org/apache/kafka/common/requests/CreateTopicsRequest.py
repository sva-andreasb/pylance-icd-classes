NO_NUM_PARTITIONS = "int  -1"
NO_REPLICATION_FACTOR = "short  -1"
def ():
    '''returns Builder\n\n
    (final Struct struct, final short version)\n
    (final int partitions, final short replicationFactor, final Map<String, String> configs)\n
    (final int partitions, final short replicationFactor)\n
    (final Map<Integer, List<Integer>> replicasAssignments, final Map<String, String> configs)\n
    (final Map<Integer, List<Integer>> replicasAssignments)\n
    (final Map<String, TopicDetails> topics, final int timeout)\n
    (final Map<String, TopicDetails> topics, final int timeout, final boolean validateOnly)\n
    '''
def getErrorResponse():
    '''returns AbstractResponse\n\n
    getErrorResponse(final int throttleTimeMs, final Throwable e)\n
    '''
def timeout():
    '''returns int\n\n
    timeout()\n
    '''
def validateOnly():
    '''returns boolean\n\n
    validateOnly()\n
    '''
def duplicateTopics():
    '''returns Set<String>\n\n
    duplicateTopics()\n
    '''
def toStruct():
    '''returns Struct\n\n
    toStruct()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString()\n
    '''
def build():
    '''returns CreateTopicsRequest\n\n
    build(final short version)\n
    '''
