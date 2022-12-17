ATT_AMOC = "String  \"ATT_AMOC\""
PING_EP = "String  \"/telemetry/search\""
def ():
    '''returns AMOCProcessor\n\n
    ()\n
    '''
def getAMOCMeter():
    '''returns String\n\n
    getAMOCMeter(final String maximoMeter)\n
    '''
def processResource():
    '''returns JSONArtifact\n\n
    processResource(JSONResourceInfo resourceInfo, final MboRemote owner, final UserInfo userInfo, final int pageSize, final int currentPage, final JSONAnalyzer jsonAnalyzer)\n
    '''
def mapReadings():
    '''returns JSONObject\n\n
    mapReadings(final JSONObject jo, final MboRemote owner)\n
    '''
def pingHistorian():
    '''returns boolean\n\n
    pingHistorian(final IoTFService srv)\n
    '''
def getHeaders():
    '''returns String\n\n
    getHeaders(final Map propInfo)\n
    '''
def getBaseAttURL():
    '''returns String\n\n
    getBaseAttURL()\n
    '''
