def ():
    '''returns BaseLargeGanttView\n\n
    ()\n
    '''
def loadSKDUIInfo():
    '''returns SKDUIInfo\n\n
    loadSKDUIInfo()\n
    '''
def getTooltip():
    '''returns DynamicTooltip\n\n
    getTooltip(final WebClientSession sess, final String projectid, final String col, final String id)\n
    '''
def getTooltipForUnloadedCPM():
    '''returns DynamicTooltip\n\n
    getTooltipForUnloadedCPM(final WebClientSession sess, @MXEventParam("projectid") final String projectId, @MXEventParam("activityid") final String activityId, @MXEventParam("fromdependency") final boolean fromDependency)\n
    '''
def getTooltipForCPM():
    '''returns DynamicTooltip\n\n
    getTooltipForCPM(final WebClientSession sess, final String projectid, final String fromId, final String toId)\n
    '''
def getTooltipForDate():
    '''returns DynamicTooltip\n\n
    getTooltipForDate(final WebClientSession sess, final String projectid, final String col, final String id, final long date)\n
    '''
def async_upload_changes():
    '''returns ReplyBuilder\n\n
    async_upload_changes(final WebClientSession sess)\n
    '''
def getActualStartEnd():
    '''returns Range<Date>\n\n
    getActualStartEnd()\n
    '''
def getCalculatedProjectMinMax():
    '''returns Range<Date>\n\n
    getCalculatedProjectMinMax()\n
    '''
def async_get_table_context_menu():
    '''returns TMenu\n\n
    async_get_table_context_menu(final WebClientSession sess, @MXEventParam("projectid") final String projectId, @MXEventParam("id") final String id, @MXEventParam("col") final String column, @MXEventParam("value") String value)\n
    '''
