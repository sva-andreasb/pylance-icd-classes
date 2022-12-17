def ():
    '''returns CrewAssignViewBean\n\n
    ()\n
    '''
def _toggleview():
    '''returns JSONObject\n\n
    _toggleview(final WebClientSession sess, final String ids, final String values)\n
    '''
def _pre3wks():
    '''returns JSONObject\n\n
    _pre3wks(final WebClientSession sess, final String ids, final String values)\n
    '''
def _next3wks():
    '''returns JSONObject\n\n
    _next3wks(final WebClientSession sess, final String ids, final String values)\n
    '''
def loadSchedulerProject():
    '''returns None\n\n
    loadSchedulerProject(final WebClientSession sess)\n
    '''
def getLayoutUI():
    '''returns JSONObject\n\n
    getLayoutUI(final WebClientSession sess, @MXEventParam("appname") final String appName, @MXEventParam("projectid") final String projectId)\n
    '''
def applyModelChange():
    '''returns None\n\n
    applyModelChange(final MXGanttModel model, final JSONObject obj, final MXActivity currentActivity, final MXResource res, final WebClientSession session)\n
    '''
def addModelChange():
    '''returns None\n\n
    addModelChange(final MXGanttModel model, final JSONObject obj, final MXActivity currentActivity, final MXResource res, final WebClientSession session)\n
    addModelChange(final MXGanttModel model, final JSONObject obj, final MXActivity currentActivity, final WebClientSession session)\n
    '''
def setSkillMapping():
    '''returns boolean\n\n
    setSkillMapping(final MXGanttModel model, final IlvGeneralActivity currentActivity, final MXResource res, final boolean update)\n
    '''
def setSegmentInfo():
    '''returns None\n\n
    setSegmentInfo(final IlvGeneralActivity activity, final MXResource res)\n
    '''
def newWorkAction():
    '''returns JSONObject\n\n
    newWorkAction(final WebClientSession sess, final String actionid, final String params)\n
    '''
def splitAction():
    '''returns JSONObject\n\n
    splitAction(final WebClientSession sess, final String actionid, final String params)\n
    '''
def createNewAssignment():
    '''returns MXActivity\n\n
    createNewAssignment(final MXGanttModel model, final WebClientSession session, final MXActivity activity, final MXResource res, final long start, final long end, final int selectedseg, final boolean activityIsParent)\n
    '''
def splitAssignment():
    '''returns None\n\n
    splitAssignment(final MXGanttModel model, final WebClientSession session, final MXActivity segmentactivity, final MXResource res, final long start, final long end)\n
    '''
def reassign():
    '''returns JSONObject\n\n
    reassign(final WebClientSession sess, final String actionid, final String params)\n
    '''
def AssignAssignment():
    '''returns None\n\n
    AssignAssignment(final MXGanttModel model, final ReplyBuilder reply, final WebClientSession sess, final MXActivity act, final MXResource res)\n
    '''
def newassignment():
    '''returns JSONObject\n\n
    newassignment(final WebClientSession sess, final String actionid, final String params)\n
    '''
def canReassign():
    '''returns boolean\n\n
    canReassign(final String[] selectedresources, final Selection selected)\n
    '''
def processChange():
    '''returns None\n\n
    processChange(final Future<MXGanttModel> model, final JSONObject change, final WebClientSession sess, final ReplyBuilder reply)\n
    '''
def markAssignmentDelete():
    '''returns None\n\n
    markAssignmentDelete(final Future<MXGanttModel> modelFuture, final JSONObject obj, final MXActivity act)\n
    '''
def showmenu():
    '''returns boolean\n\n
    showmenu(final MXGanttModel model, final MXActivity act, final MXResource res)\n
    '''
def isDailyView():
    '''returns boolean\n\n
    isDailyView()\n
    '''
