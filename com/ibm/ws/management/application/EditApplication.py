TableDDL = "String  \"META-INF/Table.ddl\""
BackendDir = "String  \"META-INF/backends/\""
def ():
    '''returns EditApplication\n\n
    (final String aName, final Hashtable prf, final String mod, final String wID, final AppManagement mgmt)\n
    '''
def checkIfAppExists():
    '''returns Object\n\n
    checkIfAppExists()\n
    '''
def getApplicationInfo():
    '''returns Vector\n\n
    getApplicationInfo()\n
    '''
def setApplicationInfo():
    '''returns None\n\n
    setApplicationInfo(final Vector tasks)\n
    '''
def exportApplication():
    '''returns None\n\n
    exportApplication(final String pathName)\n
    '''
def extractDDL():
    '''returns None\n\n
    extractDDL(final String ddlPrefix, final String dirName)\n
    '''
def publishWSDL():
    '''returns None\n\n
    publishWSDL(final String pathName)\n
    '''
def listModules():
    '''returns AppDeploymentTask\n\n
    listModules()\n
    '''
def listURIs():
    '''returns List\n\n
    listURIs()\n
    '''
def updateAccessIDs():
    '''returns None\n\n
    updateAccessIDs(final Boolean bAll)\n
    '''
def deleteUserAndGroupEntries():
    '''returns None\n\n
    deleteUserAndGroupEntries()\n
    '''
def getApplicationContents():
    '''returns byte[]\n\n
    getApplicationContents(final String arg_uri)\n
    '''
def getEditionInfo():
    '''returns EditionInfo[]\n\n
    getEditionInfo(final String edition)\n
    '''
def setEditionInfo():
    '''returns None\n\n
    setEditionInfo(final EditionInfo[] info)\n
    '''
def getAppAssociation():
    '''returns String[]\n\n
    getAppAssociation(final String scope, final String retVal)\n
    '''
