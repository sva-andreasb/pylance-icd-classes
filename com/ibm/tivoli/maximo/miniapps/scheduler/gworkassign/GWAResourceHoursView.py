def ():
    '''returns GWAResourceHoursView\n\n
    ()\n
    '''
def getLayoutUI():
    '''returns JSONObject\n\n
    getLayoutUI(final WebClientSession sess, @MXEventParam("appname") final String appName, @MXEventParam("projectid") final String projectId)\n
    '''
def getProjectData():
    '''returns JSONObject\n\n
    getProjectData(final WebClientSession sess)\n
    '''
def async_get_table_context_menu():
    '''returns TMenu\n\n
    async_get_table_context_menu(final WebClientSession sess, @MXEventParam("projectid") final String projectId, @MXEventParam("id") final String id, @MXEventParam("col") final String column, @MXEventParam("value") String value, @MXEventParam("selection") final JSONObject selection, @MXEventParam("selecteddate") final long selecteddate)\n
    '''
def getTooltip():
    '''returns DynamicTooltip\n\n
    getTooltip(final WebClientSession sess, @MXEventParam("projectid") final String projectid, @MXEventParam("col") final String col, @MXEventParam("id") final String id, @MXEventParam("date") final long date)\n
    '''
def workviewSelected():
    '''returns JSONObject\n\n
    workviewSelected(final WebClientSession sess, @MXEventParam("selection") final String selection)\n
    '''
def saveModAvailReasonCode():
    '''returns JSONObject\n\n
    saveModAvailReasonCode(final WebClientSession sess, @MXEventParam("projectid") final String projectId, @MXEventParam("selection") final String selection, @MXEventParam("objectName") final String objectName, @MXEventParam("date") final long date, @MXEventParam("reasonCode") final String reasonCode, @MXEventParam("durationType") final String durationType)\n
    '''
def deleteModAvailReasonCode():
    '''returns JSONObject\n\n
    deleteModAvailReasonCode(final WebClientSession sess, @MXEventParam("projectid") final String projectId, @MXEventParam("selection") final String selection, @MXEventParam("objectName") final String objectName, @MXEventParam("date") final long date, @MXEventParam("durationType") final String durationType)\n
    '''
def unassignAll():
    '''returns JSONObject\n\n
    unassignAll(final WebClientSession sess, @MXEventParam("projectid") final String projectId, @MXEventParam("id") final String id, @MXEventParam("date") final long date)\n
    '''
def gotoWeek():
    '''returns JSONObject\n\n
    gotoWeek(final WebClientSession sess, @MXEventParam("startWeekDay") final long startWeekDay, @MXEventParam("resetWeek") final boolean resetWeek)\n
    '''
