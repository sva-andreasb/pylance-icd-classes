PROCESS_EVENT = "int  1"
CANCEL_EVENT = "int  0"
ERROR_CHECKED_NONE = "int  0"
ERROR_CHECKED_PAGE = "int  1"
ERROR_CHECKED_APP = "int  2"
def WebClientEvent():
'''public WebClientEvent(final String type, final String targetId, final Object value, final WebClientSession wcs)
public WebClientEvent(final String type, final String targetId, final Object value, final String row, final WebClientSession wcs)
public WebClientEvent(final String type, final String targetId, final Object value, final String row, final String additionalEvent, final long uniqueid, final WebClientSession wcs)
public WebClientEvent(final String type, final String targetId, final Object value, final String row, final String additionalEvent, final String additionalEventValue, final long uniqueid, final WebClientSession wcs)
public WebClientEvent(final String type, final String targetId, final Object value, final String row, final String additionalEvent, final String additionalEventValue, final long uniqueid, final WebClientSession wcs, final BaseInstance creatingInstance)
public WebClientEvent(final String type, final String targetId, final Object value, final WebClientSession wcs, final ComponentInstance source)
public WebClientEvent(final String type, final String targetId, final Object value, final SessionContext sessionContext)
public WebClientEvent(final String type, final String targetId, final Object value, final String row, final String additionalEvent, final long uniqueid, final SessionContext sessionContext)
'''
pass
def getSourceControlInstance():
'''public ControlInstance getSourceControlInstance()
'''
pass
def getSourceControl():
'''public ControlHandler getSourceControl()
'''
pass
def setSourceControl():
'''public void setSourceControl(final ControlInstance sourceControl)
public void setSourceControl(final ControlHandler sourceControl)
'''
pass
def getSourceComponentInstance():
'''public ComponentInstance getSourceComponentInstance()
'''
pass
def setSourceComponent():
'''public void setSourceComponent(final ComponentInstance sourceComponent)
'''
pass
def getType():
'''public String getType()
'''
pass
def getTargetId():
'''public String getTargetId()
'''
pass
def getValue():
'''public Object getValue()
'''
pass
def getRow():
'''public int getRow()
'''
pass
def getValueString():
'''public String getValueString()
'''
pass
def setValue():
'''public void setValue(final Object eventvalue)
'''
pass
def getEventStatus():
'''public int getEventStatus()
'''
pass
def setStatus():
'''public void setStatus(final int eventStatus)
'''
pass
def addParameter():
'''public void addParameter(final Object key, final Object value)
'''
pass
def getParameters():
'''public Hashtable<Object, Object> getParameters()
'''
pass
def getWebClientSession():
'''public WebClientSession getWebClientSession()
'''
pass
def getMessageReturn():
'''public int getMessageReturn()
'''
pass
def setMessageReturn():
'''public void setMessageReturn(final int msgReturn)
'''
pass
def getMessageReturnId():
'''public String getMessageReturnId()
'''
pass
def setMessageReturnId():
'''public void setMessageReturnId(final String msgReturnId)
'''
pass
def wasProcessed():
'''public boolean wasProcessed()
'''
pass
def setProcessed():
'''public void setProcessed()
'''
pass
def getAdditionalEvent():
'''public String getAdditionalEvent()
'''
pass
def getUniqueId():
'''public long getUniqueId()
'''
pass
def getAdditionalEventValue():
'''public String getAdditionalEventValue()
'''
pass
def setRow():
'''public void setRow(final int row)
'''
pass
def getSessionContext():
'''public SessionContext getSessionContext()
'''
pass
def cancelRender():
'''public void cancelRender()
'''
pass
def canRender():
'''public boolean canRender()
'''
pass
def isPassedSigCheck():
'''public boolean isPassedSigCheck()
'''
pass
def setPassedSigCheck():
'''public void setPassedSigCheck(final boolean passedSigCheck)
'''
pass
def setAdditionalEventValue():
'''public void setAdditionalEventValue(final String eventValue)
'''
pass
def setAdditionalEvent():
'''public void setAdditionalEvent(final String event)
'''
pass
def setTransformedValue():
'''public void setTransformedValue(final Object transformedValue)
'''
pass
def getTransformedValue():
'''public Object getTransformedValue()
'''
pass
def hasTransformedValue():
'''public boolean hasTransformedValue()
'''
pass
def getParameter():
'''public Object getParameter(final Object key)
'''
pass
def toString():
'''public String toString()
'''
pass
def getLevelCheckedForErrors():
'''public int getLevelCheckedForErrors()
'''
pass
def setLevelCheckedForErrors():
'''public void setLevelCheckedForErrors(final int level)
'''
pass
def conditionalReqChecked():
'''public boolean conditionalReqChecked()
'''
pass
def setConditionalReqChecked():
'''public void setConditionalReqChecked(final boolean conditionalReqChecked)
'''
pass
def getRequestType():
'''public String getRequestType()
'''
pass
def setRequestType():
'''public void setRequestType(final String requestType)
'''
pass
def getEventMap():
'''public Map<String, Object> getEventMap()
'''
pass
def setEventMap():
'''public void setEventMap(final Map<String, Object> eventMap)
'''
pass
def isClientEvent():
'''public boolean isClientEvent()
'''
pass
def setClientEvent():
'''public void setClientEvent(final boolean clientEvent)
'''
pass
