def ():
    '''returns IoTCloudantProcessor\n\n
    ()\n
    '''
def syncMeterReadings():
    '''returns None\n\n
    syncMeterReadings(String iotOrg, final String deviceType, final String instanceName, final Date lastRun)\n
    '''
def processHistorianData():
    '''returns None\n\n
    processHistorianData(final IoTFDeviceMappingInfo mappingInfo, String histURL, final URLFormatter uf, final String endPointName, final String iotOrg, final String deviceType, final Date lastRun)\n
    '''
def processResource():
    '''returns JSONArtifact\n\n
    processResource(final JSONResourceInfo resourceInfo, final MboRemote owner, final UserInfo userInfo, final int pageSize, final int currentPage, final JSONAnalyzer jsonAnalyzer)\n
    '''
def mapReadings():
    '''returns None\n\n
    mapReadings(final JSONArray readings, final JSONObject jo, final IoTFDeviceMappingInfo mapInfo)\n
    '''
def getReadings():
    '''returns Object\n\n
    getReadings(final JSONObject jo, final IoTFDeviceMappingInfo mapInfo)\n
    '''
def evaluateExpression():
    '''returns JSONObject\n\n
    evaluateExpression(final JSONObject jsonData, final String path)\n
    '''
def pingHistorian():
    '''returns boolean\n\n
    pingHistorian(final IoTFService srv)\n
    '''
