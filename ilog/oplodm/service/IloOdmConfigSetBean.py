COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
DATASOURCES_PATH_IN_JAR = "String  \"dataSources\""
def ():
    '''returns DCPJarableFile\n\n
    (final URL[] baseURLs, final File odmAppFile)\n
    (final URL[] baseURLs, final URL odmAppURL)\n
    (final OutputStream ostream)\n
    (final IloDecisionProcessConfiguration config, final URL realURL, final String pathInJar)\n
    '''
def getOdmAppDir():
    '''returns File\n\n
    getOdmAppDir()\n
    '''
def getOdmAppURL():
    '''returns URL\n\n
    getOdmAppURL()\n
    '''
def getClassPathCollectionURLs():
    '''returns ListIterator<URL>\n\n
    getClassPathCollectionURLs()\n
    '''
def addClasspathURL():
    '''returns None\n\n
    addClasspathURL(final URL jarOrDir)\n
    '''
def isUsingCompiledModels():
    '''returns boolean\n\n
    isUsingCompiledModels()\n
    '''
def setUsingCompiledModels():
    '''returns None\n\n
    setUsingCompiledModels(final boolean compiledModels)\n
    '''
def setRelationalModelDescURL():
    '''returns None\n\n
    setRelationalModelDescURL(final URL rm)\n
    '''
def setStudioDefaultSettingsURL():
    '''returns None\n\n
    setStudioDefaultSettingsURL(final URL studioDefaultSettings)\n
    '''
def getDeploymentDescURL():
    '''returns URL\n\n
    getDeploymentDescURL()\n
    '''
def getRelationalModelDescURL():
    '''returns URL\n\n
    getRelationalModelDescURL()\n
    '''
def getStudioDefaultSettingsURL():
    '''returns URL\n\n
    getStudioDefaultSettingsURL()\n
    '''
def getStudioDescURL():
    '''returns URL\n\n
    getStudioDescURL()\n
    '''
def getOptimDescURL():
    '''returns URL\n\n
    getOptimDescURL()\n
    '''
def setOptimDescURL():
    '''returns None\n\n
    setOptimDescURL(final URL optim)\n
    '''
def setDataSourcesDescURL():
    '''returns None\n\n
    setDataSourcesDescURL(final URL datasources)\n
    '''
def setViewsDescURL():
    '''returns None\n\n
    setViewsDescURL(final URL views)\n
    '''
def setOplModelURL():
    '''returns None\n\n
    setOplModelURL(final URL oplModel)\n
    '''
def getOplModelURL():
    '''returns URL\n\n
    getOplModelURL()\n
    '''
def setMappingURL():
    '''returns None\n\n
    setMappingURL(final URL mappingDat)\n
    '''
def getMappingDatURL():
    '''returns URL\n\n
    getMappingDatURL()\n
    '''
def addComplementaryDatURL():
    '''returns None\n\n
    addComplementaryDatURL(final URL compDatFile)\n
    '''
def getComplementaryDataURLs():
    '''returns Iterator<URL>\n\n
    getComplementaryDataURLs()\n
    '''
def addSettingsURL():
    '''returns boolean\n\n
    addSettingsURL(final URL settingsURL)\n
    '''
def addSettingsURLs():
    '''returns int\n\n
    addSettingsURLs(final List<URL> settingsURLList)\n
    '''
def getSettingsURLs():
    '''returns Iterator<URL>\n\n
    getSettingsURLs()\n
    '''
def addSubModelURL():
    '''returns None\n\n
    addSubModelURL(final URL model)\n
    '''
def getOplSubModelURL():
    '''returns URL\n\n
    getOplSubModelURL(final String modelName)\n
    '''
def getOplSubModelURLs():
    '''returns Iterator<URL>\n\n
    getOplSubModelURLs()\n
    '''
def openStream():
    '''returns InputStream\n\n
    openStream()\n
    openStream()\n
    '''
def getConfigSetFile():
    '''returns IloJarableFile\n\n
    getConfigSetFile()\n
    '''
def setExtendedViewsURL():
    '''returns None\n\n
    setExtendedViewsURL(final URL url)\n
    '''
def getExtendedViewsURL():
    '''returns URL\n\n
    getExtendedViewsURL()\n
    '''
def getExtendedViews():
    '''returns IloViewDescriptionSet\n\n
    getExtendedViews()\n
    '''
def getStudioExtensionsURL():
    '''returns URL\n\n
    getStudioExtensionsURL()\n
    '''
def getStudioExtensionConfig():
    '''returns IloExtensionConfiguration\n\n
    getStudioExtensionConfig()\n
    '''
def setExtensionsURL():
    '''returns None\n\n
    setExtensionsURL(final URL url)\n
    '''
def setDecisionProcessConfigurationURL():
    '''returns None\n\n
    setDecisionProcessConfigurationURL(final URL dpcURL)\n
    '''
def getDecisionProcessConfigurationURL():
    '''returns URL\n\n
    getDecisionProcessConfigurationURL()\n
    '''
def getDecisionProcessConfiguration():
    '''returns IloDecisionProcessConfiguration\n\n
    getDecisionProcessConfiguration()\n
    '''
def filesToPackage():
    '''returns Iterator<IloJarableFile>\n\n
    filesToPackage()\n
    '''
def getOrCreateDecisionProcessConfiguration():
    '''returns IloDecisionProcessConfiguration\n\n
    getOrCreateDecisionProcessConfiguration(final boolean relativeUrl)\n
    '''
def createResource():
    '''returns Resource\n\n
    createResource(final URI uri)\n
    '''
def getID():
    '''returns String\n\n
    getID(final EObject e)\n
    '''
def addResourcesURL():
    '''returns boolean\n\n
    addResourcesURL(final URL resourcesURL)\n
    '''
def addResourcesURLs():
    '''returns int\n\n
    addResourcesURLs(final List<URL> resourcesURLList)\n
    '''
def getResourcesURLs():
    '''returns Iterator<URL>\n\n
    getResourcesURLs()\n
    '''
def writeLinkTo():
    '''returns None\n\n
    writeLinkTo(final String href)\n
    '''
def writeDocument():
    '''returns None\n\n
    writeDocument()\n
    '''
