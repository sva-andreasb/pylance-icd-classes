def ():
    '''returns GWAResourceScheduleView\n\n
    ()\n
    '''
def getLayoutUI():
    '''returns JSONObject\n\n
    getLayoutUI(final WebClientSession sess, @MXEventParam("appname") final String appName, @MXEventParam("projectid") final String projectId)\n
    '''
def createUIOptions():
    '''returns UIOptions\n\n
    createUIOptions(final String projectId)\n
    '''
def addLockDurationIcon():
    '''returns None\n\n
    addLockDurationIcon(final UIOptions opts, final boolean create)\n
    '''
def addGotoToolbarOptions():
    '''returns None\n\n
    addGotoToolbarOptions(final UIOptions opts)\n
    '''
def addViewNavToolbarOptions():
    '''returns None\n\n
    addViewNavToolbarOptions(final UIOptions opts)\n
    '''
def async_upload_changes():
    '''returns ReplyBuilder\n\n
    async_upload_changes(final WebClientSession sess)\n
    '''
def processMove():
    '''returns None\n\n
    processMove(final JSONObject change, final WebClientSession sess, final ReplyBuilder reply)\n
    '''
def processChange():
    '''returns None\n\n
    processChange(final JSONObject change, final WebClientSession sess, final ReplyBuilder reply)\n
    '''
def updateStartEndTimes():
    '''returns int\n\n
    updateStartEndTimes(final GWASchedule schedule, final JSONObject change, final WebClientSession sess, final Activity activity)\n
    '''
def on_handle_applink_menu_item():
    '''returns Object\n\n
    on_handle_applink_menu_item(final WebClientSession sess, @MXEventParam("id") final String id, @MXEventParam("value") final String action, @MXEventParam("values") final String values, @MXEventParam("selection") final JSONObject selection)\n
    '''
def getActualStartEnd():
    '''returns Range<Date>\n\n
    getActualStartEnd()\n
    '''
def getCalculatedProjectMinMax():
    '''returns Range<Date>\n\n
    getCalculatedProjectMinMax()\n
    '''
def getTooltip():
    '''returns DynamicTooltip\n\n
    getTooltip(final WebClientSession sess, final String projectid, final String col, final String id)\n
    '''
def getTooltipForCPM():
    '''returns DynamicTooltip\n\n
    getTooltipForCPM(final WebClientSession sess, final String projectid, final String fromId, final String toId)\n
    '''
def getTooltipForDate():
    '''returns DynamicTooltip\n\n
    getTooltipForDate(final WebClientSession sess, final String projectid, final String col, final String id, final long date)\n
    '''
def addActionMenuItems():
    '''returns None\n\n
    addActionMenuItems(final TMenu popupmenu, final String[] selectedactivitys, final GWASchedule schedule, final IMXActivityPropertyInfo actproptinfo, final String projectId, final String propName, final String propValue, final String frame)\n
    '''
def getRelatedAssignments():
    '''returns ReplyBuilder\n\n
    getRelatedAssignments(final WebClientSession sess, @MXEventParam("projectid") final String projectId, @MXEventParam("activityid") final String activityid)\n
    '''
def gotoWeek():
    '''returns JSONObject\n\n
    gotoWeek(final WebClientSession sess, @MXEventParam("direction") final int direction)\n
    '''
def gotoWeekDate():
    '''returns JSONObject\n\n
    gotoWeekDate(final WebClientSession sess, @MXEventParam("selectedDate") final long selectedDate)\n
    '''
def setWeekDate():
    '''returns JSONObject\n\n
    setWeekDate(final WebClientSession sess, @MXEventParam("currentDate") final long currentDate)\n
    '''
def _refreshSelected():
    '''returns JSONObject\n\n
    _refreshSelected(final WebClientSession sess, @MXEventParam("ids") final String ids)\n
    '''
def newWorkAction():
    '''returns JSONObject\n\n
    newWorkAction(final WebClientSession sess, final String actionid, final String params)\n
    '''
def createNewAssignment():
    '''returns Activity\n\n
    createNewAssignment(final GWASchedule model, final WebClientSession session, final Activity act, final Resource res, final long assignmentId, final MboRemote wo)\n
    '''
def deleteWorkAction():
    '''returns JSONObject\n\n
    deleteWorkAction(final WebClientSession sess, final String actionid, final String params)\n
    '''
def unassign():
    '''returns JSONObject\n\n
    unassign(final WebClientSession sess, final String actionid, final String params)\n
    '''
def mergeWorkAction():
    '''returns JSONObject\n\n
    mergeWorkAction(final WebClientSession sess, final String actionid, final String params)\n
    '''
def updateDuration():
    '''returns None\n\n
    updateDuration(final GWASchedule schedule, final Date oldStartTime, final Date oldEndTime, final Date newStartTime, final Date newEndTime, final Activity activity)\n
    '''
