PROCESS_EVENT = "int  1"
CANCEL_EVENT = "int  0"
ERROR_CHECKED_NONE = "int  0"
ERROR_CHECKED_PAGE = "int  1"
ERROR_CHECKED_APP = "int  2"
def WebClientEvent():
    '''    public WebClientEvent(final String type, final String targetId, final Object value, final WebClientSession wcs)
    public WebClientEvent(final String type, final String targetId, final Object value, final String row, final WebClientSession wcs)
    public WebClientEvent(final String type, final String targetId, final Object value, final String row, final String additionalEvent, final long uniqueid, final WebClientSession wcs)
    public WebClientEvent(final String type, final String targetId, final Object value, final String row, final String additionalEvent, final String additionalEventValue, final long uniqueid, final WebClientSession wcs)
    public WebClientEvent(final String type, final String targetId, final Object value, final String row, final String additionalEvent, final String additionalEventValue, final long uniqueid, final WebClientSession wcs, final BaseInstance creatingInstance)
    public WebClientEvent(final String type, final String targetId, final Object value, final WebClientSession wcs, final ComponentInstance source)
    public WebClientEvent(final String type, final String targetId, final Object value, final SessionContext sessionContext)
    public WebClientEvent(final String type, final String targetId, final Object value, final String row, final String additionalEvent, final long uniqueid, final SessionContext sessionContext)
    '''
def getSourceControlInstance():
    '''    public ControlInstance getSourceControlInstance()
    '''
def getSourceControl():
    '''    public ControlHandler getSourceControl()
    '''
def setSourceControl():
    '''    public void setSourceControl(final ControlInstance sourceControl)
    public void setSourceControl(final ControlHandler sourceControl)
    '''
def getSourceComponentInstance():
    '''    public ComponentInstance getSourceComponentInstance()
    '''
def setSourceComponent():
    '''    public void setSourceComponent(final ComponentInstance sourceComponent)
    '''
def getType():
    '''    public String getType()
    '''
def getTargetId():
    '''    public String getTargetId()
    '''
def getValue():
    '''    public Object getValue()
    '''
def getRow():
    '''    public int getRow()
    '''
def getValueString():
    '''    public String getValueString()
    '''
def setValue():
    '''    public void setValue(final Object eventvalue)
    '''
def getEventStatus():
    '''    public int getEventStatus()
    '''
def setStatus():
    '''    public void setStatus(final int eventStatus)
    '''
def addParameter():
    '''    public void addParameter(final Object key, final Object value)
    '''
def getParameters():
    '''    public Hashtable<Object, Object> getParameters()
    '''
def getWebClientSession():
    '''    public WebClientSession getWebClientSession()
    '''
def getMessageReturn():
    '''    public int getMessageReturn()
    '''
def setMessageReturn():
    '''    public void setMessageReturn(final int msgReturn)
    '''
def getMessageReturnId():
    '''    public String getMessageReturnId()
    '''
def setMessageReturnId():
    '''    public void setMessageReturnId(final String msgReturnId)
    '''
def wasProcessed():
    '''    public boolean wasProcessed()
    '''
def setProcessed():
    '''    public void setProcessed()
    '''
def getAdditionalEvent():
    '''    public String getAdditionalEvent()
    '''
def getUniqueId():
    '''    public long getUniqueId()
    '''
def getAdditionalEventValue():
    '''    public String getAdditionalEventValue()
    '''
def setRow():
    '''    public void setRow(final int row)
    '''
def getSessionContext():
    '''    public SessionContext getSessionContext()
    '''
def cancelRender():
    '''    public void cancelRender()
    '''
def canRender():
    '''    public boolean canRender()
    '''
def isPassedSigCheck():
    '''    public boolean isPassedSigCheck()
    '''
def setPassedSigCheck():
    '''    public void setPassedSigCheck(final boolean passedSigCheck)
    '''
def setAdditionalEventValue():
    '''    public void setAdditionalEventValue(final String eventValue)
    '''
def setAdditionalEvent():
    '''    public void setAdditionalEvent(final String event)
    '''
def setTransformedValue():
    '''    public void setTransformedValue(final Object transformedValue)
    '''
def getTransformedValue():
    '''    public Object getTransformedValue()
    '''
def hasTransformedValue():
    '''    public boolean hasTransformedValue()
    '''
def getParameter():
    '''    public Object getParameter(final Object key)
    '''
def toString():
    '''    public String toString()
    '''
def getLevelCheckedForErrors():
    '''    public int getLevelCheckedForErrors()
    '''
def setLevelCheckedForErrors():
    '''    public void setLevelCheckedForErrors(final int level)
    '''
def conditionalReqChecked():
    '''    public boolean conditionalReqChecked()
    '''
def setConditionalReqChecked():
    '''    public void setConditionalReqChecked(final boolean conditionalReqChecked)
    '''
def getRequestType():
    '''    public String getRequestType()
    '''
def setRequestType():
    '''    public void setRequestType(final String requestType)
    '''
def getEventMap():
    '''    public Map<String, Object> getEventMap()
    '''
def setEventMap():
    '''    public void setEventMap(final Map<String, Object> eventMap)
    '''
def isClientEvent():
    '''    public boolean isClientEvent()
    '''
def setClientEvent():
    '''    public void setClientEvent(final boolean clientEvent)
    '''
