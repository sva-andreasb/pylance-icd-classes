def ApiServerWorker():
'''public ApiServerWorker(final TopologyManagerFactory topologyManagerFactory, final ApiProps apiProps)
public ApiServerWorker(final TopologyManagerFactory topologyManagerFactory, final TopologyBuilderFactory topologyBuilderFactory, final ApiProps props)
'''
pass
def registerLocale():
'''public static void registerLocale(final String sessionId, final Locale locale)
'''
pass
def unregisterLocale():
'''public static void unregisterLocale(final String sessionId)
'''
pass
def login():
'''public String login(final ApiServerBean bean, final String user, final String password, final String clientIp, final long version)
'''
pass
def logout():
'''public void logout(final ApiServerBean bean, final String sessionId)
'''
pass
def getTopLevelClasses():
'''public ArrayList getTopLevelClasses(final ApiServerBean bean, final String sessionId)
'''
pass
def getClassNames():
'''public String[] getClassNames(final String sessionId)
'''
pass
def isBusinessService():
'''public boolean isBusinessService(final ModelObject mo)
'''
pass
def isApplication():
'''public boolean isApplication(final ModelObject mo)
'''
pass
def beginTransaction():
'''public void beginTransaction(final ApiServerBean bean, final String sessionId, final int timeout)
'''
pass
def run():
'''public void run()
'''
pass
def commitTransaction():
'''public void commitTransaction(final ApiServerBean bean, final String sessionId)
'''
pass
def rollback():
'''public void rollback(final ApiServerBean bean, final String sessionId)
'''
pass
def getMetaData():
'''public ObjectClass getMetaData(final String className, final boolean flatten)
'''
pass
def getInventorySummary():
'''public String getInventorySummary(final boolean cached, final String fileName)
'''
pass
def getAllMeta():
'''public ObjectClass[] getAllMeta(final boolean flatten)
'''
pass
def getUser():
'''public String getUser(final ApiServerBean bean, final String sessionId)
'''
pass
def startBulkload():
'''public long startBulkload(final long timeout)
'''
pass
def setBulkloadId():
'''public void setBulkloadId(final long bulkloadId)
'''
pass
def endBulkload():
'''public void endBulkload(final long transactionId)
'''
pass
