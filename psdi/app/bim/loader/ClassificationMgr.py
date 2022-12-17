OBJECT_TYPE_FACILITY = "String  \"FACILITY\""
OBJECT_TYPE_FLOOR = "String  \"FLOOR\""
OBJECT_TYPE_SPACE = "String  \"SPACE\""
OBJECT_TYPE_COMPONENT = "String  \"COMPONENT\""
OBJECT_TYPE_SYSTEM = "String  \"SYSTEM\""
OBJECT_TYPE_ZONE = "String  \"ZONE\""
OBJECT_TYPE_ASSET = "String  \"ASSET\""
OBJECT_TYPE_TYPE = "String  \"TYPE\""
OBJECT_TYPE_CONTACT = "String  \"CONTACT\""
OBJECT_TYPE_COMPANY = "String  \"COMPANY\""
OBJECT_TYPE_ITEM = "String  \"ITEM\""
OBJECT_TYPE_JOB = "String  \"JOB\""
QUERY_CLASSSTRUCT = "String  \"CLASSSTRUCTUREID =:1\""
def ():
    '''returns ClassificationMgr\n\n
    (final ProgressLogger<?> logger, final String siteId, final String orgId, final UserInfo userInfo)\n
    '''
def cleanup():
    '''returns None\n\n
    cleanup()\n
    '''
def getClassification():
    '''returns String\n\n
    getClassification(String classificationName, final String cobieObjectType, final Item item, final boolean allowSite, final boolean allowOrg)\n
    '''
def getClassificationSingle():
    '''returns String\n\n
    getClassificationSingle(final String classificationName, final String cobieObjectType, final Item item, final boolean allowSite, final boolean allowOrg)\n
    '''
def getClassifcationDescriotion():
    '''returns String\n\n
    getClassifcationDescriotion(final String classStructId, final ItemBase item)\n
    '''
def setAddMissing():
    '''returns None\n\n
    setAddMissing(final boolean addMissing)\n
    '''
def setTypesAreSpec():
    '''returns None\n\n
    setTypesAreSpec(final boolean typesAreSpecs)\n
    '''
def associateAttributeTypesWithClassifications():
    '''returns None\n\n
    associateAttributeTypesWithClassifications(final AttributeTypeMap typeMap, final AttributeMapMgr mapMgr, final String[] sheets)\n
    '''
def fixupProductDefaultUseWith():
    '''returns None\n\n
    fixupProductDefaultUseWith()\n
    '''
