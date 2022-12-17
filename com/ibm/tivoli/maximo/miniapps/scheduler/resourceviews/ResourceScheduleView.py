def ():
    '''returns ResourceScheduleView\n\n
    ()\n
    '''
def addFilterToggle():
    '''returns None\n\n
    addFilterToggle(final UIOptions opts)\n
    '''
def setFilterState():
    '''returns ReplyBuilder\n\n
    setFilterState(@MXEventParam("filter") final boolean val)\n
    '''
def validateAssignment():
    '''returns None\n\n
    validateAssignment(final WebClientSession sess, final ReplyBuilder reply, final MXGanttModel model, final MXResource res, final MXActivity act)\n
    '''
def getLayoutUI():
    '''returns JSONObject\n\n
    getLayoutUI(final WebClientSession sess, @MXEventParam("appname") final String appName, @MXEventParam("projectid") final String projectId)\n
    '''
def loadSchedulerProject():
    '''returns None\n\n
    loadSchedulerProject(final WebClientSession sess)\n
    '''
def async_upload_changes():
    '''returns ReplyBuilder\n\n
    async_upload_changes(final WebClientSession sess)\n
    '''
def addModelChange():
    '''returns None\n\n
    addModelChange(final MXGanttModel model, final MXActivity currentActivity, final MXResource res, final MXReservation reservation, final WebClientSession session)\n
    addModelChange(final MXGanttModel model, final JSONObject obj, final MXActivity currentActivity, final MXResource res, final MXReservation reservation, final WebClientSession session)\n
    '''
def applyModelChange():
    '''returns None\n\n
    applyModelChange(final MXGanttModel model, final JSONObject obj, final MXActivity currentActivity, final MXResource res, final MXReservation reservation, final WebClientSession session)\n
    '''
def setSkillMapping():
    '''returns boolean\n\n
    setSkillMapping(final MXGanttModel model, final IlvGeneralActivity currentActivity, final MXResource res, final MXReservation unused_reservation, final boolean update)\n
    '''
def isLocked():
    '''returns boolean\n\n
    isLocked(final MXActivity activity)\n
    '''
def canDeleteWork():
    '''returns boolean\n\n
    canDeleteWork(final MXActivity activity)\n
    '''
def canAssignToLoc():
    '''returns boolean\n\n
    canAssignToLoc(final MXActivity activity, final String[] selectedresources, final String actresid, final MXGanttModel model)\n
    '''
def dummyAction():
    '''returns JSONObject\n\n
    dummyAction(final WebClientSession sess, final String actionid, final String params)\n
    '''
def addViewNotesAction():
    '''returns None\n\n
    addViewNotesAction(final TMenu menu, final String projectId, final MXActivity activity)\n
    '''
def addServerAction():
    '''returns None\n\n
    addServerAction(final TMenu menu, final String projectId, final MXActivity activity, final MXResource resource, final String actionTitle, final String actionName)\n
    '''
def newWorkAction():
    '''returns JSONObject\n\n
    newWorkAction(final WebClientSession sess, final String actionid, final String params)\n
    '''
def splitShiftAction():
    '''returns JSONObject\n\n
    splitShiftAction(final WebClientSession sess, final String actionid, final String params)\n
    '''
def splitAction():
    '''returns JSONObject\n\n
    splitAction(final WebClientSession sess, final String actionid, final String params)\n
    '''
def split3Action():
    '''returns JSONObject\n\n
    split3Action(final WebClientSession sess, final String actionid, final String params)\n
    '''
def mergeAllWorkAction():
    '''returns JSONObject\n\n
    mergeAllWorkAction(final WebClientSession sess, final String actionid, final String params)\n
    '''
def mergeWorkAction():
    '''returns JSONObject\n\n
    mergeWorkAction(final WebClientSession sess, final String actionid, final String params)\n
    '''
def getTooltip():
    '''returns DynamicTooltip\n\n
    getTooltip(final WebClientSession sess, @MXEventParam("projectid") final String projectid, @MXEventParam("col") final String col, @MXEventParam("id") final String id)\n
    '''
def splitAssignment():
    '''returns None\n\n
    splitAssignment(final MXGanttModel model, final WebClientSession session, final MXActivity activity, final MXResource res, final ReplyBuilder reply, final long start, final long end)\n
    '''
def split3Assignment():
    '''returns None\n\n
    split3Assignment(final MXGanttModel model, final WebClientSession session, final MXActivity activity, final MXResource res, final ReplyBuilder reply, final long start, final long end)\n
    '''
def splitShiftAssignment():
    '''returns None\n\n
    splitShiftAssignment(final MXGanttModel model, final WebClientSession session, final MXActivity activity, final MXResource res, final ReplyBuilder reply, final long start, final long end)\n
    '''
def mergeAssignments():
    '''returns None\n\n
    mergeAssignments(final MXGanttModel model, final WebClientSession session, final MXActivity parentActivity, final MXActivity activity, final MXResource res, final ReplyBuilder reply)\n
    '''
def createNewAssignment():
    '''returns MXActivity\n\n
    createNewAssignment(final MXGanttModel model, final WebClientSession session, final MXActivity act, final MXResource res, final long start, final long end)\n
    '''
def getShiftBreakPoints():
    '''returns long[]\n\n
    getShiftBreakPoints(final MXGanttModel model, final MXResource resource, final long start, final long end)\n
    '''
def getRelatedAssignments():
    '''returns ReplyBuilder\n\n
    getRelatedAssignments(final WebClientSession sess, @MXEventParam("projectid") final String projectId, @MXEventParam("activityid") final String activityid)\n
    '''
def visit():
    '''returns None\n\n
    visit(final IlvActivity item, final IlvGanttModel model, final JSONArray state)\n
    '''
def getMultiSkillResourceSet():
    '''returns List<List>\n\n
    getMultiSkillResourceSet(final WebClientSession sess, @MXEventParam("projectid") final String projectId, @MXEventParam("activityid") final String activityid)\n
    '''
def assigntoselectedlocations():
    '''returns JSONObject\n\n
    assigntoselectedlocations(final WebClientSession sess, final String actionid, final String params)\n
    '''
def assignAssignment():
    '''returns None\n\n
    assignAssignment(final MXGanttModel model, final ReplyBuilder reply, final WebClientSession sess, final MXActivity act, final MXResource res)\n
    '''
def isCapabilityMat():
    '''returns boolean\n\n
    isCapabilityMat(final WebClientSession sess, final MXGanttModel model, final IlvGeneralActivity currentActivity, final MXResource res)\n
    '''
def isQulificationMat():
    '''returns String\n\n
    isQulificationMat(final WebClientSession sess, final MXGanttModel model, final IlvGeneralActivity currentActivity, final MXResource res)\n
    '''
def validateScheduleWindow():
    '''returns boolean\n\n
    validateScheduleWindow(final WebClientSession sess, final MXGanttModel model, final IlvGeneralActivity currentActivity, final MXResource res)\n
    '''
def assignto():
    '''returns JSONObject\n\n
    assignto(final WebClientSession sess, final String actionid, final String params)\n
    '''
def unassign():
    '''returns JSONObject\n\n
    unassign(final WebClientSession sess, final String actionid, final String params)\n
    '''
def canUnAssign():
    '''returns boolean\n\n
    canUnAssign(final MXActivity activity, final String[] selectedactivitis, final String actresid, final MXGanttModel model)\n
    '''
def canAssignToLaborCrew():
    '''returns boolean\n\n
    canAssignToLaborCrew(final String[] selectedresources, final Selection selected)\n
    '''
def canAssignToLaborCrewAvail():
    '''returns boolean\n\n
    canAssignToLaborCrewAvail(final String[] selectedresources, final Selection selected)\n
    '''
def autoRefreshModel():
    '''returns ReplyBuilder\n\n
    autoRefreshModel(@MXEventParam("projectid") final String projectId)\n
    '''
def onReset():
    '''returns None\n\n
    onReset()\n
    '''
