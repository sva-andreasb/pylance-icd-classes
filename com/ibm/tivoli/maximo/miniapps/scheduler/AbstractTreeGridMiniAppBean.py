TESTIDS_ENABLED_PROPERTY = "String  \"mxe.skd.automationids.enabled\""
SKD_BUILD_ID = "String  \"20200715-0100\""
SCHEDULER_MSG_GROUP = "String  \"scheduler\""
def ():
    '''returns AbstractTreeGridMiniAppBean\n\n
    ()\n
    '''
def getUserInfo():
    '''returns UserInfo\n\n
    getUserInfo()\n
    '''
def addQuickSearch():
    '''returns None\n\n
    addQuickSearch(final UIOptions opts)\n
    '''
def addToggleDependencies():
    '''returns None\n\n
    addToggleDependencies(final UIOptions opts, final boolean create)\n
    '''
def addLinkToWorkViewFilter():
    '''returns None\n\n
    addLinkToWorkViewFilter(final UIOptions opts, final boolean create, final boolean initialState)\n
    '''
def addFilterToggle():
    '''returns None\n\n
    addFilterToggle(final UIOptions opts)\n
    '''
def onReset():
    '''returns None\n\n
    onReset()\n
    '''
def getCurrentProjectId():
    '''returns String\n\n
    getCurrentProjectId()\n
    '''
def isGUIMirrored():
    '''returns boolean\n\n
    isGUIMirrored()\n
    '''
def setGridTitleInUIOptions():
    '''returns None\n\n
    setGridTitleInUIOptions(final UIOptions opts, final boolean readOnly)\n
    '''
def async_export_echo():
    '''returns None\n\n
    async_export_echo(final WebClientSession sess)\n
    '''
def getLastKnownState():
    '''returns String\n\n
    getLastKnownState()\n
    '''
def async_upload_state():
    '''returns JSONObject\n\n
    async_upload_state(final WebClientSession sess, @MXEventParam("cfgid") final String cfgid, @MXEventParam("cookie") final String cookie)\n
    '''
def async_load_text():
    '''returns JSONObject\n\n
    async_load_text(final WebClientSession sess)\n
    '''
def loadSKDUIInfo():
    '''returns SKDUIInfo\n\n
    loadSKDUIInfo()\n
    '''
def async_get_table_context_menu():
    '''returns TMenu\n\n
    async_get_table_context_menu(final WebClientSession sess, @MXEventParam("projectid") final String projectId, @MXEventParam("id") final String id, @MXEventParam("col") final String column, @MXEventParam("value") String value)\n
    '''
def on_handle_applink_menu_item():
    '''returns Object\n\n
    on_handle_applink_menu_item(final WebClientSession sess, @MXEventParam("id") final String id, @MXEventParam("value") final String action, @MXEventParam("values") final String values)\n
    '''
def callMethod():
    '''returns Object\n\n
    callMethod(final String methodName, final Class<?>[] paramTypes, final Object[] params)\n
    '''
def callBeanMethod():
    '''returns Object\n\n
    callBeanMethod(final String method, final Class<?>[] paramTypes, final Object[] params)\n
    '''
def async_upload_changes():
    '''returns ReplyBuilder\n\n
    async_upload_changes(final WebClientSession sess)\n
    '''
def getTimeZone():
    '''returns TimeZone\n\n
    getTimeZone()\n
    '''
def getAppName():
    '''returns String\n\n
    getAppName()\n
    '''
def getTooltipForPoint():
    '''returns DynamicTooltip\n\n
    getTooltipForPoint(@MXEventParam("id") final String id, @MXEventParam("point_index") final int pointIndex)\n
    '''
def async_push_client_message():
    '''returns None\n\n
    async_push_client_message()\n
    '''
def sendEventToTreeGrid():
    '''returns None\n\n
    sendEventToTreeGrid(final String eventId, final String eventArg)\n
    '''
def getPresentationOptions():
    '''returns JSONObject\n\n
    getPresentationOptions()\n
    '''
def isShowingWeather():
    '''returns boolean\n\n
    isShowingWeather()\n
    '''
def label():
    '''returns String\n\n
    label(final String key)\n
    label(final String key, final String def)\n
    '''
def appendCss():
    '''returns None\n\n
    appendCss(final StringBuilder sb, final String key, final String value)\n
    '''
def filterCss():
    '''returns String\n\n
    filterCss(String css, final MiniAppControl control)\n
    '''
def getBaseImageUrl():
    '''returns String\n\n
    getBaseImageUrl()\n
    '''
def loadMiniAppResource():
    '''returns String\n\n
    loadMiniAppResource(final String path)\n
    '''
def getSchedulerProperties():
    '''returns Properties\n\n
    getSchedulerProperties()\n
    '''
def loadTemplate():
    '''returns String\n\n
    loadTemplate(final String id)\n
    '''
def loadTooltip():
    '''returns String\n\n
    loadTooltip(final String id)\n
    '''
def getSKDAppServiceBean():
    '''returns SKDAppServiceBeanRemote\n\n
    getSKDAppServiceBean()\n
    '''
def resolveTemplate():
    '''returns String\n\n
    resolveTemplate(final String templateName, final MboRemote projectMbo)\n
    '''
def setupBean():
    '''returns None\n\n
    setupBean(final WebClientSession wcs)\n
    '''
def initializeProjectData():
    '''returns None\n\n
    initializeProjectData()\n
    '''
def getUIOptions():
    '''returns UIOptions\n\n
    getUIOptions()\n
    '''
def setSerializationHelper():
    '''returns None\n\n
    setSerializationHelper(final MXSerializationHelper mxSerializationHelper)\n
    '''
def clearSavedState():
    '''returns None\n\n
    clearSavedState()\n
    '''
def getApplicationResource():
    '''returns String\n\n
    getApplicationResource(final String path)\n
    '''
def getShiftWorkPeriodInfoForDate():
    '''returns ShiftInfo\n\n
    getShiftWorkPeriodInfoForDate(final IMXGanttModel sched, final Properties props, final Date d)\n
    getShiftWorkPeriodInfoForDate(final IMXGanttModel model, final Date d)\n
    getShiftWorkPeriodInfoForDate(final IMXResource mxr, final IMXGanttModel model, final Date d)\n
    '''
def getTooltipForDateInSchedule():
    '''returns DynamicTooltip\n\n
    getTooltipForDateInSchedule(final IMXGanttModel schedule, final Properties props, final long date)\n
    '''
def getClientSession():
    '''returns WebClientSession\n\n
    getClientSession()\n
    '''
def beanSupplier():
    '''returns Supplier<AbstractTreeGridMiniAppBean>\n\n
    beanSupplier()\n
    '''
def uiOptionsSupplier():
    '''returns Supplier<UIOptions>\n\n
    uiOptionsSupplier()\n
    '''
def get():
    '''returns UIOptions\n\n
    get()\n
    '''
def getModAvailForDate():
    '''returns IMXActivity\n\n
    getModAvailForDate(final IMXResource mxr, final IMXGanttModel model, final Date d)\n
    '''
def getShiftBreakInfoForDate():
    '''returns ShiftInfo\n\n
    getShiftBreakInfoForDate(final IMXResource mxr, final IMXGanttModel model, final Date d)\n
    '''
def updateDateTimeProperty():
    '''returns None\n\n
    updateDateTimeProperty(final String prop, final JSONObject obj, final IMXActivity act)\n
    '''
def updateStringProperty():
    '''returns None\n\n
    updateStringProperty(final String prop, final JSONObject obj, final IMXActivity act, final boolean acceptEmptyString)\n
    '''
def updateIntProperty():
    '''returns boolean\n\n
    updateIntProperty(final String prop, final JSONObject obj, final IMXActivity act)\n
    '''
def updateBooleanProperty():
    '''returns None\n\n
    updateBooleanProperty(final String prop, final JSONObject obj, final IMXActivity act)\n
    '''
def getProjectMbo():
    '''returns MboRemote\n\n
    getProjectMbo()\n
    '''
def getShiftWorkTime():
    '''returns SKDShiftWorkTime\n\n
    getShiftWorkTime()\n
    '''
def setShiftWorkTime():
    '''returns None\n\n
    setShiftWorkTime(final SKDShiftWorkTime shiftWorkTime)\n
    '''
def getStart():
    '''returns Date\n\n
    getStart()\n
    '''
def setStart():
    '''returns None\n\n
    setStart(final Date start)\n
    '''
def getEnd():
    '''returns Date\n\n
    getEnd()\n
    '''
def setEnd():
    '''returns None\n\n
    setEnd(final Date end)\n
    '''
def getColor():
    '''returns String\n\n
    getColor()\n
    '''
def setColor():
    '''returns None\n\n
    setColor(final String color)\n
    '''
