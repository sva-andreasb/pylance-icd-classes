def canConnectWithUser():
    '''returns boolean\n\n
    canConnectWithUser(final String jdbcUrl, final String dbuser, final String dbPassword)\n
    '''
def instanceExists():
    '''returns boolean\n\n
    instanceExists(String dbname)\n
    '''
def hasDbaAuthority():
    '''returns boolean\n\n
    hasDbaAuthority(final String jdbcurl, String dbuser, final String dbpassword)\n
    '''
def tablespaceExists():
    '''returns boolean\n\n
    tablespaceExists(final String dbtsname)\n
    '''
def tableSpaceSize():
    '''returns boolean\n\n
    tableSpaceSize(final String dbtsname, final String dbtssize)\n
    '''
def canCreateTablespace():
    '''returns boolean\n\n
    canCreateTablespace(final String dbTsLocation)\n
    '''
def spaceAvailableForTablespace():
    '''returns boolean\n\n
    spaceAvailableForTablespace(final String dbTsLocation, final int spaceRequired, final String adminUser, final String adminPassword)\n
    '''
def canCreateDatabase():
    '''returns boolean\n\n
    canCreateDatabase(final String dbLocation, final String adminUser, final String adminPassword)\n
    '''
def isInstanceRunning():
    '''returns boolean\n\n
    isInstanceRunning(final String instanceName)\n
    '''
def isValidOracleHome():
    '''returns boolean\n\n
    isValidOracleHome(final String oracleHome)\n
    '''
def setOracleHomeDirectory():
    '''returns None\n\n
    setOracleHomeDirectory(final String oracleHome)\n
    '''
