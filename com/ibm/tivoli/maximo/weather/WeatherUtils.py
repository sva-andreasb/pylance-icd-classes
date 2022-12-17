def woInWeatherAlertLifeSpan():
    '''returns boolean\n\n
    woInWeatherAlertLifeSpan(final MboRemote wo, final MboRemote alertImpact)\n
    '''
def assignmentInWeatherAlertLifeSpan():
    '''returns boolean\n\n
    assignmentInWeatherAlertLifeSpan(final Assignment assignment, final WeatherAlertImpact alertImpact)\n
    '''
def overlapAlert():
    '''returns boolean\n\n
    overlapAlert(final Date WorkStart, final Date WorkFinish, final MboRemote alertImpact)\n
    '''
def woInWeatherZone():
    '''returns boolean\n\n
    woInWeatherZone(final MboRemote wo, final MboRemote zone)\n
    '''
def geoDistance():
    '''returns double\n\n
    geoDistance(final WeatherAddress addr, final MboRemote zone)\n
    '''
def getLifeSpanMin():
    '''returns int\n\n
    getLifeSpanMin(final String lifespan)\n
    '''
def getWeatherAlertImpactForLoc():
    '''returns MboSetRemote\n\n
    getWeatherAlertImpactForLoc(final WeatherAddress addr, final UserInfo userInfo)\n
    '''
def getweatherAlertForAddr():
    '''returns String\n\n
    getweatherAlertForAddr(final Date apptdate, final WeatherAddress addr, final UserInfo userinfo)\n
    '''
def locationInWeatherZone():
    '''returns boolean\n\n
    locationInWeatherZone(final WeatherAddress addr, final MboRemote zone)\n
    '''
