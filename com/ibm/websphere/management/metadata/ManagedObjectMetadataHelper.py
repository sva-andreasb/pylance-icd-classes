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
def ManagedObjectMetadataHelper():
    '''public ManagedObjectMetadataHelper(final ManagedObjectMetadataAccessor metadataAccessor)
    '''
def getAccessor():
    '''public ManagedObjectMetadataAccessor getAccessor()
    '''
def getNodeMajorVersion():
    '''public String getNodeMajorVersion(final String nodeName)
    '''
def getNodeMinorVersion():
    '''public String getNodeMinorVersion(final String nodeName)
    '''
def getNodeUpdateVersion():
    '''public String getNodeUpdateVersion(final String nodeName)
    '''
def getNodeServiceVersion():
    '''public String getNodeServiceVersion(final String nodeName)
    '''
def getNodeBaseProductVersion():
    '''public String getNodeBaseProductVersion(final String nodeName)
    '''
def getNodeBaseProductShortName():
    '''public String getNodeBaseProductShortName(final String nodeName)
    '''
def compareNodeVersion():
    '''public int compareNodeVersion(final String nodeName, final String version)
    '''
def isNodeZOS():
    '''public boolean isNodeZOS(final String nodeName)
    '''
def getNodePlatformOS():
    '''public String getNodePlatformOS(final String nodeName)
    '''
def getNodeSysplexName():
    '''public String getNodeSysplexName(final String nodeName)
    '''
def getNodeProductVersions():
    '''public SortedMap getNodeProductVersions(final String nodeName)
    '''
def getNodeDeployedFeatures():
    '''public ArrayList getNodeDeployedFeatures(final String nodeName)
    '''
def getNodeProductsAndVersions():
    '''public Properties getNodeProductsAndVersions(final String nodeName)
    '''
def listRuntimeComponents():
    '''public ArrayList listRuntimeComponents(final String nodeName)
    '''
def VersionParser():
    '''public VersionParser(final String inputString)
    '''
def hasMoreComponents():
    '''public boolean hasMoreComponents()
    '''
def nextComponent():
    '''public int nextComponent()
    '''
