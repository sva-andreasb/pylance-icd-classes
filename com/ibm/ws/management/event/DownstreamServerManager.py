TIMEOUT = "int  120000"
OP_ADD_DOWNSTREAM_SERVER = "int  0"
OP_REMOVE_DOWNSTREAM_SERVER = "int  1"
OP_UPDATE_LISTENERS = "int  2"
def ():
    '''returns QueueConsumerThread\n\n
    ()\n
    (final int operation, final ServerInfo[] serverInfoList)\n
    (final int operation, final ServerInfo serverInfo)\n
    (final ThreadManager threadManager)\n
    (final ServerInfo serverInfo, final int queueNumber)\n
    (final ServerUpdateOpInfo opInfo, final int serverInfoListIndex)\n
    ()\n
    (final ThreadManager threadManager, final int threadIndex, final String profileKey)\n
    '''
def addDownstreamServer():
    '''returns None\n\n
    addDownstreamServer(final ServerInfo serverInfo)\n
    '''
def addDownstreamProcess():
    '''returns None\n\n
    addDownstreamProcess(final ServerInfo serverInfo)\n
    '''
def removeDownstreamServer():
    '''returns None\n\n
    removeDownstreamServer(final ServerInfo serverInfo)\n
    '''
def removeDownstreamProcess():
    '''returns None\n\n
    removeDownstreamProcess(final ServerInfo serverInfo)\n
    '''
def setFilter():
    '''returns None\n\n
    setFilter(final Object id, final ConsolidatedFilter filter, final String targetProcess)\n
    '''
def unsetFilter():
    '''returns None\n\n
    unsetFilter(final Object id)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString()\n
    '''
def getOperation():
    '''returns int\n\n
    getOperation()\n
    getOperation()\n
    '''
def getServerInfoList():
    '''returns ServerInfo[]\n\n
    getServerInfoList()\n
    '''
def getServerInfo():
    '''returns ServerInfo\n\n
    getServerInfo(final int serverInfoListIndex)\n
    getServerInfo()\n
    getServerInfo()\n
    '''
def getQueueNumber():
    '''returns int\n\n
    getQueueNumber()\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def getServerOpInfo():
    '''returns ServerUpdateOpInfo\n\n
    getServerOpInfo()\n
    '''
def run():
    '''returns None\n\n
    run()\n
    '''
