def ():
    '''returns IoTFService\n\n
    (final MXServer mxServer)\n
    ()\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def getDeviceTypesNotIn():
    '''returns List<Object>\n\n
    getDeviceTypesNotIn(@WSMboKey("IOTFCFG") final MboRemote iotf, final List<String> excludeTheseTypes, final String sort)\n
    '''
def getNotMappedYetDeviceTypes():
    '''returns List<Object>\n\n
    getNotMappedYetDeviceTypes(@WSMboKey("IOTFCFG") final MboRemote iotf, final String sort)\n
    '''
def getAllIoTHistorians():
    '''returns List<Object>\n\n
    getAllIoTHistorians()\n
    '''
def pingHistorian():
    '''returns boolean\n\n
    pingHistorian()\n
    '''
def getHistorianDatabaseName():
    '''returns String\n\n
    getHistorianDatabaseName(final String orgid, final String historian, final Date dt)\n
    '''
def getAnyHistorianDatabaseName():
    '''returns String\n\n
    getAnyHistorianDatabaseName(final String orgid, final String historian, String choice, String bucket, final Date dt, final int offset, final boolean isDefault)\n
    '''
def getAllDeviceTypes():
    '''returns List<Object>\n\n
    getAllDeviceTypes(@WSMboKey("IOTFCFG") final MboRemote iotf, final String sort)\n
    '''
def getLastMessageFromCache():
    '''returns JSONArray\n\n
    getLastMessageFromCache(final String org, final String apiKey, final String authToken, final String type, final String deviceid)\n
    '''
def canDeleteOrg():
    '''returns None\n\n
    canDeleteOrg(@WSMboKey("IOTFCFG") final MboRemote iotf)\n
    '''
def canDeleteDeviceType():
    '''returns None\n\n
    canDeleteDeviceType(@WSMboKey("IOTFDEVICETYPECFG") final MboRemote iotf)\n
    '''
def clearDeviceRefernceForOrg():
    '''returns None\n\n
    clearDeviceRefernceForOrg(@WSMboKey("IOTFCFG") final MboRemote iotf)\n
    '''
def clearDeviceRefernce():
    '''returns None\n\n
    clearDeviceRefernce(@WSMboKey("IOTFDEVICETYPECFG") final MboRemote iotf)\n
    '''
def syncDevices():
    '''returns None\n\n
    syncDevices(final String iotfOrg, final UserInfo userInfo)\n
    '''
def getDevices():
    '''returns List<Object>\n\n
    getDevices(final String iotfOrg, final UserInfo userInfo, final String deviceType, final int limit)\n
    getDevices(final String iotfOrg, final String apiKey, final String apiToken, final String deviceType, final int limit)\n
    '''
def deleteDocument():
    '''returns None\n\n
    deleteDocument(final Map<String, Object> metaData, String postUrl, final HTTPHandler handler)\n
    '''
def invokeIoTAPI():
    '''returns byte[]\n\n
    invokeIoTAPI(final String org, final String apiKey, final String authToken, final String apiURL)\n
    '''
def getBaseIoTURL():
    '''returns String\n\n
    getBaseIoTURL(final String org)\n
    getBaseIoTURL(final String org, final String endPointName)\n
    '''
