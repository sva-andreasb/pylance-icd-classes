CELLPREFIX = "String  \"cell=\""
NODEPREFIX = "String  \"node=\""
SERVERPREFIX = "String  \"process=\""
AUTHZGROUPPREFIX = "String  \"authorization=\""
BLAPREFIX = "String  \"bla=\""
CUSPREFIX = "String  \"cus=\""
ASSETPREFIX = "String  \"asset=\""
APPPREFIX = "String  \"Application=\""
CLUSTER_PREFIX = "String  \"name=\""
DELIM = "String  \",\""
NODEGROUPPREFIX = "String  \"nodegroup=\""
DELIM_CFGID = "String  \"/:|\""
def contains():
    '''returns boolean\n\n
    contains(final String resName, final String cfgType)\n
    '''
def getCellName():
    '''returns String\n\n
    getCellName(final String resourceName, final boolean mbean)\n
    '''
def getNodeGroupName():
    '''returns String\n\n
    getNodeGroupName(final String resourceName, final boolean mbean)\n
    '''
def getNodeName():
    '''returns String\n\n
    getNodeName(final String resourceName, final boolean mbean)\n
    '''
def getServerName():
    '''returns String\n\n
    getServerName(final String resourceName, final boolean mbean)\n
    '''
def getAuthzGroupName():
    '''returns String\n\n
    getAuthzGroupName(final String resourceName, final boolean mbean)\n
    '''
def getBlaName():
    '''returns String\n\n
    getBlaName(final String resourceName, final boolean mbean)\n
    '''
def getCusName():
    '''returns String\n\n
    getCusName(final String resourceName, final boolean mbean)\n
    '''
def getAssetName():
    '''returns String\n\n
    getAssetName(final String resourceName, final boolean mbean)\n
    '''
def getClusterName():
    '''returns String\n\n
    getClusterName(final String resourceName, final boolean mbean)\n
    '''
def getAppName():
    '''returns String\n\n
    getAppName(final String resourceName, final String methodName, final boolean mbean)\n
    '''
