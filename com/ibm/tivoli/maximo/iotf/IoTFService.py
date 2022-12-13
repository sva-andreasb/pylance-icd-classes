def IoTFService():
'''public IoTFService(final MXServer mxServer)
public IoTFService()
'''
pass
def init():
'''public void init()
'''
pass
def getDeviceTypesNotIn():
'''public List<Object> getDeviceTypesNotIn(@WSMboKey("IOTFCFG") final MboRemote iotf, final List<String> excludeTheseTypes, final String sort)
'''
pass
def getNotMappedYetDeviceTypes():
'''public List<Object> getNotMappedYetDeviceTypes(@WSMboKey("IOTFCFG") final MboRemote iotf, final String sort)
'''
pass
def getAllIoTHistorians():
'''public List<Object> getAllIoTHistorians()
'''
pass
def validateHistorianEndPoint():
'''public Map<String, Object> validateHistorianEndPoint(final String orgid, final String url, final String user, final String password, final String bucket, final String dbname)
'''
pass
def pingHistorian():
'''public boolean pingHistorian()
'''
pass
def getHistorianDatabaseName():
'''public String getHistorianDatabaseName(final String orgid, final String historian, final Date dt)
'''
pass
def getAnyHistorianDatabaseName():
'''public String getAnyHistorianDatabaseName(final String orgid, final String historian, String choice, String bucket, final Date dt, final int offset, final boolean isDefault)
'''
pass
def getAllDeviceTypes():
'''public List<Object> getAllDeviceTypes(@WSMboKey("IOTFCFG") final MboRemote iotf, final String sort)
'''
pass
def pingIoT():
'''public Map<String, Object> pingIoT(final String iotfOrg, final String apiKey, final String authToken, final String processclass)
'''
pass
def pingIoTF():
'''public Map<String, Object> pingIoTF(final String iotfOrg, final String apiKey, final String authToken)
'''
pass
def testConnectivity():
'''public Map<String, Object> testConnectivity(@WSMboKey("IOTFCFG") final MboRemote iotfOrg)
'''
pass
def getLastMessageFromCache():
'''public Map<String, Object> getLastMessageFromCache(@WSMboKey("IOTFCFG") final MboRemote iotf, final String deviceType)
public JSONArray getLastMessageFromCache(final String org, final String apiKey, final String authToken, final String type, final String deviceid)
'''
pass
def getLastMessageFromCacheForDevice():
'''public Map<String, Object> getLastMessageFromCacheForDevice(@WSMboKey("IOTFCFG") final MboRemote iotf, final String deviceType, final String deviceid)
'''
pass
def canDeleteOrg():
'''public void canDeleteOrg(@WSMboKey("IOTFCFG") final MboRemote iotf)
'''
pass
def canDeleteDeviceType():
'''public void canDeleteDeviceType(@WSMboKey("IOTFDEVICETYPECFG") final MboRemote iotf)
'''
pass
def clearDeviceRefernceForOrg():
'''public void clearDeviceRefernceForOrg(@WSMboKey("IOTFCFG") final MboRemote iotf)
'''
pass
def clearDeviceRefernce():
'''public void clearDeviceRefernce(@WSMboKey("IOTFDEVICETYPECFG") final MboRemote iotf)
'''
pass
def checkCronTaskInstance():
'''public Map<String, Object> checkCronTaskInstance(final String instancename)
'''
pass
def syncDevices():
'''public void syncDevices(final String iotfOrg, final UserInfo userInfo)
'''
pass
def getDevices():
'''public List<Object> getDevices(final String iotfOrg, final UserInfo userInfo, final String deviceType, final int limit)
public List<Object> getDevices(final String iotfOrg, final String apiKey, final String apiToken, final String deviceType, final int limit)
'''
pass
def deleteDocument():
'''public void deleteDocument(final Map<String, Object> metaData, String postUrl, final HTTPHandler handler)
'''
pass
def invokeIoTAPI():
'''public byte[] invokeIoTAPI(final String org, final String apiKey, final String authToken, final String apiURL)
'''
pass
def getBaseIoTURL():
'''public String getBaseIoTURL(final String org)
public String getBaseIoTURL(final String org, final String endPointName)
'''
pass
