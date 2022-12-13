ROWMARKID = "String  \"[R:{0}]\""
MSG_BTNOK = "int  2"
MSG_BTNCANCEL = "int  4"
MSG_BTNYES = "int  8"
MSG_BTNNO = "int  16"
SPECIALSAVECHARS = "String  \"=: #!\""
MXE_WEBCLIENT_MAXASYNCREQUESTSBEFORERENDER = "String  \"mxe.webclient.maxasyncrequestsbeforerender\""
MXE_WEBCLIENT_ASYNCRENDERTIMELIMIT = "String  \"mxe.webclient.asyncrendertimelimit\""
STARTCENTER_CACHE_NAME = "String  \"StartCenterListCache\""
PORTLETLAYOUT_CACHE_NAME = "String  \"PortletlLayoutCache\""
PORTLETLAYOUT_CACHE_UID = "String  \"PortletlLayoutCacheUID\""
PORTLET_CACHE_PREFIX = "String  \"PORTLETCHACHE_\""
PORTLETS_ALLOWED_CACHE = "String  \"PORTLETSALLOWED\""
STARTCENTER_UID_CACHE_NAME = "String  \"CURRENTSTARTCENTERUID\""
MXE_WEBCLIENT_DEEPREQUIREDCHECK = "String  \"mxe.webclient.deepRequiredCheck\""
def getWebClientRuntime():
    '''public static WebClientRuntime getWebClientRuntime()
    '''
def loadDOM():
    '''public static synchronized Document loadDOM(final InputStream inputStream)
    public static synchronized Document loadDOM(final String input)
    '''
def getWebClientSession():
    '''public WebClientSession getWebClientSession(final HttpServletRequest request)
    '''
def addWebClientSession():
    '''public void addWebClientSession(final HttpSession httpSession, final WebClientSession wcs)
    '''
def removeWebClientSession():
    '''public WebClientSession removeWebClientSession(final HttpSession httpSession)
    '''
def getAppDescriptor():
    '''public AppDescriptor getAppDescriptor(final String appName, final WebClientSession wcs)
    public synchronized AppDescriptor getAppDescriptor(final String appName)
    '''
def getPresentationCache():
    '''public PresentationCache getPresentationCache()
    '''
def getAppName():
    '''public static String getAppName(final Element element)
    '''
def getLibraryDescriptor():
    '''public LibraryDescriptor getLibraryDescriptor(String libraryName, final WebClientSession wcs)
    '''
def getToolBoxDescriptor():
    '''public synchronized ToolBoxDescriptor getToolBoxDescriptor(final String toolboxName, final WebClientSession wcs)
    '''
def getCmsMenuDescriptor():
    '''public CmsMenuDescriptor getCmsMenuDescriptor(final String mboName, final String menuItem)
    '''
def getCMSRegistry():
    '''public ICmsRegistry getCMSRegistry()
    '''
def isCmsEnabled():
    '''public boolean isCmsEnabled()
    '''
def loadHelpTaxonomy():
    '''public void loadHelpTaxonomy()
    '''
def getDisObject():
    '''public DataIntegrationServices getDisObject()
    '''
def getCmsMenuDescriptorObject():
    '''public JSONObject getCmsMenuDescriptorObject(final DataBean bean, final String menuId)
    '''
def getControlDescriptor():
    '''public ControlDescriptor getControlDescriptor(final String type)
    '''
def getComponentDescriptor():
    '''public ComponentDescriptor getComponentDescriptor(final String type)
    '''
def getElementProperty():
    '''public String getElementProperty(final Element xmlControlElement, final ControlDescriptor cd, final String propName)
    '''
def getStreamFromJar():
    '''public HashMap<String, InputStream> getStreamFromJar(String productDir)
    '''
def getOptionMenu():
    '''public String getOptionMenu(final String appName, final String sigOption)
    '''
def getFieldSize():
    '''public int getFieldSize(final boolean onTable, final String maxtype, final int datalength)
    public int getFieldSize(final boolean onTable, final int maxtype, final int datalength)
    '''
def getMaxTypeAsInt():
    '''public static int getMaxTypeAsInt(final String type)
    '''
def getFieldPadding():
    '''public int getFieldPadding()
    '''
def getFieldSizeFactor():
    '''public double getFieldSizeFactor()
    '''
def getFieldSizeMaximum():
    '''public int getFieldSizeMaximum()
    '''
def getTablecolSizeFactor():
    '''public double getTablecolSizeFactor()
    '''
def getTablecolSizeDefault():
    '''public int getTablecolSizeDefault()
    '''
def getDateFieldSize():
    '''public int getDateFieldSize()
    '''
def getDateTimeFieldSize():
    '''public int getDateTimeFieldSize()
    '''
def getTimeFieldSize():
    '''public int getTimeFieldSize()
    '''
def getWebClientProperty():
    '''public static String getWebClientProperty(final String prop)
    public static String getWebClientProperty(final String prop, final String defaultValue)
    '''
def getHelpString():
    '''public static String[] getHelpString(final String propvalue)
    '''
def getHelpUrl():
    '''public String getHelpUrl(final String packagename, final String filename, final String langcode)
    '''
def getWebClientSystemProperty():
    '''public static String getWebClientSystemProperty(final String prop)
    public static String getWebClientSystemProperty(final String prop, final String defaultValue)
    '''
def isNull():
    '''public static boolean isNull(final String val)
    '''
def isNullCheck():
    '''public static boolean isNullCheck(final String val)
    '''
def removeControl():
    '''public void removeControl(final ControlInstance control)
    '''
def reset():
    '''public synchronized void reset()
    '''
def checkSession():
    '''public static WebClientEvent checkSession(final WebClientSession wcs, WebClientEvent event)
    '''
def getMaximoRequestURL():
    '''public static String getMaximoRequestURL(final HttpServletRequest request)
    '''
def getMaximoBaseURL():
    '''public static String getMaximoBaseURL(final HttpServletRequest request)
    '''
def getMaximoRequestContextURL():
    '''public static String getMaximoRequestContextURL(final HttpServletRequest request)
    '''
def getMXSession():
    '''public static MXSession getMXSession(final HttpSession session)
    '''
def sendEvent():
    '''public static int sendEvent(final WebClientSession wcs, final String targetId, final String event, final Object value)
    public static int sendEvent(final WebClientEvent event)
    '''
def removePrepend():
    '''public static String removePrepend(final String value)
    '''
def makesafevalue():
    '''public static String makesafevalue(final String value)
    '''
def makesafeWithAmpersand():
    '''public static String makesafeWithAmpersand(final String value)
    '''
def decodeSafevalue():
    '''public static String decodeSafevalue(final String value)
    '''
def removeQuotes():
    '''public static String removeQuotes(String value)
    '''
def replaceLogicalsWithSymbols():
    '''public static String replaceLogicalsWithSymbols(final String value)
    '''
def makesafejavascriptstringparameter():
    '''public static String makesafejavascriptstringparameter(final String value)
    '''
def formatDataString():
    '''public static String formatDataString(final String dataString)
    '''
def hasInvalidXMLChars():
    '''public static boolean hasInvalidXMLChars(final String value)
    '''
def removeInvalidXMLChars():
    '''public static String removeInvalidXMLChars(final String value)
    '''
def getHost():
    '''public static String getHost()
    '''
def wrapText():
    '''public static String wrapText(final String text, final int lineLength)
    public static String wrapText(final String text, String wrapString, final int lineLength)
    public static String wrapText(final String text, final int lineLength, final boolean canBreakWords, final boolean hyphenateBreaks)
    '''
def getHostAddress():
    '''public static String getHostAddress()
    '''
def isParam():
    '''public static boolean isParam(final HttpServletRequest request, final String val)
    '''
def replaceString():
    '''public static String replaceString(String str, final String pattern, final String replacement)
    '''
def updateString():
    '''public static String updateString(final DataBean attrSource, final String str, final String attributes)
    '''
def escapeForJScript():
    '''public static String escapeForJScript(final String str)
    '''
def isNumeric():
    '''public static boolean isNumeric(final MboValueData mvData)
    '''
def replaceParams():
    '''public static String replaceParams(String message, final String[] params)
    '''
def getPrependValue():
    '''public static String getPrependValue(final String prependString)
    '''
def formatStringForTags():
    '''public static String formatStringForTags(final String str)
    '''
def unFormatString():
    '''public static String unFormatString(final String str)
    '''
def createStatusText():
    '''public static String createStatusText(final MXException[] warnings, final WebClientSession wcs)
    '''
def findAttribute():
    '''public static String findAttribute(final String name, final Element element)
    '''
def findElement():
    '''public static Element findElement(final Element element, final String id)
    public static Element findElement(final Element element, final String id, final boolean isCaseSensitive)
    '''
def findChildElement():
    '''public static Element findChildElement(final Element element, final String id, final boolean isCaseSensitive)
    '''
def findElementByTagName():
    '''public static Element findElementByTagName(final Element element, final String tagName)
    '''
def findChildElementByTagName():
    '''public static Element findChildElementByTagName(final Element element, final String tagName)
    '''
def stringToCodepoints():
    '''public static String stringToCodepoints(final String theString, final boolean escapeSpace, final boolean escapeUnicode)
    '''
def toHex():
    '''public static char toHex(final int nibble)
    '''
def csvStringFromArray():
    '''public static String csvStringFromArray(final Object[] values)
    '''
def removeAppDescriptor():
    '''public AppDescriptor removeAppDescriptor(String appName)
    '''
def removeLibraryDescriptor():
    '''public LibraryDescriptor removeLibraryDescriptor(String name)
    '''
def doubleUpQuotes():
    '''public static String doubleUpQuotes(final String inputData)
    '''
def getSupportedContainer():
    '''public HashMap<String, String> getSupportedContainer(final String ctrlType)
    '''
def getPropFromElement():
    '''public String getPropFromElement(final Element xmlControlElement, final String propName)
    '''
def setRuntimeAppdescripterIndex():
    '''public void setRuntimeAppdescripterIndex(final String newApp, final AppDescriptor runTimeAd)
    '''
def formatStringUniqueId():
    '''public static long formatStringUniqueId(final String tempStr, final Locale userlocale)
    '''
def breakupMsgLookup():
    '''public static String[] breakupMsgLookup(final String lookup)
    '''
def getAppXML():
    '''public String getAppXML(final String appName)
    '''
def setAppXML():
    '''public void setAppXML(final String appName, @TraceMaskValue final String appXML)
    '''
def removeAppXML():
    '''public String removeAppXML(String appName)
    '''
def hasLicenseAccess():
    '''public boolean hasLicenseAccess(final String licensevalue)
    '''
def getSkin():
    '''public String getSkin()
    '''
def setSkin():
    '''public void setSkin(final String skin)
    '''
def parseParamForRow():
    '''public static String[] parseParamForRow(final WebClientSession wcs, final String param)
    public static String[] parseParamForRow(final String param)
    '''
def addRowMarker():
    '''public static String addRowMarker(final String id, final int row)
    '''
def removeSharedAttributeRowMarker():
    '''public static String removeSharedAttributeRowMarker(final String id)
    '''
def removeRowMarker():
    '''public static String removeRowMarker(String id)
    '''
def getRowFromId():
    '''public static int getRowFromId(final String id)
    '''
def containsRowMarker():
    '''public static boolean containsRowMarker(final String value)
    '''
def lineBreakString():
    '''public static String lineBreakString(final String toProcess, final int chunckSize)
    '''
def isAllLatin():
    '''public static boolean isAllLatin(final String titleString)
    '''
def shortenString():
    '''public static String shortenString(final String orig, final int checklength)
    '''
def addToTranslatableLabels():
    '''public static void addToTranslatableLabels(final String type, final String key)
    '''
def getTranslatableLabels():
    '''public static String getTranslatableLabels(final String type, final String key)
    '''
def getExcludeApps():
    '''public Properties getExcludeApps(final String appName)
    '''
def cacheExcludeApps():
    '''public void cacheExcludeApps()
    '''
def getPropsFromJar():
    '''public HashMap<String, InputStream> getPropsFromJar(String productDir)
    '''
def getLocaleFromRequest():
    '''public static Object[] getLocaleFromRequest(final HttpServletRequest request)
    '''
def send503Error():
    '''public static boolean send503Error(final HttpServletResponse response, final MXSession s, final boolean maxUserSessions)
    public static boolean send503Error(final HttpServletResponse response, final MXSession s, final String url)
    '''
def getDojoDirectory():
    '''public static String getDojoDirectory(final HttpServletRequest request)
    '''
def getEntityRelationshipModel():
    '''public synchronized EntityRelationshipModel getEntityRelationshipModel(final String app)
    '''
def createSendEventString():
    '''public static String createSendEventString(final String event, final String target, final String val, final int jsMethod)
    '''
def canUseStaticIds():
    '''public boolean canUseStaticIds()
    '''
def addFieldClassInfo():
    '''public synchronized FieldClassInfo addFieldClassInfo(final FieldClassInfo fci)
    '''
def getFieldClassInfo():
    '''public synchronized FieldClassInfo getFieldClassInfo(final String name)
    '''
def getAppDescFromCache():
    '''public static String getAppDescFromCache(final String appId, final MXSession mxs)
    public static String getAppDescFromCache(String appId, final MXSession mxs, String langCode)
    '''
def resetAppDescCache():
    '''public static void resetAppDescCache()
    '''
def isMTEnabled():
    '''public static boolean isMTEnabled()
    '''
def getMTtenantId():
    '''public static int getMTtenantId()
    '''
def getCacheIdForAppName():
    '''public static String getCacheIdForAppName(String Id)
    '''
def canBeUsedInRecordHover():
    '''public boolean canBeUsedInRecordHover(final String controlType)
    '''
def getAppSigOptionList():
    '''public static Map<String, SigOptionInfo> getAppSigOptionList(final String appId)
    '''
def padString():
    '''public static String padString(String value, final String pad, final int length)
    '''
def isRunningInWebLogic():
    '''public static boolean isRunningInWebLogic()
    '''
