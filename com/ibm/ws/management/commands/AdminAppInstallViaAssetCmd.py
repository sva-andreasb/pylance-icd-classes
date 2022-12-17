ADMIN_TASK = "String  \"AdminTask\""
ADDCOMPUNIT_CMD = "String  \"addCompUnit\""
BLA_ID = "String  \"-blaID \""
ASSET_ID = "String  \"-cuSourceID \""
def getName():
    '''returns String\n\n
    getName()\n
    '''
def getDescription():
    '''returns String\n\n
    getDescription(final Locale locale)\n
    '''
def ():
    '''returns AdminAppInstallViaAssetCmd\n\n
    (final String assetId, final String blaId)\n
    '''
def getInstallCmdScript():
    '''returns String\n\n
    getInstallCmdScript(final Hashtable taskHash, final String lang)\n
    '''
def setAppDeploymentOptionsData():
    '''returns None\n\n
    setAppDeploymentOptionsData(final String earLocation, final String[][] taskData)\n
    '''
def setDefaultBindingsOptions():
    '''returns None\n\n
    setDefaultBindingsOptions(final String[][] taskData)\n
    '''
def setName():
    '''returns None\n\n
    setName(final String newName)\n
    '''
def setAppName():
    '''returns None\n\n
    setAppName(final String newAppName)\n
    '''
