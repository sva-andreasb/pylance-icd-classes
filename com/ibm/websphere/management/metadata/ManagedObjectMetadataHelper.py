BASE_WAS_PRODUCT_VERSION = "String  \"com.ibm.websphere.baseProductVersion\""
BASE_WAS_PRODUCT_SHORT_NAME = "String  \"com.ibm.websphere.baseProductShortName\""
BASE_WAS_APP_ACTIVATION_PLANS = "String  \"com.ibm.websphere.baseRuntimeComponents\""
NODE_OS = "String  \"com.ibm.websphere.nodeOperatingSystem\""
NODE_OS_AS400 = "String  \"os400\""
NODE_OS_AIX = "String  \"aix\""
NODE_OS_HPUX = "String  \"hpux\""
NODE_OS_LINUX = "String  \"linux\""
NODE_OS_SOLARIS = "String  \"solaris\""
NODE_OS_WINDOWS = "String  \"windows\""
NODE_OS_ZOS = "String  \"os390\""
NODE_SYSPLEX_NAME = "String  \"com.ibm.websphere.nodeSysplexName\""
NODE_DEPLOYED_FEATURES = "String  \"com.ibm.websphere.deployed.features\""
def ():
    '''returns VersionParser\n\n
    (final ManagedObjectMetadataAccessor metadataAccessor)\n
    (final String inputString)\n
    '''
def getAccessor():
    '''returns ManagedObjectMetadataAccessor\n\n
    getAccessor()\n
    '''
def getNodeMajorVersion():
    '''returns String\n\n
    getNodeMajorVersion(final String nodeName)\n
    '''
def getNodeMinorVersion():
    '''returns String\n\n
    getNodeMinorVersion(final String nodeName)\n
    '''
def getNodeUpdateVersion():
    '''returns String\n\n
    getNodeUpdateVersion(final String nodeName)\n
    '''
def getNodeServiceVersion():
    '''returns String\n\n
    getNodeServiceVersion(final String nodeName)\n
    '''
def getNodeBaseProductVersion():
    '''returns String\n\n
    getNodeBaseProductVersion(final String nodeName)\n
    '''
def getNodeBaseProductShortName():
    '''returns String\n\n
    getNodeBaseProductShortName(final String nodeName)\n
    '''
def compareNodeVersion():
    '''returns int\n\n
    compareNodeVersion(final String nodeName, final String version)\n
    '''
def isNodeZOS():
    '''returns boolean\n\n
    isNodeZOS(final String nodeName)\n
    '''
def getNodePlatformOS():
    '''returns String\n\n
    getNodePlatformOS(final String nodeName)\n
    '''
def getNodeSysplexName():
    '''returns String\n\n
    getNodeSysplexName(final String nodeName)\n
    '''
def getNodeProductVersions():
    '''returns SortedMap\n\n
    getNodeProductVersions(final String nodeName)\n
    '''
def getNodeDeployedFeatures():
    '''returns ArrayList\n\n
    getNodeDeployedFeatures(final String nodeName)\n
    '''
def getNodeProductsAndVersions():
    '''returns Properties\n\n
    getNodeProductsAndVersions(final String nodeName)\n
    '''
def listRuntimeComponents():
    '''returns ArrayList\n\n
    listRuntimeComponents(final String nodeName)\n
    '''
def hasMoreComponents():
    '''returns boolean\n\n
    hasMoreComponents()\n
    '''
def nextComponent():
    '''returns int\n\n
    nextComponent()\n
    '''
