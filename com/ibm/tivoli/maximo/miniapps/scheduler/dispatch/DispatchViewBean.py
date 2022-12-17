def ():
    '''returns DispatchViewBean\n\n
    ()\n
    '''
def getUtil():
    '''returns DispatchUtil\n\n
    getUtil()\n
    '''
def getMapFacade():
    '''returns MapFacadeTG\n\n
    getMapFacade()\n
    '''
def getRouteDetailsForResources():
    '''returns JSONObject\n\n
    getRouteDetailsForResources(@MXEventParam("resources") final JSONArray resources, @MXEventParam("start_time") final long startTime, @MXEventParam("end_time") final long endTime, @MXEventParam("refresh_options") final JSONObject refreshOptions)\n
    '''
def loadData():
    '''returns None\n\n
    loadData(final WebClientSession sess, @MXEventParam("projectid") final String projectId, @MXEventParam("addShiftInfo") final boolean addShiftInfo, @MXEventParam("resObj1") final String resObj1, @MXEventParam("resKey1") final String resKey1)\n
    '''
def loadUI():
    '''returns JSONObject\n\n
    loadUI(final WebClientSession sess, @MXEventParam("projectid") final String projectId, @MXEventParam("addShiftInfo") final boolean addShiftInfo, @MXEventParam("resObj1") final String resObj1, @MXEventParam("resKey1") final String resKey1)\n
    '''
def call():
    '''returns MXGanttModel\n\n
    call()\n
    '''
def getTooltip():
    '''returns DynamicTooltip\n\n
    getTooltip(final WebClientSession sess, @MXEventParam("projectid") final String projectid, @MXEventParam("col") final String col, @MXEventParam("id") final String id)\n
    '''
def getTooltipForDate():
    '''returns DynamicTooltip\n\n
    getTooltipForDate(final WebClientSession sess, @MXEventParam("projectid") final String projectid, @MXEventParam("col") final String col, @MXEventParam("id") final String id, @MXEventParam("date") final long date)\n
    '''
def getTooltipForPoint():
    '''returns DynamicTooltip\n\n
    getTooltipForPoint(@MXEventParam("id") final String id, @MXEventParam("point_index") final int pointIndex)\n
    '''
def async_upload_changes():
    '''returns ReplyBuilder\n\n
    async_upload_changes(final WebClientSession sess)\n
    '''
def processChange():
    '''returns None\n\n
    processChange(final Future<MXGanttModel> model, final JSONObject change, final WebClientSession sess, final ReplyBuilder reply)\n
    '''
def updateDuration():
    '''returns None\n\n
    updateDuration(final MXGanttModel model, final Date oldStartTime, final Date oldEndTime, final Date newStartTime, final Date newEndTime, final MXActivity mxa)\n
    '''
def initializeProjectData():
    '''returns None\n\n
    initializeProjectData()\n
    '''
def onReset():
    '''returns None\n\n
    onReset()\n
    '''
def async_get_table_context_menu():
    '''returns TMenu\n\n
    async_get_table_context_menu(final WebClientSession sess, @MXEventParam("projectid") final String projectId, @MXEventParam("selection") final JSONObject selection)\n
    '''
def isLocked():
    '''returns boolean\n\n
    isLocked(final MXActivity activity)\n
    '''
def refreshResource():
    '''returns JSONObject\n\n
    refreshResource(final WebClientSession sess, final String actionid, final String params)\n
    '''
def createAssignment():
    '''returns JSONObject\n\n
    createAssignment(final WebClientSession sess, final String actionid, final String params)\n
    '''
def deleteAssignment():
    '''returns JSONObject\n\n
    deleteAssignment(final WebClientSession sess, final String actionid, final String params)\n
    '''
def splitAssignment():
    '''returns JSONObject\n\n
    splitAssignment(final WebClientSession sess, final String actionid, final String params)\n
    splitAssignment(final WebClientSession sess, final String actionid, final String params, final int numberOfSplits)\n
    '''
def splitAssignment3():
    '''returns JSONObject\n\n
    splitAssignment3(final WebClientSession sess, final String actionid, final String params)\n
    '''
def splitAssignmentToShift():
    '''returns JSONObject\n\n
    splitAssignmentToShift(final WebClientSession sess, final String actionid, final String params)\n
    '''
def lock():
    '''returns JSONObject\n\n
    lock(final WebClientSession sess, final String actionid, final String params)\n
    '''
def unlock():
    '''returns JSONObject\n\n
    unlock(final WebClientSession sess, final String actionid, final String params)\n
    '''
def toggleLock():
    '''returns JSONObject\n\n
    toggleLock(final WebClientSession sess, final String actionid, final String params, final boolean lock)\n
    '''
def getExtraResources():
    '''returns List<WebResource>\n\n
    getExtraResources(final String servletBaseUrl, final String miniappBaseUrl)\n
    '''
def isSerializable():
    '''returns boolean\n\n
    isSerializable(final String field, final Object val)\n
    '''
def SAVEBULKTRAVELTIME():
    '''returns JSONObject\n\n
    SAVEBULKTRAVELTIME(@MXEventParam("data") final JSONArray params)\n
    '''
def SHOWMULTIPLEROUTEERRORS():
    '''returns JsonObject\n\n
    SHOWMULTIPLEROUTEERRORS(@MXEventParam("data") final JSONArray param)\n
    '''
def on_reload_model_for_traveltime():
    '''returns None\n\n
    on_reload_model_for_traveltime()\n
    '''
def autoRefreshModel():
    '''returns ReplyBuilder\n\n
    autoRefreshModel(@MXEventParam("projectid") final String projectId)\n
    '''
