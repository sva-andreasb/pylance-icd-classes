APPDEPL_SYSTEM_APP2_FLAG = "String  META-INF/ibm-application-sa2.props""
def getNodeVersionForAppTargets():
'''public static Hashtable getNodeVersionForAppTargets(final Hashtable servertbl, final RepositoryContext cellContext, final WorkSpace ws)
public static Hashtable getNodeVersionForAppTargets(final Vector v, final String cellName, final WorkSpace ws)
'''
pass
def getNodeInfoForTargets():
'''public static Map<ObjectName, Set<NodeInfo>> getNodeInfoForTargets(final WorkSpace workSpace, final RepositoryContext cellContext, final Map<String, String> moduleToServers)
public static Map<ObjectName, Set<NodeInfo>> getNodeInfoForTargets(final WorkSpace workSpace, final String cellName, final Set<RepositoryContext> servers)
'''
pass
def appValidation():
'''public static Vector appValidation(final AppDeploymentController controller, final String cellName, final WorkSpace ws)
public static Vector appValidation(final int rarVersion, final int earVersion, final int appVersion, final List options, final Hashtable targetnodeVersionTable)
public static Vector appValidation(final int rarVersion, final int earVersion, final int appVersion, final List options, final Hashtable targetnodeVersionTable, final EARFile earFile, final String sessionId)
public static Vector appValidation(final int rarVersion, final int earVersion, final int appVersion, final List options, final Hashtable targetnodeVersionTable, final EARFile earFile, final Hashtable currentTargetNodeVersionTable, final Archive module, final String sessionId)
'''
pass
def MDBValidation():
'''public static Vector MDBValidation(final Hashtable targetVersionTable, final Hashtable servertbl, final AppDeploymentTask mdbTask)
'''
pass
def validateLightweightEJBs():
'''public static Vector validateLightweightEJBs(final EARFile earFile, final Hashtable targetNodes)
'''
pass
def listSystemApps():
'''public static List listSystemApps(final Repository repo)
'''
pass
def getTargetName():
'''public static String getTargetName(final String serverName, final String node, final String cell, final boolean isCluster)
'''
pass
def getModuleID():
'''public static String getModuleID(final String name, final String type)
'''
pass
def createTargetMod():
'''public static TargetModuleIDImpl createTargetMod(final String name, final String type, final Target target, final TargetModuleID parent)
'''
pass
def getFilePermissionOptions():
'''public static String[][] getFilePermissionOptions(final Hashtable props)
'''
pass
def getFilePermissionString():
'''public static String getFilePermissionString(final List l)
'''
pass
def envEntryValidation():
'''public static Vector envEntryValidation(final EARFile earfile, final ResourceBundle res)
'''
pass
def validateEnvEntry():
'''public static Vector validateEnvEntry(final List _envEntries, final String uri, final ResourceBundle res)
'''
pass
def getTargetNodes():
'''public static List getTargetNodes(final Scheduler sch, final String moduleURI, final String ddURI)
'''
pass
def isNodeValidForCluster():
'''public static void isNodeValidForCluster(final String cellName, final String nodeName, final String clusterName, final String workspaceID, final Locale locale, final List errors)
'''
pass
def isEE5SchemaDD():
'''public static boolean isEE5SchemaDD(final Module module, final Archive archive)
public static boolean isEE5SchemaDD(final ModuleFile moduleFile)
'''
pass
def getModuleVersion():
'''public static int getModuleVersion(final ModuleFile moduleFile)
'''
pass
def getActivationPlanForV6SysApp():
'''public Hashtable<String, List<ObjectName>> getActivationPlanForV6SysApp(final String binURLExpanded)
'''
pass
def getDeploymentDescriptorXMLOnly():
'''public static EObject getDeploymentDescriptorXMLOnly(final AppDeploymentInfo appDeployInfo, final EObject mergedDeploymentDescriptor)
'''
pass
def checkWeb25Modules():
'''public static boolean checkWeb25Modules(final EARFile earFile)
public static boolean checkWeb25Modules(final EARFile earFile, final Hashtable props)
'''
pass
def checkEJB3Modules():
'''public static boolean checkEJB3Modules(final EARFile earFile)
public static boolean checkEJB3Modules(final EARFile earFile, final Hashtable props)
'''
pass