COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def ():
    '''returns IloScenarioSourceProvider\n\n
    ()\n
    '''
def getRepositoryProfile():
    '''returns IloRepositoryAccessProfile\n\n
    getRepositoryProfile()\n
    '''
def setRepositoryProfile():
    '''returns None\n\n
    setRepositoryProfile(final IloRepositoryAccessProfile value)\n
    '''
def getSecurityProfile():
    '''returns IloSecurityProfile\n\n
    getSecurityProfile()\n
    '''
def setSecurityProfile():
    '''returns None\n\n
    setSecurityProfile(final IloSecurityProfile value)\n
    '''
def getDeploymentProfile():
    '''returns IloDeploymentProfile\n\n
    getDeploymentProfile()\n
    '''
def setDeploymentProfile():
    '''returns None\n\n
    setDeploymentProfile(final IloDeploymentProfile value)\n
    '''
def scenarioSourceIds():
    '''returns Set<String>\n\n
    scenarioSourceIds()\n
    '''
def scenarioExporterIds():
    '''returns Set<String>\n\n
    scenarioExporterIds()\n
    '''
def getScenarioSourceTemplate():
    '''returns IloScenarioSourceTemplate\n\n
    getScenarioSourceTemplate(final String id)\n
    '''
def getScenarioExporterTemplate():
    '''returns IloFormTemplate\n\n
    getScenarioExporterTemplate(final String id)\n
    '''
def getScenarioUpdater():
    '''returns IloScenarioUpdater\n\n
    getScenarioUpdater(final String id)\n
    '''
def getScenarioUpdaterLocation():
    '''returns IloProcessingContext\n\n
    getScenarioUpdaterLocation(final String id)\n
    '''
def getScenarioExporter():
    '''returns IloScenarioExporter\n\n
    getScenarioExporter(final String id)\n
    '''
def addScenarioSource():
    '''returns None\n\n
    addScenarioSource(final IloScenarioSourceTemplate template, final IloScenarioUpdater updater)\n
    addScenarioSource(final IloScenarioSourceTemplate template, final IloScenarioUpdater updater, final IloProcessingContext location)\n
    '''
def addScenarioExporter():
    '''returns None\n\n
    addScenarioExporter(final IloFormTemplate template, final IloScenarioExporter exporter)\n
    '''
def addConnectionProfile():
    '''returns None\n\n
    addConnectionProfile(final String id, final IloDBConnectionProfileImpl connection)\n
    '''
def visit():
    '''returns None\n\n
    visit(final Visitor visitor)\n
    '''
def predefinedCredentialIds():
    '''returns Iterator<String>\n\n
    predefinedCredentialIds()\n
    '''
def getPredefinedCredential():
    '''returns IloCredential\n\n
    getPredefinedCredential(final String id)\n
    '''
def addPredefinedCredential():
    '''returns None\n\n
    addPredefinedCredential(final String id, final IloCredential credential)\n
    '''
def getDefaultScenarioSourceTemplate():
    '''returns IloTemplateInstance\n\n
    getDefaultScenarioSourceTemplate()\n
    '''
def getDefaultUpdaterId():
    '''returns String\n\n
    getDefaultUpdaterId()\n
    '''
def setDefaultUpdaterId():
    '''returns None\n\n
    setDefaultUpdaterId(final String defaultUpdaterId)\n
    '''
def getScenarioSourceTemplates():
    '''returns IloScenarioSourceTemplate[]\n\n
    getScenarioSourceTemplates()\n
    '''
def getScenarioExporterTemplates():
    '''returns IloFormTemplate[]\n\n
    getScenarioExporterTemplates()\n
    '''
def getScenarioMigrator():
    '''returns IloScenarioMigrator\n\n
    getScenarioMigrator()\n
    '''
def setScenarioMigrator():
    '''returns None\n\n
    setScenarioMigrator(final IloScenarioMigrator migrator)\n
    '''
def getScenarioDataCheckers():
    '''returns IloScenarioDataChecker[]\n\n
    getScenarioDataCheckers()\n
    '''
def addScenarioDataChecker():
    '''returns None\n\n
    addScenarioDataChecker(final IloScenarioDataChecker checker)\n
    '''
def setResourcesEstimationProfile():
    '''returns None\n\n
    setResourcesEstimationProfile(final IloResourcesEstimationProfile value)\n
    '''
def getResourcesEstimationProfile():
    '''returns IloResourcesEstimationProfile\n\n
    getResourcesEstimationProfile()\n
    '''
def getProperties():
    '''returns Properties\n\n
    getProperties()\n
    '''
def getServiceInitHook():
    '''returns IloServiceInitHook\n\n
    getServiceInitHook()\n
    '''
def setServiceInitHook():
    '''returns None\n\n
    setServiceInitHook(final IloServiceInitHook serviceInitHook)\n
    '''
