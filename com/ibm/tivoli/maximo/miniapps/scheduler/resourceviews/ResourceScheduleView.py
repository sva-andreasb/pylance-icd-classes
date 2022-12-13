def ResourceScheduleView():
    '''public ResourceScheduleView()
    '''
def addFilterToggle():
    '''public void addFilterToggle(final UIOptions opts)
    '''
def setFilterState():
    '''public ReplyBuilder setFilterState(@MXEventParam("filter") final boolean val)
    '''
def validateAssignment():
    '''public void validateAssignment(final WebClientSession sess, final ReplyBuilder reply, final MXGanttModel model, final MXResource res, final MXActivity act)
    '''
def getScheduleWindow():
    '''public Map<String, Object> getScheduleWindow(final WebClientSession sess, @MXEventParam("projectid") final String projectId, @MXEventParam("activityid") final String activityid)
    '''
def getLayoutUI():
    '''public JSONObject getLayoutUI(final WebClientSession sess, @MXEventParam("appname") final String appName, @MXEventParam("projectid") final String projectId)
    '''
def loadSchedulerProject():
    '''public void loadSchedulerProject(final WebClientSession sess)
    '''
def async_upload_changes():
    '''public ReplyBuilder async_upload_changes(final WebClientSession sess)
    '''
def addModelChange():
    '''public void addModelChange(final MXGanttModel model, final MXActivity currentActivity, final MXResource res, final MXReservation reservation, final WebClientSession session)
    public void addModelChange(final MXGanttModel model, final JSONObject obj, final MXActivity currentActivity, final MXResource res, final MXReservation reservation, final WebClientSession session)
    '''
def applyModelChange():
    '''public void applyModelChange(final MXGanttModel model, final JSONObject obj, final MXActivity currentActivity, final MXResource res, final MXReservation reservation, final WebClientSession session)
    '''
def setSkillMapping():
    '''public boolean setSkillMapping(final MXGanttModel model, final IlvGeneralActivity currentActivity, final MXResource res, final MXReservation unused_reservation, final boolean update)
    '''
def isLocked():
    '''public boolean isLocked(final MXActivity activity)
    '''
def canDeleteWork():
    '''public boolean canDeleteWork(final MXActivity activity)
    '''
def canAssignToLoc():
    '''public boolean canAssignToLoc(final MXActivity activity, final String[] selectedresources, final String actresid, final MXGanttModel model)
    '''
def dummyAction():
    '''public JSONObject dummyAction(final WebClientSession sess, final String actionid, final String params)
    '''
def addViewNotesAction():
    '''public void addViewNotesAction(final TMenu menu, final String projectId, final MXActivity activity)
    '''
def addServerAction():
    '''public void addServerAction(final TMenu menu, final String projectId, final MXActivity activity, final MXResource resource, final String actionTitle, final String actionName)
    '''
def newWorkAction():
    '''public JSONObject newWorkAction(final WebClientSession sess, final String actionid, final String params)
    '''
def splitShiftAction():
    '''public JSONObject splitShiftAction(final WebClientSession sess, final String actionid, final String params)
    '''
def splitAction():
    '''public JSONObject splitAction(final WebClientSession sess, final String actionid, final String params)
    '''
def split3Action():
    '''public JSONObject split3Action(final WebClientSession sess, final String actionid, final String params)
    '''
def mergeAllWorkAction():
    '''public JSONObject mergeAllWorkAction(final WebClientSession sess, final String actionid, final String params)
    '''
def mergeWorkAction():
    '''public JSONObject mergeWorkAction(final WebClientSession sess, final String actionid, final String params)
    '''
def getTooltip():
    '''public DynamicTooltip getTooltip(final WebClientSession sess, @MXEventParam("projectid") final String projectid, @MXEventParam("col") final String col, @MXEventParam("id") final String id)
    '''
def splitAssignment():
    '''public void splitAssignment(final MXGanttModel model, final WebClientSession session, final MXActivity activity, final MXResource res, final ReplyBuilder reply, final long start, final long end)
    '''
def split3Assignment():
    '''public void split3Assignment(final MXGanttModel model, final WebClientSession session, final MXActivity activity, final MXResource res, final ReplyBuilder reply, final long start, final long end)
    '''
def splitShiftAssignment():
    '''public void splitShiftAssignment(final MXGanttModel model, final WebClientSession session, final MXActivity activity, final MXResource res, final ReplyBuilder reply, final long start, final long end)
    '''
def mergeAssignments():
    '''public void mergeAssignments(final MXGanttModel model, final WebClientSession session, final MXActivity parentActivity, final MXActivity activity, final MXResource res, final ReplyBuilder reply)
    '''
def createNewAssignment():
    '''public MXActivity createNewAssignment(final MXGanttModel model, final WebClientSession session, final MXActivity act, final MXResource res, final long start, final long end)
    '''
def getShiftBreakPoints():
    '''public long[] getShiftBreakPoints(final MXGanttModel model, final MXResource resource, final long start, final long end)
    '''
def getRelatedAssignments():
    '''public ReplyBuilder getRelatedAssignments(final WebClientSession sess, @MXEventParam("projectid") final String projectId, @MXEventParam("activityid") final String activityid)
    '''
def visit():
    '''public void visit(final IlvActivity item, final IlvGanttModel model, final JSONArray state)
    '''
def getMultiSkillResourceSet():
    '''public List<List> getMultiSkillResourceSet(final WebClientSession sess, @MXEventParam("projectid") final String projectId, @MXEventParam("activityid") final String activityid)
    '''
def assigntoselectedlocations():
    '''public JSONObject assigntoselectedlocations(final WebClientSession sess, final String actionid, final String params)
    '''
def assignAssignment():
    '''public void assignAssignment(final MXGanttModel model, final ReplyBuilder reply, final WebClientSession sess, final MXActivity act, final MXResource res)
    '''
def isCapabilityMat():
    '''public boolean isCapabilityMat(final WebClientSession sess, final MXGanttModel model, final IlvGeneralActivity currentActivity, final MXResource res)
    '''
def isQulificationMat():
    '''public String isQulificationMat(final WebClientSession sess, final MXGanttModel model, final IlvGeneralActivity currentActivity, final MXResource res)
    '''
def validateScheduleWindow():
    '''public boolean validateScheduleWindow(final WebClientSession sess, final MXGanttModel model, final IlvGeneralActivity currentActivity, final MXResource res)
    '''
def assignto():
    '''public JSONObject assignto(final WebClientSession sess, final String actionid, final String params)
    '''
def unassign():
    '''public JSONObject unassign(final WebClientSession sess, final String actionid, final String params)
    '''
def canUnAssign():
    '''public boolean canUnAssign(final MXActivity activity, final String[] selectedactivitis, final String actresid, final MXGanttModel model)
    '''
def canAssignToLaborCrew():
    '''public boolean canAssignToLaborCrew(final String[] selectedresources, final Selection selected)
    '''
def canAssignToLaborCrewAvail():
    '''public boolean canAssignToLaborCrewAvail(final String[] selectedresources, final Selection selected)
    '''
def autoRefreshModel():
    '''public ReplyBuilder autoRefreshModel(@MXEventParam("projectid") final String projectId)
    '''
def onReset():
    '''public void onReset()
    '''
