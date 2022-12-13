def OslcYaml():
'''public OslcYaml()
'''
pass
def setSwaggerVersion():
'''public OslcYaml setSwaggerVersion(final String swaggerVersion)
'''
pass
def setOpenAPIVersion():
'''public OslcYaml setOpenAPIVersion(final String openAPIVersion)
'''
pass
def setInfo():
'''public OslcYaml setInfo(final String title, final String description, final String version)
'''
pass
def setInfoTermsOfService():
'''public OslcYaml setInfoTermsOfService(final String tos)
'''
pass
def setInfoContact():
'''public OslcYaml setInfoContact(final Object contactInfo)
'''
pass
def setInfoLicense():
'''public OslcYaml setInfoLicense(final Object licenseIfo)
'''
pass
def setPatternedObject():
'''public OslcYaml setPatternedObject(final String patternName, final Object content)
'''
pass
def setHost():
'''public OslcYaml setHost(final String host)
public OslcYaml setHost(final String host, final int port)
'''
pass
def setSchemes():
'''public OslcYaml setSchemes(final String... strs)
'''
pass
def addSecuritySchemes():
'''public OslcYaml addSecuritySchemes(final String key, final Object schemes)
'''
pass
def addSecurity():
'''public OslcYaml addSecurity(final String key, final Object scope)
'''
pass
def setBasePath():
'''public OslcYaml setBasePath(final String basePath)
'''
pass
def setServer():
'''public OslcYaml setServer(final JSONObject server)
'''
pass
def setConsumes():
'''public OslcYaml setConsumes(final String... consumes)
'''
pass
def addActionSchemaToComponent():
'''public boolean addActionSchemaToComponent(final String actionName, final JSONObject actionSchema)
'''
pass
def addOSSchemaToComponent():
'''public boolean addOSSchemaToComponent(final String osName, final UserInfo userInfo)
'''
pass
def addMethodBasicInfo():
'''public OslcYaml addMethodBasicInfo(final String pathName, final String methodName, final String summary, final String description)
'''
pass
def addMethodOperationId():
'''public OslcYaml addMethodOperationId(final String pathName, final String methodName, final String id)
public OslcYaml addMethodOperationId()
'''
pass
def addMethodProduces():
'''public OslcYaml addMethodProduces(final String pathName, final String methodName, final String... produces)
'''
pass
def addMethodTags():
'''public OslcYaml addMethodTags(final String pathName, final String methodName, final String... tags)
'''
pass
def addMethodParams():
'''public OslcYaml addMethodParams(final String pathName, final String methodName, final JSONObject params)
'''
pass
def addMethodRequestBody():
'''public OslcYaml addMethodRequestBody(final String pathName, final String methodName, final JSONObject body)
'''
pass
def addMethodRequestBodyContent():
'''public OslcYaml addMethodRequestBodyContent(final String pathName, final String methodName, final String contentType, final JSONObject params)
'''
pass
def addMethodResponse():
'''public OslcYaml addMethodResponse(final String pathName, final String methodName, final String status, final JSONObject statusContent)
'''
pass
def addMethodResponseForOS():
'''public OslcYaml addMethodResponseForOS(final String pathName, final String methodName, final String status, final JSONObject statusContent, final boolean osSchemaAdded, final String osName, final boolean isResource)
'''
pass
def addMethodExternalDocs():
'''public OslcYaml addMethodExternalDocs()
'''
pass
def addMethodConsumes():
'''public OslcYaml addMethodConsumes(final String pathName, final String methodName, final String... consumes)
'''
pass
def addMethodSchemes():
'''public OslcYaml addMethodSchemes(final String pathName, final String methodName, final String... schemes)
'''
pass
def addMethodDeprecated():
'''public OslcYaml addMethodDeprecated()
'''
pass
def addMethodPatternedObject():
'''public OslcYaml addMethodPatternedObject()
'''
pass
def addDefinitionsProperties():
'''public OslcYaml addDefinitionsProperties(final String defName, final String propertyName, final JSONObject definitions)
'''
pass
def addDefinitionsRequired():
'''public OslcYaml addDefinitionsRequired(final String defName, final JSONArray requiredArr)
'''
pass
def addDefinitionsDescription():
'''public OslcYaml addDefinitionsDescription(final String defName, final String description)
'''
pass
def addParameters():
'''public OslcYaml addParameters(final String paramName, final JSONObject parameters)
'''
pass
def addResponses():
'''public OslcYaml addResponses(final String paramName, final JSONObject parameters)
'''
pass
def addSecurityDefinitions():
'''public OslcYaml addSecurityDefinitions()
'''
pass
def addTags():
'''public OslcYaml addTags()
'''
pass
def addExternalDocs():
'''public OslcYaml addExternalDocs()
'''
pass
def getJSON():
'''public JSONObject getJSON()
'''
pass
def getYaml():
'''public String getYaml()
'''
pass
def setParamBasicInfo():
'''public void setParamBasicInfo(final JSONObject param, final String in, final String name, final String description, final String required, final String type)
'''
pass
def main():
'''public static void main(final String... args)
'''
pass
def getYamlfromJSON():
'''public static String getYamlfromJSON(final JSONObject object)
'''
pass
def jsonPrettyPrinter():
'''public static void jsonPrettyPrinter(final Object object)
'''
pass
def setIsJson():
'''public void setIsJson(final boolean isJson)
'''
pass
