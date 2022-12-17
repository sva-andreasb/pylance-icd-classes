DIAG_OPTION_OFF = "int  0"
DIAG_OPTION_ORPHAN_NOTIFY = "int  1"
DIAG_OPTION_ORPHAN_CODE_PATH = "int  2"
DIAG_OPTION_CONN_WAIT_CODE_PATH = "int  4"
def ():
    '''returns CMPropertiesImpl\n\n
    ()\n
    (final String name, final String dataSourceClassName)\n
    (final Properties props)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def getReference():
    '''returns Reference\n\n
    getReference()\n
    '''
def loadFromReference():
    '''returns CMProperties\n\n
    loadFromReference(final Reference ref)\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def setName():
    '''returns None\n\n
    setName(final String newName)\n
    '''
def getDataSourceClassName():
    '''returns String\n\n
    getDataSourceClassName()\n
    '''
def setDataSourceClassName():
    '''returns None\n\n
    setDataSourceClassName(final String newDataSourceClassName)\n
    '''
def getDataBaseVersion():
    '''returns String\n\n
    getDataBaseVersion()\n
    '''
def setDataBaseVersion():
    '''returns None\n\n
    setDataBaseVersion(final String newDataBaseVersion)\n
    '''
def getMinConnectionPoolSize():
    '''returns int\n\n
    getMinConnectionPoolSize()\n
    '''
def setMinConnectionPoolSize():
    '''returns None\n\n
    setMinConnectionPoolSize(final int newPoolSize)\n
    '''
def getMaxConnectionPoolSize():
    '''returns int\n\n
    getMaxConnectionPoolSize()\n
    '''
def setMaxConnectionPoolSize():
    '''returns None\n\n
    setMaxConnectionPoolSize(final int newPoolSize)\n
    '''
def getConnectionTimeout():
    '''returns int\n\n
    getConnectionTimeout()\n
    '''
def getConnectionTimeoutInMillis():
    '''returns int\n\n
    getConnectionTimeoutInMillis()\n
    '''
def setConnectionTimeout():
    '''returns None\n\n
    setConnectionTimeout(final int newTimeout)\n
    '''
def getIdleTimeout():
    '''returns int\n\n
    getIdleTimeout()\n
    '''
def getIdleTimeoutInMillis():
    '''returns int\n\n
    getIdleTimeoutInMillis()\n
    '''
def setIdleTimeout():
    '''returns None\n\n
    setIdleTimeout(final int newTimeout)\n
    '''
def getOrphanTimeout():
    '''returns int\n\n
    getOrphanTimeout()\n
    '''
def getOrphanTimeoutInMillis():
    '''returns long\n\n
    getOrphanTimeoutInMillis()\n
    '''
def setOrphanTimeout():
    '''returns None\n\n
    setOrphanTimeout(final int newTimeout)\n
    '''
def getAgedTimeout():
    '''returns int\n\n
    getAgedTimeout()\n
    '''
def getAgedTimeoutInMillis():
    '''returns long\n\n
    getAgedTimeoutInMillis()\n
    '''
def setAgedTimeout():
    '''returns None\n\n
    setAgedTimeout(final int newTimeout)\n
    '''
def getMaxStatementCacheSize():
    '''returns int\n\n
    getMaxStatementCacheSize()\n
    '''
def setMaxStatementCacheSize():
    '''returns None\n\n
    setMaxStatementCacheSize(final int newCacheSize)\n
    '''
def getUser():
    '''returns String\n\n
    getUser()\n
    '''
def getInformixLockModeWait():
    '''returns int\n\n
    getInformixLockModeWait()\n
    '''
def getInformixAllowNewLine():
    '''returns boolean\n\n
    getInformixAllowNewLine()\n
    '''
def getOracleStmtCacheSize():
    '''returns int\n\n
    getOracleStmtCacheSize()\n
    '''
def setUser():
    '''returns None\n\n
    setUser(final String newUser)\n
    '''
def getTmpUser():
    '''returns String\n\n
    getTmpUser()\n
    '''
def setTmpUser():
    '''returns None\n\n
    setTmpUser(final String newUser)\n
    '''
def setTmpPassword():
    '''returns None\n\n
    setTmpPassword(final String newPassword)\n
    '''
def setInformixLockModeWait():
    '''returns None\n\n
    setInformixLockModeWait(final int value)\n
    '''
def setInformixAllowNewLine():
    '''returns None\n\n
    setInformixAllowNewLine(final boolean value)\n
    '''
def setOracleStmtCacheSize():
    '''returns None\n\n
    setOracleStmtCacheSize(final int value)\n
    '''
def setPassword():
    '''returns None\n\n
    setPassword(final String newPassword)\n
    '''
def isAutoConnCleanupDisabled():
    '''returns boolean\n\n
    isAutoConnCleanupDisabled()\n
    '''
def setAutoConnCleanupDisabled():
    '''returns None\n\n
    setAutoConnCleanupDisabled(final boolean value)\n
    '''
def getErrorMap():
    '''returns Hashtable\n\n
    getErrorMap()\n
    '''
def setErrorMap():
    '''returns None\n\n
    setErrorMap(final Hashtable newErrorMap)\n
    '''
def isDisable2Phase():
    '''returns boolean\n\n
    isDisable2Phase()\n
    '''
def setDisable2Phase():
    '''returns None\n\n
    setDisable2Phase(final boolean value)\n
    '''
def setDataSourceProperty():
    '''returns None\n\n
    setDataSourceProperty(final String key, final String value)\n
    '''
def getDataSourceProperty():
    '''returns String\n\n
    getDataSourceProperty(final String key)\n
    '''
def dataSourcePropertyNames():
    '''returns Enumeration\n\n
    dataSourcePropertyNames()\n
    '''
def getDataSourceProperties():
    '''returns DataSourceProperties\n\n
    getDataSourceProperties()\n
    '''
def validate():
    '''returns None\n\n
    validate()\n
    '''
def encodePassword():
    '''returns None\n\n
    encodePassword()\n
    '''
def decodePassword():
    '''returns None\n\n
    decodePassword()\n
    '''
def clone():
    '''returns Object\n\n
    clone()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object obj)\n
    '''
def isValidateEnabled():
    '''returns boolean\n\n
    isValidateEnabled()\n
    '''
def setValidate():
    '''returns None\n\n
    setValidate(final boolean theValue)\n
    '''
def getValidateSQL():
    '''returns String\n\n
    getValidateSQL()\n
    '''
def setValidateSQL():
    '''returns None\n\n
    setValidateSQL(final String theValue)\n
    '''
def getLogOrphan():
    '''returns boolean\n\n
    getLogOrphan()\n
    '''
def setLogOrphan():
    '''returns None\n\n
    setLogOrphan(final boolean theValue)\n
    '''
def getOraTransLoose():
    '''returns boolean\n\n
    getOraTransLoose()\n
    '''
def setOraTransLoose():
    '''returns None\n\n
    setOraTransLoose(final boolean theValue)\n
    '''
def isResetReadOnlyEnabled():
    '''returns boolean\n\n
    isResetReadOnlyEnabled()\n
    '''
def getMBeanFactoryId():
    '''returns String\n\n
    getMBeanFactoryId()\n
    '''
def getMBeanProviderId():
    '''returns String\n\n
    getMBeanProviderId()\n
    '''
def setMBeanFactoryId():
    '''returns None\n\n
    setMBeanFactoryId(final String mbeanFactoryId)\n
    '''
def setMBeanProviderId():
    '''returns None\n\n
    setMBeanProviderId(final String mbeanProviderId)\n
    '''
def setDiagOptions():
    '''returns None\n\n
    setDiagOptions(final int iOptions)\n
    '''
def getDiagOptions():
    '''returns int\n\n
    getDiagOptions()\n
    '''
def isDiagOptionEnabled():
    '''returns boolean\n\n
    isDiagOptionEnabled(final int iOptions)\n
    '''
def getDiagOptionsString():
    '''returns String\n\n
    getDiagOptionsString()\n
    '''
