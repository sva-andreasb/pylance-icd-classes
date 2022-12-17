sqlDelimeters_ = "String  \" \n\t\r\f'\\"{},()\\[]:=+-*/<>!&|;.\""
def ():
    '''returns RepositorySetupManagerImpl\n\n
    (final Connection c)\n
    '''
def setGivenSchema():
    '''returns None\n\n
    setGivenSchema(final String givenSchema)\n
    '''
def getGivenSchema():
    '''returns String\n\n
    getGivenSchema()\n
    '''
def getDefaultOrGivenSchema():
    '''returns String\n\n
    getDefaultOrGivenSchema()\n
    '''
def createRepository():
    '''returns boolean\n\n
    createRepository(final String anotherString, final CreateType other, final boolean b, final PrintWriter printWriter)\n
    '''
def getCreateScript():
    '''returns List<String>\n\n
    getCreateScript(final boolean b, final String s)\n
    '''
def getUpgradeScript():
    '''returns List<String>\n\n
    getUpgradeScript(final boolean b, final RepositoryVersion repositoryVersion)\n
    '''
def removeRepository():
    '''returns List<Exception>\n\n
    removeRepository(final String s, final PrintWriter printWriter, final RepositoryVersion repositoryVersion)\n
    '''
def getDropScript():
    '''returns List<String>\n\n
    getDropScript(final boolean b, final String s, final RepositoryVersion repositoryVersion)\n
    '''
def grantRevokeAccess():
    '''returns None\n\n
    grantRevokeAccess(final RepositoryVersion repositoryVersion, final String s, final boolean b, final String s2, final boolean b2, final String[] array, final PrintWriter printWriter)\n
    '''
def getGrantRevokeAccessScript():
    '''returns List<String>\n\n
    getGrantRevokeAccessScript(final RepositoryVersion repositoryVersion, final String s, final boolean b, final String s2, final boolean b2, final String[] array)\n
    '''
def addStmtTerminator():
    '''returns List<String>\n\n
    addStmtTerminator(final List<String> list)\n
    '''
def getBindStaticPackages():
    '''returns List<String>\n\n
    getBindStaticPackages(final String str, final RepositoryVersion repositoryVersion, final boolean b)\n
    '''
def bindStaticPackages():
    '''returns int\n\n
    bindStaticPackages(final String s, final RepositoryVersion repositoryVersion, final boolean b, final PrintWriter printWriter)\n
    '''
def validate():
    '''returns List<String>\n\n
    validate(final String s, final List<String> list, final List<String> list2, final List<String> list3)\n
    validate(final String s)\n
    '''
def getRepositoryVersion():
    '''returns RepositoryVersion\n\n
    getRepositoryVersion(final String s)\n
    getRepositoryVersion(final Connection connection, final ConnectionManager.ConnectionInfo connectionInfo)\n
    '''
def getRepositorySchemas():
    '''returns List<String>\n\n
    getRepositorySchemas(final Connection connection)\n
    '''
