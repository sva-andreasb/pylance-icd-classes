JSCHE_STRING = "String  \"string\""
JSCHE_NUMBER = "String  \"number\""
JSCHE_NULL = "String  \"null\""
JSCHE_INTEGER = "String  \"integer\""
JSCHE_BOOLEAN = "String  \"boolean\""
JSCHE_ARRAY = "String  \"array\""
JSCHE_OBJECT = "String  \"object\""
def setAddEnum():
    '''    public void setAddEnum(final boolean addEnum)
    '''
def isAddEnum():
    '''    public boolean isAddEnum()
    '''
def setUserInfo():
    '''    public void setUserInfo(final UserInfo userInfo)
    '''
def setResourceProperties():
    '''    public void setResourceProperties(final Map<String, OslcResourceProperty> resourceProperties)
    '''
def OslcJsonSchemaGenerator():
    '''    public OslcJsonSchemaGenerator(final String osName, final Map<String, OslcResourceProperty> resourceProperties, final boolean internalValue, final UserInfo userInfo, final boolean oasSchemaCompliance)
    public OslcJsonSchemaGenerator(final OslcRequest oslcRequest, final String osName, final String relatedResource, final boolean oasSchemaCompliance)
    '''
def createResourceProperty():
    '''    public void createResourceProperty(final boolean occurs, final String propName, final JSONSchema jschema, final String propNs, final String valueType, final String linkOSName, final MosDetailInfo mosDetailInfo, final OslcResourceDetailInfo resourceDetailInfo, final IfaceColumnInfo colInfo)
    '''
def createAttachmentResourceProperty():
    '''    public void createAttachmentResourceProperty(String occurs, final String propName, final JSONSchema jsonschema, final String valueType, final String subSchemaURI, final String title, final String usageURIs, final String representationURI, final MosDetailInfo mosDetailInfo)
    '''
def createLiteralProperty():
    '''    public void createLiteralProperty(final boolean occurs, final String propName, final JSONSchema js, final String propNs, final String valueType, final MosDetailInfo mosDetailInfo, final IfaceColumnInfo colInfo, final Mbo zombieMbo)
    '''
def createRelationLiteralProperty():
    '''    public void createRelationLiteralProperty(final boolean occurs, final String propName, final JSONSchema js, final MboValueInfo mvi, final MboValueInfoStatic mvis, final String overrideTitle)
    '''
def createAttachmentLiteralProperty():
    '''    public void createAttachmentLiteralProperty(final boolean occur, final String propName, final JSONSchema jsonschema, final String type, final String title, final String defaultValueOrigin, final int maxLength, final IfaceColumnInfo ifcl)
    '''
def createImplicitProperties():
    '''    public void createImplicitProperties(final JSONSchema jsonschema)
    '''
def relationJSONSchema():
    '''    public void relationJSONSchema(final String xattr, String curxattr, final MboSetRemote msr, final Mbo zombieMbo, final JSONSchema jsonSchema)
    public void relationJSONSchema(final String xattr, String curxattr, final MboSetRemote msr, final Mbo zombieMbo, final JSONSchema jsonSchema, final String alias)
    '''
def relatedJSONSchema():
    '''    public void relatedJSONSchema(final String xattr, final String curxattr, final MboSetRemote msr, final Mbo zombieMbo, final JSONSchema jsonSchema, final Map<String, OslcResourceProperty> resProp)
    '''
def generateJSONSchema():
    '''    public JSONSchema generateJSONSchema()
    '''
def getRepresentation():
    '''    public OslcResourceResponse getRepresentation()
    '''
def getRepresentationAsJSON():
    '''    public JSONObject getRepresentationAsJSON()
    '''
def getShape():
    '''    public byte[] getShape()
    '''
def getShapeAsJSON():
    '''    public JSONObject getShapeAsJSON()
    '''
def addPrimaryKeys():
    '''    public void addPrimaryKeys(final JSONSchema jsonSchema, final MosDetailInfo mosDetailInfo)
    '''
def loadOSDetailDescriptions():
    '''    public void loadOSDetailDescriptions()
    '''
def getMapDesc():
    '''    public Map<String, String> getMapDesc()
    '''
def setMapDesc():
    '''    public void setMapDesc(final Map<String, String> mapDesc)
    '''
def isOasSchemaCompliance():
    '''    public boolean isOasSchemaCompliance()
    '''
def setOasSchemaCompliance():
    '''    public void setOasSchemaCompliance(final boolean oasSchemaCompliance)
    '''
