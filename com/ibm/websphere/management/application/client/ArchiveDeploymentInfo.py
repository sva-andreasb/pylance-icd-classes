destModPath = "String  ibm.update.mod.path""
JAR_XML_EXT_URI = "String  META-INF/ibm-ejb-jar-ext.xml""
JAR_XMI_BINDINGS_URI = "String  META-INF/ibm-ejb-jar-bnd.xmi""
APP_XML_BINDINGS_URI = "String  META-INF/ibm-application-bnd.xml""
APP_XMI_BINDINGS_URI = "String  META-INF/ibm-application-bnd.xmi""
WAR_XMI_BINDINGS_URI = "String  WEB-INF/ibm-web-bnd.xmi""
def ArchiveDeploymentInfo():
'''public ArchiveDeploymentInfo(final EARFile ear)
public ArchiveDeploymentInfo(final EARFile ear, final Hashtable prefs)
'''
pass
def getModuleForDD():
'''public Module getModuleForDD(final EObject obj)
'''
pass
def getModuleFileForDD():
'''public ModuleFile getModuleFileForDD(final EObject obj)
'''
pass
def close():
'''public void close(final boolean bSave)
'''
pass
def getSavedResults():
'''public Hashtable getSavedResults()
'''
pass
def createDefaultBindings():
'''public void createDefaultBindings(final Preferences prefs)
'''
pass
def getSecurityPolicyData():
'''public String getSecurityPolicyData(final ResourceBundle resBundle)
'''
pass
def getSecurityPolicyWarning():
'''public String getSecurityPolicyWarning()
'''
pass
def saveAsFile():
'''public void saveAsFile(final String moduleUri, final String fileUriInModule, final InputStream in)
public static String saveAsFile(final EARFile archive, final String moduleUri, final String fileUriInModule, final InputStream in)
'''
pass
def getAppDisplayName():
'''public String getAppDisplayName()
'''
pass
def getURI():
'''public String getURI()
'''
pass
def getResource():
'''public Resource getResource(final String modUri, final String uri, final String resURI)
'''
pass
def getAppDeploymentResource():
'''public Resource getAppDeploymentResource(final boolean processEmbeddedCfg)
'''
pass
def getAppDeploymentObject():
'''public ApplicationDeployment getAppDeploymentObject(final boolean processEmbeddedCfg)
'''
pass
def checkIfEarDeployed():
'''public boolean checkIfEarDeployed()
'''
pass
def checkIfEnhancedEar():
'''public boolean checkIfEnhancedEar()
'''
pass
def isStandaloneDeployment():
'''public boolean isStandaloneDeployment()
'''
pass
def getInputStream():
'''public InputStream getInputStream(final String moduleURI, final String fileURI)
'''
pass
def containsURI():
'''public boolean containsURI(final String moduleURI, final String fileURI)
'''
pass
def loadClass():
'''public Class loadClass(final EObject obj, final String className, final String type)
'''
pass
def loadJCAProps():
'''public static Hashtable loadJCAProps(final org.eclipse.jst.j2ee.commonarchivecore.internal.EARFile earFile)
'''
pass
def getEarManifest():
'''public ArchiveManifest getEarManifest()
'''
pass
def getEnhancedEarDeploymentResource():
'''public Resource getEnhancedEarDeploymentResource(final String resourceName)
'''
pass
