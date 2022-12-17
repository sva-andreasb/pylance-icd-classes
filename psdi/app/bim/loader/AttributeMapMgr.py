QUERY_MAP_LOOKUP = "String  \"MAPNAME =:1  and ( SITEID =:2 or SITEID is null )  and ( ORGID =:3 or ORGID is null )\""
TYPE_ALN = "String  \"ALN\""
TYPE_AMOUNT = "String  \"AMOUNT\""
TYPE_BIGINT = "String  \"BIGINT\""
TYPE_BLOB = "String  \"BLOB\""
TYPE_CLOB = "String  \"CLOB\""
TYPE_CRYPTO = "String  \"CRYPTO\""
TYPE_CRYPTOX = "String  \"CRYPTOX\""
TYPE_DATE = "String  \"DATE\""
TYPE_DATETIME = "String  \"DATETIME\""
TYPE_DECIMAL = "String  \"DECIMAL\""
TYPE_DURATION = "String  \"DURATION\""
TYPE_FLOAT = "String  \"FLOAT\""
TYPE_GL = "String  \"GL\""
TYPE_INTEGER = "String  \"INTEGER\""
TYPE_LONGALN = "String  \"LONGALN\""
TYPE_LOWER = "String  \"LOWER\""
TYPE_SMALLINT = "String  \"SMALLINT\""
TYPE_TIME = "String  \"TIME\""
TYPE_UPPER = "String  \"UPPER\""
TYPE_YORN = "String  \"YORN\""
def ():
    '''returns AttributeMapMgr\n\n
    (final ModelProcessIntf loader, final String fieldMapName, final String specMapName)\n
    '''
def isSkipAttributeType():
    '''returns boolean\n\n
    isSkipAttributeType(final ItemAttributeType attribType)\n
    '''
def isSkipAttribute():
    '''returns boolean\n\n
    isSkipAttribute(String attribName, final String sheetName)\n
    '''
def isSkipAttributeForMbo():
    '''returns boolean\n\n
    isSkipAttributeForMbo(String attribName, final String mboName)\n
    '''
def setMappedFields():
    '''returns None\n\n
    setMappedFields(final Enumeration<ItemATTRIBUTE> attributes, final MboRemote mbo)\n
    '''
def setMappedField():
    '''returns boolean\n\n
    setMappedField(final ItemATTRIBUTE attrib, final String tableName, final MboRemote mbo)\n
    '''
def getMappedSpec():
    '''returns SpecEntry\n\n
    getMappedSpec(final String attributeName)\n
    '''
def getAttributeForSpec():
    '''returns String\n\n
    getAttributeForSpec(final String attrId)\n
    '''
def getMappedField():
    '''returns Set<ItemATTRIBUTE>\n\n
    getMappedField(final ItemBase item, final MboRemote mbo)\n
    '''
def getAssetAttridId():
    '''returns String\n\n
    getAssetAttridId()\n
    '''
def getDataType():
    '''returns String\n\n
    getDataType()\n
    '''
def getDescription():
    '''returns String\n\n
    getDescription()\n
    '''
def getOrgId():
    '''returns String\n\n
    getOrgId()\n
    '''
def getSiteId():
    '''returns String\n\n
    getSiteId()\n
    '''
