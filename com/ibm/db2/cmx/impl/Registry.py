def Registry():
'''public Registry()
'''
pass
def purgeCache():
'''public void purgeCache()
'''
pass
def registerNewProfileForDataSourceId():
'''public void registerNewProfileForDataSourceId(final String key, final Profile.DataSource value)
'''
pass
def deregisterProfileForDataSourceId():
'''public void deregisterProfileForDataSourceId(final String key)
'''
pass
def registerNewProfileForDriverId():
'''public void registerNewProfileForDriverId(final String key, final Profile.Driver value)
'''
pass
def deregisterProfileForDriverId():
'''public void deregisterProfileForDriverId(final String key)
'''
pass
def updateDriverProfile():
'''public void updateDriverProfile(final String key, final Profile.Driver driver)
'''
pass
def updateDataSourceProfile():
'''public void updateDataSourceProfile(final String key, final Profile.DataSource dataSource)
'''
pass
def updateDatabase():
'''public void updateDatabase(final String key, final Database database)
'''
pass
def deleteDriverProfile():
'''public void deleteDriverProfile(final String key)
'''
pass
def deleteDataSourceProfile():
'''public void deleteDataSourceProfile(final String s)
'''
pass
def deleteDatabase():
'''public void deleteDatabase(final String key)
'''
pass
def getActiveDriversUsingProfile():
'''public Set<String> getActiveDriversUsingProfile(final String key)
'''
pass
def getActiveDataSourcesUsingProfile():
'''public Set<String> getActiveDataSourcesUsingProfile(final String key)
'''
pass
def getActiveDataSourcesUsingDatabase():
'''public Set<String> getActiveDataSourcesUsingDatabase(final String key)
'''
pass
def getDriverDescriptor():
'''public DriverDescriptor getDriverDescriptor(final String key)
'''
pass
def getDataSourceDescriptor():
'''public DataSourceDescriptor getDataSourceDescriptor(final String key)
'''
pass
def registerMonitoredLogicalDataSource():
'''public void registerMonitoredLogicalDataSource(final String s, final MonitorSettings monitorSettings)
'''
pass
def registerMonitoredDatabaseURL_NoResolve():
'''public void registerMonitoredDatabaseURL_NoResolve(final String s, final int i, final String s2, final MonitorSettings monitorSettings)
'''
pass
def registerMonitoredDatabaseURL_Resolve():
'''public void registerMonitoredDatabaseURL_Resolve(final String s, final int i, final String s2, final MonitorSettings monitorSettings)
'''
pass
def registerMonitoredLocation():
'''public void registerMonitoredLocation(final String s, final MonitorSettings monitorSettings)
'''
pass
def getMonitoredDataCache():
'''public MonitoredDataCache getMonitoredDataCache()
'''
pass
def cacheMonitoredData():
'''public void cacheMonitoredData(final MonitoredData monitoredData)
'''
pass
def setCachingIntervalForMonitoredData():
'''public void setCachingIntervalForMonitoredData(final int n)
'''
pass
def setInMemoryCacheLimitForMonitoredData():
'''public void setInMemoryCacheLimitForMonitoredData(final long inMemoryCacheLimitForMonitoredData_)
'''
pass
def run():
'''public void run()
'''
pass
