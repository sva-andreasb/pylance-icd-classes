destModPath = "String  \"ibm.update.mod.path\""
JAR_XML_EXT_URI = "String  \"META-INF/ibm-ejb-jar-ext.xml\""
JAR_XMI_BINDINGS_URI = "String  \"META-INF/ibm-ejb-jar-bnd.xmi\""
APP_XML_BINDINGS_URI = "String  \"META-INF/ibm-application-bnd.xml\""
APP_XMI_BINDINGS_URI = "String  \"META-INF/ibm-application-bnd.xmi\""
WAR_XMI_BINDINGS_URI = "String  \"WEB-INF/ibm-web-bnd.xmi\""
def ():
    '''returns ArchiveDeploymentInfo\n\n
    (final EARFile ear)\n
    (final EARFile ear, final Hashtable prefs)\n
    '''
def getModuleForDD():
    '''returns Module\n\n
    getModuleForDD(final EObject obj)\n
    '''
def getModuleFileForDD():
    '''returns ModuleFile\n\n
    getModuleFileForDD(final EObject obj)\n
    '''
def close():
    '''returns None\n\n
    close(final boolean bSave)\n
    '''
def getSavedResults():
    '''returns Hashtable\n\n
    getSavedResults()\n
    '''
def createDefaultBindings():
    '''returns None\n\n
    createDefaultBindings(final Preferences prefs)\n
    '''
def getSecurityPolicyData():
    '''returns String\n\n
    getSecurityPolicyData(final ResourceBundle resBundle)\n
    '''
def getSecurityPolicyWarning():
    '''returns String\n\n
    getSecurityPolicyWarning()\n
    '''
def saveAsFile():
    '''returns None\n\n
    saveAsFile(final String moduleUri, final String fileUriInModule, final InputStream in)\n
    '''
def getAppDisplayName():
    '''returns String\n\n
    getAppDisplayName()\n
    '''
def getURI():
    '''returns String\n\n
    getURI()\n
    '''
def getResource():
    '''returns Resource\n\n
    getResource(final String modUri, final String uri, final String resURI)\n
    '''
def getAppDeploymentResource():
    '''returns Resource\n\n
    getAppDeploymentResource(final boolean processEmbeddedCfg)\n
    '''
def getAppDeploymentObject():
    '''returns ApplicationDeployment\n\n
    getAppDeploymentObject(final boolean processEmbeddedCfg)\n
    '''
def checkIfEarDeployed():
    '''returns boolean\n\n
    checkIfEarDeployed()\n
    '''
def checkIfEnhancedEar():
    '''returns boolean\n\n
    checkIfEnhancedEar()\n
    '''
def isStandaloneDeployment():
    '''returns boolean\n\n
    isStandaloneDeployment()\n
    '''
def getInputStream():
    '''returns InputStream\n\n
    getInputStream(final String moduleURI, final String fileURI)\n
    '''
def containsURI():
    '''returns boolean\n\n
    containsURI(final String moduleURI, final String fileURI)\n
    '''
def loadClass():
    '''returns Class\n\n
    loadClass(final EObject obj, final String className, final String type)\n
    '''
def getEarManifest():
    '''returns ArchiveManifest\n\n
    getEarManifest()\n
    '''
def getEnhancedEarDeploymentResource():
    '''returns Resource\n\n
    getEnhancedEarDeploymentResource(final String resourceName)\n
    '''
