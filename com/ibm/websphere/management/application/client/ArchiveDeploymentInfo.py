destModPath = "String  \"ibm.update.mod.path\""
JAR_XML_EXT_URI = "String  \"META-INF/ibm-ejb-jar-ext.xml\""
JAR_XMI_BINDINGS_URI = "String  \"META-INF/ibm-ejb-jar-bnd.xmi\""
APP_XML_BINDINGS_URI = "String  \"META-INF/ibm-application-bnd.xml\""
APP_XMI_BINDINGS_URI = "String  \"META-INF/ibm-application-bnd.xmi\""
WAR_XMI_BINDINGS_URI = "String  \"WEB-INF/ibm-web-bnd.xmi\""
def ArchiveDeploymentInfo():
    '''    public ArchiveDeploymentInfo(final EARFile ear)
    public ArchiveDeploymentInfo(final EARFile ear, final Hashtable prefs)
    '''
def getModuleForDD():
    '''    public Module getModuleForDD(final EObject obj)
    '''
def getModuleFileForDD():
    '''    public ModuleFile getModuleFileForDD(final EObject obj)
    '''
def close():
    '''    public void close(final boolean bSave)
    '''
def getSavedResults():
    '''    public Hashtable getSavedResults()
    '''
def createDefaultBindings():
    '''    public void createDefaultBindings(final Preferences prefs)
    '''
def getSecurityPolicyData():
    '''    public String getSecurityPolicyData(final ResourceBundle resBundle)
    '''
def getSecurityPolicyWarning():
    '''    public String getSecurityPolicyWarning()
    '''
def saveAsFile():
    '''    public void saveAsFile(final String moduleUri, final String fileUriInModule, final InputStream in)
    public static String saveAsFile(final EARFile archive, final String moduleUri, final String fileUriInModule, final InputStream in)
    '''
def getAppDisplayName():
    '''    public String getAppDisplayName()
    '''
def getURI():
    '''    public String getURI()
    '''
def getResource():
    '''    public Resource getResource(final String modUri, final String uri, final String resURI)
    '''
def getAppDeploymentResource():
    '''    public Resource getAppDeploymentResource(final boolean processEmbeddedCfg)
    '''
def getAppDeploymentObject():
    '''    public ApplicationDeployment getAppDeploymentObject(final boolean processEmbeddedCfg)
    '''
def checkIfEarDeployed():
    '''    public boolean checkIfEarDeployed()
    '''
def checkIfEnhancedEar():
    '''    public boolean checkIfEnhancedEar()
    '''
def isStandaloneDeployment():
    '''    public boolean isStandaloneDeployment()
    '''
def getInputStream():
    '''    public InputStream getInputStream(final String moduleURI, final String fileURI)
    '''
def containsURI():
    '''    public boolean containsURI(final String moduleURI, final String fileURI)
    '''
def loadClass():
    '''    public Class loadClass(final EObject obj, final String className, final String type)
    '''
def loadJCAProps():
    '''    public static Hashtable loadJCAProps(final org.eclipse.jst.j2ee.commonarchivecore.internal.EARFile earFile)
    '''
def getEarManifest():
    '''    public ArchiveManifest getEarManifest()
    '''
def getEnhancedEarDeploymentResource():
    '''    public Resource getEnhancedEarDeploymentResource(final String resourceName)
    '''
