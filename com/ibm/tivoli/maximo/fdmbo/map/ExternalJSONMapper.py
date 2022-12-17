def ():
    '''returns ExternalJSONMapper\n\n
    (final String mapName)\n
    '''
def processJSON():
    '''returns MboRemote\n\n
    processJSON(final JSONArtifact jsonData, final String messageType, final String mosName, final UserInfo userInfo, final MXTransaction mxTrans)\n
    '''
def mapJSONtoOS():
    '''returns StructureData\n\n
    mapJSONtoOS(final JSONArtifact jsonData, final String interfaceName, final UserInfo userInfo)\n
    mapJSONtoOS(final JSONArtifact jsonData, final String messageType, final String mosName, final UserInfo userInfo)\n
    mapJSONtoOS(JSONArtifact jsonData, final String messageType, final String mosName, final UserInfo userInfo, final boolean toJSON)\n
    '''
def mapOSToJSON():
    '''returns JSONArtifact\n\n
    mapOSToJSON(final StructureData strucIn, final UserInfo userInfo)\n
    mapOSToJSON(final StructureData strucIn, final UserInfo userInfo, final boolean fromJSON)\n
    '''
def mapMboToJSON():
    '''returns JSONArtifact\n\n
    mapMboToJSON(final MboRemote mbo, final UserInfo userInfo)\n
    '''
def mapMboSetToJSON():
    '''returns JSONArtifact\n\n
    mapMboSetToJSON(final MboSetRemote mboSet, final UserInfo userInfo)\n
    '''
def formatConditionalValue():
    '''returns String\n\n
    formatConditionalValue(final List<JSONMapPropertyValuesInfo> values, final Object jo, final String jsonData, final MboSetInfo msi)\n
    '''
def meetCondition():
    '''returns boolean\n\n
    meetCondition(final String condition, final Object jo, final String jsonData, final MboSetInfo msi)\n
    '''
def setForInsert():
    '''returns None\n\n
    setForInsert(final JSONObject jo, final String jsonData, final MboSetRemote mboSet)\n
    '''
