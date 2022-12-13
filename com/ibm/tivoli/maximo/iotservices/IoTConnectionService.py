def IoTConnectionService():
    '''    public IoTConnectionService(final MXServer mxServer)
    public IoTConnectionService()
    '''
def init():
    '''    public void init()
    '''
def pingIoT():
    '''    public JSONObject pingIoT(@WSMboKey("IOTSERVICE") final MboRemote iotserv, final boolean iotcfg)
    '''
def getAllDeviceTypes():
    '''    public List<Object> getAllDeviceTypes(@WSMboKey("IOTSERVICE") final MboRemote iotserv, final String sort)
    '''
def getDeviceTypeList():
    '''    public List<Object> getDeviceTypeList(@WSMboKey("IOTSERVICE") final MboRemote iotserv, final String sort, final boolean isMapped)
    '''
def getNotMappedYetDeviceTypes():
    '''    public List<Object> getNotMappedYetDeviceTypes(@WSMboKey("IOTSERVICE") final MboRemote iotserv, final String sort)
    '''
def getLastMessageFromCache():
    '''    public Map<String, Object> getLastMessageFromCache(@WSMboKey("IOTSERVICE") final MboRemote iotService, final String deviceType)
    '''
def getLastMessageFromCacheForDevice():
    '''    public Map<String, Object> getLastMessageFromCacheForDevice(@WSMboKey("IOTSERVICE") final MboRemote iotserv, final String deviceType, final String deviceid)
    '''
def getSampleAggregateResultForDeviceType():
    '''    public JSONObject getSampleAggregateResultForDeviceType(@WSMboKey("IOTSERVICE") final MboRemote iotService, final String deviceType, final String feedMapProperty, final String deviceid)
    '''
def clearDeviceRefernceForService():
    '''    public void clearDeviceRefernceForService(@WSMboKey("IOTSERVICE") final MboRemote iotservice)
    '''
def clearDeviceReferenceAssetLocationLevel():
    '''    public void clearDeviceReferenceAssetLocationLevel(final MboRemote iotconfig)
    '''
def clearDeviceRefernce():
    '''    public void clearDeviceRefernce(@WSMboKey("IOTFDEVICETYPECFG") final MboRemote iotf)
    '''
def getEndPointValues():
    '''    public List<String> getEndPointValues(final String servicename)
    '''
def refreshIoTServicesCache():
    '''    public void refreshIoTServicesCache(final MboSet mboset)
    '''
def getDevices():
    '''    public List<Object> getDevices(@WSMboKey("IOTSERVICE") final MboRemote iotserv, final String deviceType, final String limit)
    '''
def checkCronTaskInstance():
    '''    public Map<String, Object> checkCronTaskInstance(final String instancename)
    '''
def devices():
    '''    public List<Object> devices(final String deviceType)
    '''
def createAsset():
    '''    public void createAsset(final String iotfOrg, final String deviceType, final JSONObject deviceJO)
    '''
def getHistorianDatabaseName():
    '''    public String getHistorianDatabaseName(final String orgid, final String historian, final Date dt)
    '''
def getAnyHistorianDatabaseName():
    '''    public String getAnyHistorianDatabaseName(final String orgid, final String historian, String choice, String bucket, final Date dt, final int offset, final boolean isDefault)
    '''
def deleteDocument():
    '''    public void deleteDocument(final Map<String, Object> metaData, String postUrl, final HTTPHandler handler)
    '''
def canDeleteDeviceType():
    '''    public void canDeleteDeviceType(@WSMboKey("IOTFDEVICETYPECFG") final MboRemote iotdevtype)
    '''
def anyDeviceTypesMapped():
    '''    public boolean anyDeviceTypesMapped(@WSMboKey("IOTSERVICE") final MboRemote iotserv)
    '''
def isDeviceTypeAssociated():
    '''    public boolean isDeviceTypeAssociated(@WSMboKey("IOTFDEVICETYPECFG") final MboRemote iotservice, final String deviceType)
    '''
def getTimePeriods():
    '''    public List<String> getTimePeriods(@WSMboKey("IOTSERVICE") final MboRemote iotserv)
    '''
def listOwnerChain():
    '''    public static String listOwnerChain(MboSet mboset)
    '''
