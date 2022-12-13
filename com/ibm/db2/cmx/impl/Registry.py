def Registry():
    '''public Registry()
    '''
def purgeCache():
    '''public void purgeCache()
    '''
def registerNewProfileForDataSourceId():
    '''public void registerNewProfileForDataSourceId(final String key, final Profile.DataSource value)
    '''
def deregisterProfileForDataSourceId():
    '''public void deregisterProfileForDataSourceId(final String key)
    '''
def registerNewProfileForDriverId():
    '''public void registerNewProfileForDriverId(final String key, final Profile.Driver value)
    '''
def deregisterProfileForDriverId():
    '''public void deregisterProfileForDriverId(final String key)
    '''
def updateDriverProfile():
    '''public void updateDriverProfile(final String key, final Profile.Driver driver)
    '''
def updateDataSourceProfile():
    '''public void updateDataSourceProfile(final String key, final Profile.DataSource dataSource)
    '''
def updateDatabase():
    '''public void updateDatabase(final String key, final Database database)
    '''
def deleteDriverProfile():
    '''public void deleteDriverProfile(final String key)
    '''
def deleteDataSourceProfile():
    '''public void deleteDataSourceProfile(final String s)
    '''
def deleteDatabase():
    '''public void deleteDatabase(final String key)
    '''
def getActiveDriversUsingProfile():
    '''public Set<String> getActiveDriversUsingProfile(final String key)
    '''
def getActiveDataSourcesUsingProfile():
    '''public Set<String> getActiveDataSourcesUsingProfile(final String key)
    '''
def getActiveDataSourcesUsingDatabase():
    '''public Set<String> getActiveDataSourcesUsingDatabase(final String key)
    '''
def getDriverDescriptor():
    '''public DriverDescriptor getDriverDescriptor(final String key)
    '''
def getDataSourceDescriptor():
    '''public DataSourceDescriptor getDataSourceDescriptor(final String key)
    '''
def registerMonitoredLogicalDataSource():
    '''public void registerMonitoredLogicalDataSource(final String s, final MonitorSettings monitorSettings)
    '''
def registerMonitoredDatabaseURL_NoResolve():
    '''public void registerMonitoredDatabaseURL_NoResolve(final String s, final int i, final String s2, final MonitorSettings monitorSettings)
    '''
def registerMonitoredDatabaseURL_Resolve():
    '''public void registerMonitoredDatabaseURL_Resolve(final String s, final int i, final String s2, final MonitorSettings monitorSettings)
    '''
def registerMonitoredLocation():
    '''public void registerMonitoredLocation(final String s, final MonitorSettings monitorSettings)
    '''
def getMonitoredDataCache():
    '''public MonitoredDataCache getMonitoredDataCache()
    '''
def cacheMonitoredData():
    '''public void cacheMonitoredData(final MonitoredData monitoredData)
    '''
def setCachingIntervalForMonitoredData():
    '''public void setCachingIntervalForMonitoredData(final int n)
    '''
def setInMemoryCacheLimitForMonitoredData():
    '''public void setInMemoryCacheLimitForMonitoredData(final long inMemoryCacheLimitForMonitoredData_)
    '''
def run():
    '''public void run()
    '''
