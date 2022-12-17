def ():
    '''returns DataSourceConfigHelperMBean\n\n
    (final VariableMap varMap, final Repository rep)\n
    '''
def getPropertiesForDataSource():
    '''returns ArrayList\n\n
    getPropertiesForDataSource(final String dsClassName, final String providerLibPath)\n
    '''
def testConnectionToDataSource():
    '''returns String\n\n
    testConnectionToDataSource(final String dsClassName, final String user, final String password, final Properties dataSourceProps, final String providerLibPath, final String language, final String country)\n
    testConnectionToDataSource(final String dsClassName, final String user, final String password, final Properties dataSourceProps, final String providerLibPath, final Locale locale)\n
    '''
def reload():
    '''returns None\n\n
    reload()\n
    '''
def testConnection():
    '''returns int\n\n
    testConnection(final String configId)\n
    '''
