def ():
    '''returns ApiServerWorker\n\n
    (final TopologyManagerFactory topologyManagerFactory, final ApiProps apiProps)\n
    (final TopologyManagerFactory topologyManagerFactory, final TopologyBuilderFactory topologyBuilderFactory, final ApiProps props)\n
    '''
def login():
    '''returns String\n\n
    login(final ApiServerBean bean, final String user, final String password, final String clientIp, final long version)\n
    '''
def logout():
    '''returns None\n\n
    logout(final ApiServerBean bean, final String sessionId)\n
    '''
def getTopLevelClasses():
    '''returns ArrayList\n\n
    getTopLevelClasses(final ApiServerBean bean, final String sessionId)\n
    '''
def getClassNames():
    '''returns String[]\n\n
    getClassNames(final String sessionId)\n
    '''
def isBusinessService():
    '''returns boolean\n\n
    isBusinessService(final ModelObject mo)\n
    '''
def isApplication():
    '''returns boolean\n\n
    isApplication(final ModelObject mo)\n
    '''
def beginTransaction():
    '''returns None\n\n
    beginTransaction(final ApiServerBean bean, final String sessionId, final int timeout)\n
    '''
def run():
    '''returns None\n\n
    run()\n
    '''
def commitTransaction():
    '''returns None\n\n
    commitTransaction(final ApiServerBean bean, final String sessionId)\n
    '''
def rollback():
    '''returns None\n\n
    rollback(final ApiServerBean bean, final String sessionId)\n
    '''
def getMetaData():
    '''returns ObjectClass\n\n
    getMetaData(final String className, final boolean flatten)\n
    '''
def getInventorySummary():
    '''returns String\n\n
    getInventorySummary(final boolean cached, final String fileName)\n
    '''
def getAllMeta():
    '''returns ObjectClass[]\n\n
    getAllMeta(final boolean flatten)\n
    '''
def getUser():
    '''returns String\n\n
    getUser(final ApiServerBean bean, final String sessionId)\n
    '''
def startBulkload():
    '''returns long\n\n
    startBulkload(final long timeout)\n
    '''
def setBulkloadId():
    '''returns None\n\n
    setBulkloadId(final long bulkloadId)\n
    '''
def endBulkload():
    '''returns None\n\n
    endBulkload(final long transactionId)\n
    '''
