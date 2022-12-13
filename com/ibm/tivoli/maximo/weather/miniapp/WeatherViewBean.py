SCHEDULER_MSG_GROUP = "String  \"scheduler\""
def label():
    '''    public String label(final String key)
    '''
def filterCss():
    '''    public String filterCss(final String css, final MiniAppControl control)
    '''
def getBaseImageUrl():
    '''    public String getBaseImageUrl()
    '''
def getPresentationOptions():
    '''    public JSONObject getPresentationOptions()
    '''
def discoverWeather():
    '''    public JSONObject discoverWeather()
    '''
def discoverWeatherWithOptions():
    '''    public JSONObject discoverWeatherWithOptions(@MXEventParam("options") final JSONObject options)
    '''
def jsonError():
    '''    public JSONObject jsonError(final int code, final String text)
    public JSONObject jsonError(final int code, final String text, final Throwable t)
    '''
def getCurrentWeather():
    '''    public JSONObject getCurrentWeather(@MXEventParam("lat") final double lat, @MXEventParam("lng") final double lng)
    '''
def getDailyWeather():
    '''    public JSONObject getDailyWeather(@MXEventParam("lat") final double lat, @MXEventParam("lng") final double lng)
    '''
def getHourlyWeather():
    '''    public JSONObject getHourlyWeather(@MXEventParam("lat") final double lat, @MXEventParam("lng") final double lng)
    '''
def getAppName():
    '''    public String getAppName()
    '''
