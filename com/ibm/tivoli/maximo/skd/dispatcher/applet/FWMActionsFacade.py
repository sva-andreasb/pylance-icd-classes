REFRESH_MODEL_NEEDED = "int  0"
REFRESH_PARTIAL_MODEL_NEEDED = "int  1"
REFRESH_APPLET_MODEL_ONLY = "int  2"
def ():
    '''returns UpdateInformation\n\n
    (final JSObject window, final String namespace)\n
    (final MXResource newresource, final MXActivity activity, final MXResource oldresource)\n
    '''
def isInitialized():
    '''returns boolean\n\n
    isInitialized()\n
    '''
def executeJSCall():
    '''returns None\n\n
    executeJSCall(final String functionName)\n
    executeJSCall(final String functionName, final JSONArtifact params)\n
    executeJSCall(final String functionName, final JSONArtifact params, final String callbackMethodName, final String errorCallback)\n
    '''
def executeJSFNCall():
    '''returns None\n\n
    executeJSFNCall(final String functionName, final String param1)\n
    executeJSFNCall(final String functionName, final String param1, final String param2)\n
    '''
def deleteAssignment():
    '''returns None\n\n
    deleteAssignment(final String assignId, final MXResource resource)\n
    '''
def onAssignmentDelete():
    '''returns int\n\n
    onAssignmentDelete(final JSONObject data)\n
    '''
def createAssignment():
    '''returns None\n\n
    createAssignment(final String assignId, final MXResource resource)\n
    '''
def onAssignmentCreate():
    '''returns int\n\n
    onAssignmentCreate(final JSONObject data)\n
    '''
def syncUpdatedAssignments():
    '''returns None\n\n
    syncUpdatedAssignments()\n
    '''
def addUpdateActivity():
    '''returns None\n\n
    addUpdateActivity(final MXResource newResource, final MXActivity currentActivity)\n
    addUpdateActivity(final MXResource newResource, final MXActivity currentActivity, final MXResource oldresource)\n
    '''
def splitAssignment():
    '''returns None\n\n
    splitAssignment(final String assignmentId, final Integer numberOfSplits, final MXResource resource)\n
    '''
def onAssignmentSplit():
    '''returns int\n\n
    onAssignmentSplit(final JSONObject data)\n
    '''
def drawRouteCallback():
    '''returns int\n\n
    drawRouteCallback()\n
    '''
def splitAssignmentToShift():
    '''returns None\n\n
    splitAssignmentToShift(final String assignmentId, final MXResource resource)\n
    '''
def onAssignmentSplitToShift():
    '''returns int\n\n
    onAssignmentSplitToShift(final JSONObject data)\n
    '''
def updateMap():
    '''returns None\n\n
    updateMap(final IlvGanttModel ganttModel, final JSONObject refreshOptions)\n
    updateMap(final IlvTimeInterval visibleInterval, final IlvGanttModel ganttModel, final JSONObject refreshOptions)\n
    '''
def setMapReady():
    '''returns None\n\n
    setMapReady()\n
    '''
def clearRoutes():
    '''returns None\n\n
    clearRoutes()\n
    '''
def refreshRoutes():
    '''returns None\n\n
    refreshRoutes(final IlvGanttModel ganttModel)\n
    '''
def triggerServerMessages():
    '''returns None\n\n
    triggerServerMessages()\n
    '''
def onBulkAssignments():
    '''returns int\n\n
    onBulkAssignments(final JSONObject data)\n
    '''
def onSLRTravelTimeUpdated():
    '''returns int\n\n
    onSLRTravelTimeUpdated(final JSONObject data)\n
    '''
def onServerError():
    '''returns int\n\n
    onServerError(final JSONObject data)\n
    '''
def onRefreshResources():
    '''returns int\n\n
    onRefreshResources(final JSONObject data)\n
    '''
def toggleLock():
    '''returns None\n\n
    toggleLock(final String assignId, final MXResource resource, final Boolean lock)\n
    '''
def onAssignmentToggleLock():
    '''returns int\n\n
    onAssignmentToggleLock(final JSONObject data)\n
    '''
def notifyAssignmentSelecting():
    '''returns None\n\n
    notifyAssignmentSelecting(final String activityId)\n
    '''
def refreshResource():
    '''returns None\n\n
    refreshResource(final MXResource resource)\n
    '''
def onRefreshResource():
    '''returns int\n\n
    onRefreshResource(final JSONObject data)\n
    '''
