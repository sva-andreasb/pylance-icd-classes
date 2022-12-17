def ():
    '''returns GResourceView\n\n
    ()\n
    '''
def getLayoutUI():
    '''returns JSONObject\n\n
    getLayoutUI(final WebClientSession sess, @MXEventParam("appname") final String appName, @MXEventParam("projectid") final String projectId)\n
    '''
def getProjectData():
    '''returns JSONObject\n\n
    getProjectData(final WebClientSession sess, @MXEventParam("ganttStart") final long ganttStart)\n
    '''
def async_get_table_context_menu():
    '''returns TMenu\n\n
    async_get_table_context_menu(final WebClientSession sess, @MXEventParam("projectid") final String projectId, @MXEventParam("id") final String id, @MXEventParam("col") final String column, @MXEventParam("value") String value, @MXEventParam("selection") final JSONObject selection, @MXEventParam("selecteddate") final long selecteddate)\n
    '''
def getTooltip():
    '''returns DynamicTooltip\n\n
    getTooltip(final WebClientSession sess, @MXEventParam("projectid") final String projectid, @MXEventParam("col") final String col, @MXEventParam("id") final String id, @MXEventParam("date") final long date)\n
    '''
def saveModAvailReasonCode():
    '''returns JSONObject\n\n
    saveModAvailReasonCode(final WebClientSession sess, @MXEventParam("projectid") final String projectId, @MXEventParam("selection") final String selection, @MXEventParam("objectName") final String objectName, @MXEventParam("date") final long date, @MXEventParam("reasonCode") final String reasonCode, @MXEventParam("durationType") final String durationType)\n
    '''
def deleteModAvailReasonCode():
    '''returns JSONObject\n\n
    deleteModAvailReasonCode(final WebClientSession sess, @MXEventParam("projectid") final String projectId, @MXEventParam("selection") final String selection, @MXEventParam("objectName") final String objectName, @MXEventParam("date") final long date, @MXEventParam("durationType") final String durationType)\n
    '''
def addGotoToolbarOptions():
    '''returns None\n\n
    addGotoToolbarOptions(final UIOptions opts)\n
    '''
def gotoPeriod():
    '''returns JSONObject\n\n
    gotoPeriod(final WebClientSession sess, @MXEventParam("direction") final int direction, @MXEventParam("zoomLevel") final int zoomLevel, @MXEventParam("weekStart") final long weekStart)\n
    '''
def setStartDate():
    '''returns JSONObject\n\n
    setStartDate(final WebClientSession sess, @MXEventParam("currentDate") final long currentDate)\n
    '''
