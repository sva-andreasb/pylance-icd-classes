def ():
    '''returns DBConnection\n\n
    (final String url, final String user, final String password, final String databaseType)\n
    (final Connection connection, final String databaseType)\n
    '''
def getConnection():
    '''returns Connection\n\n
    getConnection()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def cleanDB():
    '''returns None\n\n
    cleanDB()\n
    '''
def isFormatOK():
    '''returns boolean\n\n
    isFormatOK()\n
    '''
def setDatabaseProperties():
    '''returns None\n\n
    setDatabaseProperties(final Model dbProperties)\n
    '''
def getDatabaseProperties():
    '''returns Model\n\n
    getDatabaseProperties()\n
    '''
def getDefaultModelProperties():
    '''returns Model\n\n
    getDefaultModelProperties()\n
    '''
def getAllModelNames():
    '''returns ExtendedIterator<String>\n\n
    getAllModelNames()\n
    '''
def containsModel():
    '''returns boolean\n\n
    containsModel(final String name)\n
    '''
def containsDefaultModel():
    '''returns boolean\n\n
    containsDefaultModel()\n
    '''
def setDatabaseType():
    '''returns None\n\n
    setDatabaseType(final String databaseType)\n
    '''
def getDatabaseType():
    '''returns String\n\n
    getDatabaseType()\n
    '''
def getDriver():
    '''returns IRDBDriver\n\n
    getDriver()\n
    '''
def setDriver():
    '''returns None\n\n
    setDriver(final IRDBDriver driver)\n
    '''
