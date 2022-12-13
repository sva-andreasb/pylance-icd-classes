BASE_WAS_PRODUCT_VERSION = "String  com.ibm.websphere.baseProductVersion""
BASE_WAS_PRODUCT_SHORT_NAME = "String  com.ibm.websphere.baseProductShortName""
BASE_WAS_APP_ACTIVATION_PLANS = "String  com.ibm.websphere.baseRuntimeComponents""
NODE_OS = "String  com.ibm.websphere.nodeOperatingSystem""
NODE_OS_AS400 = "String  os400""
NODE_OS_AIX = "String  aix""
NODE_OS_HPUX = "String  hpux""
NODE_OS_LINUX = "String  linux""
NODE_OS_SOLARIS = "String  solaris""
NODE_OS_WINDOWS = "String  windows""
NODE_OS_ZOS = "String  os390""
NODE_SYSPLEX_NAME = "String  com.ibm.websphere.nodeSysplexName""
NODE_DEPLOYED_FEATURES = "String  com.ibm.websphere.deployed.features""
def ManagedObjectMetadataHelper():
'''public ManagedObjectMetadataHelper(final ManagedObjectMetadataAccessor metadataAccessor)
'''
pass
def getAccessor():
'''public ManagedObjectMetadataAccessor getAccessor()
'''
pass
def getNodeMajorVersion():
'''public String getNodeMajorVersion(final String nodeName)
'''
pass
def getNodeMinorVersion():
'''public String getNodeMinorVersion(final String nodeName)
'''
pass
def getNodeUpdateVersion():
'''public String getNodeUpdateVersion(final String nodeName)
'''
pass
def getNodeServiceVersion():
'''public String getNodeServiceVersion(final String nodeName)
'''
pass
def getNodeBaseProductVersion():
'''public String getNodeBaseProductVersion(final String nodeName)
'''
pass
def getNodeBaseProductShortName():
'''public String getNodeBaseProductShortName(final String nodeName)
'''
pass
def compareNodeVersion():
'''public int compareNodeVersion(final String nodeName, final String version)
'''
pass
def isNodeZOS():
'''public boolean isNodeZOS(final String nodeName)
'''
pass
def getNodePlatformOS():
'''public String getNodePlatformOS(final String nodeName)
'''
pass
def getNodeSysplexName():
'''public String getNodeSysplexName(final String nodeName)
'''
pass
def getNodeProductVersions():
'''public SortedMap getNodeProductVersions(final String nodeName)
'''
pass
def getNodeDeployedFeatures():
'''public ArrayList getNodeDeployedFeatures(final String nodeName)
'''
pass
def getNodeProductsAndVersions():
'''public Properties getNodeProductsAndVersions(final String nodeName)
'''
pass
def listRuntimeComponents():
'''public ArrayList listRuntimeComponents(final String nodeName)
'''
pass
def VersionParser():
'''public VersionParser(final String inputString)
'''
pass
def hasMoreComponents():
'''public boolean hasMoreComponents()
'''
pass
def nextComponent():
'''public int nextComponent()
'''
pass
