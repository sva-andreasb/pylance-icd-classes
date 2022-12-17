def ():
    '''returns ACfgDatabase\n\n
    ()\n
    '''
def dropInstance():
    '''returns TaskResult\n\n
    dropInstance()\n
    '''
def dropDatabase():
    '''returns TaskResult\n\n
    dropDatabase()\n
    '''
def dropTemporaryTablespace():
    '''returns TaskResult\n\n
    dropTemporaryTablespace()\n
    '''
def dropDataTablespace():
    '''returns TaskResult\n\n
    dropDataTablespace()\n
    '''
def dropIndexTablespace():
    '''returns TaskResult\n\n
    dropIndexTablespace()\n
    '''
def dropDatabaseUser():
    '''returns TaskResult\n\n
    dropDatabaseUser()\n
    '''
def getConnection():
    '''returns Connection\n\n
    getConnection(final String userid, final String password, final String dbSchema)\n
    '''
def runConfigurationStep():
    '''returns TaskResult\n\n
    runConfigurationStep()\n
    '''
def undoConfiguration():
    '''returns TaskResult\n\n
    undoConfiguration()\n
    '''
def hasDatabaseSchemaBeenDeployed():
    '''returns TaskResult\n\n
    hasDatabaseSchemaBeenDeployed()\n
    '''
def verifyCompletion():
    '''returns TaskResult\n\n
    verifyCompletion()\n
    '''
def cronTaskExists():
    '''returns boolean\n\n
    cronTaskExists(final String userName)\n
    '''
def createCronTask():
    '''returns TaskResult\n\n
    createCronTask(final String userName)\n
    '''
def handleTextSearch():
    '''returns TaskResult\n\n
    handleTextSearch()\n
    '''
def updateLightningProperties():
    '''returns None\n\n
    updateLightningProperties()\n
    '''
def handleInstallEvent():
    '''returns None\n\n
    handleInstallEvent(final ICmnInstallEvent requestEvent)\n
    '''
