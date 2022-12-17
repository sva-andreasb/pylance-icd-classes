SCHEDULER_MSG_GROUP = "String  \"scheduler\""
def label():
    '''returns String\n\n
    label(final String key)\n
    '''
def filterCss():
    '''returns String\n\n
    filterCss(final String css, final MiniAppControl control)\n
    '''
def getBaseImageUrl():
    '''returns String\n\n
    getBaseImageUrl()\n
    '''
def getPresentationOptions():
    '''returns JSONObject\n\n
    getPresentationOptions()\n
    '''
def discoverWeather():
    '''returns JSONObject\n\n
    discoverWeather()\n
    '''
def discoverWeatherWithOptions():
    '''returns JSONObject\n\n
    discoverWeatherWithOptions(@MXEventParam("options") final JSONObject options)\n
    '''
def jsonError():
    '''returns JSONObject\n\n
    jsonError(final int code, final String text)\n
    jsonError(final int code, final String text, final Throwable t)\n
    '''
def getCurrentWeather():
    '''returns JSONObject\n\n
    getCurrentWeather(@MXEventParam("lat") final double lat, @MXEventParam("lng") final double lng)\n
    '''
def getDailyWeather():
    '''returns JSONObject\n\n
    getDailyWeather(@MXEventParam("lat") final double lat, @MXEventParam("lng") final double lng)\n
    '''
def getHourlyWeather():
    '''returns JSONObject\n\n
    getHourlyWeather(@MXEventParam("lat") final double lat, @MXEventParam("lng") final double lng)\n
    '''
def getAppName():
    '''returns String\n\n
    getAppName()\n
    '''
