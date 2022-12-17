def ():
    '''returns ResourceMaxHoursView\n\n
    ()\n
    '''
def getLayoutUI():
    '''returns JSONObject\n\n
    getLayoutUI(final WebClientSession sess, @MXEventParam("appname") final String appName, @MXEventParam("projectid") final String projectId)\n
    '''
def getProjectData():
    '''returns JSONObject\n\n
    getProjectData(@MXEventParam("start") final long start, @MXEventParam("end") final long end)\n
    '''
def changeResourceDisplayMode():
    '''returns JSONObject\n\n
    changeResourceDisplayMode(final WebClientSession sess, @MXEventParam("display") final String display)\n
    '''
def getProjectDataForDates():
    '''returns JSONObject\n\n
    getProjectDataForDates(final Date start, final Date end)\n
    '''
def getTooltipForDate():
    '''returns DynamicTooltip\n\n
    getTooltipForDate(final WebClientSession sess, @MXEventParam("projectid") final String projectid, @MXEventParam("col") final String col, @MXEventParam("id") final String id, @MXEventParam("date") final long date)\n
    '''
def async_get_table_context_menu():
    '''returns TMenu\n\n
    async_get_table_context_menu(final WebClientSession sess, @MXEventParam("projectid") final String projectId, @MXEventParam("id") final String id, @MXEventParam("col") final String column, @MXEventParam("value") String value, @MXEventParam("selection") final JSONObject selection)\n
    '''
