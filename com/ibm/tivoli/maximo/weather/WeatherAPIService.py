def WeatherAPIService():
    '''public WeatherAPIService(final MXServer mxServer)
    public WeatherAPIService()
    '''
def init():
    '''public void init()
    '''
def getCurrentWeatherForGeocode():
    '''public Map<String, Object> getCurrentWeatherForGeocode(final UserInfo userInfo, final double latY, final double longX, final String productName)
    '''
def getDailyForecastForGeocode():
    '''public Map<String, Object> getDailyForecastForGeocode(final UserInfo userInfo, final double latY, final double longX, final int duration, final String productName)
    '''
def getHourlyForecastForGeocode():
    '''public Map<String, Object> getHourlyForecastForGeocode(final UserInfo userInfo, final double latY, final double longX, final String hours, final String productName)
    '''
def getHistoricalWeatherForGeocode():
    '''public Map<String, Object> getHistoricalWeatherForGeocode(final UserInfo userInfo, final double latY, final double longX, final Date startDate, final Date endDate, final String productName)
    '''
def getWeatherAlertsForGeocode():
    '''public Map<String, Object> getWeatherAlertsForGeocode(final UserInfo userInfo, final double latY, final double longX, final String productName)
    '''
def getWeatherAlertsDetails():
    '''public Map<String, Object> getWeatherAlertsDetails(final UserInfo userInfo, final String detailKey, final String productName)
    '''
def getCurrentWeatherForLocation():
    '''public Map<String, Object> getCurrentWeatherForLocation(final UserInfo userInfo, final String postalCode, String locationCode, final String country, final String productName)
    '''
def getDailyForecastForLocation():
    '''public Map<String, Object> getDailyForecastForLocation(final UserInfo userInfo, final String postalCode, String locationCode, final String country, final int duration, final String productName)
    '''
def getHourlyForecastForLocation():
    '''public Map<String, Object> getHourlyForecastForLocation(final UserInfo userInfo, final String postalCode, String locationCode, final String country, final String hours, final String productName)
    '''
def getHistoricalWeatherForLocation():
    '''public Map<String, Object> getHistoricalWeatherForLocation(final UserInfo userInfo, final String postalCode, String locationCode, final String country, final Date startDate, final Date endDate, final String productName)
    '''
def getWeatherAlertsForLocation():
    '''public Map<String, Object> getWeatherAlertsForLocation(final UserInfo userInfo, final String postalCode, String locationCode, final String country, final String productName)
    '''
def checkConnection():
    '''public void checkConnection(@WSMboKey("WEATHERORG") final MboRemote weatherOrg)
    '''
def getServiceAddresses():
    '''public MboSetRemote getServiceAddresses()
    '''
def registryEndPointsForAlerts():
    '''public void registryEndPointsForAlerts(final boolean register)
    '''
def processAssetsRegistry():
    '''public void processAssetsRegistry(@WSMboKey("WEATHERZONE") final MboRemote weatherZone, final String actioncode)
    '''
def getProductCatalog():
    '''public List<Object> getProductCatalog(final String org)
    '''
def isWeatherLicenseInstalled():
    '''public boolean isWeatherLicenseInstalled(final String productName)
    '''
def logWeatherAPICall():
    '''public void logWeatherAPICall(String productName, final String resourceName, final UserInfo userInfo)
    '''
def distance():
    '''public double distance(final double lat1, final double lon1, final double lat2, final double lon2, final String uom)
    '''
