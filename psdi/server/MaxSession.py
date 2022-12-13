def addServerToMaxSession():
    '''public static void addServerToMaxSession(final Connection con, final long sessionId, final String userId, final String serverHost, final String serverName, final int tenantId)
    '''
def deleteAllRowsForServer():
    '''public static void deleteAllRowsForServer(Connection con, final String serverName, final String serverHost)
    '''
def unlockRecords():
    '''public static void unlockRecords(final Connection con, final String serverName, final String serverHost)
    '''
def removeDeadTenantSession():
    '''public static void removeDeadTenantSession(final Connection con)
    '''
def updateReloadCache():
    '''public static void updateReloadCache(final Connection con, final String serverName, final String serverHost, final String reload, final boolean updateAllServers)
    '''
def getAllTeanants():
    '''public static List<Integer> getAllTeanants(final Connection con)
    '''
def getAllServerNamesWithTimestamp():
    '''public static Vector getAllServerNamesWithTimestamp(final Connection con)
    '''
def getAllServerNames():
    '''public static Vector getAllServerNames(final Connection con)
    '''
def getAllServersInfo():
    '''public static Vector getAllServersInfo(final Connection con)
    '''
def getServerInfo():
    '''public static String getServerInfo(final Connection con, final String serverHost, final String serverName)
    '''
def getAllTenantsServerInfo():
    '''public static Map<Integer, String> getAllTenantsServerInfo(final Connection con, final String serverHost, final String serverName)
    '''
def getTenantList():
    '''public static List<Integer> getTenantList(final Connection con, final String serverName, final String serverHost)
    '''
def getNewReloadCacheForOwnerServer():
    '''public static String getNewReloadCacheForOwnerServer(final String dbReloadCache, final String cacheName)
    '''
def updateExecute():
    '''public static int updateExecute(final Connection con, final String serverHost, final String serverName, final String newCacheValue, final String oldValue, final boolean updateHeartbeat)
    '''
def updateMaxSessionTimestamp():
    '''public static void updateMaxSessionTimestamp(final Connection con, final String serverHost, final String serverName)
    '''
