DISCOVERY_ADD_INSTANCE_NAME = "String  \"AddNewDiscoveredCIs\""
DISCOVERY_ADD_ACTION_NAME = "String  \"AddOnlyNew\""
DISCOVERY_UPDATE_INSTANCE_NAME = "String  \"AddUpdateDiscoveredCIs\""
DISCOVERY_UPDATE_ACTION_NAME = "String  \"AddChange\""
DISCOVERY_ACTION_PARAM_NAME = "String  \"ACTION\""
DISCOVERY_SCOPE_PARAM_NAME = "String  \"SCOPE\""
DISCOVERY_SERVICENAME_PARAM_NAME = "String  \"SERVICENAME\""
DISCOVERY_SYSTEMNAME_PARAM_NAME = "String  \"SYSTEMNAME\""
DISCOVERY_ACTION_PARAM_DEFAULT = "String  \"AddChange\""
DISCOVERY_SCOPE_PARAM_DEFAULT = "String  \"\""
DISCOVERY_SERVICENAME_PARAM_DEFAULT = "String  \"MXCIImport\""
DISCOVERY_SYSTEMNAME_PARAM_DEFAULT = "String  \"SRM_SaaS_ES\""
ID_SIMPLE_FORMAT = "String  \"SIMPLECI\""
def retrieveMboInfo():
    '''public static List<String>[] retrieveMboInfo(final String ifaceName, final boolean parent)
    '''
def retrieveMBOList():
    '''public static Map<String, String> retrieveMBOList(final String obj, final String columnName, final String attribute, final String value, final String where, final String secondColumn)
    '''
def loadStaticLists():
    '''public static void loadStaticLists(final String ciClassificationId)
    '''
def parseScope():
    '''public static String[] parseScope(final String providedScope)
    '''
def releaseStaticListsResources():
    '''public static void releaseStaticListsResources()
    '''
def deleteOldCSNowResolved():
    '''public static void deleteOldCSNowResolved(final Map<Object, String> discoveredSys)
    '''
def deleteOldIPRelationships():
    '''public static void deleteOldIPRelationships(final Map<Object, String> discoveredSys)
    '''
