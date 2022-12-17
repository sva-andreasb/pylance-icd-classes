def ():
    '''returns Builder\n\n
    (final Struct struct, final short version)\n
    (final int controllerId, final int controllerEpoch, final boolean deletePartitions, final Set<TopicPartition> partitions)\n
    '''
def getErrorResponse():
    '''returns StopReplicaResponse\n\n
    getErrorResponse(final int throttleTimeMs, final Throwable e)\n
    '''
def controllerId():
    '''returns int\n\n
    controllerId()\n
    '''
def controllerEpoch():
    '''returns int\n\n
    controllerEpoch()\n
    '''
def deletePartitions():
    '''returns boolean\n\n
    deletePartitions()\n
    '''
def partitions():
    '''returns Set<TopicPartition>\n\n
    partitions()\n
    '''
def build():
    '''returns StopReplicaRequest\n\n
    build(final short version)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
