NOT_CLICKABLE = "int  -1"
CLICKABLE_OFF = "int  0"
CLICKABLE_ON = "int  1"
CONTAINER_WARNING_IMAGE = "String  \"async/container_warning.gif\""
CONTAINER_ERROR_IMAGE = "String  \"async/container_error.gif\""
CONTAINER_WARNING = "String  \"warning\""
CONTAINER_ERROR = "String  \"error\""
def ComponentInstance():
    '''public ComponentInstance()
    '''
def setControl():
    '''public void setControl(final ControlInstance control)
    '''
def hiddenByProperty():
    '''public boolean hiddenByProperty()
    '''
def initialize():
    '''public void initialize()
    '''
def hiddenByProp():
    '''public boolean hiddenByProp(final String hideWhen)
    '''
def getCurrent():
    '''public static ComponentInstance getCurrent(final ServletRequest request)
    '''
def render():
    '''public int render()
    '''
def isHoversActive():
    '''public boolean isHoversActive()
    '''
def setIsHoversActive():
    '''public void setIsHoversActive(final boolean aBool)
    '''
def getControl():
    '''public ControlInstance getControl()
    '''
def renderChildrenControls():
    '''public void renderChildrenControls()
    '''
def renderChildComponents():
    '''public void renderChildComponents()
    '''
def isChild():
    '''public boolean isChild(final Element child)
    '''
def isComponent():
    '''public boolean isComponent(final Element component)
    '''
def hasChildren():
    '''public boolean hasChildren()
    '''
def hasComponents():
    '''public synchronized boolean hasComponents()
    '''
def getChildrenDesignOnly():
    '''public boolean getChildrenDesignOnly()
    '''
def hasChanged():
    '''public boolean hasChanged()
    '''
def rerendering():
    '''public boolean rerendering()
    '''
def needsRender():
    '''public boolean needsRender()
    '''
def broadcastEvent():
    '''public int broadcastEvent(final WebClientEvent event)
    '''
def action():
    '''public int action()
    '''
def query():
    '''public int query()
    '''
def showMenubarMenu():
    '''public int showMenubarMenu()
    '''
def signout():
    '''public void signout()
    '''
def showMenu():
    '''public int showMenu()
    '''
def click():
    '''public int click()
    '''
def canChangeRowFocus():
    '''public boolean canChangeRowFocus()
    '''
def formatLabel():
    '''public String formatLabel(final String settingKey, final String label)
    public String formatLabel(final String label)
    '''
def setLabelFormat():
    '''public void setLabelFormat(final String settingKey)
    '''
def setChangedFlag():
    '''public void setChangedFlag()
    public void setChangedFlag(final boolean flag)
    '''
def clearChangedFlag():
    '''public void clearChangedFlag()
    '''
def setFocus():
    '''public void setFocus()
    '''
def getClickState():
    '''public int getClickState()
    '''
def getProperty():
    '''public String getProperty(final String key)
    '''
def getOriginalProperty():
    '''public String getOriginalProperty(final String key)
    '''
def findProperty():
    '''public String findProperty(final String key)
    '''
def getLinkedComponentInstance():
    '''public ComponentInstance getLinkedComponentInstance()
    '''
def getMenuType():
    '''public String getMenuType()
    '''
def getLookupName():
    '''public String getLookupName()
    '''
def getApplink():
    '''public String getApplink()
    '''
def isOnTableRow():
    '''public boolean isOnTableRow()
    '''
def isOnTableFilterRow():
    '''public boolean isOnTableFilterRow()
    '''
def isOnTableTitleRow():
    '''public boolean isOnTableTitleRow()
    '''
def setComponentContainerId():
    '''public void setComponentContainerId(final String id)
    '''
def getComponentContainerId():
    '''public String getComponentContainerId()
    '''
def cleanup():
    '''public void cleanup()
    '''
def controlPropertyChanged():
    '''public void controlPropertyChanged(final String property)
    '''
def isVisible():
    '''public boolean isVisible()
    '''
def hasLocalProperty():
    '''public boolean hasLocalProperty(final String key)
    '''
def getCssClass():
    '''public String getCssClass()
    '''
def isDefaultRender():
    '''public boolean isDefaultRender()
    '''
def isDisabled():
    '''public boolean isDisabled()
    '''
def isMasked():
    '''public boolean isMasked()
    '''
def hasMaskedChanged():
    '''public boolean hasMaskedChanged()
    '''
def getDesignerSelected():
    '''public boolean getDesignerSelected()
    '''
def skipRender():
    '''public boolean skipRender()
    '''
def getRenderId():
    '''public String getRenderId()
    '''
def getId():
    '''public String getId()
    public String getId(final boolean useRow)
    '''
def getIdWithoutRow():
    '''public String getIdWithoutRow()
    '''
def getDataBean():
    '''public DataBean getDataBean()
    '''
def isIncluded():
    '''public boolean isIncluded()
    '''
def isAsyncEnabled():
    '''public boolean isAsyncEnabled()
    '''
def updateStyle():
    '''public void updateStyle(final String attribute, final String value)
    public void updateStyle(final String style)
    '''
def updateAttribute():
    '''public void updateAttribute(final String attribute, final String value)
    '''
def getUpdatedStyles():
    '''public JSONArray getUpdatedStyles()
    '''
def getUpdatedAttributes():
    '''public JSONArray getUpdatedAttributes()
    '''
def getCurrentUpdates():
    '''public String getCurrentUpdates()
    '''
def hasUnappliedUIUpdates():
    '''public boolean hasUnappliedUIUpdates()
    '''
def clearUIUpdates():
    '''public void clearUIUpdates()
    '''
def getErrorInfo():
    '''public ContainerErrorInfo getErrorInfo()
    '''
def getLabelledByRenderId():
    '''public String getLabelledByRenderId()
    '''
def getLabelForRenderId():
    '''public String getLabelForRenderId()
    '''
def findComponentByDescriptorId():
    '''public ComponentInstance findComponentByDescriptorId(final String id)
    '''
def fetchtooltip():
    '''public int fetchtooltip()
    '''
def getFocusRenderId():
    '''public String getFocusRenderId()
    '''
