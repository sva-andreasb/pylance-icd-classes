def IoTCloudantProcessor():
    '''public IoTCloudantProcessor()
    '''
def syncMeterReadings():
    '''public void syncMeterReadings(String iotOrg, final String deviceType, final String instanceName, final Date lastRun)
    '''
def processHistorianData():
    '''public void processHistorianData(final IoTFDeviceMappingInfo mappingInfo, String histURL, final URLFormatter uf, final String endPointName, final String iotOrg, final String deviceType, final Date lastRun)
    '''
def processResource():
    '''public JSONArtifact processResource(final JSONResourceInfo resourceInfo, final MboRemote owner, final UserInfo userInfo, final int pageSize, final int currentPage, final JSONAnalyzer jsonAnalyzer)
    '''
def mapReadings():
    '''public void mapReadings(final JSONArray readings, final JSONObject jo, final IoTFDeviceMappingInfo mapInfo)
    '''
def getReadings():
    '''public Object getReadings(final JSONObject jo, final IoTFDeviceMappingInfo mapInfo)
    '''
def evaluateExpression():
    '''public JSONObject evaluateExpression(final JSONObject jsonData, final String path)
    '''
def pingHistorian():
    '''public boolean pingHistorian(final IoTFService srv)
    '''
