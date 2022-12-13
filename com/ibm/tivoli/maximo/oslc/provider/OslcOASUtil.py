def addYamlMethodParamsForRoute():
'''public static void addYamlMethodParamsForRoute(final JSONObject paramsMeta, final String pathName, final String methodName, final OslcYaml oslcYaml)
'''
pass
def generateQueryParamsInfo():
'''public static List<JSONObject> generateQueryParamsInfo(final List<QueryParamsInfo> queryParamsMeta)
'''
pass
def addYamlMethodParams():
'''public static void addYamlMethodParams(final String in, final String name, final String type, final String required, final String description, final String pathName, final String methodName, final OslcYaml oslcYaml)
public static void addYamlMethodParams(final String ref, final String pathName, final String methodName, final OslcYaml oslcYaml)
'''
pass
def addYamlMethodParamsSystem():
'''public static void addYamlMethodParamsSystem(final String ref, final String pathName, final String methodName, final OslcYaml oslcYaml)
'''
pass
def addYamlParamsDetail():
'''public static JSONObject addYamlParamsDetail(final String in, final String name, final String type, final Boolean required, final String description, final String paramName, final String defaultValue, final JSONObject schema, final JSONArray enumValue, final OslcYaml oslcYaml, final JSONObject paramsObject)
'''
pass
def yamlParamsDetailBuilder():
'''public static JSONObject yamlParamsDetailBuilder(final String in, final String name, final String type, final Boolean required, final String description, final String paramName, final String defaultValue, JSONObject schema, final JSONArray enumValue)
'''
pass
def yamlRespDetailBuilder():
'''public static JSONObject yamlRespDetailBuilder(final String description, final JSONObject schema, final JSONObject headers, final JSONObject examples)
'''
pass
def addYamlParamsRequired():
'''public static void addYamlParamsRequired(final List<String> list, final JSONObject paramsObject)
'''
pass
def addYamlDefDetailsProperties():
'''public static void addYamlDefDetailsProperties(final String defName, final String propertyName, final String type, final String format, final String description, final String defaultValue, final JSONArray enumValue, final String refObj, final OslcYaml oslcYaml)
'''
pass
def statusContent():
'''public static JSONObject statusContent(final String code)
'''
pass
def generateEnum():
'''public static JSONArray generateEnum(final Set<String> set)
'''
pass
def generateEnumFromRelatedResources():
'''public static JSONArray generateEnumFromRelatedResources(final Map<String, OslcResourceDetailInfo> oslcRelatedResources)
'''
pass
def capitalizeFirstLetter():
'''public static String capitalizeFirstLetter(final String string)
'''
pass
def assignActions():
'''public static void assignActions(final List<OslcActionInfo> actionList, final JSONArray actionNameList)
'''
pass
def buildActionMeta():
'''public static void buildActionMeta(final OslcActionInfo oslcActionInfo, final OslcYaml oslcYaml, final String path, final String method)
'''
pass
def buildPOSTWsMethodActionMeta():
'''public static void buildPOSTWsMethodActionMeta(final MethodInfo methodInfo, final OslcYaml oslcYaml, final String path)
'''
pass
def buildGETWsMethodRequestActionMeta():
'''public static void buildGETWsMethodRequestActionMeta(final MethodInfo methodInfo, final OslcYaml oslcYaml, final String path)
'''
pass
