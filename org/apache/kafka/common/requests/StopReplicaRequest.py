def schemaVersions():
    '''    public static Schema[] schemaVersions()
    '''
def StopReplicaRequest():
    '''    public StopReplicaRequest(final Struct struct, final short version)
    '''
def getErrorResponse():
    '''    public StopReplicaResponse getErrorResponse(final int throttleTimeMs, final Throwable e)
    '''
def controllerId():
    '''    public int controllerId()
    '''
def controllerEpoch():
    '''    public int controllerEpoch()
    '''
def deletePartitions():
    '''    public boolean deletePartitions()
    '''
def partitions():
    '''    public Set<TopicPartition> partitions()
    '''
def parse():
    '''    public static StopReplicaRequest parse(final ByteBuffer buffer, final short version)
    '''
def Builder():
    '''    public Builder(final int controllerId, final int controllerEpoch, final boolean deletePartitions, final Set<TopicPartition> partitions)
    '''
def build():
    '''    public StopReplicaRequest build(final short version)
    '''
def toString():
    '''    public String toString()
    '''
