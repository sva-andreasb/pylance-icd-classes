def createEvent():
    '''    public static void createEvent(final String productCode, final UserInfo userInfo)
    '''
def createSubscription():
    '''    public static void createSubscription(final String productCode, final String personid, final UserInfo userInfo)
    '''
def getLatitudeLongitudeForWO():
    '''    public static WeatherAddress getLatitudeLongitudeForWO(final MboRemote workOrder)
    '''
def getLatitudeLongitudeForLocation():
    '''    public static WeatherAddress getLatitudeLongitudeForLocation(final MboRemote locationMbo)
    '''
def getWeatherLookup():
    '''    public static WeatherForecastLookup getWeatherLookup(final long woid, Date start, Date end, final UserInfo userInfo)
    '''
def GetWeatherConfig():
    '''    public static WeatherConfig GetWeatherConfig(final String appname, final String weatherName, final String portforlio, final UserInfo userInfo)
    '''
def getWeatherDisplayConfig():
    '''    public static WeatherDisplayConfig getWeatherDisplayConfig(final String appname, final UserInfo userInfo)
    '''
def woInWeatherAlertLifeSpan():
    '''    public boolean woInWeatherAlertLifeSpan(final MboRemote wo, final MboRemote alertImpact)
    '''
def assignmentInWeatherAlertLifeSpan():
    '''    public boolean assignmentInWeatherAlertLifeSpan(final Assignment assignment, final WeatherAlertImpact alertImpact)
    '''
def overlapAlert():
    '''    public boolean overlapAlert(final Date WorkStart, final Date WorkFinish, final MboRemote alertImpact)
    '''
def woInWeatherZone():
    '''    public boolean woInWeatherZone(final MboRemote wo, final MboRemote zone)
    '''
def geoDistance():
    '''    public double geoDistance(final WeatherAddress addr, final MboRemote zone)
    public static double geoDistance(final double lat1, final double lon1, final double lat2, final double lon2, final String uom)
    '''
def getLifeSpanMin():
    '''    public int getLifeSpanMin(final String lifespan)
    '''
def getWeatherAlertImpactForLoc():
    '''    public MboSetRemote getWeatherAlertImpactForLoc(final WeatherAddress addr, final UserInfo userInfo)
    '''
def getweatherAlertForAddr():
    '''    public String getweatherAlertForAddr(final Date apptdate, final WeatherAddress addr, final UserInfo userinfo)
    '''
def locationInWeatherZone():
    '''    public boolean locationInWeatherZone(final WeatherAddress addr, final MboRemote zone)
    '''
