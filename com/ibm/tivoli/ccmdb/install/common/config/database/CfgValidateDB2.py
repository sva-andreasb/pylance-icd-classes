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
def tablespaceHasFreeMinimumRequiredFreePages():
    '''returns int\n\n
    tablespaceHasFreeMinimumRequiredFreePages(final String dbtsname, final int minFreePages)\n
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
def dbApplCtlHeapSize():
    '''returns boolean\n\n
    dbApplCtlHeapSize(final String dbacsize)\n
    '''
def dbApplHeapSize():
    '''returns boolean\n\n
    dbApplHeapSize(final String dbahsize)\n
    '''
def dbLockListSize():
    '''returns boolean\n\n
    dbLockListSize(final String dbllsize)\n
    '''
def dbLogSecSize():
    '''returns boolean\n\n
    dbLogSecSize(final String dbslsize)\n
    '''
