def CrewAssignViewBean():
'''public CrewAssignViewBean()
'''
pass
def _toggleview():
'''public JSONObject _toggleview(final WebClientSession sess, final String ids, final String values)
'''
pass
def _pre3wks():
'''public JSONObject _pre3wks(final WebClientSession sess, final String ids, final String values)
'''
pass
def _next3wks():
'''public JSONObject _next3wks(final WebClientSession sess, final String ids, final String values)
'''
pass
def loadSchedulerProject():
'''public void loadSchedulerProject(final WebClientSession sess)
'''
pass
def getLayoutUI():
'''public JSONObject getLayoutUI(final WebClientSession sess, @MXEventParam("appname") final String appName, @MXEventParam("projectid") final String projectId)
'''
pass
def applyModelChange():
'''public void applyModelChange(final MXGanttModel model, final JSONObject obj, final MXActivity currentActivity, final MXResource res, final WebClientSession session)
'''
pass
def addModelChange():
'''public void addModelChange(final MXGanttModel model, final JSONObject obj, final MXActivity currentActivity, final MXResource res, final WebClientSession session)
public void addModelChange(final MXGanttModel model, final JSONObject obj, final MXActivity currentActivity, final WebClientSession session)
'''
pass
def setSkillMapping():
'''public boolean setSkillMapping(final MXGanttModel model, final IlvGeneralActivity currentActivity, final MXResource res, final boolean update)
'''
pass
def setSegmentInfo():
'''public void setSegmentInfo(final IlvGeneralActivity activity, final MXResource res)
'''
pass
def newWorkAction():
'''public JSONObject newWorkAction(final WebClientSession sess, final String actionid, final String params)
'''
pass
def splitAction():
'''public JSONObject splitAction(final WebClientSession sess, final String actionid, final String params)
'''
pass
def createNewAssignment():
'''public MXActivity createNewAssignment(final MXGanttModel model, final WebClientSession session, final MXActivity activity, final MXResource res, final long start, final long end, final int selectedseg, final boolean activityIsParent)
'''
pass
def splitAssignment():
'''public void splitAssignment(final MXGanttModel model, final WebClientSession session, final MXActivity segmentactivity, final MXResource res, final long start, final long end)
'''
pass
def reassign():
'''public JSONObject reassign(final WebClientSession sess, final String actionid, final String params)
'''
pass
def AssignAssignment():
'''public void AssignAssignment(final MXGanttModel model, final ReplyBuilder reply, final WebClientSession sess, final MXActivity act, final MXResource res)
'''
pass
def newassignment():
'''public JSONObject newassignment(final WebClientSession sess, final String actionid, final String params)
'''
pass
def canReassign():
'''public boolean canReassign(final String[] selectedresources, final Selection selected)
'''
pass
def processChange():
'''public void processChange(final Future<MXGanttModel> model, final JSONObject change, final WebClientSession sess, final ReplyBuilder reply)
'''
pass
def markAssignmentDelete():
'''public void markAssignmentDelete(final Future<MXGanttModel> modelFuture, final JSONObject obj, final MXActivity act)
'''
pass
def showmenu():
'''public boolean showmenu(final MXGanttModel model, final MXActivity act, final MXResource res)
'''
pass
def loadProject():
'''public synchronized Future<MXGanttModel> loadProject(final JSONObject projectOptions)
'''
pass
def isDailyView():
'''public boolean isDailyView()
'''
pass
