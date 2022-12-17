JSCHE_STRING = "String  \"string\""
JSCHE_NUMBER = "String  \"number\""
JSCHE_NULL = "String  \"null\""
JSCHE_INTEGER = "String  \"integer\""
JSCHE_BOOLEAN = "String  \"boolean\""
JSCHE_ARRAY = "String  \"array\""
JSCHE_OBJECT = "String  \"object\""
def setAddEnum():
    '''returns None\n\n
    setAddEnum(final boolean addEnum)\n
    '''
def isAddEnum():
    '''returns boolean\n\n
    isAddEnum()\n
    '''
def setUserInfo():
    '''returns None\n\n
    setUserInfo(final UserInfo userInfo)\n
    '''
def setResourceProperties():
    '''returns None\n\n
    setResourceProperties(final Map<String, OslcResourceProperty> resourceProperties)\n
    '''
def ():
    '''returns OslcJsonSchemaGenerator\n\n
    (final String osName, final Map<String, OslcResourceProperty> resourceProperties, final boolean internalValue, final UserInfo userInfo, final boolean oasSchemaCompliance)\n
    (final OslcRequest oslcRequest, final String osName, final String relatedResource, final boolean oasSchemaCompliance)\n
    '''
def createResourceProperty():
    '''returns None\n\n
    createResourceProperty(final boolean occurs, final String propName, final JSONSchema jschema, final String propNs, final String valueType, final String linkOSName, final MosDetailInfo mosDetailInfo, final OslcResourceDetailInfo resourceDetailInfo, final IfaceColumnInfo colInfo)\n
    '''
def createAttachmentResourceProperty():
    '''returns None\n\n
    createAttachmentResourceProperty(String occurs, final String propName, final JSONSchema jsonschema, final String valueType, final String subSchemaURI, final String title, final String usageURIs, final String representationURI, final MosDetailInfo mosDetailInfo)\n
    '''
def createLiteralProperty():
    '''returns None\n\n
    createLiteralProperty(final boolean occurs, final String propName, final JSONSchema js, final String propNs, final String valueType, final MosDetailInfo mosDetailInfo, final IfaceColumnInfo colInfo, final Mbo zombieMbo)\n
    '''
def createRelationLiteralProperty():
    '''returns None\n\n
    createRelationLiteralProperty(final boolean occurs, final String propName, final JSONSchema js, final MboValueInfo mvi, final MboValueInfoStatic mvis, final String overrideTitle)\n
    '''
def createAttachmentLiteralProperty():
    '''returns None\n\n
    createAttachmentLiteralProperty(final boolean occur, final String propName, final JSONSchema jsonschema, final String type, final String title, final String defaultValueOrigin, final int maxLength, final IfaceColumnInfo ifcl)\n
    '''
def createImplicitProperties():
    '''returns None\n\n
    createImplicitProperties(final JSONSchema jsonschema)\n
    '''
def relationJSONSchema():
    '''returns None\n\n
    relationJSONSchema(final String xattr, String curxattr, final MboSetRemote msr, final Mbo zombieMbo, final JSONSchema jsonSchema)\n
    relationJSONSchema(final String xattr, String curxattr, final MboSetRemote msr, final Mbo zombieMbo, final JSONSchema jsonSchema, final String alias)\n
    '''
def relatedJSONSchema():
    '''returns None\n\n
    relatedJSONSchema(final String xattr, final String curxattr, final MboSetRemote msr, final Mbo zombieMbo, final JSONSchema jsonSchema, final Map<String, OslcResourceProperty> resProp)\n
    '''
def generateJSONSchema():
    '''returns JSONSchema\n\n
    generateJSONSchema()\n
    '''
def getRepresentation():
    '''returns OslcResourceResponse\n\n
    getRepresentation()\n
    '''
def getRepresentationAsJSON():
    '''returns JSONObject\n\n
    getRepresentationAsJSON()\n
    '''
def getShape():
    '''returns byte[]\n\n
    getShape()\n
    '''
def getShapeAsJSON():
    '''returns JSONObject\n\n
    getShapeAsJSON()\n
    '''
def addPrimaryKeys():
    '''returns None\n\n
    addPrimaryKeys(final JSONSchema jsonSchema, final MosDetailInfo mosDetailInfo)\n
    '''
def loadOSDetailDescriptions():
    '''returns None\n\n
    loadOSDetailDescriptions()\n
    '''
def setMapDesc():
    '''returns None\n\n
    setMapDesc(final Map<String, String> mapDesc)\n
    '''
def isOasSchemaCompliance():
    '''returns boolean\n\n
    isOasSchemaCompliance()\n
    '''
def setOasSchemaCompliance():
    '''returns None\n\n
    setOasSchemaCompliance(final boolean oasSchemaCompliance)\n
    '''
