NOT_CLICKABLE = "int  -1"
CLICKABLE_OFF = "int  0"
CLICKABLE_ON = "int  1"
CONTAINER_WARNING_IMAGE = "String  \"async/container_warning.gif\""
CONTAINER_ERROR_IMAGE = "String  \"async/container_error.gif\""
CONTAINER_WARNING = "String  \"warning\""
CONTAINER_ERROR = "String  \"error\""
def ():
    '''returns ComponentInstance\n\n
    ()\n
    '''
def setControl():
    '''returns None\n\n
    setControl(final ControlInstance control)\n
    '''
def hiddenByProperty():
    '''returns boolean\n\n
    hiddenByProperty()\n
    '''
def initialize():
    '''returns None\n\n
    initialize()\n
    '''
def hiddenByProp():
    '''returns boolean\n\n
    hiddenByProp(final String hideWhen)\n
    '''
def render():
    '''returns int\n\n
    render()\n
    '''
def isHoversActive():
    '''returns boolean\n\n
    isHoversActive()\n
    '''
def setIsHoversActive():
    '''returns None\n\n
    setIsHoversActive(final boolean aBool)\n
    '''
def getControl():
    '''returns ControlInstance\n\n
    getControl()\n
    '''
def renderChildrenControls():
    '''returns None\n\n
    renderChildrenControls()\n
    '''
def renderChildComponents():
    '''returns None\n\n
    renderChildComponents()\n
    '''
def isChild():
    '''returns boolean\n\n
    isChild(final Element child)\n
    '''
def isComponent():
    '''returns boolean\n\n
    isComponent(final Element component)\n
    '''
def hasChildren():
    '''returns boolean\n\n
    hasChildren()\n
    '''
def getChildrenDesignOnly():
    '''returns boolean\n\n
    getChildrenDesignOnly()\n
    '''
def hasChanged():
    '''returns boolean\n\n
    hasChanged()\n
    '''
def rerendering():
    '''returns boolean\n\n
    rerendering()\n
    '''
def needsRender():
    '''returns boolean\n\n
    needsRender()\n
    '''
def broadcastEvent():
    '''returns int\n\n
    broadcastEvent(final WebClientEvent event)\n
    '''
def action():
    '''returns int\n\n
    action()\n
    '''
def query():
    '''returns int\n\n
    query()\n
    '''
def showMenubarMenu():
    '''returns int\n\n
    showMenubarMenu()\n
    '''
def signout():
    '''returns None\n\n
    signout()\n
    '''
def showMenu():
    '''returns int\n\n
    showMenu()\n
    '''
def click():
    '''returns int\n\n
    click()\n
    '''
def canChangeRowFocus():
    '''returns boolean\n\n
    canChangeRowFocus()\n
    '''
def formatLabel():
    '''returns String\n\n
    formatLabel(final String settingKey, final String label)\n
    formatLabel(final String label)\n
    '''
def setLabelFormat():
    '''returns None\n\n
    setLabelFormat(final String settingKey)\n
    '''
def setChangedFlag():
    '''returns None\n\n
    setChangedFlag()\n
    setChangedFlag(final boolean flag)\n
    '''
def clearChangedFlag():
    '''returns None\n\n
    clearChangedFlag()\n
    '''
def setFocus():
    '''returns None\n\n
    setFocus()\n
    '''
def getClickState():
    '''returns int\n\n
    getClickState()\n
    '''
def getProperty():
    '''returns String\n\n
    getProperty(final String key)\n
    '''
def getOriginalProperty():
    '''returns String\n\n
    getOriginalProperty(final String key)\n
    '''
def findProperty():
    '''returns String\n\n
    findProperty(final String key)\n
    '''
def getLinkedComponentInstance():
    '''returns ComponentInstance\n\n
    getLinkedComponentInstance()\n
    '''
def getMenuType():
    '''returns String\n\n
    getMenuType()\n
    '''
def getLookupName():
    '''returns String\n\n
    getLookupName()\n
    '''
def getApplink():
    '''returns String\n\n
    getApplink()\n
    '''
def isOnTableRow():
    '''returns boolean\n\n
    isOnTableRow()\n
    '''
def isOnTableFilterRow():
    '''returns boolean\n\n
    isOnTableFilterRow()\n
    '''
def isOnTableTitleRow():
    '''returns boolean\n\n
    isOnTableTitleRow()\n
    '''
def setComponentContainerId():
    '''returns None\n\n
    setComponentContainerId(final String id)\n
    '''
def getComponentContainerId():
    '''returns String\n\n
    getComponentContainerId()\n
    '''
def cleanup():
    '''returns None\n\n
    cleanup()\n
    '''
def controlPropertyChanged():
    '''returns None\n\n
    controlPropertyChanged(final String property)\n
    '''
def isVisible():
    '''returns boolean\n\n
    isVisible()\n
    '''
def hasLocalProperty():
    '''returns boolean\n\n
    hasLocalProperty(final String key)\n
    '''
def getCssClass():
    '''returns String\n\n
    getCssClass()\n
    '''
def isDefaultRender():
    '''returns boolean\n\n
    isDefaultRender()\n
    '''
def isDisabled():
    '''returns boolean\n\n
    isDisabled()\n
    '''
def isMasked():
    '''returns boolean\n\n
    isMasked()\n
    '''
def hasMaskedChanged():
    '''returns boolean\n\n
    hasMaskedChanged()\n
    '''
def getDesignerSelected():
    '''returns boolean\n\n
    getDesignerSelected()\n
    '''
def skipRender():
    '''returns boolean\n\n
    skipRender()\n
    '''
def getRenderId():
    '''returns String\n\n
    getRenderId()\n
    '''
def getId():
    '''returns String\n\n
    getId()\n
    getId(final boolean useRow)\n
    '''
def getIdWithoutRow():
    '''returns String\n\n
    getIdWithoutRow()\n
    '''
def getDataBean():
    '''returns DataBean\n\n
    getDataBean()\n
    '''
def isIncluded():
    '''returns boolean\n\n
    isIncluded()\n
    '''
def isAsyncEnabled():
    '''returns boolean\n\n
    isAsyncEnabled()\n
    '''
def updateStyle():
    '''returns None\n\n
    updateStyle(final String attribute, final String value)\n
    updateStyle(final String style)\n
    '''
def updateAttribute():
    '''returns None\n\n
    updateAttribute(final String attribute, final String value)\n
    '''
def getUpdatedStyles():
    '''returns JSONArray\n\n
    getUpdatedStyles()\n
    '''
def getUpdatedAttributes():
    '''returns JSONArray\n\n
    getUpdatedAttributes()\n
    '''
def getCurrentUpdates():
    '''returns String\n\n
    getCurrentUpdates()\n
    '''
def hasUnappliedUIUpdates():
    '''returns boolean\n\n
    hasUnappliedUIUpdates()\n
    '''
def clearUIUpdates():
    '''returns None\n\n
    clearUIUpdates()\n
    '''
def getErrorInfo():
    '''returns ContainerErrorInfo\n\n
    getErrorInfo()\n
    '''
def getLabelledByRenderId():
    '''returns String\n\n
    getLabelledByRenderId()\n
    '''
def getLabelForRenderId():
    '''returns String\n\n
    getLabelForRenderId()\n
    '''
def findComponentByDescriptorId():
    '''returns ComponentInstance\n\n
    findComponentByDescriptorId(final String id)\n
    '''
def fetchtooltip():
    '''returns int\n\n
    fetchtooltip()\n
    '''
def getFocusRenderId():
    '''returns String\n\n
    getFocusRenderId()\n
    '''
