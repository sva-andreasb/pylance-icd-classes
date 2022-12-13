SYSTEM_LEVEL = "int 0"
ORG_LEVEL = "int 1"
SITE_LEVEL = "int 2"
MBO_INDEX = "String restmboindex""
HREF = "String href""
LOCALREF = "String localref""
ID = "String _id""
APIMBOCORRELATIONID = "String apimbocorrelationid""
APIOBJPATH = "String apiobjpath""
BULKID = "String _bulkid""
KEY_SEP_ENCODETOKEN = "String \"sp\"""
KEY_SEP_CHAR = "char '/'"
CSRFTOKEN = "String csrftoken""
MXTOKEN = "String __mxtoken""
MXUSER = "String __mxuser""
MT_TENANTCODE_HEADER = "String tenantcode""
MT_TENANTCODE_QP = "String _tenantcode""
API_INIT_REQUEST = "String apiinitrequest""
API_FLAG = "String API""
APP_SERVER_SECURITY = "String appserversecurity""
LOOKUP_SRC_ATTR = "String lookupsrcattr""
API_KEY = "String apikey""
ADD_LOCALIZED_REP = "String addlocalizedrep""
ADD_SCHEMA = "String addschema""
QUERY_LOCALIZED = "String querylocalized""
AS_USER = "String asuser""
ADD_DOMAIN_DESC = "String adddomdesc""
SELF_REF_DUP = "String selfrefrel""
SELF_REF_REL = "String selfrefrel""
SELF_REF = "String selfref""
LOCALIZED_DATE = "String localizeddate""
SET_VALUE_MODE = "String setvaluemode""
ENABLE_SESSION = "String enablesession""
SET_VALUE_MBO = "String setvaluerootmbo""
GUESTUSER = "String MGUEST""
GUESTID = "String guestid""
IGNORECOLLECTIONREF = "String ignorecollectionref""
IGNOREKEYREF = "String ignorekeyref""
IGNOREROWSTAMP = "String ignorers""
SEVENDAYCACHE = "int 604800"
TWODAYCACHE = "int 172800"
WHOAMIAPI = "String whoamiapi""
ADD_REL_TO_SCHEMA = "String addreltoschema""
SELFREF = "String selfref""
APPS = "String apps""
OSLCCTX = "String oslcctx""
MBOSETLIMITCOUNT = "String mbosetlimitcount""
BRANCH_FILTER = "String branchfilter""
API_ERRORS = "String apierrors""
ADD_ACTION = "String act""
CLIENT_CERT = "String client_cert""
def generateCSRFToken():
'''public static String generateCSRFToken()
'''
pass
def generateApiKeyToken():
'''public static String generateApiKeyToken()
'''
pass
def getLocalizedDateTime():
'''public static String getLocalizedDateTime(final int maxType, final Date rawData, final Locale l)
'''
pass
def getKPIWhere():
'''public static String getKPIWhere(final String kpiName, final UserInfo userInfo)
'''
pass
def setKPIWhere():
'''public static void setKPIWhere(final String kpiName, final MboSetRemote msr)
'''
pass
def getMboForPath():
'''public static MboRemote getMboForPath(final MboRemote mbo, final String relPath)
'''
pass
def getMboForAttribute():
'''public static MboRemote getMboForAttribute(final MboRemote mbo, final String attrName)
'''
pass
def setNotIn():
'''public static void setNotIn(final MboSetRemote mboSet, final String inClause, final String attributeName)
public static void setNotIn(final MboSetRemote mboSet, String inClause, final String attributeName, final JSONArray ja)
'''
pass
def getNotificationHistMessage():
'''public static JSONObject getNotificationHistMessage(final MboRemote notfMbo)
'''
pass
def setDomainImplicits():
'''public static void setDomainImplicits(final JSONObject mboOjo, final String mboAttrName, final String alias, final MboRemote mbo, final OslcRequest request)
'''
pass
def getDomainImplicitSchema():
'''public static DomainInfo getDomainImplicitSchema(final MboValueInfo mvi, final String mboAttrName, final String alias)
'''
pass
def generateCSV():
'''public static byte[] generateCSV(final String osName, final MboSetRemote msr, final String[] cols, final boolean useAttrTitle, final boolean addAttrNameToTitle)
'''
pass
def allowedOptions():
'''public static void allowedOptions(final MboRemote mbo, final JSONObject jo)
'''
pass
def logTransaction():
'''public static void logTransaction(final OslcRequest request, final Long mboId, final MXTransaction mxTran)
'''
pass
def setDomainInternalWhere():
'''public static void setDomainInternalWhere(final MboSetRemote mboset, final OslcRequest request)
public static void setDomainInternalWhere(final MboSetRemote mboset, final String domIntWhere)
'''
pass
def setDomainListWhere():
'''public static void setDomainListWhere(final MboSetRemote mboset, final OslcRequest request)
public static void setDomainListWhere(final MboSetRemote mboset, final String fd, final String orgid, final String siteid)
'''
pass
def getDomainInfo():
'''public static DomainInfo getDomainInfo(final String objectName, final String domainName, final String siteid, final String orgid)
'''
pass
def handleTimeLineQuery():
'''public static void handleTimeLineQuery(final MboSetRemote msr, final OslcRequest oslcRequest, final String osTlAttr)
public static void handleTimeLineQuery(final MboSetRemote msr, final String tlAttr, final String tlRange)
public static void handleTimeLineQuery(final MboSetRemote msr, final String tlAttr, final String tlRange, boolean tlmodeDate)
'''
pass
def keyStringToMbo():
'''public static MboRemote keyStringToMbo(final String keyString, final MboSetRemote mboSet)
'''
pass
def startAndEnd():
'''public static Date[] startAndEnd(final Date base, String tlRange)
'''
pass
def getDate():
'''public static Date getDate(final Date base, final int val, final String unit)
'''
pass
def handleSubQbeAndSort():
'''public static Integer handleSubQbeAndSort(final MboSetRemote childMboSet, final MboRemote pmbo, String relation, final OslcRequest oslcRequest)
'''
pass
def getPropertiesFromRequest():
'''public static Map<String, OslcResourceProperty> getPropertiesFromRequest(final OslcRequest oslcRequest, final String osName)
public static Map<String, OslcResourceProperty> getPropertiesFromRequest(final OslcRequest oslcRequest, final String osName, final boolean queryResource, final boolean ordered)
'''
pass
def generateUniqueID():
'''public static String generateUniqueID()
'''
pass
def getOrgSiteLevel():
'''public static int getOrgSiteLevel(final String objectName)
'''
pass
def getLifeSpanForTimedCache():
'''public static int getLifeSpanForTimedCache()
'''
pass
def checkAuth():
'''public static void checkAuth(final String app, final String optionName, final OslcRequest request, final MboRemote mbo)
'''
pass
def resolveURIToWhere():
'''public static String resolveURIToWhere(final String uri, final UserInfo userInfo, final OslcRequest oslcRequest)
'''
pass
def parseSelect():
'''public static Map<String, OslcResourceProperty> parseSelect(final String selectExp)
'''
pass
def getIdentifierAsQName():
'''public static QName getIdentifierAsQName(String identifier, final Map<String, String> reqPrefixNsMap, final Map<String, String> prefixNsMap)
'''
pass
def generateOrderedPropertyMap():
'''public static void generateOrderedPropertyMap(final boolean leanJson, final Map<String, OslcResourceProperty> propertySet, final IOslcProperty oslcProperty, final Map<String, String> reqPrefixNsMap, final Map<String, String> configPrefixNsMap)
'''
pass
def generateIndexedPropertyMap():
'''public static void generateIndexedPropertyMap(final boolean leanJson, final Map<String, OslcResourceProperty> propertySet, final IOslcProperty oslcProperty, final Map<String, String> reqPrefixNsMap, final Map<String, String> configPrefixNsMap)
'''
pass
def jsonToBytes():
'''public static byte[] jsonToBytes(final JSONObject ojo)
public static byte[] jsonToBytes(final JSONObject ojo, final boolean pretty)
'''
pass
def jsonarrayToBytes():
'''public static byte[] jsonarrayToBytes(final JSONArray ja)
public static byte[] jsonarrayToBytes(final JSONArray ja, final boolean pretty)
'''
pass
def bytesToJSONObject():
'''public static JSONObject bytesToJSONObject(final byte[] data)
'''
pass
def bytesToOrderedJSONObject():
'''public static OrderedJSONObject bytesToOrderedJSONObject(final byte[] data)
'''
pass
def bytesToJSONArray():
'''public static JSONArray bytesToJSONArray(final byte[] data)
'''
pass
def bytesToJSON():
'''public static JSONArtifact bytesToJSON(final byte[] data)
'''
pass
def bytesToOrderedJSON():
'''public static JSONArtifact bytesToOrderedJSON(final byte[] data)
'''
pass
def getOslcWebAppURL():
'''public static String getOslcWebAppURL()
'''
pass
def transformURIWithPublicURI():
'''public static String transformURIWithPublicURI(final String uri)
'''
pass
def getResourceTypeAsQName():
'''public static QName getResourceTypeAsQName(final String resourceTypeURI)
'''
pass
def getKeyValueMap():
'''public static Map<String, Object> getKeyValueMap(final Map<String, String> keyMap, final MboRemote mbo)
'''
pass
def getLocaleInsensitiveValue():
'''public static String getLocaleInsensitiveValue(final MboValueInfo mboValueInfo, final MboRemote mbo)
'''
pass
def getAttributeValue():
'''public static Object getAttributeValue(final MboValueInfo mboValueInfo, final MboRemote mbo)
'''
pass
def getOslcBaseURI():
'''public static String getOslcBaseURI()
'''
pass
def generateURITokenFromKeyValueMap():
'''public static String generateURITokenFromKeyValueMap(final Map<String, Object> map)
'''
pass
def modelToBytes():
'''public static byte[] modelToBytes(final Model rdfModel)
'''
pass
def bytesToModel():
'''public static Model bytesToModel(final byte[] resourceBytes)
'''
pass
def generateIdFromMboId():
'''public static String generateIdFromMboId(final MboRemote mbo)
'''
pass
def recoverResourceId():
'''public static String recoverResourceId(String encodedId)
'''
pass
def tokenizeResourceId():
'''public static List<String> tokenizeResourceId(final String recoveredId)
'''
pass
def encodeResourceId():
'''public static String encodeResourceId(final String clearTextId)
'''
pass
def recoverResource():
'''public static Mbo recoverResource(final String encodedId, final MboSet mboSet)
public static Mbo recoverResource(final Map<String, String> map, final MboSet mboSet)
'''
pass
def getLinkURIFor():
'''public static String getLinkURIFor(final String oslcBaseURI, final String osName, final String id)
'''
pass
def resolveURIExpression():
'''public static String resolveURIExpression(final String uriExp, final MboRemote mbo)
'''
pass
def getMboMboValueInfoForAttribute():
'''public static MboValueInfo getMboMboValueInfoForAttribute(final MboSetRemote mboSet, String attributeName, final boolean showHidden)
public static MboValueInfo getMboMboValueInfoForAttribute(final MboSetRemote mboSet, String attributeName)
'''
pass
def getMboMboValueForAttribute():
'''public static MboValue getMboMboValueForAttribute(final MboRemote mbo, String attributeName)
'''
pass
def getQueryPropertyList():
'''public static Map<String, PropertyInfo> getQueryPropertyList(final String resourceType, final UserInfo userInfo)
'''
pass
def getIdentificationRules():
'''public static List<List<RulePropertyInfo>> getIdentificationRules(final String resourceType, final UserInfo userInfo)
'''
pass
def getStoredShape():
'''public static Resource getStoredShape(final String resourceType, final UserInfo userInfo)
'''
pass
def getRegistryEndpoint():
'''public static String getRegistryEndpoint()
'''
pass
def getRegistryQueryBaseURI():
'''public static String getRegistryQueryBaseURI(final String registryURI, final byte[] resourceBytes)
'''
pass
def dateTimeToString():
'''public static String dateTimeToString(final Date d, final Locale l, final TimeZone tz)
'''
pass
def timeToString():
'''public static String timeToString(final Date d, final Locale l)
'''
pass
def getLogger():
'''public static MXLogger getLogger()
'''
pass
def fileVirusScanner():
'''public static void fileVirusScanner(final String fileName, final InputStream in)
'''
pass
def encode():
'''public static String encode(String token, final boolean pathToken)
'''
pass
def generateESID():
'''public static String generateESID(final String osName)
'''
pass
def generateRandomID():
'''public static String generateRandomID()
'''
pass
def validateAttachmentExt():
'''public static void validateAttachmentExt(final String fileName)
'''
pass
def generateObjQueryFromQbeJSON():
'''public static String generateObjQueryFromQbeJSON(final String objectName, final JSONObject jo, final UserInfo userInfo)
'''
pass
def generateOslcQueryFromQbeJSON():
'''public static String generateOslcQueryFromQbeJSON(final String osName, final JSONObject jo, final UserInfo userInfo)
'''
pass
def toLocalizedFormat():
'''public static String toLocalizedFormat(final String isoValue, final MboValueInfo mboValueInfo, final UserInfo userInfo, final boolean inClause)
'''
pass
def toISOFormat():
'''public static String toISOFormat(final String localeValue, final MboValueInfo mboValueInfo, final UserInfo userInfo, final boolean inClause)
'''
pass
def generateLocalizedQueryJSON():
'''public static void generateLocalizedQueryJSON(final String osName, final JSONObject jo, final UserInfo userInfo)
'''
pass
def generateISOQueryJSON():
'''public static void generateISOQueryJSON(final String osName, final JSONObject jo, final UserInfo userInfo)
'''
pass
def addQueryParamToURI():
'''public static String addQueryParamToURI(final String uri, final String paramName, final String paramValue)
'''
pass
def setRestrictWhere():
'''public static void setRestrictWhere(final MboSetRemote mboset, final MosInfo mosInfo)
'''
pass
def createURIFromBase():
'''public static String createURIFromBase(final List<String> path)
'''
pass
def getLocalResourceId():
'''public static String getLocalResourceId(final MboRemote mbo, final MosDetailInfo mosDetailInfo)
'''
pass
def setTimeLineFunctionFilter():
'''public static void setTimeLineFunctionFilter(final MboSetRemote mboset, final OslcRequest oslcRequest)
'''
pass
def convertQueryWhereToOslcWhere():
'''public static List<IOslcTerm> convertQueryWhereToOslcWhere(final String queryWhere, final UserInfo userInfo, final String osName, final MboSetRemote mboSet)
'''
pass
def convertQueryWhereToObjWhere():
'''public static List<IOslcTerm> convertQueryWhereToObjWhere(final String queryWhere, final UserInfo userInfo, final String objectName, final MboSetRemote mboSet)
'''
pass
def getModeOrFromQueryWhere():
'''public static Boolean getModeOrFromQueryWhere(final String queryWhere)
'''
pass
def searchTokens():
'''public static String[] searchTokens(final String searchString)
'''
pass
def persistCSRFToken():
'''public static void persistCSRFToken(final UserInfo userInfo, final String csrfToken)
'''
pass
def validateCSRFToken():
'''public static boolean validateCSRFToken(final UserInfo userInfo, final String csrfToken)
'''
pass
def createStatusText():
'''public static String createStatusText(final MXException[] warnings, final OslcRequest request)
'''
pass
def getMessage():
'''public static String getMessage(final MXException mxe, final OslcRequest request)
'''
pass
def generateJSONSchema():
'''public static JSONObject generateJSONSchema(final String osName, final String selectClause, final boolean addEnums, final String queryTemplate, final UserInfo userInfo)
public static JSONObject generateJSONSchema(final String osName, final String selectClause, final boolean addEnums, final String queryTemplate, final UserInfo userInfo, final boolean strict)
'''
pass
def serializeResourceAsObject():
'''public static byte[] serializeResourceAsObject(final Object obj, final String osName, final String templateName, final boolean retainMbos)
public static byte[] serializeResourceAsObject(final Object obj, final String osName, final String templateName)
'''
pass
def addSqlClauseToJSON():
'''public static void addSqlClauseToJSON(final OslcRequest request, final OslcResourceInfo resourceInfo, final String clause, final String clauseName, final JSONObject jo)
'''
pass
def getYNCOptionValue():
'''public static Integer getYNCOptionValue(final String optionChosen)
'''
pass
def getContentTypeFrom():
'''public static String getContentTypeFrom(final String fileName)
'''
pass
def setCORSHeaders():
'''public static void setCORSHeaders(final HttpServletRequest request, final HttpServletResponse response)
'''
pass
def addRelationJSONSchema():
'''public static void addRelationJSONSchema(final JSONArray ja, final String objectName)
'''
pass
def getCOSAttachmentBucketName():
'''public static String getCOSAttachmentBucketName()
'''
pass
def getDomainId():
'''public static String getDomainId(final MboRemote mbo, final String attrName)
'''
pass
def getAttachmentStore():
'''public static String getAttachmentStore()
'''
pass
def getCustomStorage():
'''public static AttachmentStorage getCustomStorage()
'''
pass
def getApiModules():
'''public static Map<String, String> getApiModules()
'''
pass
def xorEncode():
'''public static String xorEncode(final String s, final String key)
'''
pass
def xorDecode():
'''public static String xorDecode(final String s, final String key)
'''
pass
