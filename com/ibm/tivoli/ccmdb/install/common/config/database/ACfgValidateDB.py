def canConnectWithUser():
    '''returns boolean\n\n
    canConnectWithUser(final String jdbcUrl, final String dbuser, final String dbpassword)\n
    '''
def instanceExists():
    '''returns boolean\n\n
    instanceExists(final String dbinstance)\n
    '''
def dbExists():
    '''returns boolean\n\n
    dbExists(final String dbname)\n
    '''
def hasDbaAuthority():
    '''returns boolean\n\n
    hasDbaAuthority(final String jdbcUrl, final String dbaUser, final String dbaPassword)\n
    '''
def tableSpaceExists():
    '''returns boolean\n\n
    tableSpaceExists(final String dbtsname)\n
    '''
def tableSpaceSize():
    '''returns boolean\n\n
    tableSpaceSize(final String dbtsname, final String dbtssize)\n
    '''
def bufferPoolExists():
    '''returns boolean\n\n
    bufferPoolExists(final String dbbpname)\n
    '''
def bufferPoolSize():
    '''returns boolean\n\n
    bufferPoolSize(final String dbbpname, final String dbbpsize)\n
    '''
def dbSize():
    '''returns boolean\n\n
    dbSize(final String dbsize, final String dbname)\n
    '''
def dbLogFileSize():
    '''returns boolean\n\n
    dbLogFileSize(final String dblfsize, final String dbname)\n
    '''
def isCompatibleDatabaseExists():
    '''returns boolean\n\n
    isCompatibleDatabaseExists(final String minReqDBVersion, final String schemaOwner)\n
    '''
def isDatabaseReadyForUpdatedb():
    '''returns boolean\n\n
    isDatabaseReadyForUpdatedb(String schemaOwner)\n
    '''
def isXXTablesExists():
    '''returns boolean\n\n
    isXXTablesExists(final String schemaOwner)\n
    '''
def isMXServerUp():
    '''returns boolean\n\n
    isMXServerUp(final String serverName, final String dbType, String schemaOwner)\n
    '''
def nativeTableExists():
    '''returns boolean\n\n
    nativeTableExists(final String tbname, final String dbType, final String schemaName)\n
    '''
def rowFound():
    '''returns boolean\n\n
    rowFound(final String sql, final String dbType)\n
    '''
