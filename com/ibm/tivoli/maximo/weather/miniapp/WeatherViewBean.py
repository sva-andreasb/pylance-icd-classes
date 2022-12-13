SCHEDULER_MSG_GROUP = "String  scheduler""
def label():
'''public String label(final String key)
'''
pass
def filterCss():
'''public String filterCss(final String css, final MiniAppControl control)
'''
pass
def getBaseImageUrl():
'''public String getBaseImageUrl()
'''
pass
def getPresentationOptions():
'''public JSONObject getPresentationOptions()
'''
pass
def discoverWeather():
'''public JSONObject discoverWeather()
'''
pass
def discoverWeatherWithOptions():
'''public JSONObject discoverWeatherWithOptions(@MXEventParam("options") final JSONObject options)
'''
pass
def jsonError():
'''public JSONObject jsonError(final int code, final String text)
public JSONObject jsonError(final int code, final String text, final Throwable t)
'''
pass
def getCurrentWeather():
'''public JSONObject getCurrentWeather(@MXEventParam("lat") final double lat, @MXEventParam("lng") final double lng)
'''
pass
def getDailyWeather():
'''public JSONObject getDailyWeather(@MXEventParam("lat") final double lat, @MXEventParam("lng") final double lng)
'''
pass
def getHourlyWeather():
'''public JSONObject getHourlyWeather(@MXEventParam("lat") final double lat, @MXEventParam("lng") final double lng)
'''
pass
def getAppName():
'''public String getAppName()
'''
pass
