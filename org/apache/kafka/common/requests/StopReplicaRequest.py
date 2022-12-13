def schemaVersions():
'''public static Schema[] schemaVersions()
'''
pass
def StopReplicaRequest():
'''public StopReplicaRequest(final Struct struct, final short version)
'''
pass
def getErrorResponse():
'''public StopReplicaResponse getErrorResponse(final int throttleTimeMs, final Throwable e)
'''
pass
def controllerId():
'''public int controllerId()
'''
pass
def controllerEpoch():
'''public int controllerEpoch()
'''
pass
def deletePartitions():
'''public boolean deletePartitions()
'''
pass
def partitions():
'''public Set<TopicPartition> partitions()
'''
pass
def parse():
'''public static StopReplicaRequest parse(final ByteBuffer buffer, final short version)
'''
pass
def Builder():
'''public Builder(final int controllerId, final int controllerEpoch, final boolean deletePartitions, final Set<TopicPartition> partitions)
'''
pass
def build():
'''public StopReplicaRequest build(final short version)
'''
pass
def toString():
'''public String toString()
'''
pass
