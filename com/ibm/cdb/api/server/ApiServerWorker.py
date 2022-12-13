def ApiServerWorker():
    '''public ApiServerWorker(final TopologyManagerFactory topologyManagerFactory, final ApiProps apiProps)
    public ApiServerWorker(final TopologyManagerFactory topologyManagerFactory, final TopologyBuilderFactory topologyBuilderFactory, final ApiProps props)
    '''
def registerLocale():
    '''public static void registerLocale(final String sessionId, final Locale locale)
    '''
def unregisterLocale():
    '''public static void unregisterLocale(final String sessionId)
    '''
def login():
    '''public String login(final ApiServerBean bean, final String user, final String password, final String clientIp, final long version)
    '''
def logout():
    '''public void logout(final ApiServerBean bean, final String sessionId)
    '''
def getTopLevelClasses():
    '''public ArrayList getTopLevelClasses(final ApiServerBean bean, final String sessionId)
    '''
def getClassNames():
    '''public String[] getClassNames(final String sessionId)
    '''
def isBusinessService():
    '''public boolean isBusinessService(final ModelObject mo)
    '''
def isApplication():
    '''public boolean isApplication(final ModelObject mo)
    '''
def beginTransaction():
    '''public void beginTransaction(final ApiServerBean bean, final String sessionId, final int timeout)
    '''
def run():
    '''public void run()
    '''
def commitTransaction():
    '''public void commitTransaction(final ApiServerBean bean, final String sessionId)
    '''
def rollback():
    '''public void rollback(final ApiServerBean bean, final String sessionId)
    '''
def getMetaData():
    '''public ObjectClass getMetaData(final String className, final boolean flatten)
    '''
def getInventorySummary():
    '''public String getInventorySummary(final boolean cached, final String fileName)
    '''
def getAllMeta():
    '''public ObjectClass[] getAllMeta(final boolean flatten)
    '''
def getUser():
    '''public String getUser(final ApiServerBean bean, final String sessionId)
    '''
def startBulkload():
    '''public long startBulkload(final long timeout)
    '''
def setBulkloadId():
    '''public void setBulkloadId(final long bulkloadId)
    '''
def endBulkload():
    '''public void endBulkload(final long transactionId)
    '''
