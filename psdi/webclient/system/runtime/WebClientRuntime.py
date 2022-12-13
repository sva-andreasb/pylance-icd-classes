ROWMARKID = "String  [R:{0}]""
MSG_BTNOK = "int  2"
MSG_BTNCANCEL = "int  4"
MSG_BTNYES = "int  8"
MSG_BTNNO = "int  16"
SPECIALSAVECHARS = "String  =: #!""
MXE_WEBCLIENT_MAXASYNCREQUESTSBEFORERENDER = "String  mxe.webclient.maxasyncrequestsbeforerender""
MXE_WEBCLIENT_ASYNCRENDERTIMELIMIT = "String  mxe.webclient.asyncrendertimelimit""
STARTCENTER_CACHE_NAME = "String  StartCenterListCache""
PORTLETLAYOUT_CACHE_NAME = "String  PortletlLayoutCache""
PORTLETLAYOUT_CACHE_UID = "String  PortletlLayoutCacheUID""
PORTLET_CACHE_PREFIX = "String  PORTLETCHACHE_""
PORTLETS_ALLOWED_CACHE = "String  PORTLETSALLOWED""
STARTCENTER_UID_CACHE_NAME = "String  CURRENTSTARTCENTERUID""
MXE_WEBCLIENT_DEEPREQUIREDCHECK = "String  mxe.webclient.deepRequiredCheck""
def getWebClientRuntime():
'''public static WebClientRuntime getWebClientRuntime()
'''
pass
def loadDOM():
'''public static synchronized Document loadDOM(final InputStream inputStream)
public static synchronized Document loadDOM(final String input)
'''
pass
def getWebClientSession():
'''public WebClientSession getWebClientSession(final HttpServletRequest request)
'''
pass
def addWebClientSession():
'''public void addWebClientSession(final HttpSession httpSession, final WebClientSession wcs)
'''
pass
def removeWebClientSession():
'''public WebClientSession removeWebClientSession(final HttpSession httpSession)
'''
pass
def getAppDescriptor():
'''public AppDescriptor getAppDescriptor(final String appName, final WebClientSession wcs)
public synchronized AppDescriptor getAppDescriptor(final String appName)
'''
pass
def getPresentationCache():
'''public PresentationCache getPresentationCache()
'''
pass
def getAppName():
'''public static String getAppName(final Element element)
'''
pass
def getLibraryDescriptor():
'''public LibraryDescriptor getLibraryDescriptor(String libraryName, final WebClientSession wcs)
'''
pass
def getToolBoxDescriptor():
'''public synchronized ToolBoxDescriptor getToolBoxDescriptor(final String toolboxName, final WebClientSession wcs)
'''
pass
def getCmsMenuDescriptor():
'''public CmsMenuDescriptor getCmsMenuDescriptor(final String mboName, final String menuItem)
'''
pass
def getCMSRegistry():
'''public ICmsRegistry getCMSRegistry()
'''
pass
def isCmsEnabled():
'''public boolean isCmsEnabled()
'''
pass
def loadHelpTaxonomy():
'''public void loadHelpTaxonomy()
'''
pass
def getDisObject():
'''public DataIntegrationServices getDisObject()
'''
pass
def getCmsMenuDescriptorObject():
'''public JSONObject getCmsMenuDescriptorObject(final DataBean bean, final String menuId)
'''
pass
def getControlDescriptor():
'''public ControlDescriptor getControlDescriptor(final String type)
'''
pass
def getComponentDescriptor():
'''public ComponentDescriptor getComponentDescriptor(final String type)
'''
pass
def getElementProperty():
'''public String getElementProperty(final Element xmlControlElement, final ControlDescriptor cd, final String propName)
'''
pass
def getStreamFromJar():
'''public HashMap<String, InputStream> getStreamFromJar(String productDir)
'''
pass
def getOptionMenu():
'''public String getOptionMenu(final String appName, final String sigOption)
'''
pass
def getFieldSize():
'''public int getFieldSize(final boolean onTable, final String maxtype, final int datalength)
public int getFieldSize(final boolean onTable, final int maxtype, final int datalength)
'''
pass
def getMaxTypeAsInt():
'''public static int getMaxTypeAsInt(final String type)
'''
pass
def getFieldPadding():
'''public int getFieldPadding()
'''
pass
def getFieldSizeFactor():
'''public double getFieldSizeFactor()
'''
pass
def getFieldSizeMaximum():
'''public int getFieldSizeMaximum()
'''
pass
def getTablecolSizeFactor():
'''public double getTablecolSizeFactor()
'''
pass
def getTablecolSizeDefault():
'''public int getTablecolSizeDefault()
'''
pass
def getDateFieldSize():
'''public int getDateFieldSize()
'''
pass
def getDateTimeFieldSize():
'''public int getDateTimeFieldSize()
'''
pass
def getTimeFieldSize():
'''public int getTimeFieldSize()
'''
pass
def getWebClientProperty():
'''public static String getWebClientProperty(final String prop)
public static String getWebClientProperty(final String prop, final String defaultValue)
'''
pass
def getHelpString():
'''public static String[] getHelpString(final String propvalue)
'''
pass
def getHelpUrl():
'''public String getHelpUrl(final String packagename, final String filename, final String langcode)
'''
pass
def getWebClientSystemProperty():
'''public static String getWebClientSystemProperty(final String prop)
public static String getWebClientSystemProperty(final String prop, final String defaultValue)
'''
pass
def isNull():
'''public static boolean isNull(final String val)
'''
pass
def isNullCheck():
'''public static boolean isNullCheck(final String val)
'''
pass
def removeControl():
'''public void removeControl(final ControlInstance control)
'''
pass
def reset():
'''public synchronized void reset()
'''
pass
def checkSession():
'''public static WebClientEvent checkSession(final WebClientSession wcs, WebClientEvent event)
'''
pass
def getMaximoRequestURL():
'''public static String getMaximoRequestURL(final HttpServletRequest request)
'''
pass
def getMaximoBaseURL():
'''public static String getMaximoBaseURL(final HttpServletRequest request)
'''
pass
def getMaximoRequestContextURL():
'''public static String getMaximoRequestContextURL(final HttpServletRequest request)
'''
pass
def getMXSession():
'''public static MXSession getMXSession(final HttpSession session)
'''
pass
def sendEvent():
'''public static int sendEvent(final WebClientSession wcs, final String targetId, final String event, final Object value)
public static int sendEvent(final WebClientEvent event)
'''
pass
def removePrepend():
'''public static String removePrepend(final String value)
'''
pass
def makesafevalue():
'''public static String makesafevalue(final String value)
'''
pass
def makesafeWithAmpersand():
'''public static String makesafeWithAmpersand(final String value)
'''
pass
def decodeSafevalue():
'''public static String decodeSafevalue(final String value)
'''
pass
def removeQuotes():
'''public static String removeQuotes(String value)
'''
pass
def replaceLogicalsWithSymbols():
'''public static String replaceLogicalsWithSymbols(final String value)
'''
pass
def makesafejavascriptstringparameter():
'''public static String makesafejavascriptstringparameter(final String value)
'''
pass
def formatDataString():
'''public static String formatDataString(final String dataString)
'''
pass
def hasInvalidXMLChars():
'''public static boolean hasInvalidXMLChars(final String value)
'''
pass
def removeInvalidXMLChars():
'''public static String removeInvalidXMLChars(final String value)
'''
pass
def getHost():
'''public static String getHost()
'''
pass
def wrapText():
'''public static String wrapText(final String text, final int lineLength)
public static String wrapText(final String text, String wrapString, final int lineLength)
public static String wrapText(final String text, final int lineLength, final boolean canBreakWords, final boolean hyphenateBreaks)
'''
pass
def getHostAddress():
'''public static String getHostAddress()
'''
pass
def isParam():
'''public static boolean isParam(final HttpServletRequest request, final String val)
'''
pass
def replaceString():
'''public static String replaceString(String str, final String pattern, final String replacement)
'''
pass
def updateString():
'''public static String updateString(final DataBean attrSource, final String str, final String attributes)
'''
pass
def escapeForJScript():
'''public static String escapeForJScript(final String str)
'''
pass
def isNumeric():
'''public static boolean isNumeric(final MboValueData mvData)
'''
pass
def replaceParams():
'''public static String replaceParams(String message, final String[] params)
'''
pass
def getPrependValue():
'''public static String getPrependValue(final String prependString)
'''
pass
def formatStringForTags():
'''public static String formatStringForTags(final String str)
'''
pass
def unFormatString():
'''public static String unFormatString(final String str)
'''
pass
def createStatusText():
'''public static String createStatusText(final MXException[] warnings, final WebClientSession wcs)
'''
pass
def findAttribute():
'''public static String findAttribute(final String name, final Element element)
'''
pass
def findElement():
'''public static Element findElement(final Element element, final String id)
public static Element findElement(final Element element, final String id, final boolean isCaseSensitive)
'''
pass
def findChildElement():
'''public static Element findChildElement(final Element element, final String id, final boolean isCaseSensitive)
'''
pass
def findElementByTagName():
'''public static Element findElementByTagName(final Element element, final String tagName)
'''
pass
def findChildElementByTagName():
'''public static Element findChildElementByTagName(final Element element, final String tagName)
'''
pass
def stringToCodepoints():
'''public static String stringToCodepoints(final String theString, final boolean escapeSpace, final boolean escapeUnicode)
'''
pass
def toHex():
'''public static char toHex(final int nibble)
'''
pass
def csvStringFromArray():
'''public static String csvStringFromArray(final Object[] values)
'''
pass
def removeAppDescriptor():
'''public AppDescriptor removeAppDescriptor(String appName)
'''
pass
def removeLibraryDescriptor():
'''public LibraryDescriptor removeLibraryDescriptor(String name)
'''
pass
def doubleUpQuotes():
'''public static String doubleUpQuotes(final String inputData)
'''
pass
def getSupportedContainer():
'''public HashMap<String, String> getSupportedContainer(final String ctrlType)
'''
pass
def getPropFromElement():
'''public String getPropFromElement(final Element xmlControlElement, final String propName)
'''
pass
def setRuntimeAppdescripterIndex():
'''public void setRuntimeAppdescripterIndex(final String newApp, final AppDescriptor runTimeAd)
'''
pass
def formatStringUniqueId():
'''public static long formatStringUniqueId(final String tempStr, final Locale userlocale)
'''
pass
def breakupMsgLookup():
'''public static String[] breakupMsgLookup(final String lookup)
'''
pass
def getAppXML():
'''public String getAppXML(final String appName)
'''
pass
def setAppXML():
'''public void setAppXML(final String appName, @TraceMaskValue final String appXML)
'''
pass
def removeAppXML():
'''public String removeAppXML(String appName)
'''
pass
def hasLicenseAccess():
'''public boolean hasLicenseAccess(final String licensevalue)
'''
pass
def getSkin():
'''public String getSkin()
'''
pass
def setSkin():
'''public void setSkin(final String skin)
'''
pass
def parseParamForRow():
'''public static String[] parseParamForRow(final WebClientSession wcs, final String param)
public static String[] parseParamForRow(final String param)
'''
pass
def addRowMarker():
'''public static String addRowMarker(final String id, final int row)
'''
pass
def removeSharedAttributeRowMarker():
'''public static String removeSharedAttributeRowMarker(final String id)
'''
pass
def removeRowMarker():
'''public static String removeRowMarker(String id)
'''
pass
def getRowFromId():
'''public static int getRowFromId(final String id)
'''
pass
def containsRowMarker():
'''public static boolean containsRowMarker(final String value)
'''
pass
def lineBreakString():
'''public static String lineBreakString(final String toProcess, final int chunckSize)
'''
pass
def isAllLatin():
'''public static boolean isAllLatin(final String titleString)
'''
pass
def shortenString():
'''public static String shortenString(final String orig, final int checklength)
'''
pass
def addToTranslatableLabels():
'''public static void addToTranslatableLabels(final String type, final String key)
'''
pass
def getTranslatableLabels():
'''public static String getTranslatableLabels(final String type, final String key)
'''
pass
def getExcludeApps():
'''public Properties getExcludeApps(final String appName)
'''
pass
def cacheExcludeApps():
'''public void cacheExcludeApps()
'''
pass
def getPropsFromJar():
'''public HashMap<String, InputStream> getPropsFromJar(String productDir)
'''
pass
def getLocaleFromRequest():
'''public static Object[] getLocaleFromRequest(final HttpServletRequest request)
'''
pass
def send503Error():
'''public static boolean send503Error(final HttpServletResponse response, final MXSession s, final boolean maxUserSessions)
public static boolean send503Error(final HttpServletResponse response, final MXSession s, final String url)
'''
pass
def getDojoDirectory():
'''public static String getDojoDirectory(final HttpServletRequest request)
'''
pass
def getEntityRelationshipModel():
'''public synchronized EntityRelationshipModel getEntityRelationshipModel(final String app)
'''
pass
def createSendEventString():
'''public static String createSendEventString(final String event, final String target, final String val, final int jsMethod)
'''
pass
def canUseStaticIds():
'''public boolean canUseStaticIds()
'''
pass
def addFieldClassInfo():
'''public synchronized FieldClassInfo addFieldClassInfo(final FieldClassInfo fci)
'''
pass
def getFieldClassInfo():
'''public synchronized FieldClassInfo getFieldClassInfo(final String name)
'''
pass
def getAppDescFromCache():
'''public static String getAppDescFromCache(final String appId, final MXSession mxs)
public static String getAppDescFromCache(String appId, final MXSession mxs, String langCode)
'''
pass
def resetAppDescCache():
'''public static void resetAppDescCache()
'''
pass
def isMTEnabled():
'''public static boolean isMTEnabled()
'''
pass
def getMTtenantId():
'''public static int getMTtenantId()
'''
pass
def getCacheIdForAppName():
'''public static String getCacheIdForAppName(String Id)
'''
pass
def canBeUsedInRecordHover():
'''public boolean canBeUsedInRecordHover(final String controlType)
'''
pass
def getAppSigOptionList():
'''public static Map<String, SigOptionInfo> getAppSigOptionList(final String appId)
'''
pass
def padString():
'''public static String padString(String value, final String pad, final int length)
'''
pass
def isRunningInWebLogic():
'''public static boolean isRunningInWebLogic()
'''
pass
