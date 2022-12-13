def IoTCloudantProcessor():
    '''    public IoTCloudantProcessor()
    '''
def getReadingDate():
    '''    public Map<String, Object> getReadingDate(final JSONObject json, final String iotServiceName, final IoTMeterToPayloadMappingInfo mappingInfo)
    '''
def setReadingsForHistorianData():
    '''    public String setReadingsForHistorianData(final JSONObject jo, final IoTMeterToPayloadMappingInfo mappingInfo, final Date readingDate)
    '''
def processResource():
    '''    public JSONArtifact processResource(final JSONResourceInfo resourceInfo, final MboRemote owner, final UserInfo userInfo, final int pageSize, final int currentPage, final JSONAnalyzer jsonAnalyzer)
    '''
def mapReadings():
    '''    public void mapReadings(final JSONArray readings, final JSONObject jo, final IoTMeterToPayloadMappingInfo mapInfo)
    '''
def getReadings():
    '''    public Object getReadings(final JSONObject jo, final IoTMeterToPayloadMappingInfo mapInfo)
    '''
def evaluateExpression():
    '''    public JSONObject evaluateExpression(final JSONObject jsonData, final String path)
    '''
