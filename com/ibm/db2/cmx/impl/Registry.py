def ():
    '''returns Registry\n\n
    ()\n
    '''
def purgeCache():
    '''returns None\n\n
    purgeCache()\n
    '''
def registerNewProfileForDataSourceId():
    '''returns None\n\n
    registerNewProfileForDataSourceId(final String key, final Profile.DataSource value)\n
    '''
def deregisterProfileForDataSourceId():
    '''returns None\n\n
    deregisterProfileForDataSourceId(final String key)\n
    '''
def registerNewProfileForDriverId():
    '''returns None\n\n
    registerNewProfileForDriverId(final String key, final Profile.Driver value)\n
    '''
def deregisterProfileForDriverId():
    '''returns None\n\n
    deregisterProfileForDriverId(final String key)\n
    '''
def updateDriverProfile():
    '''returns None\n\n
    updateDriverProfile(final String key, final Profile.Driver driver)\n
    '''
def updateDataSourceProfile():
    '''returns None\n\n
    updateDataSourceProfile(final String key, final Profile.DataSource dataSource)\n
    '''
def updateDatabase():
    '''returns None\n\n
    updateDatabase(final String key, final Database database)\n
    '''
def deleteDriverProfile():
    '''returns None\n\n
    deleteDriverProfile(final String key)\n
    '''
def deleteDataSourceProfile():
    '''returns None\n\n
    deleteDataSourceProfile(final String s)\n
    '''
def deleteDatabase():
    '''returns None\n\n
    deleteDatabase(final String key)\n
    '''
def getActiveDriversUsingProfile():
    '''returns Set<String>\n\n
    getActiveDriversUsingProfile(final String key)\n
    '''
def getActiveDataSourcesUsingProfile():
    '''returns Set<String>\n\n
    getActiveDataSourcesUsingProfile(final String key)\n
    '''
def getActiveDataSourcesUsingDatabase():
    '''returns Set<String>\n\n
    getActiveDataSourcesUsingDatabase(final String key)\n
    '''
def getDriverDescriptor():
    '''returns DriverDescriptor\n\n
    getDriverDescriptor(final String key)\n
    '''
def getDataSourceDescriptor():
    '''returns DataSourceDescriptor\n\n
    getDataSourceDescriptor(final String key)\n
    '''
def registerMonitoredLogicalDataSource():
    '''returns None\n\n
    registerMonitoredLogicalDataSource(final String s, final MonitorSettings monitorSettings)\n
    '''
def registerMonitoredDatabaseURL_NoResolve():
    '''returns None\n\n
    registerMonitoredDatabaseURL_NoResolve(final String s, final int i, final String s2, final MonitorSettings monitorSettings)\n
    '''
def registerMonitoredDatabaseURL_Resolve():
    '''returns None\n\n
    registerMonitoredDatabaseURL_Resolve(final String s, final int i, final String s2, final MonitorSettings monitorSettings)\n
    '''
def registerMonitoredLocation():
    '''returns None\n\n
    registerMonitoredLocation(final String s, final MonitorSettings monitorSettings)\n
    '''
def getMonitoredDataCache():
    '''returns MonitoredDataCache\n\n
    getMonitoredDataCache()\n
    '''
def cacheMonitoredData():
    '''returns None\n\n
    cacheMonitoredData(final MonitoredData monitoredData)\n
    '''
def setCachingIntervalForMonitoredData():
    '''returns None\n\n
    setCachingIntervalForMonitoredData(final int n)\n
    '''
def setInMemoryCacheLimitForMonitoredData():
    '''returns None\n\n
    setInMemoryCacheLimitForMonitoredData(final long inMemoryCacheLimitForMonitoredData_)\n
    '''
def run():
    '''returns None\n\n
    run()\n
    '''
