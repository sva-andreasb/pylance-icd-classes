def addServerToMaxSession():
'''public static void addServerToMaxSession(final Connection con, final long sessionId, final String userId, final String serverHost, final String serverName, final int tenantId)
'''
pass
def deleteAllRowsForServer():
'''public static void deleteAllRowsForServer(Connection con, final String serverName, final String serverHost)
'''
pass
def unlockRecords():
'''public static void unlockRecords(final Connection con, final String serverName, final String serverHost)
'''
pass
def removeDeadTenantSession():
'''public static void removeDeadTenantSession(final Connection con)
'''
pass
def updateReloadCache():
'''public static void updateReloadCache(final Connection con, final String serverName, final String serverHost, final String reload, final boolean updateAllServers)
'''
pass
def getAllTeanants():
'''public static List<Integer> getAllTeanants(final Connection con)
'''
pass
def getAllServerNamesWithTimestamp():
'''public static Vector getAllServerNamesWithTimestamp(final Connection con)
'''
pass
def getAllServerNames():
'''public static Vector getAllServerNames(final Connection con)
'''
pass
def getAllServersInfo():
'''public static Vector getAllServersInfo(final Connection con)
'''
pass
def getServerInfo():
'''public static String getServerInfo(final Connection con, final String serverHost, final String serverName)
'''
pass
def getAllTenantsServerInfo():
'''public static Map<Integer, String> getAllTenantsServerInfo(final Connection con, final String serverHost, final String serverName)
'''
pass
def getTenantList():
'''public static List<Integer> getTenantList(final Connection con, final String serverName, final String serverHost)
'''
pass
def getNewReloadCacheForOwnerServer():
'''public static String getNewReloadCacheForOwnerServer(final String dbReloadCache, final String cacheName)
'''
pass
def updateExecute():
'''public static int updateExecute(final Connection con, final String serverHost, final String serverName, final String newCacheValue, final String oldValue, final boolean updateHeartbeat)
'''
pass
def updateMaxSessionTimestamp():
'''public static void updateMaxSessionTimestamp(final Connection con, final String serverHost, final String serverName)
'''
pass
