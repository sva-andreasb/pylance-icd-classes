def IoTConnectionService():
'''public IoTConnectionService(final MXServer mxServer)
public IoTConnectionService()
'''
pass
def init():
'''public void init()
'''
pass
def pingIoT():
'''public JSONObject pingIoT(@WSMboKey("IOTSERVICE") final MboRemote iotserv, final boolean iotcfg)
'''
pass
def getAllDeviceTypes():
'''public List<Object> getAllDeviceTypes(@WSMboKey("IOTSERVICE") final MboRemote iotserv, final String sort)
'''
pass
def getDeviceTypeList():
'''public List<Object> getDeviceTypeList(@WSMboKey("IOTSERVICE") final MboRemote iotserv, final String sort, final boolean isMapped)
'''
pass
def getNotMappedYetDeviceTypes():
'''public List<Object> getNotMappedYetDeviceTypes(@WSMboKey("IOTSERVICE") final MboRemote iotserv, final String sort)
'''
pass
def getLastMessageFromCache():
'''public Map<String, Object> getLastMessageFromCache(@WSMboKey("IOTSERVICE") final MboRemote iotService, final String deviceType)
'''
pass
def getLastMessageFromCacheForDevice():
'''public Map<String, Object> getLastMessageFromCacheForDevice(@WSMboKey("IOTSERVICE") final MboRemote iotserv, final String deviceType, final String deviceid)
'''
pass
def getSampleAggregateResultForDeviceType():
'''public JSONObject getSampleAggregateResultForDeviceType(@WSMboKey("IOTSERVICE") final MboRemote iotService, final String deviceType, final String feedMapProperty, final String deviceid)
'''
pass
def clearDeviceRefernceForService():
'''public void clearDeviceRefernceForService(@WSMboKey("IOTSERVICE") final MboRemote iotservice)
'''
pass
def clearDeviceReferenceAssetLocationLevel():
'''public void clearDeviceReferenceAssetLocationLevel(final MboRemote iotconfig)
'''
pass
def clearDeviceRefernce():
'''public void clearDeviceRefernce(@WSMboKey("IOTFDEVICETYPECFG") final MboRemote iotf)
'''
pass
def getEndPointValues():
'''public List<String> getEndPointValues(final String servicename)
'''
pass
def refreshIoTServicesCache():
'''public void refreshIoTServicesCache(final MboSet mboset)
'''
pass
def getDevices():
'''public List<Object> getDevices(@WSMboKey("IOTSERVICE") final MboRemote iotserv, final String deviceType, final String limit)
'''
pass
def checkCronTaskInstance():
'''public Map<String, Object> checkCronTaskInstance(final String instancename)
'''
pass
def devices():
'''public List<Object> devices(final String deviceType)
'''
pass
def createAsset():
'''public void createAsset(final String iotfOrg, final String deviceType, final JSONObject deviceJO)
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
def deleteDocument():
'''public void deleteDocument(final Map<String, Object> metaData, String postUrl, final HTTPHandler handler)
'''
pass
def canDeleteDeviceType():
'''public void canDeleteDeviceType(@WSMboKey("IOTFDEVICETYPECFG") final MboRemote iotdevtype)
'''
pass
def anyDeviceTypesMapped():
'''public boolean anyDeviceTypesMapped(@WSMboKey("IOTSERVICE") final MboRemote iotserv)
'''
pass
def isDeviceTypeAssociated():
'''public boolean isDeviceTypeAssociated(@WSMboKey("IOTFDEVICETYPECFG") final MboRemote iotservice, final String deviceType)
'''
pass
def getTimePeriods():
'''public List<String> getTimePeriods(@WSMboKey("IOTSERVICE") final MboRemote iotserv)
'''
pass
def listOwnerChain():
'''public static String listOwnerChain(MboSet mboset)
'''
pass
