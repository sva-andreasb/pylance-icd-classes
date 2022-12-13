def ExternalJSONMapper():
'''public ExternalJSONMapper(final String mapName)
'''
pass
def processJSON():
'''public MboRemote processJSON(final JSONArtifact jsonData, final String messageType, final String mosName, final UserInfo userInfo, final MXTransaction mxTrans)
'''
pass
def mapJSONtoOS():
'''public StructureData mapJSONtoOS(final JSONArtifact jsonData, final String interfaceName, final UserInfo userInfo)
public StructureData mapJSONtoOS(final JSONArtifact jsonData, final String messageType, final String mosName, final UserInfo userInfo)
public StructureData mapJSONtoOS(JSONArtifact jsonData, final String messageType, final String mosName, final UserInfo userInfo, final boolean toJSON)
'''
pass
def mapOSToJSON():
'''public JSONArtifact mapOSToJSON(final StructureData strucIn, final UserInfo userInfo)
public JSONArtifact mapOSToJSON(final StructureData strucIn, final UserInfo userInfo, final boolean fromJSON)
'''
pass
def mapMboToJSON():
'''public JSONArtifact mapMboToJSON(final MboRemote mbo, final UserInfo userInfo)
'''
pass
def mapMboSetToJSON():
'''public JSONArtifact mapMboSetToJSON(final MboSetRemote mboSet, final UserInfo userInfo)
'''
pass
def formatConditionalValue():
'''public String formatConditionalValue(final List<JSONMapPropertyValuesInfo> values, final Object jo, final String jsonData, final MboSetInfo msi)
'''
pass
def meetCondition():
'''public boolean meetCondition(final String condition, final Object jo, final String jsonData, final MboSetInfo msi)
'''
pass
def setForInsert():
'''public void setForInsert(final JSONObject jo, final String jsonData, final MboSetRemote mboSet)
'''
pass
