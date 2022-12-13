def GWAResourceScheduleView():
'''public GWAResourceScheduleView()
'''
pass
def getLayoutUI():
'''public JSONObject getLayoutUI(final WebClientSession sess, @MXEventParam("appname") final String appName, @MXEventParam("projectid") final String projectId)
'''
pass
def createUIOptions():
'''public UIOptions createUIOptions(final String projectId)
'''
pass
def addLockDurationIcon():
'''public void addLockDurationIcon(final UIOptions opts, final boolean create)
'''
pass
def addGotoToolbarOptions():
'''public void addGotoToolbarOptions(final UIOptions opts)
'''
pass
def addViewNavToolbarOptions():
'''public void addViewNavToolbarOptions(final UIOptions opts)
'''
pass
def async_load_gantt_data():
'''public synchronized JSONObject async_load_gantt_data(final WebClientSession sess)
'''
pass
def async_upload_changes():
'''public ReplyBuilder async_upload_changes(final WebClientSession sess)
'''
pass
def processMove():
'''public void processMove(final JSONObject change, final WebClientSession sess, final ReplyBuilder reply)
'''
pass
def processChange():
'''public void processChange(final JSONObject change, final WebClientSession sess, final ReplyBuilder reply)
'''
pass
def updateStartEndTimes():
'''public int updateStartEndTimes(final GWASchedule schedule, final JSONObject change, final WebClientSession sess, final Activity activity)
'''
pass
def on_handle_applink_menu_item():
'''public Object on_handle_applink_menu_item(final WebClientSession sess, @MXEventParam("id") final String id, @MXEventParam("value") final String action, @MXEventParam("values") final String values, @MXEventParam("selection") final JSONObject selection)
'''
pass
def getActualStartEnd():
'''public Range<Date> getActualStartEnd()
'''
pass
def getCalculatedProjectMinMax():
'''public Range<Date> getCalculatedProjectMinMax()
'''
pass
def getTooltip():
'''public DynamicTooltip getTooltip(final WebClientSession sess, final String projectid, final String col, final String id)
'''
pass
def getTooltipForCPM():
'''public DynamicTooltip getTooltipForCPM(final WebClientSession sess, final String projectid, final String fromId, final String toId)
'''
pass
def getTooltipForDate():
'''public DynamicTooltip getTooltipForDate(final WebClientSession sess, final String projectid, final String col, final String id, final long date)
'''
pass
def addActionMenuItems():
'''public void addActionMenuItems(final TMenu popupmenu, final String[] selectedactivitys, final GWASchedule schedule, final IMXActivityPropertyInfo actproptinfo, final String projectId, final String propName, final String propValue, final String frame)
'''
pass
def getRelatedAssignments():
'''public ReplyBuilder getRelatedAssignments(final WebClientSession sess, @MXEventParam("projectid") final String projectId, @MXEventParam("activityid") final String activityid)
'''
pass
def gotoWeek():
'''public JSONObject gotoWeek(final WebClientSession sess, @MXEventParam("direction") final int direction)
'''
pass
def gotoWeekDate():
'''public JSONObject gotoWeekDate(final WebClientSession sess, @MXEventParam("selectedDate") final long selectedDate)
'''
pass
def setWeekDate():
'''public JSONObject setWeekDate(final WebClientSession sess, @MXEventParam("currentDate") final long currentDate)
'''
pass
def _refreshSelected():
'''public JSONObject _refreshSelected(final WebClientSession sess, @MXEventParam("ids") final String ids)
'''
pass
def newWorkAction():
'''public JSONObject newWorkAction(final WebClientSession sess, final String actionid, final String params)
'''
pass
def createNewAssignment():
'''public Activity createNewAssignment(final GWASchedule model, final WebClientSession session, final Activity act, final Resource res, final long assignmentId, final MboRemote wo)
'''
pass
def deleteWorkAction():
'''public JSONObject deleteWorkAction(final WebClientSession sess, final String actionid, final String params)
'''
pass
def unassign():
'''public JSONObject unassign(final WebClientSession sess, final String actionid, final String params)
'''
pass
def mergeWorkAction():
'''public JSONObject mergeWorkAction(final WebClientSession sess, final String actionid, final String params)
'''
pass
def updateDuration():
'''public void updateDuration(final GWASchedule schedule, final Date oldStartTime, final Date oldEndTime, final Date newStartTime, final Date newEndTime, final Activity activity)
'''
pass
