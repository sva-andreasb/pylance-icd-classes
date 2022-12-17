def migrateDataSourcesXML():
    '''returns Properties\n\n
    migrateDataSourcesXML(final String driverClass, final Element dataSourceXML)\n
    '''
def migrateDataSource():
    '''returns Properties\n\n
    migrateDataSource(String driverClass, final String urlPrefix, final String databaseName, final String jtaEnabledStr)\n
    '''
def migrateAdminDotConfig():
    '''returns Properties\n\n
    migrateAdminDotConfig(final String dbDriver, final String dbUrl, final String dbUser, final String dbPassword, final String connectionPoolSize)\n
    '''
def convertUrlToUrlPrefixAndDatabaseName():
    '''returns String[]\n\n
    convertUrlToUrlPrefixAndDatabaseName(final String url, final String driverClassName)\n
    '''
