SYSTEM_LEVEL = "int  0"
ORG_LEVEL = "int  1"
SITE_LEVEL = "int  2"
MBO_INDEX = "String  \"restmboindex\""
HREF = "String  \"href\""
LOCALREF = "String  \"localref\""
ID = "String  \"_id\""
APIMBOCORRELATIONID = "String  \"apimbocorrelationid\""
APIOBJPATH = "String  \"apiobjpath\""
BULKID = "String  \"_bulkid\""
KEY_SEP_ENCODETOKEN = "String  \"\\"sp\\"\""
KEY_SEP_CHAR = "char  '/'"
CSRFTOKEN = "String  \"csrftoken\""
MXTOKEN = "String  \"__mxtoken\""
MXUSER = "String  \"__mxuser\""
MT_TENANTCODE_HEADER = "String  \"tenantcode\""
MT_TENANTCODE_QP = "String  \"_tenantcode\""
API_INIT_REQUEST = "String  \"apiinitrequest\""
API_FLAG = "String  \"API\""
APP_SERVER_SECURITY = "String  \"appserversecurity\""
LOOKUP_SRC_ATTR = "String  \"lookupsrcattr\""
API_KEY = "String  \"apikey\""
ADD_LOCALIZED_REP = "String  \"addlocalizedrep\""
ADD_SCHEMA = "String  \"addschema\""
QUERY_LOCALIZED = "String  \"querylocalized\""
AS_USER = "String  \"asuser\""
ADD_DOMAIN_DESC = "String  \"adddomdesc\""
SELF_REF_DUP = "String  \"selfrefrel\""
SELF_REF_REL = "String  \"selfrefrel\""
SELF_REF = "String  \"selfref\""
LOCALIZED_DATE = "String  \"localizeddate\""
SET_VALUE_MODE = "String  \"setvaluemode\""
ENABLE_SESSION = "String  \"enablesession\""
SET_VALUE_MBO = "String  \"setvaluerootmbo\""
GUESTUSER = "String  \"MGUEST\""
GUESTID = "String  \"guestid\""
IGNORECOLLECTIONREF = "String  \"ignorecollectionref\""
IGNOREKEYREF = "String  \"ignorekeyref\""
IGNOREROWSTAMP = "String  \"ignorers\""
SEVENDAYCACHE = "int  604800"
TWODAYCACHE = "int  172800"
WHOAMIAPI = "String  \"whoamiapi\""
ADD_REL_TO_SCHEMA = "String  \"addreltoschema\""
SELFREF = "String  \"selfref\""
APPS = "String  \"apps\""
OSLCCTX = "String  \"oslcctx\""
MBOSETLIMITCOUNT = "String  \"mbosetlimitcount\""
BRANCH_FILTER = "String  \"branchfilter\""
API_ERRORS = "String  \"apierrors\""
ADD_ACTION = "String  \"act\""
CLIENT_CERT = "String  \"client_cert\""
def generateCSRFToken():
    '''public static String generateCSRFToken()
    '''
def generateApiKeyToken():
    '''public static String generateApiKeyToken()
    '''
def getLocalizedDateTime():
    '''public static String getLocalizedDateTime(final int maxType, final Date rawData, final Locale l)
    '''
def getKPIWhere():
    '''public static String getKPIWhere(final String kpiName, final UserInfo userInfo)
    '''
def setKPIWhere():
    '''public static void setKPIWhere(final String kpiName, final MboSetRemote msr)
    '''
def getMboForPath():
    '''public static MboRemote getMboForPath(final MboRemote mbo, final String relPath)
    '''
def getMboForAttribute():
    '''public static MboRemote getMboForAttribute(final MboRemote mbo, final String attrName)
    '''
def setNotIn():
    '''public static void setNotIn(final MboSetRemote mboSet, final String inClause, final String attributeName)
    public static void setNotIn(final MboSetRemote mboSet, String inClause, final String attributeName, final JSONArray ja)
    '''
def getNotificationHistMessage():
    '''public static JSONObject getNotificationHistMessage(final MboRemote notfMbo)
    '''
def setDomainImplicits():
    '''public static void setDomainImplicits(final JSONObject mboOjo, final String mboAttrName, final String alias, final MboRemote mbo, final OslcRequest request)
    '''
def getDomainImplicitSchema():
    '''public static DomainInfo getDomainImplicitSchema(final MboValueInfo mvi, final String mboAttrName, final String alias)
    '''
def generateCSV():
    '''public static byte[] generateCSV(final String osName, final MboSetRemote msr, final String[] cols, final boolean useAttrTitle, final boolean addAttrNameToTitle)
    '''
def allowedOptions():
    '''public static void allowedOptions(final MboRemote mbo, final JSONObject jo)
    '''
def logTransaction():
    '''public static void logTransaction(final OslcRequest request, final Long mboId, final MXTransaction mxTran)
    '''
def setDomainInternalWhere():
    '''public static void setDomainInternalWhere(final MboSetRemote mboset, final OslcRequest request)
    public static void setDomainInternalWhere(final MboSetRemote mboset, final String domIntWhere)
    '''
def setDomainListWhere():
    '''public static void setDomainListWhere(final MboSetRemote mboset, final OslcRequest request)
    public static void setDomainListWhere(final MboSetRemote mboset, final String fd, final String orgid, final String siteid)
    '''
def getDomainInfo():
    '''public static DomainInfo getDomainInfo(final String objectName, final String domainName, final String siteid, final String orgid)
    '''
def handleTimeLineQuery():
    '''public static void handleTimeLineQuery(final MboSetRemote msr, final OslcRequest oslcRequest, final String osTlAttr)
    public static void handleTimeLineQuery(final MboSetRemote msr, final String tlAttr, final String tlRange)
    public static void handleTimeLineQuery(final MboSetRemote msr, final String tlAttr, final String tlRange, boolean tlmodeDate)
    '''
def keyStringToMbo():
    '''public static MboRemote keyStringToMbo(final String keyString, final MboSetRemote mboSet)
    '''
def startAndEnd():
    '''public static Date[] startAndEnd(final Date base, String tlRange)
    '''
def getDate():
    '''public static Date getDate(final Date base, final int val, final String unit)
    '''
def handleSubQbeAndSort():
    '''public static Integer handleSubQbeAndSort(final MboSetRemote childMboSet, final MboRemote pmbo, String relation, final OslcRequest oslcRequest)
    '''
def getPropertiesFromRequest():
    '''public static Map<String, OslcResourceProperty> getPropertiesFromRequest(final OslcRequest oslcRequest, final String osName)
    public static Map<String, OslcResourceProperty> getPropertiesFromRequest(final OslcRequest oslcRequest, final String osName, final boolean queryResource, final boolean ordered)
    '''
def generateUniqueID():
    '''public static String generateUniqueID()
    '''
def getOrgSiteLevel():
    '''public static int getOrgSiteLevel(final String objectName)
    '''
def getLifeSpanForTimedCache():
    '''public static int getLifeSpanForTimedCache()
    '''
def checkAuth():
    '''public static void checkAuth(final String app, final String optionName, final OslcRequest request, final MboRemote mbo)
    '''
def resolveURIToWhere():
    '''public static String resolveURIToWhere(final String uri, final UserInfo userInfo, final OslcRequest oslcRequest)
    '''
def parseSelect():
    '''public static Map<String, OslcResourceProperty> parseSelect(final String selectExp)
    '''
def getIdentifierAsQName():
    '''public static QName getIdentifierAsQName(String identifier, final Map<String, String> reqPrefixNsMap, final Map<String, String> prefixNsMap)
    '''
def generateOrderedPropertyMap():
    '''public static void generateOrderedPropertyMap(final boolean leanJson, final Map<String, OslcResourceProperty> propertySet, final IOslcProperty oslcProperty, final Map<String, String> reqPrefixNsMap, final Map<String, String> configPrefixNsMap)
    '''
def generateIndexedPropertyMap():
    '''public static void generateIndexedPropertyMap(final boolean leanJson, final Map<String, OslcResourceProperty> propertySet, final IOslcProperty oslcProperty, final Map<String, String> reqPrefixNsMap, final Map<String, String> configPrefixNsMap)
    '''
def jsonToBytes():
    '''public static byte[] jsonToBytes(final JSONObject ojo)
    public static byte[] jsonToBytes(final JSONObject ojo, final boolean pretty)
    '''
def jsonarrayToBytes():
    '''public static byte[] jsonarrayToBytes(final JSONArray ja)
    public static byte[] jsonarrayToBytes(final JSONArray ja, final boolean pretty)
    '''
def bytesToJSONObject():
    '''public static JSONObject bytesToJSONObject(final byte[] data)
    '''
def bytesToOrderedJSONObject():
    '''public static OrderedJSONObject bytesToOrderedJSONObject(final byte[] data)
    '''
def bytesToJSONArray():
    '''public static JSONArray bytesToJSONArray(final byte[] data)
    '''
def bytesToJSON():
    '''public static JSONArtifact bytesToJSON(final byte[] data)
    '''
def bytesToOrderedJSON():
    '''public static JSONArtifact bytesToOrderedJSON(final byte[] data)
    '''
def getOslcWebAppURL():
    '''public static String getOslcWebAppURL()
    '''
def transformURIWithPublicURI():
    '''public static String transformURIWithPublicURI(final String uri)
    '''
def getResourceTypeAsQName():
    '''public static QName getResourceTypeAsQName(final String resourceTypeURI)
    '''
def getKeyValueMap():
    '''public static Map<String, Object> getKeyValueMap(final Map<String, String> keyMap, final MboRemote mbo)
    '''
def getLocaleInsensitiveValue():
    '''public static String getLocaleInsensitiveValue(final MboValueInfo mboValueInfo, final MboRemote mbo)
    '''
def getAttributeValue():
    '''public static Object getAttributeValue(final MboValueInfo mboValueInfo, final MboRemote mbo)
    '''
def getOslcBaseURI():
    '''public static String getOslcBaseURI()
    '''
def generateURITokenFromKeyValueMap():
    '''public static String generateURITokenFromKeyValueMap(final Map<String, Object> map)
    '''
def modelToBytes():
    '''public static byte[] modelToBytes(final Model rdfModel)
    '''
def bytesToModel():
    '''public static Model bytesToModel(final byte[] resourceBytes)
    '''
def generateIdFromMboId():
    '''public static String generateIdFromMboId(final MboRemote mbo)
    '''
def recoverResourceId():
    '''public static String recoverResourceId(String encodedId)
    '''
def tokenizeResourceId():
    '''public static List<String> tokenizeResourceId(final String recoveredId)
    '''
def encodeResourceId():
    '''public static String encodeResourceId(final String clearTextId)
    '''
def recoverResource():
    '''public static Mbo recoverResource(final String encodedId, final MboSet mboSet)
    public static Mbo recoverResource(final Map<String, String> map, final MboSet mboSet)
    '''
def getLinkURIFor():
    '''public static String getLinkURIFor(final String oslcBaseURI, final String osName, final String id)
    '''
def resolveURIExpression():
    '''public static String resolveURIExpression(final String uriExp, final MboRemote mbo)
    '''
def getMboMboValueInfoForAttribute():
    '''public static MboValueInfo getMboMboValueInfoForAttribute(final MboSetRemote mboSet, String attributeName, final boolean showHidden)
    public static MboValueInfo getMboMboValueInfoForAttribute(final MboSetRemote mboSet, String attributeName)
    '''
def getMboMboValueForAttribute():
    '''public static MboValue getMboMboValueForAttribute(final MboRemote mbo, String attributeName)
    '''
def getQueryPropertyList():
    '''public static Map<String, PropertyInfo> getQueryPropertyList(final String resourceType, final UserInfo userInfo)
    '''
def getIdentificationRules():
    '''public static List<List<RulePropertyInfo>> getIdentificationRules(final String resourceType, final UserInfo userInfo)
    '''
def getStoredShape():
    '''public static Resource getStoredShape(final String resourceType, final UserInfo userInfo)
    '''
def getRegistryEndpoint():
    '''public static String getRegistryEndpoint()
    '''
def getRegistryQueryBaseURI():
    '''public static String getRegistryQueryBaseURI(final String registryURI, final byte[] resourceBytes)
    '''
def dateTimeToString():
    '''public static String dateTimeToString(final Date d, final Locale l, final TimeZone tz)
    '''
def timeToString():
    '''public static String timeToString(final Date d, final Locale l)
    '''
def getLogger():
    '''public static MXLogger getLogger()
    '''
def fileVirusScanner():
    '''public static void fileVirusScanner(final String fileName, final InputStream in)
    '''
def encode():
    '''public static String encode(String token, final boolean pathToken)
    '''
def generateESID():
    '''public static String generateESID(final String osName)
    '''
def generateRandomID():
    '''public static String generateRandomID()
    '''
def validateAttachmentExt():
    '''public static void validateAttachmentExt(final String fileName)
    '''
def generateObjQueryFromQbeJSON():
    '''public static String generateObjQueryFromQbeJSON(final String objectName, final JSONObject jo, final UserInfo userInfo)
    '''
def generateOslcQueryFromQbeJSON():
    '''public static String generateOslcQueryFromQbeJSON(final String osName, final JSONObject jo, final UserInfo userInfo)
    '''
def toLocalizedFormat():
    '''public static String toLocalizedFormat(final String isoValue, final MboValueInfo mboValueInfo, final UserInfo userInfo, final boolean inClause)
    '''
def toISOFormat():
    '''public static String toISOFormat(final String localeValue, final MboValueInfo mboValueInfo, final UserInfo userInfo, final boolean inClause)
    '''
def generateLocalizedQueryJSON():
    '''public static void generateLocalizedQueryJSON(final String osName, final JSONObject jo, final UserInfo userInfo)
    '''
def generateISOQueryJSON():
    '''public static void generateISOQueryJSON(final String osName, final JSONObject jo, final UserInfo userInfo)
    '''
def addQueryParamToURI():
    '''public static String addQueryParamToURI(final String uri, final String paramName, final String paramValue)
    '''
def setRestrictWhere():
    '''public static void setRestrictWhere(final MboSetRemote mboset, final MosInfo mosInfo)
    '''
def createURIFromBase():
    '''public static String createURIFromBase(final List<String> path)
    '''
def getLocalResourceId():
    '''public static String getLocalResourceId(final MboRemote mbo, final MosDetailInfo mosDetailInfo)
    '''
def setTimeLineFunctionFilter():
    '''public static void setTimeLineFunctionFilter(final MboSetRemote mboset, final OslcRequest oslcRequest)
    '''
def convertQueryWhereToOslcWhere():
    '''public static List<IOslcTerm> convertQueryWhereToOslcWhere(final String queryWhere, final UserInfo userInfo, final String osName, final MboSetRemote mboSet)
    '''
def convertQueryWhereToObjWhere():
    '''public static List<IOslcTerm> convertQueryWhereToObjWhere(final String queryWhere, final UserInfo userInfo, final String objectName, final MboSetRemote mboSet)
    '''
def getModeOrFromQueryWhere():
    '''public static Boolean getModeOrFromQueryWhere(final String queryWhere)
    '''
def searchTokens():
    '''public static String[] searchTokens(final String searchString)
    '''
def persistCSRFToken():
    '''public static void persistCSRFToken(final UserInfo userInfo, final String csrfToken)
    '''
def validateCSRFToken():
    '''public static boolean validateCSRFToken(final UserInfo userInfo, final String csrfToken)
    '''
def createStatusText():
    '''public static String createStatusText(final MXException[] warnings, final OslcRequest request)
    '''
def getMessage():
    '''public static String getMessage(final MXException mxe, final OslcRequest request)
    '''
def generateJSONSchema():
    '''public static JSONObject generateJSONSchema(final String osName, final String selectClause, final boolean addEnums, final String queryTemplate, final UserInfo userInfo)
    public static JSONObject generateJSONSchema(final String osName, final String selectClause, final boolean addEnums, final String queryTemplate, final UserInfo userInfo, final boolean strict)
    '''
def serializeResourceAsObject():
    '''public static byte[] serializeResourceAsObject(final Object obj, final String osName, final String templateName, final boolean retainMbos)
    public static byte[] serializeResourceAsObject(final Object obj, final String osName, final String templateName)
    '''
def addSqlClauseToJSON():
    '''public static void addSqlClauseToJSON(final OslcRequest request, final OslcResourceInfo resourceInfo, final String clause, final String clauseName, final JSONObject jo)
    '''
def getYNCOptionValue():
    '''public static Integer getYNCOptionValue(final String optionChosen)
    '''
def getContentTypeFrom():
    '''public static String getContentTypeFrom(final String fileName)
    '''
def setCORSHeaders():
    '''public static void setCORSHeaders(final HttpServletRequest request, final HttpServletResponse response)
    '''
def addRelationJSONSchema():
    '''public static void addRelationJSONSchema(final JSONArray ja, final String objectName)
    '''
def getCOSAttachmentBucketName():
    '''public static String getCOSAttachmentBucketName()
    '''
def getDomainId():
    '''public static String getDomainId(final MboRemote mbo, final String attrName)
    '''
def getAttachmentStore():
    '''public static String getAttachmentStore()
    '''
def getCustomStorage():
    '''public static AttachmentStorage getCustomStorage()
    '''
def getApiModules():
    '''public static Map<String, String> getApiModules()
    '''
def xorEncode():
    '''public static String xorEncode(final String s, final String key)
    '''
def xorDecode():
    '''public static String xorDecode(final String s, final String key)
    '''
