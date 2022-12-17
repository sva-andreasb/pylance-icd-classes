PROCESS_EVENT = "int  1"
CANCEL_EVENT = "int  0"
ERROR_CHECKED_NONE = "int  0"
ERROR_CHECKED_PAGE = "int  1"
ERROR_CHECKED_APP = "int  2"
def ():
    '''returns WebClientEvent\n\n
    (final String type, final String targetId, final Object value, final WebClientSession wcs)\n
    (final String type, final String targetId, final Object value, final String row, final WebClientSession wcs)\n
    (final String type, final String targetId, final Object value, final String row, final String additionalEvent, final long uniqueid, final WebClientSession wcs)\n
    (final String type, final String targetId, final Object value, final String row, final String additionalEvent, final String additionalEventValue, final long uniqueid, final WebClientSession wcs)\n
    (final String type, final String targetId, final Object value, final String row, final String additionalEvent, final String additionalEventValue, final long uniqueid, final WebClientSession wcs, final BaseInstance creatingInstance)\n
    (final String type, final String targetId, final Object value, final WebClientSession wcs, final ComponentInstance source)\n
    (final String type, final String targetId, final Object value, final SessionContext sessionContext)\n
    (final String type, final String targetId, final Object value, final String row, final String additionalEvent, final long uniqueid, final SessionContext sessionContext)\n
    '''
def getSourceControlInstance():
    '''returns ControlInstance\n\n
    getSourceControlInstance()\n
    '''
def getSourceControl():
    '''returns ControlHandler\n\n
    getSourceControl()\n
    '''
def setSourceControl():
    '''returns None\n\n
    setSourceControl(final ControlInstance sourceControl)\n
    setSourceControl(final ControlHandler sourceControl)\n
    '''
def getSourceComponentInstance():
    '''returns ComponentInstance\n\n
    getSourceComponentInstance()\n
    '''
def setSourceComponent():
    '''returns None\n\n
    setSourceComponent(final ComponentInstance sourceComponent)\n
    '''
def getType():
    '''returns String\n\n
    getType()\n
    '''
def getTargetId():
    '''returns String\n\n
    getTargetId()\n
    '''
def getValue():
    '''returns Object\n\n
    getValue()\n
    '''
def getRow():
    '''returns int\n\n
    getRow()\n
    '''
def getValueString():
    '''returns String\n\n
    getValueString()\n
    '''
def setValue():
    '''returns None\n\n
    setValue(final Object eventvalue)\n
    '''
def getEventStatus():
    '''returns int\n\n
    getEventStatus()\n
    '''
def setStatus():
    '''returns None\n\n
    setStatus(final int eventStatus)\n
    '''
def addParameter():
    '''returns None\n\n
    addParameter(final Object key, final Object value)\n
    '''
def getWebClientSession():
    '''returns WebClientSession\n\n
    getWebClientSession()\n
    '''
def getMessageReturn():
    '''returns int\n\n
    getMessageReturn()\n
    '''
def setMessageReturn():
    '''returns None\n\n
    setMessageReturn(final int msgReturn)\n
    '''
def getMessageReturnId():
    '''returns String\n\n
    getMessageReturnId()\n
    '''
def setMessageReturnId():
    '''returns None\n\n
    setMessageReturnId(final String msgReturnId)\n
    '''
def wasProcessed():
    '''returns boolean\n\n
    wasProcessed()\n
    '''
def setProcessed():
    '''returns None\n\n
    setProcessed()\n
    '''
def getAdditionalEvent():
    '''returns String\n\n
    getAdditionalEvent()\n
    '''
def getUniqueId():
    '''returns long\n\n
    getUniqueId()\n
    '''
def getAdditionalEventValue():
    '''returns String\n\n
    getAdditionalEventValue()\n
    '''
def setRow():
    '''returns None\n\n
    setRow(final int row)\n
    '''
def getSessionContext():
    '''returns SessionContext\n\n
    getSessionContext()\n
    '''
def cancelRender():
    '''returns None\n\n
    cancelRender()\n
    '''
def canRender():
    '''returns boolean\n\n
    canRender()\n
    '''
def isPassedSigCheck():
    '''returns boolean\n\n
    isPassedSigCheck()\n
    '''
def setPassedSigCheck():
    '''returns None\n\n
    setPassedSigCheck(final boolean passedSigCheck)\n
    '''
def setAdditionalEventValue():
    '''returns None\n\n
    setAdditionalEventValue(final String eventValue)\n
    '''
def setAdditionalEvent():
    '''returns None\n\n
    setAdditionalEvent(final String event)\n
    '''
def setTransformedValue():
    '''returns None\n\n
    setTransformedValue(final Object transformedValue)\n
    '''
def getTransformedValue():
    '''returns Object\n\n
    getTransformedValue()\n
    '''
def hasTransformedValue():
    '''returns boolean\n\n
    hasTransformedValue()\n
    '''
def getParameter():
    '''returns Object\n\n
    getParameter(final Object key)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def getLevelCheckedForErrors():
    '''returns int\n\n
    getLevelCheckedForErrors()\n
    '''
def setLevelCheckedForErrors():
    '''returns None\n\n
    setLevelCheckedForErrors(final int level)\n
    '''
def conditionalReqChecked():
    '''returns boolean\n\n
    conditionalReqChecked()\n
    '''
def setConditionalReqChecked():
    '''returns None\n\n
    setConditionalReqChecked(final boolean conditionalReqChecked)\n
    '''
def getRequestType():
    '''returns String\n\n
    getRequestType()\n
    '''
def setRequestType():
    '''returns None\n\n
    setRequestType(final String requestType)\n
    '''
def setEventMap():
    '''returns None\n\n
    setEventMap(final Map<String, Object> eventMap)\n
    '''
def isClientEvent():
    '''returns boolean\n\n
    isClientEvent()\n
    '''
def setClientEvent():
    '''returns None\n\n
    setClientEvent(final boolean clientEvent)\n
    '''
