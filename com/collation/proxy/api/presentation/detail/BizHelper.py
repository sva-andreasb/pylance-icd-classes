def getApplicationComponents():
    '''public static List getApplicationComponents(final Guid guid, final long version, final SessionContext session)
    '''
def getAppDependentComponents():
    '''public static ArrayList getAppDependentComponents(final long version, final Guid guid, final SessionContext session)
    '''
def getDependencies():
    '''public static List getDependencies(final List comp, final long version, final SessionContext session)
    '''
def getAppServerIdsFromCluster():
    '''public static List getAppServerIdsFromCluster(final Guid id, final long version, final SessionContext session)
    '''
def getAppDependentHosts():
    '''public static ArrayList getAppDependentHosts(final long version, final SessionContext session, final Guid id)
    '''
def getHosts():
    '''public static List getHosts(final List components, final long version, final SessionContext session)
    '''
def getHost():
    '''public static ModelObject getHost(final ModelObject mo)
    '''
def getBizServiceComponents():
    '''public static ArrayList getBizServiceComponents(final long version, final SessionContext session, final Guid guid)
    '''
def getBizServiceDependentComponents():
    '''public static ArrayList getBizServiceDependentComponents(final long version, final SessionContext session, final Guid guid)
    '''
def handleApplicationsInsizeBizService():
    '''public static List handleApplicationsInsizeBizService(final ModelObjectLite modelObjectLite, final Guid guid, final long version, final SessionContext session)
    '''
def getBizServiceDependentHosts():
    '''public static ArrayList getBizServiceDependentHosts(final Guid guid, final long version, final SessionContext session)
    '''
