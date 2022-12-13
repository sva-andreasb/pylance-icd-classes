REFRESH_MODEL_NEEDED = "int  0"
REFRESH_PARTIAL_MODEL_NEEDED = "int  1"
REFRESH_APPLET_MODEL_ONLY = "int  2"
def FWMActionsFacade():
'''public FWMActionsFacade(final JSObject window, final String namespace)
'''
pass
def isInitialized():
'''public boolean isInitialized()
'''
pass
def executeJSCall():
'''public void executeJSCall(final String functionName)
public void executeJSCall(final String functionName, final JSONArtifact params)
public void executeJSCall(final String functionName, final JSONArtifact params, final String callbackMethodName, final String errorCallback)
'''
pass
def executeJSFNCall():
'''public void executeJSFNCall(final String functionName, final String param1)
public void executeJSFNCall(final String functionName, final String param1, final String param2)
'''
pass
def deleteAssignment():
'''public void deleteAssignment(final String assignId, final MXResource resource)
'''
pass
def onAssignmentDelete():
'''public int onAssignmentDelete(final JSONObject data)
'''
pass
def createAssignment():
'''public void createAssignment(final String assignId, final MXResource resource)
'''
pass
def onAssignmentCreate():
'''public int onAssignmentCreate(final JSONObject data)
'''
pass
def syncUpdatedAssignments():
'''public void syncUpdatedAssignments()
'''
pass
def addUpdateActivity():
'''public void addUpdateActivity(final MXResource newResource, final MXActivity currentActivity)
public void addUpdateActivity(final MXResource newResource, final MXActivity currentActivity, final MXResource oldresource)
'''
pass
def splitAssignment():
'''public void splitAssignment(final String assignmentId, final Integer numberOfSplits, final MXResource resource)
'''
pass
def onAssignmentSplit():
'''public int onAssignmentSplit(final JSONObject data)
'''
pass
def drawRouteCallback():
'''public int drawRouteCallback()
'''
pass
def splitAssignmentToShift():
'''public void splitAssignmentToShift(final String assignmentId, final MXResource resource)
'''
pass
def onAssignmentSplitToShift():
'''public int onAssignmentSplitToShift(final JSONObject data)
'''
pass
def updateMap():
'''public void updateMap(final IlvGanttModel ganttModel, final JSONObject refreshOptions)
public void updateMap(final IlvTimeInterval visibleInterval, final IlvGanttModel ganttModel, final JSONObject refreshOptions)
'''
pass
def setMapReady():
'''public void setMapReady()
'''
pass
def clearRoutes():
'''public void clearRoutes()
'''
pass
def refreshRoutes():
'''public void refreshRoutes(final IlvGanttModel ganttModel)
'''
pass
def triggerServerMessages():
'''public void triggerServerMessages()
'''
pass
def onBulkAssignments():
'''public int onBulkAssignments(final JSONObject data)
'''
pass
def onSLRTravelTimeUpdated():
'''public int onSLRTravelTimeUpdated(final JSONObject data)
'''
pass
def onServerError():
'''public int onServerError(final JSONObject data)
'''
pass
def onRefreshResources():
'''public int onRefreshResources(final JSONObject data)
'''
pass
def toggleLock():
'''public void toggleLock(final String assignId, final MXResource resource, final Boolean lock)
'''
pass
def onAssignmentToggleLock():
'''public int onAssignmentToggleLock(final JSONObject data)
'''
pass
def notifyAssignmentSelecting():
'''public void notifyAssignmentSelecting(final String activityId)
'''
pass
def refreshResource():
'''public void refreshResource(final MXResource resource)
'''
pass
def onRefreshResource():
'''public int onRefreshResource(final JSONObject data)
'''
pass
def UpdateInformation():
'''public UpdateInformation(final MXResource newresource, final MXActivity activity, final MXResource oldresource)
'''
pass
