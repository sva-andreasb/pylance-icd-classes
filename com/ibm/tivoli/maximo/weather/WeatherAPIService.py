def ():
    '''returns WeatherAPIService\n\n
    (final MXServer mxServer)\n
    ()\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def checkConnection():
    '''returns None\n\n
    checkConnection(@WSMboKey("WEATHERORG") final MboRemote weatherOrg)\n
    '''
def getServiceAddresses():
    '''returns MboSetRemote\n\n
    getServiceAddresses()\n
    '''
def registryEndPointsForAlerts():
    '''returns None\n\n
    registryEndPointsForAlerts(final boolean register)\n
    '''
def processAssetsRegistry():
    '''returns None\n\n
    processAssetsRegistry(@WSMboKey("WEATHERZONE") final MboRemote weatherZone, final String actioncode)\n
    '''
def getProductCatalog():
    '''returns List<Object>\n\n
    getProductCatalog(final String org)\n
    '''
def isWeatherLicenseInstalled():
    '''returns boolean\n\n
    isWeatherLicenseInstalled(final String productName)\n
    '''
def logWeatherAPICall():
    '''returns None\n\n
    logWeatherAPICall(String productName, final String resourceName, final UserInfo userInfo)\n
    '''
def distance():
    '''returns double\n\n
    distance(final double lat1, final double lon1, final double lat2, final double lon2, final String uom)\n
    '''
