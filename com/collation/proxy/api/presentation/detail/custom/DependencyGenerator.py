APPLICATIONS_FOR_SOFTWARE_SERVERS = "int  1"
BUSINESS_SERVICES_FOR_SOFTWARE_SERVERS = "int  2"
SERVICE_TRANSACTIONAL_DEPENDENCIES = "int  3"
APPLICATIONS_FOR_HOST = "int  4"
BIZ_SERVICES_FOR_HOST = "int  5"
CONTAINED_SOFTWARE_SERVERS_FOR_HOST = "int  6"
DEPENDENT = "int  1"
PROVIDER = "int  2"
def handleApplicationSoftwareServer():
    '''public static List handleApplicationSoftwareServer(final Guid objectId, final long version, final SessionContext session)
    '''
def handleBusinessServiceNonHost():
    '''public static List handleBusinessServiceNonHost(final TopologyManager tm, final Guid objectId)
    '''
def handleComponentNonHosts():
    '''public static List handleComponentNonHosts(final long version, final SessionContext session, final List ids)
    '''
def handleComponentNonHost():
    '''public static List handleComponentNonHost(final long version, final SessionContext session, final Guid objectId)
    '''
def handleApplicationHost():
    '''public static List handleApplicationHost(final Guid hostId, final TopologyManager tm)
    '''
def handleBusinessServiceHost():
    '''public static List handleBusinessServiceHost(final Guid objectId, final TopologyManager tm)
    '''
def handleComponentHost():
    '''public static List handleComponentHost(final Guid objectId, final long version, final SessionContext session)
    '''
def getDependency():
    '''public static List getDependency(final int queryType, final Guid objectId, final long version, final SessionContext session, final TopologyManager tm)
    '''
def filterUnknownServers():
    '''public static void filterUnknownServers(final Map modelObjects)
    '''
def getCollationType():
    '''public static String getCollationType(final ModelObject modelObject)
    '''
def getTypes():
    '''public static Class[] getTypes(final int type)
    '''
def getClusterComponents():
    '''public static ArrayList getClusterComponents(final long version, final SessionContext session, final Guid guid)
    '''
