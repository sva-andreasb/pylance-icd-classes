def IoTFService():
    '''public IoTFService(final MXServer mxServer)
    public IoTFService()
    '''
def init():
    '''public void init()
    '''
def getDeviceTypesNotIn():
    '''public List<Object> getDeviceTypesNotIn(@WSMboKey("IOTFCFG") final MboRemote iotf, final List<String> excludeTheseTypes, final String sort)
    '''
def getNotMappedYetDeviceTypes():
    '''public List<Object> getNotMappedYetDeviceTypes(@WSMboKey("IOTFCFG") final MboRemote iotf, final String sort)
    '''
def getAllIoTHistorians():
    '''public List<Object> getAllIoTHistorians()
    '''
def validateHistorianEndPoint():
    '''public Map<String, Object> validateHistorianEndPoint(final String orgid, final String url, final String user, final String password, final String bucket, final String dbname)
    '''
def pingHistorian():
    '''public boolean pingHistorian()
    '''
def getHistorianDatabaseName():
    '''public String getHistorianDatabaseName(final String orgid, final String historian, final Date dt)
    '''
def getAnyHistorianDatabaseName():
    '''public String getAnyHistorianDatabaseName(final String orgid, final String historian, String choice, String bucket, final Date dt, final int offset, final boolean isDefault)
    '''
def getAllDeviceTypes():
    '''public List<Object> getAllDeviceTypes(@WSMboKey("IOTFCFG") final MboRemote iotf, final String sort)
    '''
def pingIoT():
    '''public Map<String, Object> pingIoT(final String iotfOrg, final String apiKey, final String authToken, final String processclass)
    '''
def pingIoTF():
    '''public Map<String, Object> pingIoTF(final String iotfOrg, final String apiKey, final String authToken)
    '''
def testConnectivity():
    '''public Map<String, Object> testConnectivity(@WSMboKey("IOTFCFG") final MboRemote iotfOrg)
    '''
def getLastMessageFromCache():
    '''public Map<String, Object> getLastMessageFromCache(@WSMboKey("IOTFCFG") final MboRemote iotf, final String deviceType)
    public JSONArray getLastMessageFromCache(final String org, final String apiKey, final String authToken, final String type, final String deviceid)
    '''
def getLastMessageFromCacheForDevice():
    '''public Map<String, Object> getLastMessageFromCacheForDevice(@WSMboKey("IOTFCFG") final MboRemote iotf, final String deviceType, final String deviceid)
    '''
def canDeleteOrg():
    '''public void canDeleteOrg(@WSMboKey("IOTFCFG") final MboRemote iotf)
    '''
def canDeleteDeviceType():
    '''public void canDeleteDeviceType(@WSMboKey("IOTFDEVICETYPECFG") final MboRemote iotf)
    '''
def clearDeviceRefernceForOrg():
    '''public void clearDeviceRefernceForOrg(@WSMboKey("IOTFCFG") final MboRemote iotf)
    '''
def clearDeviceRefernce():
    '''public void clearDeviceRefernce(@WSMboKey("IOTFDEVICETYPECFG") final MboRemote iotf)
    '''
def checkCronTaskInstance():
    '''public Map<String, Object> checkCronTaskInstance(final String instancename)
    '''
def syncDevices():
    '''public void syncDevices(final String iotfOrg, final UserInfo userInfo)
    '''
def getDevices():
    '''public List<Object> getDevices(final String iotfOrg, final UserInfo userInfo, final String deviceType, final int limit)
    public List<Object> getDevices(final String iotfOrg, final String apiKey, final String apiToken, final String deviceType, final int limit)
    '''
def deleteDocument():
    '''public void deleteDocument(final Map<String, Object> metaData, String postUrl, final HTTPHandler handler)
    '''
def invokeIoTAPI():
    '''public byte[] invokeIoTAPI(final String org, final String apiKey, final String authToken, final String apiURL)
    '''
def getBaseIoTURL():
    '''public String getBaseIoTURL(final String org)
    public String getBaseIoTURL(final String org, final String endPointName)
    '''
