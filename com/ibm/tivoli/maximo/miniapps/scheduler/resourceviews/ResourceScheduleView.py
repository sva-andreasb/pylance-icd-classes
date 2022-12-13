def ResourceScheduleView():
'''public ResourceScheduleView()
'''
pass
def addFilterToggle():
'''public void addFilterToggle(final UIOptions opts)
'''
pass
def setFilterState():
'''public ReplyBuilder setFilterState(@MXEventParam("filter") final boolean val)
'''
pass
def validateAssignment():
'''public void validateAssignment(final WebClientSession sess, final ReplyBuilder reply, final MXGanttModel model, final MXResource res, final MXActivity act)
'''
pass
def getScheduleWindow():
'''public Map<String, Object> getScheduleWindow(final WebClientSession sess, @MXEventParam("projectid") final String projectId, @MXEventParam("activityid") final String activityid)
'''
pass
def getLayoutUI():
'''public JSONObject getLayoutUI(final WebClientSession sess, @MXEventParam("appname") final String appName, @MXEventParam("projectid") final String projectId)
'''
pass
def loadSchedulerProject():
'''public void loadSchedulerProject(final WebClientSession sess)
'''
pass
def async_upload_changes():
'''public ReplyBuilder async_upload_changes(final WebClientSession sess)
'''
pass
def addModelChange():
'''public void addModelChange(final MXGanttModel model, final MXActivity currentActivity, final MXResource res, final MXReservation reservation, final WebClientSession session)
public void addModelChange(final MXGanttModel model, final JSONObject obj, final MXActivity currentActivity, final MXResource res, final MXReservation reservation, final WebClientSession session)
'''
pass
def applyModelChange():
'''public void applyModelChange(final MXGanttModel model, final JSONObject obj, final MXActivity currentActivity, final MXResource res, final MXReservation reservation, final WebClientSession session)
'''
pass
def setSkillMapping():
'''public boolean setSkillMapping(final MXGanttModel model, final IlvGeneralActivity currentActivity, final MXResource res, final MXReservation unused_reservation, final boolean update)
'''
pass
def isLocked():
'''public boolean isLocked(final MXActivity activity)
'''
pass
def canDeleteWork():
'''public boolean canDeleteWork(final MXActivity activity)
'''
pass
def canAssignToLoc():
'''public boolean canAssignToLoc(final MXActivity activity, final String[] selectedresources, final String actresid, final MXGanttModel model)
'''
pass
def dummyAction():
'''public JSONObject dummyAction(final WebClientSession sess, final String actionid, final String params)
'''
pass
def addViewNotesAction():
'''public void addViewNotesAction(final TMenu menu, final String projectId, final MXActivity activity)
'''
pass
def addServerAction():
'''public void addServerAction(final TMenu menu, final String projectId, final MXActivity activity, final MXResource resource, final String actionTitle, final String actionName)
'''
pass
def newWorkAction():
'''public JSONObject newWorkAction(final WebClientSession sess, final String actionid, final String params)
'''
pass
def splitShiftAction():
'''public JSONObject splitShiftAction(final WebClientSession sess, final String actionid, final String params)
'''
pass
def splitAction():
'''public JSONObject splitAction(final WebClientSession sess, final String actionid, final String params)
'''
pass
def split3Action():
'''public JSONObject split3Action(final WebClientSession sess, final String actionid, final String params)
'''
pass
def mergeAllWorkAction():
'''public JSONObject mergeAllWorkAction(final WebClientSession sess, final String actionid, final String params)
'''
pass
def mergeWorkAction():
'''public JSONObject mergeWorkAction(final WebClientSession sess, final String actionid, final String params)
'''
pass
def getTooltip():
'''public DynamicTooltip getTooltip(final WebClientSession sess, @MXEventParam("projectid") final String projectid, @MXEventParam("col") final String col, @MXEventParam("id") final String id)
'''
pass
def splitAssignment():
'''public void splitAssignment(final MXGanttModel model, final WebClientSession session, final MXActivity activity, final MXResource res, final ReplyBuilder reply, final long start, final long end)
'''
pass
def split3Assignment():
'''public void split3Assignment(final MXGanttModel model, final WebClientSession session, final MXActivity activity, final MXResource res, final ReplyBuilder reply, final long start, final long end)
'''
pass
def splitShiftAssignment():
'''public void splitShiftAssignment(final MXGanttModel model, final WebClientSession session, final MXActivity activity, final MXResource res, final ReplyBuilder reply, final long start, final long end)
'''
pass
def mergeAssignments():
'''public void mergeAssignments(final MXGanttModel model, final WebClientSession session, final MXActivity parentActivity, final MXActivity activity, final MXResource res, final ReplyBuilder reply)
'''
pass
def createNewAssignment():
'''public MXActivity createNewAssignment(final MXGanttModel model, final WebClientSession session, final MXActivity act, final MXResource res, final long start, final long end)
'''
pass
def getShiftBreakPoints():
'''public long[] getShiftBreakPoints(final MXGanttModel model, final MXResource resource, final long start, final long end)
'''
pass
def getRelatedAssignments():
'''public ReplyBuilder getRelatedAssignments(final WebClientSession sess, @MXEventParam("projectid") final String projectId, @MXEventParam("activityid") final String activityid)
'''
pass
def visit():
'''public void visit(final IlvActivity item, final IlvGanttModel model, final JSONArray state)
'''
pass
def getMultiSkillResourceSet():
'''public List<List> getMultiSkillResourceSet(final WebClientSession sess, @MXEventParam("projectid") final String projectId, @MXEventParam("activityid") final String activityid)
'''
pass
def assigntoselectedlocations():
'''public JSONObject assigntoselectedlocations(final WebClientSession sess, final String actionid, final String params)
'''
pass
def assignAssignment():
'''public void assignAssignment(final MXGanttModel model, final ReplyBuilder reply, final WebClientSession sess, final MXActivity act, final MXResource res)
'''
pass
def isCapabilityMat():
'''public boolean isCapabilityMat(final WebClientSession sess, final MXGanttModel model, final IlvGeneralActivity currentActivity, final MXResource res)
'''
pass
def isQulificationMat():
'''public String isQulificationMat(final WebClientSession sess, final MXGanttModel model, final IlvGeneralActivity currentActivity, final MXResource res)
'''
pass
def validateScheduleWindow():
'''public boolean validateScheduleWindow(final WebClientSession sess, final MXGanttModel model, final IlvGeneralActivity currentActivity, final MXResource res)
'''
pass
def assignto():
'''public JSONObject assignto(final WebClientSession sess, final String actionid, final String params)
'''
pass
def unassign():
'''public JSONObject unassign(final WebClientSession sess, final String actionid, final String params)
'''
pass
def canUnAssign():
'''public boolean canUnAssign(final MXActivity activity, final String[] selectedactivitis, final String actresid, final MXGanttModel model)
'''
pass
def canAssignToLaborCrew():
'''public boolean canAssignToLaborCrew(final String[] selectedresources, final Selection selected)
'''
pass
def canAssignToLaborCrewAvail():
'''public boolean canAssignToLaborCrewAvail(final String[] selectedresources, final Selection selected)
'''
pass
def autoRefreshModel():
'''public ReplyBuilder autoRefreshModel(@MXEventParam("projectid") final String projectId)
'''
pass
def onReset():
'''public void onReset()
'''
pass
