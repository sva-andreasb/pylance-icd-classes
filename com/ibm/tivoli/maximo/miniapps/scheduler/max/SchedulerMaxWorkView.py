SCHEDMAX_SYNC_ID = "String  \"schedmax_sync\""
SESSION_VALUES_REF = "String  \"session_values_ref\""
def ():
    '''returns SchedulerMaxWorkView\n\n
    ()\n
    '''
def async_set_compliance():
    '''returns boolean\n\n
    async_set_compliance(@MXEventParam("projectid") final String id, @MXEventParam("state") final boolean state)\n
    '''
def getLayoutUI():
    '''returns JSONObject\n\n
    getLayoutUI(final WebClientSession sess, @MXEventParam("appname") final String appName, @MXEventParam("projectid") final String projectId)\n
    '''
def createUIOptions():
    '''returns UIOptions\n\n
    createUIOptions(final String projectId)\n
    '''
def async_export_xls():
    '''returns None\n\n
    async_export_xls(final WebClientSession sess)\n
    '''
def getTooltipForDate():
    '''returns DynamicTooltip\n\n
    getTooltipForDate(final WebClientSession sess, @MXEventParam("projectid") final String projectid, @MXEventParam("col") final String col, @MXEventParam("id") final String id, @MXEventParam("date") final long date)\n
    '''
def async_upload_changes():
    '''returns ReplyBuilder\n\n
    async_upload_changes(final WebClientSession sess)\n
    '''
def run():
    '''returns None\n\n
    run()\n
    '''
def _cpmall():
    '''returns JSONObject\n\n
    _cpmall(final WebClientSession sess, final String ids, final String values)\n
    '''
def _cpmselected():
    '''returns JSONObject\n\n
    _cpmselected(final WebClientSession sess, @MXEventParam("ids") final String ids, final String values)\n
    '''
def _cpmcreatelinks():
    '''returns JSONObject\n\n
    _cpmcreatelinks(final WebClientSession sess, @MXEventParam("ids") final String ids, final String values)\n
    '''
def _cpmfilter():
    '''returns JSONObject\n\n
    _cpmfilter(final WebClientSession sess, @MXEventParam("filteredByCriticalPath") final boolean filteredByCriticalPath)\n
    '''
def _discardRefreshSelected():
    '''returns JSONObject\n\n
    _discardRefreshSelected(final WebClientSession sess, @MXEventParam("ids") final String ids)\n
    '''
def _refreshSelected():
    '''returns JSONObject\n\n
    _refreshSelected(final WebClientSession sess, @MXEventParam("ids") final String ids)\n
    '''
def _expandToLevel():
    '''returns JSONObject\n\n
    _expandToLevel(final WebClientSession sess, @MXEventParam("level") final Integer level)\n
    '''
def _updateSummary():
    '''returns JSONObject\n\n
    _updateSummary(final WebClientSession sess, final String ids, final String values)\n
    '''
def _getSelectedTab():
    '''returns JSONObject\n\n
    _getSelectedTab(final WebClientSession sess)\n
    '''
def processChange():
    '''returns None\n\n
    processChange(final JSONObject change, final WebClientSession sess, final ReplyBuilder reply)\n
    '''
def updateStartEndTimes():
    '''returns int\n\n
    updateStartEndTimes(final Schedule schedule, final JSONObject change, final WebClientSession sess, final Activity activity)\n
    '''
def updateDuration():
    '''returns None\n\n
    updateDuration(final Schedule schedule, final Date oldStartTime, final Date oldEndTime, final Date newStartTime, final Date newEndTime, final Activity activity)\n
    '''
def _DELETECONSTRAINTS():
    '''returns ReplyBuilder\n\n
    _DELETECONSTRAINTS(final WebClientSession session, final String value, final String valueList, final JSONObject selection)\n
    '''
def on_handle_applink_menu_item():
    '''returns Object\n\n
    on_handle_applink_menu_item(final WebClientSession sess, @MXEventParam("id") final String id, @MXEventParam("value") final String action, @MXEventParam("values") final String values, @MXEventParam("selection") final JSONObject selection)\n
    '''
def addActionMenuItems():
    '''returns None\n\n
    addActionMenuItems(final TMenu popupmenu, final String[] selectedactivitys, final Schedule schedule, final IMXActivityPropertyInfo actproptinfo, final String projectId, final String propName, final String propValue, final String frame)\n
    '''
def updateDateTimeProperty():
    '''returns None\n\n
    updateDateTimeProperty(final String prop, final JSONObject obj, final IMXActivity act)\n
    '''
