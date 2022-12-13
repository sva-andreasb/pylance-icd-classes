MXDATA = "String  mxdata""
LNG_PROPERTY = "String  lng""
LAT_PROPERTY = "String  lat""
AUTOLOCATEDATA = "String  autolocate""
GISDATA = "String  gisdata""
def MapDataUtils():
'''public MapDataUtils()
'''
pass
def loadAttributesFromTemplate():
'''public Map<String, Integer> loadAttributesFromTemplate(final String template, final String objectName, final MboRemote appMbo, final UserInfo userInfo)
'''
pass
def getLinearGraphicsbyWhereClause():
'''public List<Long> getLinearGraphicsbyWhereClause(final String whereClause, final String objectName, final MboRemote appMbo, final UserInfo userInfo)
'''
pass
def getLinearLayerGraphicInfo():
'''public String getLinearLayerGraphicInfo(final MboRemote mbo, final String objectname, final String relationship, final String msgTemplate, final String mapName, final UserInfo userinfo, final Map<String, String> attributes)
'''
pass
def deleteLinearSegment():
'''public String deleteLinearSegment(final MboRemote appMbo, final String objectName, final String relationship, final Map<String, String> attributes, final UserInfo userinfo)
'''
pass
def getGISData():
'''public JSONObject getGISData(final MboRemote currentMbo)
'''
pass
def getGISDataFromGisable():
'''public JSONObject getGISDataFromGisable(final GISable gisMbo)
'''
pass
def getLBSData():
'''public JSONObject getLBSData(final MboRemote currentMbo)
'''
pass
def getMXData():
'''public JSONObject getMXData(final MboRemote currentMbo)
'''
pass
def getParamsAsJsonObject():
'''public JSONObject getParamsAsJsonObject(final String jsonAsString)
'''
pass
def getParamsAsJsonArray():
'''public JSONArray getParamsAsJsonArray(final String jsonAsString)
'''
pass
def getMboSetAsJSONArray():
'''public JSONArray getMboSetAsJSONArray(final MboSetRemote mboSet)
'''
pass
def getMboAsJSONObject():
'''public JSONObject getMboAsJSONObject(final MboRemote mbo)
'''
pass
def setGisableAttributes():
'''public void setGisableAttributes(final MboRemote mbo, final JSONObject recordData, final JSONObject gisData)
'''
pass
def setJSONAutoLocateAttributes():
'''public Boolean setJSONAutoLocateAttributes(final MboRemote mbo, final JSONObject recordData)
'''
pass
def hasIfAnyGISInfo():
'''public boolean hasIfAnyGISInfo(final JSONObject recordData)
'''
pass
def getAllSymbologyAttributes():
'''public static Map<String, Set<String>> getAllSymbologyAttributes(final UserInfo userInfo, final MboRemote mapManager)
'''
pass
def getSymbologyConfigObject():
'''public static JSONObject getSymbologyConfigObject(final UserInfo userInfo, MboRemote mapManager)
'''
pass
def getObjectNameFromRecordData():
'''public String getObjectNameFromRecordData(final JSONObject recordData)
'''
pass
def getObjectIdFromRecordData():
'''public Long getObjectIdFromRecordData(final JSONObject recordData)
'''
pass
def getMapTipData():
'''public String getMapTipData(final MboRemote mbo, final String mboName, final String templateField, final UserInfo userInfo, final JSONArray mapTipOverrides)
'''
pass
def getMinimumLastUpdateTimestamp():
'''public Date getMinimumLastUpdateTimestamp()
'''
pass
def clearMapTipTemplateCache():
'''public void clearMapTipTemplateCache()
'''
pass
def getLBSAuditData():
'''public JSONArray getLBSAuditData(final MboRemote currentMbo, final Date startDate, final Date endDate)
'''
pass
def convertMeasure():
'''public double convertMeasure(final double measure, final String unitSource, final String unitDestiny)
'''
pass
def setPopulateRelatedAttributes():
'''public void setPopulateRelatedAttributes(final boolean isPopulateRelatedAttributes)
'''
pass
def isLinearInstalled():
'''public static boolean isLinearInstalled()
'''
pass
def calculateLinearTargetSegment():
'''public JSONObject calculateLinearTargetSegment(final MboRemote appMbo, final String mapMeasureUnit, final JSONObject linearObjTarget)
'''
pass
