def onReset():
    '''returns None\n\n
    onReset()\n
    '''
def async_get_table_context_menu():
    '''returns TMenu\n\n
    async_get_table_context_menu(final WebClientSession sess, @MXEventParam("projectid") final String projectId, @MXEventParam("id") final String id, @MXEventParam("col") final String column, @MXEventParam("value") String value)\n
    '''
def on_handle_applink_menu_item():
    '''returns Object\n\n
    on_handle_applink_menu_item(final WebClientSession sess, @MXEventParam("id") final String id, @MXEventParam("value") final String action, @MXEventParam("values") final String values, @MXEventParam("selection") final JSONObject selection)\n
    '''
def getGanttConfigInfo():
    '''returns GanttConfigInfo\n\n
    getGanttConfigInfo(final WebClientSession sess, @MXEventParam("appname") final String appName, @MXEventParam("projectid") final String projectId)\n
    '''
def async_upload_changes():
    '''returns ReplyBuilder\n\n
    async_upload_changes(final WebClientSession sess)\n
    '''
def updateStartEndTimes():
    '''returns int\n\n
    updateStartEndTimes(final Future<MXGanttModel> model, final JSONObject change, final WebClientSession sess, final MXActivity mxa)\n
    '''
def updateDuration():
    '''returns None\n\n
    updateDuration(final MXGanttModel model, final Date oldStartTime, final Date oldEndTime, final Date newStartTime, final Date newEndTime, final MXActivity mxa)\n
    '''
def loadSKDUIInfo():
    '''returns SKDUIInfo\n\n
    loadSKDUIInfo()\n
    '''
def getTooltip():
    '''returns DynamicTooltip\n\n
    getTooltip(final WebClientSession sess, @MXEventParam("projectid") final String projectid, @MXEventParam("col") final String col, @MXEventParam("id") final String id)\n
    '''
def getTooltipForCPM():
    '''returns DynamicTooltip\n\n
    getTooltipForCPM(final WebClientSession sess, @MXEventParam("projectid") final String projectid, @MXEventParam("fromid") final String fromId, @MXEventParam("toid") final String toId)\n
    '''
def getTooltipForDate():
    '''returns DynamicTooltip\n\n
    getTooltipForDate(final WebClientSession sess, @MXEventParam("projectid") final String projectid, @MXEventParam("col") final String col, @MXEventParam("id") final String id, @MXEventParam("date") final long date)\n
    '''
def getTooltipForPoint():
    '''returns DynamicTooltip\n\n
    getTooltipForPoint(@MXEventParam("id") final String id, @MXEventParam("point_index") final int pointIndex)\n
    '''
def getActivitites():
    '''returns List<MXActivity>\n\n
    getActivitites(final String[] ids, final Future<MXGanttModel> model)\n
    '''
def addActionMenuItems():
    '''returns None\n\n
    addActionMenuItems(final TMenu popupmenu, final String[] selectedactivitys, final Future<MXGanttModel> modelFutre, final IMXActivityPropertyInfo actproptinfo, final String projectId, final String propName, final String propValue, final String frame)\n
    '''
def addModelChange():
    '''returns None\n\n
    addModelChange(final MXGanttModel model, final MXActivity currentActivity, final WebClientSession session)\n
    addModelChange(final MXGanttModel model, final JSONObject obj, final MXActivity currentActivity, final WebClientSession session)\n
    '''
def getSKDPMUtility():
    '''returns SKDPMUtility\n\n
    getSKDPMUtility(final MXGanttModel model)\n
    '''
def addGotoToolbarOptions():
    '''returns None\n\n
    addGotoToolbarOptions(final UIOptions opts)\n
    '''
def addZoomToToolbarOptions():
    '''returns None\n\n
    addZoomToToolbarOptions(final UIOptions opts)\n
    '''
def addLockDurationIcon():
    '''returns None\n\n
    addLockDurationIcon(final UIOptions opts, final boolean create)\n
    '''
def addFixUI():
    '''returns None\n\n
    addFixUI(final UIOptions opts)\n
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
def canNotAssignTo():
    '''returns boolean\n\n
    canNotAssignTo(final String assignaction, final MXActivity act, final String[] selectedactivitys, final MXGanttModel model)\n
    '''
def clearSavedState():
    '''returns None\n\n
    clearSavedState()\n
    '''
def getCalculatedProjectMinMax():
    '''returns Range<Date>\n\n
    getCalculatedProjectMinMax()\n
    '''
def getActualStartEnd():
    '''returns Range<Date>\n\n
    getActualStartEnd()\n
    '''
