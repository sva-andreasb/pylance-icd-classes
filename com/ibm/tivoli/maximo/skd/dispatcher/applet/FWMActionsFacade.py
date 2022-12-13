REFRESH_MODEL_NEEDED = "int  0"
REFRESH_PARTIAL_MODEL_NEEDED = "int  1"
REFRESH_APPLET_MODEL_ONLY = "int  2"
def FWMActionsFacade():
    '''    public FWMActionsFacade(final JSObject window, final String namespace)
    '''
def isInitialized():
    '''    public boolean isInitialized()
    '''
def executeJSCall():
    '''    public void executeJSCall(final String functionName)
    public void executeJSCall(final String functionName, final JSONArtifact params)
    public void executeJSCall(final String functionName, final JSONArtifact params, final String callbackMethodName, final String errorCallback)
    '''
def executeJSFNCall():
    '''    public void executeJSFNCall(final String functionName, final String param1)
    public void executeJSFNCall(final String functionName, final String param1, final String param2)
    '''
def deleteAssignment():
    '''    public void deleteAssignment(final String assignId, final MXResource resource)
    '''
def onAssignmentDelete():
    '''    public int onAssignmentDelete(final JSONObject data)
    '''
def createAssignment():
    '''    public void createAssignment(final String assignId, final MXResource resource)
    '''
def onAssignmentCreate():
    '''    public int onAssignmentCreate(final JSONObject data)
    '''
def syncUpdatedAssignments():
    '''    public void syncUpdatedAssignments()
    '''
def addUpdateActivity():
    '''    public void addUpdateActivity(final MXResource newResource, final MXActivity currentActivity)
    public void addUpdateActivity(final MXResource newResource, final MXActivity currentActivity, final MXResource oldresource)
    '''
def splitAssignment():
    '''    public void splitAssignment(final String assignmentId, final Integer numberOfSplits, final MXResource resource)
    '''
def onAssignmentSplit():
    '''    public int onAssignmentSplit(final JSONObject data)
    '''
def drawRouteCallback():
    '''    public int drawRouteCallback()
    '''
def splitAssignmentToShift():
    '''    public void splitAssignmentToShift(final String assignmentId, final MXResource resource)
    '''
def onAssignmentSplitToShift():
    '''    public int onAssignmentSplitToShift(final JSONObject data)
    '''
def updateMap():
    '''    public void updateMap(final IlvGanttModel ganttModel, final JSONObject refreshOptions)
    public void updateMap(final IlvTimeInterval visibleInterval, final IlvGanttModel ganttModel, final JSONObject refreshOptions)
    '''
def setMapReady():
    '''    public void setMapReady()
    '''
def clearRoutes():
    '''    public void clearRoutes()
    '''
def refreshRoutes():
    '''    public void refreshRoutes(final IlvGanttModel ganttModel)
    '''
def triggerServerMessages():
    '''    public void triggerServerMessages()
    '''
def onBulkAssignments():
    '''    public int onBulkAssignments(final JSONObject data)
    '''
def onSLRTravelTimeUpdated():
    '''    public int onSLRTravelTimeUpdated(final JSONObject data)
    '''
def onServerError():
    '''    public int onServerError(final JSONObject data)
    '''
def onRefreshResources():
    '''    public int onRefreshResources(final JSONObject data)
    '''
def toggleLock():
    '''    public void toggleLock(final String assignId, final MXResource resource, final Boolean lock)
    '''
def onAssignmentToggleLock():
    '''    public int onAssignmentToggleLock(final JSONObject data)
    '''
def notifyAssignmentSelecting():
    '''    public void notifyAssignmentSelecting(final String activityId)
    '''
def refreshResource():
    '''    public void refreshResource(final MXResource resource)
    '''
def onRefreshResource():
    '''    public int onRefreshResource(final JSONObject data)
    '''
def UpdateInformation():
    '''    public UpdateInformation(final MXResource newresource, final MXActivity activity, final MXResource oldresource)
    '''
