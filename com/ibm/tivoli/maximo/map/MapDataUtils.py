MXDATA = "String  \"mxdata\""
LNG_PROPERTY = "String  \"lng\""
LAT_PROPERTY = "String  \"lat\""
AUTOLOCATEDATA = "String  \"autolocate\""
GISDATA = "String  \"gisdata\""
def ():
    '''returns MapDataUtils\n\n
    ()\n
    '''
def getLinearGraphicsbyWhereClause():
    '''returns List<Long>\n\n
    getLinearGraphicsbyWhereClause(final String whereClause, final String objectName, final MboRemote appMbo, final UserInfo userInfo)\n
    '''
def getLinearLayerGraphicInfo():
    '''returns String\n\n
    getLinearLayerGraphicInfo(final MboRemote mbo, final String objectname, final String relationship, final String msgTemplate, final String mapName, final UserInfo userinfo, final Map<String, String> attributes)\n
    '''
def deleteLinearSegment():
    '''returns String\n\n
    deleteLinearSegment(final MboRemote appMbo, final String objectName, final String relationship, final Map<String, String> attributes, final UserInfo userinfo)\n
    '''
def getGISData():
    '''returns JSONObject\n\n
    getGISData(final MboRemote currentMbo)\n
    '''
def getGISDataFromGisable():
    '''returns JSONObject\n\n
    getGISDataFromGisable(final GISable gisMbo)\n
    '''
def getLBSData():
    '''returns JSONObject\n\n
    getLBSData(final MboRemote currentMbo)\n
    '''
def getMXData():
    '''returns JSONObject\n\n
    getMXData(final MboRemote currentMbo)\n
    '''
def getParamsAsJsonObject():
    '''returns JSONObject\n\n
    getParamsAsJsonObject(final String jsonAsString)\n
    '''
def getParamsAsJsonArray():
    '''returns JSONArray\n\n
    getParamsAsJsonArray(final String jsonAsString)\n
    '''
def getMboSetAsJSONArray():
    '''returns JSONArray\n\n
    getMboSetAsJSONArray(final MboSetRemote mboSet)\n
    '''
def getMboAsJSONObject():
    '''returns JSONObject\n\n
    getMboAsJSONObject(final MboRemote mbo)\n
    '''
def setGisableAttributes():
    '''returns None\n\n
    setGisableAttributes(final MboRemote mbo, final JSONObject recordData, final JSONObject gisData)\n
    '''
def setJSONAutoLocateAttributes():
    '''returns Boolean\n\n
    setJSONAutoLocateAttributes(final MboRemote mbo, final JSONObject recordData)\n
    '''
def hasIfAnyGISInfo():
    '''returns boolean\n\n
    hasIfAnyGISInfo(final JSONObject recordData)\n
    '''
def getObjectNameFromRecordData():
    '''returns String\n\n
    getObjectNameFromRecordData(final JSONObject recordData)\n
    '''
def getObjectIdFromRecordData():
    '''returns Long\n\n
    getObjectIdFromRecordData(final JSONObject recordData)\n
    '''
def getMapTipData():
    '''returns String\n\n
    getMapTipData(final MboRemote mbo, final String mboName, final String templateField, final UserInfo userInfo, final JSONArray mapTipOverrides)\n
    '''
def getMinimumLastUpdateTimestamp():
    '''returns Date\n\n
    getMinimumLastUpdateTimestamp()\n
    '''
def clearMapTipTemplateCache():
    '''returns None\n\n
    clearMapTipTemplateCache()\n
    '''
def getLBSAuditData():
    '''returns JSONArray\n\n
    getLBSAuditData(final MboRemote currentMbo, final Date startDate, final Date endDate)\n
    '''
def convertMeasure():
    '''returns double\n\n
    convertMeasure(final double measure, final String unitSource, final String unitDestiny)\n
    '''
def setPopulateRelatedAttributes():
    '''returns None\n\n
    setPopulateRelatedAttributes(final boolean isPopulateRelatedAttributes)\n
    '''
def calculateLinearTargetSegment():
    '''returns JSONObject\n\n
    calculateLinearTargetSegment(final MboRemote appMbo, final String mapMeasureUnit, final JSONObject linearObjTarget)\n
    '''
