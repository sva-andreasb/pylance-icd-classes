JSCHE_STRING = "String  \"string\""
JSCHE_NUMBER = "String  \"number\""
JSCHE_NULL = "String  \"null\""
JSCHE_INTEGER = "String  \"integer\""
JSCHE_BOOLEAN = "String  \"boolean\""
JSCHE_ARRAY = "String  \"array\""
JSCHE_OBJECT = "String  \"object\""
def setResourceProperties():
    '''returns None\n\n
    setResourceProperties(final Map<String, OslcResourceProperty> resourceProperties)\n
    '''
def setZombie():
    '''returns None\n\n
    setZombie(final MboRemote zombie)\n
    '''
def ():
    '''returns OslcMboJsonSchemaGenerator\n\n
    (final boolean oasSchemaCompliance)\n
    (final OslcRequest oslcRequest, final String objectName, final boolean oasSchemaCompliance)\n
    (final OslcRequest oslcRequest, final String objectName, final MboRemote owner, final String relation, final boolean oasSchemaCompliance)\n
    '''
def createLiteralProperty():
    '''returns None\n\n
    createLiteralProperty(final boolean occurs, final String propName, final JSONSchema js, final String propNs, final String valueType, final MboValueInfo colInfo, final Mbo zombieMbo)\n
    '''
def createRelationLiteralProperty():
    '''returns None\n\n
    createRelationLiteralProperty(final boolean occurs, final String propName, final JSONSchema js, final MboValueInfo mvi, final MboValueInfoStatic mvis, final String overrideTitle)\n
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
def addPrimaryKeys():
    '''returns None\n\n
    addPrimaryKeys(final JSONSchema jsonSchema, final String objectName)\n
    '''
def setMapDesc():
    '''returns None\n\n
    setMapDesc(final Map<String, String> mapDesc)\n
    '''
