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
def ClassificationMgr():
    '''public ClassificationMgr(final ProgressLogger<?> logger, final String siteId, final String orgId, final UserInfo userInfo)
    '''
def cleanup():
    '''public void cleanup()
    '''
def getClassification():
    '''public String getClassification(String classificationName, final String cobieObjectType, final Item item, final boolean allowSite, final boolean allowOrg)
    '''
def getClassificationSingle():
    '''public String getClassificationSingle(final String classificationName, final String cobieObjectType, final Item item, final boolean allowSite, final boolean allowOrg)
    '''
def getClassifcationDescriotion():
    '''public String getClassifcationDescriotion(final String classStructId, final ItemBase item)
    '''
def setAddMissing():
    '''public void setAddMissing(final boolean addMissing)
    '''
def setTypesAreSpec():
    '''public void setTypesAreSpec(final boolean typesAreSpecs)
    '''
def associateAttributeTypesWithClassifications():
    '''public void associateAttributeTypesWithClassifications(final AttributeTypeMap typeMap, final AttributeMapMgr mapMgr, final String[] sheets)
    '''
def fixupProductDefaultUseWith():
    '''public void fixupProductDefaultUseWith()
    '''
