MXDATA = "String  \"mxdata\""
LNG_PROPERTY = "String  \"lng\""
LAT_PROPERTY = "String  \"lat\""
AUTOLOCATEDATA = "String  \"autolocate\""
GISDATA = "String  \"gisdata\""
def MapDataUtils():
    '''public MapDataUtils()
    '''
def loadAttributesFromTemplate():
    '''public Map<String, Integer> loadAttributesFromTemplate(final String template, final String objectName, final MboRemote appMbo, final UserInfo userInfo)
    '''
def getLinearGraphicsbyWhereClause():
    '''public List<Long> getLinearGraphicsbyWhereClause(final String whereClause, final String objectName, final MboRemote appMbo, final UserInfo userInfo)
    '''
def getLinearLayerGraphicInfo():
    '''public String getLinearLayerGraphicInfo(final MboRemote mbo, final String objectname, final String relationship, final String msgTemplate, final String mapName, final UserInfo userinfo, final Map<String, String> attributes)
    '''
def deleteLinearSegment():
    '''public String deleteLinearSegment(final MboRemote appMbo, final String objectName, final String relationship, final Map<String, String> attributes, final UserInfo userinfo)
    '''
def getGISData():
    '''public JSONObject getGISData(final MboRemote currentMbo)
    '''
def getGISDataFromGisable():
    '''public JSONObject getGISDataFromGisable(final GISable gisMbo)
    '''
def getLBSData():
    '''public JSONObject getLBSData(final MboRemote currentMbo)
    '''
def getMXData():
    '''public JSONObject getMXData(final MboRemote currentMbo)
    '''
def getParamsAsJsonObject():
    '''public JSONObject getParamsAsJsonObject(final String jsonAsString)
    '''
def getParamsAsJsonArray():
    '''public JSONArray getParamsAsJsonArray(final String jsonAsString)
    '''
def getMboSetAsJSONArray():
    '''public JSONArray getMboSetAsJSONArray(final MboSetRemote mboSet)
    '''
def getMboAsJSONObject():
    '''public JSONObject getMboAsJSONObject(final MboRemote mbo)
    '''
def setGisableAttributes():
    '''public void setGisableAttributes(final MboRemote mbo, final JSONObject recordData, final JSONObject gisData)
    '''
def setJSONAutoLocateAttributes():
    '''public Boolean setJSONAutoLocateAttributes(final MboRemote mbo, final JSONObject recordData)
    '''
def hasIfAnyGISInfo():
    '''public boolean hasIfAnyGISInfo(final JSONObject recordData)
    '''
def getAllSymbologyAttributes():
    '''public static Map<String, Set<String>> getAllSymbologyAttributes(final UserInfo userInfo, final MboRemote mapManager)
    '''
def getSymbologyConfigObject():
    '''public static JSONObject getSymbologyConfigObject(final UserInfo userInfo, MboRemote mapManager)
    '''
def getObjectNameFromRecordData():
    '''public String getObjectNameFromRecordData(final JSONObject recordData)
    '''
def getObjectIdFromRecordData():
    '''public Long getObjectIdFromRecordData(final JSONObject recordData)
    '''
def getMapTipData():
    '''public String getMapTipData(final MboRemote mbo, final String mboName, final String templateField, final UserInfo userInfo, final JSONArray mapTipOverrides)
    '''
def getMinimumLastUpdateTimestamp():
    '''public Date getMinimumLastUpdateTimestamp()
    '''
def clearMapTipTemplateCache():
    '''public void clearMapTipTemplateCache()
    '''
def getLBSAuditData():
    '''public JSONArray getLBSAuditData(final MboRemote currentMbo, final Date startDate, final Date endDate)
    '''
def convertMeasure():
    '''public double convertMeasure(final double measure, final String unitSource, final String unitDestiny)
    '''
def setPopulateRelatedAttributes():
    '''public void setPopulateRelatedAttributes(final boolean isPopulateRelatedAttributes)
    '''
def isLinearInstalled():
    '''public static boolean isLinearInstalled()
    '''
def calculateLinearTargetSegment():
    '''public JSONObject calculateLinearTargetSegment(final MboRemote appMbo, final String mapMeasureUnit, final JSONObject linearObjTarget)
    '''
