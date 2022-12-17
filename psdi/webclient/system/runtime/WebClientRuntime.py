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
def getWebClientSession():
    '''returns WebClientSession\n\n
    getWebClientSession(final HttpServletRequest request)\n
    '''
def addWebClientSession():
    '''returns None\n\n
    addWebClientSession(final HttpSession httpSession, final WebClientSession wcs)\n
    '''
def removeWebClientSession():
    '''returns WebClientSession\n\n
    removeWebClientSession(final HttpSession httpSession)\n
    '''
def getAppDescriptor():
    '''returns AppDescriptor\n\n
    getAppDescriptor(final String appName, final WebClientSession wcs)\n
    '''
def getPresentationCache():
    '''returns PresentationCache\n\n
    getPresentationCache()\n
    '''
def getLibraryDescriptor():
    '''returns LibraryDescriptor\n\n
    getLibraryDescriptor(String libraryName, final WebClientSession wcs)\n
    '''
def getCmsMenuDescriptor():
    '''returns CmsMenuDescriptor\n\n
    getCmsMenuDescriptor(final String mboName, final String menuItem)\n
    '''
def getCMSRegistry():
    '''returns ICmsRegistry\n\n
    getCMSRegistry()\n
    '''
def isCmsEnabled():
    '''returns boolean\n\n
    isCmsEnabled()\n
    '''
def loadHelpTaxonomy():
    '''returns None\n\n
    loadHelpTaxonomy()\n
    '''
def getDisObject():
    '''returns DataIntegrationServices\n\n
    getDisObject()\n
    '''
def getCmsMenuDescriptorObject():
    '''returns JSONObject\n\n
    getCmsMenuDescriptorObject(final DataBean bean, final String menuId)\n
    '''
def getControlDescriptor():
    '''returns ControlDescriptor\n\n
    getControlDescriptor(final String type)\n
    '''
def getComponentDescriptor():
    '''returns ComponentDescriptor\n\n
    getComponentDescriptor(final String type)\n
    '''
def getElementProperty():
    '''returns String\n\n
    getElementProperty(final Element xmlControlElement, final ControlDescriptor cd, final String propName)\n
    '''
def getOptionMenu():
    '''returns String\n\n
    getOptionMenu(final String appName, final String sigOption)\n
    '''
def getFieldSize():
    '''returns int\n\n
    getFieldSize(final boolean onTable, final String maxtype, final int datalength)\n
    getFieldSize(final boolean onTable, final int maxtype, final int datalength)\n
    '''
def getFieldPadding():
    '''returns int\n\n
    getFieldPadding()\n
    '''
def getFieldSizeFactor():
    '''returns double\n\n
    getFieldSizeFactor()\n
    '''
def getFieldSizeMaximum():
    '''returns int\n\n
    getFieldSizeMaximum()\n
    '''
def getTablecolSizeFactor():
    '''returns double\n\n
    getTablecolSizeFactor()\n
    '''
def getTablecolSizeDefault():
    '''returns int\n\n
    getTablecolSizeDefault()\n
    '''
def getDateFieldSize():
    '''returns int\n\n
    getDateFieldSize()\n
    '''
def getDateTimeFieldSize():
    '''returns int\n\n
    getDateTimeFieldSize()\n
    '''
def getTimeFieldSize():
    '''returns int\n\n
    getTimeFieldSize()\n
    '''
def getHelpUrl():
    '''returns String\n\n
    getHelpUrl(final String packagename, final String filename, final String langcode)\n
    '''
def removeControl():
    '''returns None\n\n
    removeControl(final ControlInstance control)\n
    '''
def removeAppDescriptor():
    '''returns AppDescriptor\n\n
    removeAppDescriptor(String appName)\n
    '''
def removeLibraryDescriptor():
    '''returns LibraryDescriptor\n\n
    removeLibraryDescriptor(String name)\n
    '''
def getPropFromElement():
    '''returns String\n\n
    getPropFromElement(final Element xmlControlElement, final String propName)\n
    '''
def setRuntimeAppdescripterIndex():
    '''returns None\n\n
    setRuntimeAppdescripterIndex(final String newApp, final AppDescriptor runTimeAd)\n
    '''
def getAppXML():
    '''returns String\n\n
    getAppXML(final String appName)\n
    '''
def setAppXML():
    '''returns None\n\n
    setAppXML(final String appName, @TraceMaskValue final String appXML)\n
    '''
def removeAppXML():
    '''returns String\n\n
    removeAppXML(String appName)\n
    '''
def hasLicenseAccess():
    '''returns boolean\n\n
    hasLicenseAccess(final String licensevalue)\n
    '''
def getSkin():
    '''returns String\n\n
    getSkin()\n
    '''
def setSkin():
    '''returns None\n\n
    setSkin(final String skin)\n
    '''
def getExcludeApps():
    '''returns Properties\n\n
    getExcludeApps(final String appName)\n
    '''
def cacheExcludeApps():
    '''returns None\n\n
    cacheExcludeApps()\n
    '''
def canUseStaticIds():
    '''returns boolean\n\n
    canUseStaticIds()\n
    '''
def canBeUsedInRecordHover():
    '''returns boolean\n\n
    canBeUsedInRecordHover(final String controlType)\n
    '''
