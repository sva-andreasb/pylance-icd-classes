JSCHE_STRING = "String string""
JSCHE_NUMBER = "String number""
JSCHE_NULL = "String null""
JSCHE_INTEGER = "String integer""
JSCHE_BOOLEAN = "String boolean""
JSCHE_ARRAY = "String array""
JSCHE_OBJECT = "String object""
def setResourceProperties():
'''public void setResourceProperties(final Map<String, OslcResourceProperty> resourceProperties)
'''
pass
def setZombie():
'''public void setZombie(final MboRemote zombie)
'''
pass
def OslcMboJsonSchemaGenerator():
'''public OslcMboJsonSchemaGenerator(final boolean oasSchemaCompliance)
public OslcMboJsonSchemaGenerator(final OslcRequest oslcRequest, final String objectName, final boolean oasSchemaCompliance)
public OslcMboJsonSchemaGenerator(final OslcRequest oslcRequest, final String objectName, final MboRemote owner, final String relation, final boolean oasSchemaCompliance)
'''
pass
def createLiteralProperty():
'''public void createLiteralProperty(final boolean occurs, final String propName, final JSONSchema js, final String propNs, final String valueType, final MboValueInfo colInfo, final Mbo zombieMbo)
'''
pass
def createRelationLiteralProperty():
'''public void createRelationLiteralProperty(final boolean occurs, final String propName, final JSONSchema js, final MboValueInfo mvi, final MboValueInfoStatic mvis, final String overrideTitle)
'''
pass
def relationJSONSchema():
'''public void relationJSONSchema(final String xattr, String curxattr, final MboSetRemote msr, final Mbo zombieMbo, final JSONSchema jsonSchema)
public void relationJSONSchema(final String xattr, String curxattr, final MboSetRemote msr, final Mbo zombieMbo, final JSONSchema jsonSchema, final String alias)
'''
pass
def relatedJSONSchema():
'''public void relatedJSONSchema(final String xattr, final String curxattr, final MboSetRemote msr, final Mbo zombieMbo, final JSONSchema jsonSchema, final Map<String, OslcResourceProperty> resProp)
'''
pass
def generateJSONSchema():
'''public JSONSchema generateJSONSchema()
'''
pass
def getRepresentation():
'''public OslcResourceResponse getRepresentation()
'''
pass
def getRepresentationAsJSON():
'''public JSONObject getRepresentationAsJSON()
'''
pass
def getShape():
'''public byte[] getShape()
'''
pass
def addPrimaryKeys():
'''public void addPrimaryKeys(final JSONSchema jsonSchema, final String objectName)
'''
pass
def getMapDesc():
'''public Map<String, String> getMapDesc()
'''
pass
def setMapDesc():
'''public void setMapDesc(final Map<String, String> mapDesc)
'''
pass
