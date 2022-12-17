INPUTMODE = "String  \"inputmode\""
DATASOURCE = "String  \"datasrc\""
ONDATACAHNGE = "String  \"ondatachange\""
PARAM_APP = "String  \"app\""
PARAM_PAGE = "String  \"page\""
PARAM_MODULE = "String  \"module\""
PARAM_PARENTCOMPONENT = "String  \"parentcomponent\""
PARAM_PARENTCONTROL = "String  \"parentcontrol\""
PARAM_PRESENTATION = "String  \"presentation\""
PARAM_TABGROUP = "String  \"tabgroup\""
PARAM_TABGROUP_MAIN = "String  \"maintabgroup\""
PARAM_TAB = "String  \"tab\""
PARAM_TABLE = "String  \"table\""
PARAM_APPTABTYPE = "String  \"apptabtype\""
PARAM_USERINFO = "String  \"userinfo.\""
PARAM_DESIGNMODE = "String  \"designmode\""
PARAM_SKINNAME = "String  \"skinname\""
PARAM_MOBILE = "String  \"mobile\""
PARAM_SCREENREADER = "String  \"screenreader\""
PARAM_VERTICALLABEL = "String  \"verticallabel\""
PARAM_LIGHTNING = "String  \"lightningportalmode\""
RERENDER_PROPERTY = "String  \"rerenderenabled\""
def ():
    '''returns ControlInstance\n\n
    ()\n
    '''
def getAdaptorInstance():
    '''returns ControlHandler\n\n
    getAdaptorInstance()\n
    '''
def getElement():
    '''returns Element\n\n
    getElement()\n
    '''
def initialize():
    '''returns None\n\n
    initialize()\n
    '''
def setElement():
    '''returns None\n\n
    setElement(final Element element)\n
    '''
def getProperty():
    '''returns String\n\n
    getProperty(final String key, final String defaultValue)\n
    getProperty(final String key)\n
    '''
def getPropertyIgnoreFlags():
    '''returns String\n\n
    getPropertyIgnoreFlags(final String key)\n
    '''
def getOriginalProperty():
    '''returns String\n\n
    getOriginalProperty(final String key)\n
    '''
def findProperty():
    '''returns String\n\n
    findProperty(final String key)\n
    '''
def setPropertyUncle():
    '''returns ControlInstance\n\n
    setPropertyUncle(final ControlInstance newUncle)\n
    '''
def registerDesignerEditedProperty():
    '''returns None\n\n
    registerDesignerEditedProperty(final String propName)\n
    '''
def isDesignerEditedProperty():
    '''returns boolean\n\n
    isDesignerEditedProperty(final String propName)\n
    '''
def isPersistentProperty():
    '''returns boolean\n\n
    isPersistentProperty(final String propName)\n
    '''
def errorLevelChanged():
    '''returns boolean\n\n
    errorLevelChanged()\n
    '''
def hasChanged():
    '''returns boolean\n\n
    hasChanged()\n
    '''
def setChangedFlag():
    '''returns None\n\n
    setChangedFlag()\n
    setChangedFlag(final boolean flag)\n
    '''
def getComponents():
    '''returns List<ComponentInstance>\n\n
    getComponents()\n
    '''
def addComponent():
    '''returns None\n\n
    addComponent(final ComponentInstance component)\n
    '''
def reInitialize():
    '''returns None\n\n
    reInitialize()\n
    '''
def preRender():
    '''returns boolean\n\n
    preRender()\n
    '''
def preRenderChecks():
    '''returns None\n\n
    preRenderChecks()\n
    '''
def render():
    '''returns int\n\n
    render()\n
    '''
def eventCheck():
    '''returns None\n\n
    eventCheck()\n
    '''
def setDisabled():
    '''returns None\n\n
    setDisabled(final boolean disabled)\n
    '''
def hasChildElements():
    '''returns boolean\n\n
    hasChildElements()\n
    '''
def handleEvent():
    '''returns int\n\n
    handleEvent(final WebClientEvent event)\n
    '''
def broadcastEvent():
    '''returns int\n\n
    broadcastEvent(final WebClientEvent event)\n
    '''
def getComponent():
    '''returns ComponentInstance\n\n
    getComponent(final String id)\n
    '''
def renderChildren():
    '''returns None\n\n
    renderChildren()\n
    '''
def setNeedsRender():
    '''returns None\n\n
    setNeedsRender(final boolean needsRender)\n
    '''
def needsRender():
    '''returns boolean\n\n
    needsRender()\n
    '''
def setFocus():
    '''returns None\n\n
    setFocus()\n
    setFocus(final String id)\n
    '''
def setFocusTable():
    '''returns None\n\n
    setFocusTable()\n
    '''
def clearComponent():
    '''returns None\n\n
    clearComponent()\n
    '''
def copy():
    '''returns Object\n\n
    copy(final String newId)\n
    '''
def getDesignerProperty():
    '''returns String\n\n
    getDesignerProperty(final String key, final Element el)\n
    '''
def findDesignerProperty():
    '''returns String\n\n
    findDesignerProperty(final String key, final Element el)\n
    '''
def setTableControl():
    '''returns None\n\n
    setTableControl(final Table table)\n
    '''
def getTableControl():
    '''returns Table\n\n
    getTableControl()\n
    '''
def setOnTableRow():
    '''returns None\n\n
    setOnTableRow()\n
    '''
def setOnTableFilterRow():
    '''returns None\n\n
    setOnTableFilterRow()\n
    '''
def isOnTableFilterRow():
    '''returns boolean\n\n
    isOnTableFilterRow()\n
    '''
def setOnTableTitleRow():
    '''returns None\n\n
    setOnTableTitleRow()\n
    '''
def isOnTableTitleRow():
    '''returns boolean\n\n
    isOnTableTitleRow()\n
    '''
def cleanup():
    '''returns None\n\n
    cleanup()\n
    '''
def isSelected():
    '''returns boolean\n\n
    isSelected()\n
    '''
def setSelected():
    '''returns None\n\n
    setSelected(final boolean selected)\n
    '''
def isVisible():
    '''returns boolean\n\n
    isVisible()\n
    '''
def hasVisibleChildren():
    '''returns boolean\n\n
    hasVisibleChildren()\n
    '''
def isFirstChildVisible():
    '''returns boolean\n\n
    isFirstChildVisible()\n
    '''
def launchexternal():
    '''returns int\n\n
    launchexternal()\n
    '''
def isMasked():
    '''returns boolean\n\n
    isMasked()\n
    '''
def isDisabled():
    '''returns boolean\n\n
    isDisabled()\n
    '''
def setVisibility():
    '''returns None\n\n
    setVisibility(final boolean visible)\n
    '''
def hasMaskedChanged():
    '''returns boolean\n\n
    hasMaskedChanged()\n
    '''
def setGeneratedControl():
    '''returns None\n\n
    setGeneratedControl(final ControlInstance generated)\n
    '''
def getGeneratedControl():
    '''returns ControlInstance\n\n
    getGeneratedControl()\n
    '''
def setOriginalControl():
    '''returns None\n\n
    setOriginalControl(final ControlInstance original)\n
    '''
def getOriginalControl():
    '''returns ControlInstance\n\n
    getOriginalControl()\n
    '''
def setDesignerSelected():
    '''returns ControlInstance\n\n
    setDesignerSelected(final boolean selected)\n
    '''
def getDesignerSelected():
    '''returns boolean\n\n
    getDesignerSelected()\n
    '''
def getDesignerSelectedControl():
    '''returns ControlInstance\n\n
    getDesignerSelectedControl()\n
    '''
def canInsert():
    '''returns boolean\n\n
    canInsert(final ControlInstance newControl)\n
    canInsert()\n
    '''
def canRemove():
    '''returns boolean\n\n
    canRemove()\n
    '''
def getDescriptorControl():
    '''returns ControlInstance\n\n
    getDescriptorControl()\n
    '''
def instantiatedatasrc():
    '''returns None\n\n
    instantiatedatasrc()\n
    '''
def isReInitialize():
    '''returns boolean\n\n
    isReInitialize()\n
    '''
def setReInitialize():
    '''returns None\n\n
    setReInitialize(final boolean reInitialize)\n
    '''
def removeChild():
    '''returns None\n\n
    removeChild(final ControlInstance child)\n
    '''
def moveChild():
    '''returns None\n\n
    moveChild(final ControlInstance child, int index)\n
    '''
def isGenerated():
    '''returns boolean\n\n
    isGenerated()\n
    '''
def setGenerated():
    '''returns None\n\n
    setGenerated(final boolean generated)\n
    '''
def addChild():
    '''returns None\n\n
    addChild(final ControlInstance child, final int index)\n
    '''
def getSkipPreRender():
    '''returns boolean\n\n
    getSkipPreRender()\n
    '''
def setSkipPreRender():
    '''returns None\n\n
    setSkipPreRender(final boolean skip)\n
    '''
def resolveParams():
    '''returns String\n\n
    resolveParams(String value)\n
    '''
def resolveParam():
    '''returns String\n\n
    resolveParam(String param)\n
    '''
def walkForId():
    '''returns String\n\n
    walkForId(final String baseType)\n
    walkForId(final String baseType, final String prop, final String proValue)\n
    '''
def quickinsert():
    '''returns int\n\n
    quickinsert()\n
    '''
def isToBeDisplayedOnCurrentTab():
    '''returns boolean\n\n
    isToBeDisplayedOnCurrentTab(final String tabDisplay)\n
    '''
def setBoundComponent():
    '''returns None\n\n
    setBoundComponent(final BoundComponentInstance boundComponent)\n
    '''
def getBoundComponent():
    '''returns BoundComponentInstance\n\n
    getBoundComponent()\n
    '''
def setReRenderFlags():
    '''returns None\n\n
    setReRenderFlags()\n
    '''
def getProperties():
    '''returns ControlProperties\n\n
    getProperties()\n
    '''
def getDataSource():
    '''returns String\n\n
    getDataSource()\n
    '''
def resetDataSource():
    '''returns None\n\n
    resetDataSource(final String value)\n
    '''
def getDataBean():
    '''returns DataBean\n\n
    getDataBean()\n
    '''
def setIncluded():
    '''returns None\n\n
    setIncluded()\n
    setIncluded(final boolean included)\n
    '''
def isIncluded():
    '''returns boolean\n\n
    isIncluded()\n
    '''
def getPropertyUncle():
    '''returns ControlInstance\n\n
    getPropertyUncle()\n
    '''
def isHiddenByLicense():
    '''returns boolean\n\n
    isHiddenByLicense()\n
    '''
def isLastChild():
    '''returns boolean\n\n
    isLastChild(final ControlInstance child)\n
    '''
def setAttributeError():
    '''returns None\n\n
    setAttributeError(final UIERMBoundControl boundControl, final ERMAttributeError error)\n
    '''
def childHasError():
    '''returns None\n\n
    childHasError(final BoundComponentInstance childWIthError, final SetValueError newError)\n
    '''
def getErrorLevel():
    '''returns int\n\n
    getErrorLevel()\n
    '''
def clearErrors():
    '''returns None\n\n
    clearErrors()\n
    '''
def childHasErrorFocus():
    '''returns None\n\n
    childHasErrorFocus()\n
    '''
def setErrorFocusOnControl():
    '''returns None\n\n
    setErrorFocusOnControl(final UIERMBoundControl ermControl, final int mboIndex)\n
    '''
def hasChangedConditionally():
    '''returns boolean\n\n
    hasChangedConditionally(final String property)\n
    '''
def stopRender():
    '''returns boolean\n\n
    stopRender()\n
    '''
def setPropertyOriginator():
    '''returns None\n\n
    setPropertyOriginator(final ControlInstance control)\n
    '''
def getPropertyOriginator():
    '''returns ControlInstance\n\n
    getPropertyOriginator()\n
    '''
def getTakesValueComponent():
    '''returns BoundComponentInstance\n\n
    getTakesValueComponent(final String attribute)\n
    '''
def findComponentByDescriptorId():
    '''returns ComponentInstance\n\n
    findComponentByDescriptorId(final String componentId)\n
    '''
def findUseForLablledByComponent():
    '''returns ComponentInstance\n\n
    findUseForLablledByComponent()\n
    '''
def getRecordHover():
    '''returns Element\n\n
    getRecordHover()\n
    '''
def hasRecordHover():
    '''returns boolean\n\n
    hasRecordHover(final ComponentInstance component)\n
    '''
def isMainrecActionMenu():
    '''returns boolean\n\n
    isMainrecActionMenu()\n
    '''
def createRenderId():
    '''returns String\n\n
    createRenderId(final String id, final PageInstance page)\n
    '''
def isFocusable():
    '''returns boolean\n\n
    isFocusable()\n
    '''
def setFocusable():
    '''returns None\n\n
    setFocusable(final boolean focusable)\n
    '''
def getConditonallyChanged():
    '''returns ArrayList<String>\n\n
    getConditonallyChanged()\n
    '''
