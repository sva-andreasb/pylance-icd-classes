def ():
    '''returns EndPoint\n\n
    (final Struct struct, final short versionId)\n
    (final short version, final int controllerId, final int controllerEpoch, final Map<TopicPartition, PartitionState> partitionStates, final Set<Broker> liveBrokers)\n
    (final int controllerEpoch, final int leader, final int leaderEpoch, final List<Integer> isr, final int zkVersion, final List<Integer> replicas, final List<Integer> offlineReplicas)\n
    (final int id, final List<EndPoint> endPoints, final String rack)\n
    (final String host, final int port, final SecurityProtocol securityProtocol, final ListenerName listenerName)\n
    '''
def getErrorResponse():
    '''returns AbstractResponse\n\n
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
def liveBrokers():
    '''returns Set<Broker>\n\n
    liveBrokers()\n
    '''
def build():
    '''returns UpdateMetadataRequest\n\n
    build(final short version)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString()\n
    toString()\n
    toString()\n
    '''
