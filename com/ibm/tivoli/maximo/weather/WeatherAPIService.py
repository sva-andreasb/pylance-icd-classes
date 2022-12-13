def WeatherAPIService():
'''public WeatherAPIService(final MXServer mxServer)
public WeatherAPIService()
'''
pass
def init():
'''public void init()
'''
pass
def getCurrentWeatherForGeocode():
'''public Map<String, Object> getCurrentWeatherForGeocode(final UserInfo userInfo, final double latY, final double longX, final String productName)
'''
pass
def getDailyForecastForGeocode():
'''public Map<String, Object> getDailyForecastForGeocode(final UserInfo userInfo, final double latY, final double longX, final int duration, final String productName)
'''
pass
def getHourlyForecastForGeocode():
'''public Map<String, Object> getHourlyForecastForGeocode(final UserInfo userInfo, final double latY, final double longX, final String hours, final String productName)
'''
pass
def getHistoricalWeatherForGeocode():
'''public Map<String, Object> getHistoricalWeatherForGeocode(final UserInfo userInfo, final double latY, final double longX, final Date startDate, final Date endDate, final String productName)
'''
pass
def getWeatherAlertsForGeocode():
'''public Map<String, Object> getWeatherAlertsForGeocode(final UserInfo userInfo, final double latY, final double longX, final String productName)
'''
pass
def getWeatherAlertsDetails():
'''public Map<String, Object> getWeatherAlertsDetails(final UserInfo userInfo, final String detailKey, final String productName)
'''
pass
def getCurrentWeatherForLocation():
'''public Map<String, Object> getCurrentWeatherForLocation(final UserInfo userInfo, final String postalCode, String locationCode, final String country, final String productName)
'''
pass
def getDailyForecastForLocation():
'''public Map<String, Object> getDailyForecastForLocation(final UserInfo userInfo, final String postalCode, String locationCode, final String country, final int duration, final String productName)
'''
pass
def getHourlyForecastForLocation():
'''public Map<String, Object> getHourlyForecastForLocation(final UserInfo userInfo, final String postalCode, String locationCode, final String country, final String hours, final String productName)
'''
pass
def getHistoricalWeatherForLocation():
'''public Map<String, Object> getHistoricalWeatherForLocation(final UserInfo userInfo, final String postalCode, String locationCode, final String country, final Date startDate, final Date endDate, final String productName)
'''
pass
def getWeatherAlertsForLocation():
'''public Map<String, Object> getWeatherAlertsForLocation(final UserInfo userInfo, final String postalCode, String locationCode, final String country, final String productName)
'''
pass
def checkConnection():
'''public void checkConnection(@WSMboKey("WEATHERORG") final MboRemote weatherOrg)
'''
pass
def getServiceAddresses():
'''public MboSetRemote getServiceAddresses()
'''
pass
def registryEndPointsForAlerts():
'''public void registryEndPointsForAlerts(final boolean register)
'''
pass
def processAssetsRegistry():
'''public void processAssetsRegistry(@WSMboKey("WEATHERZONE") final MboRemote weatherZone, final String actioncode)
'''
pass
def getProductCatalog():
'''public List<Object> getProductCatalog(final String org)
'''
pass
def isWeatherLicenseInstalled():
'''public boolean isWeatherLicenseInstalled(final String productName)
'''
pass
def logWeatherAPICall():
'''public void logWeatherAPICall(String productName, final String resourceName, final UserInfo userInfo)
'''
pass
def distance():
'''public double distance(final double lat1, final double lon1, final double lat2, final double lon2, final String uom)
'''
pass
