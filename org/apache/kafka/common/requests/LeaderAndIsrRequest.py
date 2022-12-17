def ():
    '''returns PartitionState\n\n
    (final Struct struct, final short version)\n
    (final short version, final int controllerId, final int controllerEpoch, final Map<TopicPartition, PartitionState> partitionStates, final Set<Node> liveLeaders)\n
    (final int controllerEpoch, final int leader, final int leaderEpoch, final List<Integer> isr, final int zkVersion, final List<Integer> replicas, final boolean isNew)\n
    '''
def getErrorResponse():
    '''returns LeaderAndIsrResponse\n\n
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
def liveLeaders():
    '''returns Set<Node>\n\n
    liveLeaders()\n
    '''
def build():
    '''returns LeaderAndIsrRequest\n\n
    build(final short version)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString()\n
    '''
