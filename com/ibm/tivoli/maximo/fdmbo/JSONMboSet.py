def ():
    '''returns JSONMboSet\n\n
    (final MboServerInterface ms)\n
    '''
def deserialize():
    '''returns None\n\n
    deserialize(final byte[] response, final JSONResourceInfo resourceInfo, final int index)\n
    '''
def json2MboSet():
    '''returns None\n\n
    json2MboSet(final JSONArray jsonArray, final JSONResourceInfo resourceInfo, final int start, final int end)\n
    '''
def json2Mbo():
    '''returns None\n\n
    json2Mbo(final Object jsonObj, final JSONObjectInfo detailInfo, final MboRemote parentMbo)\n
    '''
def toBeSaved():
    '''returns boolean\n\n
    toBeSaved()\n
    '''
def setup():
    '''returns MboRemote\n\n
    setup()\n
    '''
def setRelationship():
    '''returns None\n\n
    setRelationship(final String relationClause)\n
    '''
def setWhere():
    '''returns None\n\n
    setWhere(final String whereClause)\n
    '''
def setAppWhere():
    '''returns None\n\n
    setAppWhere(final String whereClause)\n
    '''
def setUserWhere():
    '''returns None\n\n
    setUserWhere(final String whereClause)\n
    '''
def getMbo():
    '''returns MboRemote\n\n
    getMbo(final int index)\n
    '''
def moveLast():
    '''returns MboRemote\n\n
    moveLast()\n
    '''
def count():
    '''returns int\n\n
    count()\n
    '''
def getCountFromResponse():
    '''returns int\n\n
    getCountFromResponse(final byte[] response)\n
    '''
def reset():
    '''returns None\n\n
    reset()\n
    '''
def resetJSON():
    '''returns None\n\n
    resetJSON()\n
    '''
def load():
    '''returns None\n\n
    load(final int index)\n
    '''
def invoke():
    '''returns byte[]\n\n
    invoke(final int index, final boolean forCount)\n
    '''
def setAdditionalData():
    '''returns None\n\n
    setAdditionalData(final MboRemote mbo, final JSONObject jo)\n
    '''
def bytesToJSONArray():
    '''returns JSONArray\n\n
    bytesToJSONArray(final byte[] data)\n
    '''
def getDataAsDouble():
    '''returns None\n\n
    getDataAsDouble(final Object value, final String attributeName, final MboRemote mbo)\n
    '''
def setUserWhereAfterParse():
    '''returns None\n\n
    setUserWhereAfterParse(final String where)\n
    '''
def setBulkUpdate():
    '''returns None\n\n
    setBulkUpdate(final boolean bulk)\n
    '''
def setResourceName():
    '''returns None\n\n
    setResourceName(final String resourceName)\n
    '''
def getResourceName():
    '''returns String\n\n
    getResourceName()\n
    '''
def formatResourceName():
    '''returns String\n\n
    formatResourceName(final String where)\n
    '''
def getProductName():
    '''returns String\n\n
    getProductName()\n
    '''
def getBulkUpdate():
    '''returns boolean\n\n
    getBulkUpdate()\n
    '''
def getEndPointName():
    '''returns String\n\n
    getEndPointName()\n
    '''
def getLimit():
    '''returns int\n\n
    getLimit()\n
    '''
def getURL():
    '''returns String\n\n
    getURL()\n
    '''
def setDateFormatType():
    '''returns None\n\n
    setDateFormatType(final String dateFormatType)\n
    '''
def getDateFormatType():
    '''returns String\n\n
    getDateFormatType()\n
    '''
def setDateFormat():
    '''returns None\n\n
    setDateFormat(final String dateFormat)\n
    '''
def getDateFormat():
    '''returns String\n\n
    getDateFormat()\n
    '''
def getNullFormat():
    '''returns String\n\n
    getNullFormat()\n
    '''
def supportsUpdate():
    '''returns boolean\n\n
    supportsUpdate()\n
    '''
