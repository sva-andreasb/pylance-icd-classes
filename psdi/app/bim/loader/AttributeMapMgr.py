QUERY_MAP_LOOKUP = "String  MAPNAME =:1  and ( SITEID =:2 or SITEID is null )  and ( ORGID =:3 or ORGID is null )""
TYPE_ALN = "String  ALN""
TYPE_AMOUNT = "String  AMOUNT""
TYPE_BIGINT = "String  BIGINT""
TYPE_BLOB = "String  BLOB""
TYPE_CLOB = "String  CLOB""
TYPE_CRYPTO = "String  CRYPTO""
TYPE_CRYPTOX = "String  CRYPTOX""
TYPE_DATE = "String  DATE""
TYPE_DATETIME = "String  DATETIME""
TYPE_DECIMAL = "String  DECIMAL""
TYPE_DURATION = "String  DURATION""
TYPE_FLOAT = "String  FLOAT""
TYPE_GL = "String  GL""
TYPE_INTEGER = "String  INTEGER""
TYPE_LONGALN = "String  LONGALN""
TYPE_LOWER = "String  LOWER""
TYPE_SMALLINT = "String  SMALLINT""
TYPE_TIME = "String  TIME""
TYPE_UPPER = "String  UPPER""
TYPE_YORN = "String  YORN""
def AttributeMapMgr():
'''public AttributeMapMgr(final ModelProcessIntf loader, final String fieldMapName, final String specMapName)
'''
pass
def isSkipAttributeType():
'''public boolean isSkipAttributeType(final ItemAttributeType attribType)
'''
pass
def isSkipAttribute():
'''public boolean isSkipAttribute(String attribName, final String sheetName)
'''
pass
def isSkipAttributeForMbo():
'''public boolean isSkipAttributeForMbo(String attribName, final String mboName)
'''
pass
def setMappedFields():
'''public void setMappedFields(final Enumeration<ItemATTRIBUTE> attributes, final MboRemote mbo)
'''
pass
def setMappedField():
'''public boolean setMappedField(final ItemATTRIBUTE attrib, final String tableName, final MboRemote mbo)
'''
pass
def getMappedSpec():
'''public SpecEntry getMappedSpec(final String attributeName)
'''
pass
def getAttributeForSpec():
'''public String getAttributeForSpec(final String attrId)
'''
pass
def getMappedField():
'''public Set<ItemATTRIBUTE> getMappedField(final ItemBase item, final MboRemote mbo)
'''
pass
def getAssetAttridId():
'''public String getAssetAttridId()
'''
pass
def getDataType():
'''public String getDataType()
'''
pass
def getDescription():
'''public String getDescription()
'''
pass
def getOrgId():
'''public String getOrgId()
'''
pass
def getSiteId():
'''public String getSiteId()
'''
pass
