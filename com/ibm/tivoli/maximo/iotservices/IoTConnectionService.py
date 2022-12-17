def ():
    '''returns IoTConnectionService\n\n
    (final MXServer mxServer)\n
    ()\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def pingIoT():
    '''returns JSONObject\n\n
    pingIoT(@WSMboKey("IOTSERVICE") final MboRemote iotserv, final boolean iotcfg)\n
    '''
def getAllDeviceTypes():
    '''returns List<Object>\n\n
    getAllDeviceTypes(@WSMboKey("IOTSERVICE") final MboRemote iotserv, final String sort)\n
    '''
def getDeviceTypeList():
    '''returns List<Object>\n\n
    getDeviceTypeList(@WSMboKey("IOTSERVICE") final MboRemote iotserv, final String sort, final boolean isMapped)\n
    '''
def getNotMappedYetDeviceTypes():
    '''returns List<Object>\n\n
    getNotMappedYetDeviceTypes(@WSMboKey("IOTSERVICE") final MboRemote iotserv, final String sort)\n
    '''
def getSampleAggregateResultForDeviceType():
    '''returns JSONObject\n\n
    getSampleAggregateResultForDeviceType(@WSMboKey("IOTSERVICE") final MboRemote iotService, final String deviceType, final String feedMapProperty, final String deviceid)\n
    '''
def clearDeviceRefernceForService():
    '''returns None\n\n
    clearDeviceRefernceForService(@WSMboKey("IOTSERVICE") final MboRemote iotservice)\n
    '''
def clearDeviceReferenceAssetLocationLevel():
    '''returns None\n\n
    clearDeviceReferenceAssetLocationLevel(final MboRemote iotconfig)\n
    '''
def clearDeviceRefernce():
    '''returns None\n\n
    clearDeviceRefernce(@WSMboKey("IOTFDEVICETYPECFG") final MboRemote iotf)\n
    '''
def getEndPointValues():
    '''returns List<String>\n\n
    getEndPointValues(final String servicename)\n
    '''
def refreshIoTServicesCache():
    '''returns None\n\n
    refreshIoTServicesCache(final MboSet mboset)\n
    '''
def getDevices():
    '''returns List<Object>\n\n
    getDevices(@WSMboKey("IOTSERVICE") final MboRemote iotserv, final String deviceType, final String limit)\n
    '''
def devices():
    '''returns List<Object>\n\n
    devices(final String deviceType)\n
    '''
def createAsset():
    '''returns None\n\n
    createAsset(final String iotfOrg, final String deviceType, final JSONObject deviceJO)\n
    '''
def getHistorianDatabaseName():
    '''returns String\n\n
    getHistorianDatabaseName(final String orgid, final String historian, final Date dt)\n
    '''
def getAnyHistorianDatabaseName():
    '''returns String\n\n
    getAnyHistorianDatabaseName(final String orgid, final String historian, String choice, String bucket, final Date dt, final int offset, final boolean isDefault)\n
    '''
def deleteDocument():
    '''returns None\n\n
    deleteDocument(final Map<String, Object> metaData, String postUrl, final HTTPHandler handler)\n
    '''
def canDeleteDeviceType():
    '''returns None\n\n
    canDeleteDeviceType(@WSMboKey("IOTFDEVICETYPECFG") final MboRemote iotdevtype)\n
    '''
def anyDeviceTypesMapped():
    '''returns boolean\n\n
    anyDeviceTypesMapped(@WSMboKey("IOTSERVICE") final MboRemote iotserv)\n
    '''
def isDeviceTypeAssociated():
    '''returns boolean\n\n
    isDeviceTypeAssociated(@WSMboKey("IOTFDEVICETYPECFG") final MboRemote iotservice, final String deviceType)\n
    '''
def getTimePeriods():
    '''returns List<String>\n\n
    getTimePeriods(@WSMboKey("IOTSERVICE") final MboRemote iotserv)\n
    '''
