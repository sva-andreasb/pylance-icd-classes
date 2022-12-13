def DispatchViewBean():
    '''    public DispatchViewBean()
    '''
def getUtil():
    '''    public DispatchUtil getUtil()
    '''
def getMapFacade():
    '''    public MapFacadeTG getMapFacade()
    '''
def getRouteDetailsForResources():
    '''    public JSONObject getRouteDetailsForResources(@MXEventParam("resources") final JSONArray resources, @MXEventParam("start_time") final long startTime, @MXEventParam("end_time") final long endTime, @MXEventParam("refresh_options") final JSONObject refreshOptions)
    '''
def loadData():
    '''    public void loadData(final WebClientSession sess, @MXEventParam("projectid") final String projectId, @MXEventParam("addShiftInfo") final boolean addShiftInfo, @MXEventParam("resObj1") final String resObj1, @MXEventParam("resKey1") final String resKey1)
    '''
def loadUI():
    '''    public JSONObject loadUI(final WebClientSession sess, @MXEventParam("projectid") final String projectId, @MXEventParam("addShiftInfo") final boolean addShiftInfo, @MXEventParam("resObj1") final String resObj1, @MXEventParam("resKey1") final String resKey1)
    '''
def getProjectModel():
    '''    public synchronized Future<MXGanttModel> getProjectModel(final UserInfo userInfo, final String id, final boolean addShiftInfo, final String resObj1, final String resKey1)
    public synchronized Future<MXGanttModel> getProjectModel(final JSONObject options, final boolean cache)
    '''
def loadProject():
    '''    public synchronized Future<MXGanttModel> loadProject(final JSONObject options)
    '''
def getProjectModelForResource():
    '''    public synchronized Future<MXGanttModel> getProjectModelForResource(final MXResource res)
    '''
def call():
    '''    public MXGanttModel call()
    '''
def getTooltip():
    '''    public DynamicTooltip getTooltip(final WebClientSession sess, @MXEventParam("projectid") final String projectid, @MXEventParam("col") final String col, @MXEventParam("id") final String id)
    '''
def getTooltipForDate():
    '''    public DynamicTooltip getTooltipForDate(final WebClientSession sess, @MXEventParam("projectid") final String projectid, @MXEventParam("col") final String col, @MXEventParam("id") final String id, @MXEventParam("date") final long date)
    '''
def getTooltipForPoint():
    '''    public DynamicTooltip getTooltipForPoint(@MXEventParam("id") final String id, @MXEventParam("point_index") final int pointIndex)
    '''
def async_upload_changes():
    '''    public ReplyBuilder async_upload_changes(final WebClientSession sess)
    '''
def processChange():
    '''    public void processChange(final Future<MXGanttModel> model, final JSONObject change, final WebClientSession sess, final ReplyBuilder reply)
    '''
def updateDuration():
    '''    public void updateDuration(final MXGanttModel model, final Date oldStartTime, final Date oldEndTime, final Date newStartTime, final Date newEndTime, final MXActivity mxa)
    '''
def initializeProjectData():
    '''    public void initializeProjectData()
    '''
def onReset():
    '''    public void onReset()
    '''
def async_get_table_context_menu():
    '''    public TMenu async_get_table_context_menu(final WebClientSession sess, @MXEventParam("projectid") final String projectId, @MXEventParam("selection") final JSONObject selection)
    '''
def isLocked():
    '''    public boolean isLocked(final MXActivity activity)
    '''
def refreshResource():
    '''    public JSONObject refreshResource(final WebClientSession sess, final String actionid, final String params)
    '''
def createAssignment():
    '''    public JSONObject createAssignment(final WebClientSession sess, final String actionid, final String params)
    '''
def deleteAssignment():
    '''    public JSONObject deleteAssignment(final WebClientSession sess, final String actionid, final String params)
    '''
def splitAssignment():
    '''    public JSONObject splitAssignment(final WebClientSession sess, final String actionid, final String params)
    public JSONObject splitAssignment(final WebClientSession sess, final String actionid, final String params, final int numberOfSplits)
    '''
def splitAssignment3():
    '''    public JSONObject splitAssignment3(final WebClientSession sess, final String actionid, final String params)
    '''
def splitAssignmentToShift():
    '''    public JSONObject splitAssignmentToShift(final WebClientSession sess, final String actionid, final String params)
    '''
def lock():
    '''    public JSONObject lock(final WebClientSession sess, final String actionid, final String params)
    '''
def unlock():
    '''    public JSONObject unlock(final WebClientSession sess, final String actionid, final String params)
    '''
def toggleLock():
    '''    public JSONObject toggleLock(final WebClientSession sess, final String actionid, final String params, final boolean lock)
    '''
def getExtraResources():
    '''    public List<WebResource> getExtraResources(final String servletBaseUrl, final String miniappBaseUrl)
    '''
def isSerializable():
    '''    public boolean isSerializable(final String field, final Object val)
    '''
def SAVEBULKTRAVELTIME():
    '''    public JSONObject SAVEBULKTRAVELTIME(@MXEventParam("data") final JSONArray params)
    '''
def SHOWMULTIPLEROUTEERRORS():
    '''    public JsonObject SHOWMULTIPLEROUTEERRORS(@MXEventParam("data") final JSONArray param)
    '''
def secondsToDuration():
    '''    public static Double secondsToDuration(long seconds)
    '''
def on_reload_model_for_traveltime():
    '''    public void on_reload_model_for_traveltime()
    '''
def autoRefreshModel():
    '''    public ReplyBuilder autoRefreshModel(@MXEventParam("projectid") final String projectId)
    '''
