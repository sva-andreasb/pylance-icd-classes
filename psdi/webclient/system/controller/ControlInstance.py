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
def ControlInstance():
    '''public ControlInstance()
    '''
def getAdaptorInstance():
    '''public ControlHandler getAdaptorInstance()
    '''
def getElement():
    '''public Element getElement()
    '''
def initialize():
    '''public void initialize()
    '''
def parseParamvalues():
    '''public Map<String, String> parseParamvalues()
    '''
def setElement():
    '''public void setElement(final Element element)
    '''
def getProperty():
    '''public String getProperty(final String key, final String defaultValue)
    public String getProperty(final String key)
    '''
def getPropertyIgnoreFlags():
    '''public String getPropertyIgnoreFlags(final String key)
    '''
def getOriginalProperty():
    '''public String getOriginalProperty(final String key)
    '''
def findProperty():
    '''public String findProperty(final String key)
    '''
def setPropertyUncle():
    '''public ControlInstance setPropertyUncle(final ControlInstance newUncle)
    '''
def registerDesignerEditedProperty():
    '''public void registerDesignerEditedProperty(final String propName)
    '''
def isDesignerEditedProperty():
    '''public boolean isDesignerEditedProperty(final String propName)
    '''
def isPersistentProperty():
    '''public boolean isPersistentProperty(final String propName)
    '''
def errorLevelChanged():
    '''public boolean errorLevelChanged()
    '''
def hasChanged():
    '''public boolean hasChanged()
    '''
def setChangedFlag():
    '''public void setChangedFlag()
    public void setChangedFlag(final boolean flag)
    '''
def getComponents():
    '''public List<ComponentInstance> getComponents()
    '''
def addComponent():
    '''public void addComponent(final ComponentInstance component)
    '''
def reInitialize():
    '''public void reInitialize()
    '''
def preRender():
    '''public boolean preRender()
    '''
def preRenderChecks():
    '''public void preRenderChecks()
    '''
def render():
    '''public int render()
    '''
def eventCheck():
    '''public void eventCheck()
    '''
def setDisabled():
    '''public void setDisabled(final boolean disabled)
    '''
def hasChildElements():
    '''public boolean hasChildElements()
    '''
def handleEvent():
    '''public int handleEvent(final WebClientEvent event)
    '''
def broadcastEvent():
    '''public int broadcastEvent(final WebClientEvent event)
    '''
def getComponent():
    '''public ComponentInstance getComponent(final String id)
    '''
def renderChildren():
    '''public void renderChildren()
    '''
def setNeedsRender():
    '''public void setNeedsRender(final boolean needsRender)
    '''
def needsRender():
    '''public boolean needsRender()
    '''
def setFocus():
    '''public void setFocus()
    public void setFocus(final String id)
    '''
def setFocusTable():
    '''public void setFocusTable()
    '''
def clearComponent():
    '''public void clearComponent()
    '''
def copy():
    '''public Object copy(final String newId)
    '''
def getDesignerProperty():
    '''public String getDesignerProperty(final String key, final Element el)
    '''
def findDesignerProperty():
    '''public String findDesignerProperty(final String key, final Element el)
    '''
def setTableControl():
    '''public void setTableControl(final Table table)
    '''
def getTableControl():
    '''public Table getTableControl()
    '''
def setOnTableRow():
    '''public void setOnTableRow()
    '''
def setOnTableFilterRow():
    '''public void setOnTableFilterRow()
    '''
def isOnTableFilterRow():
    '''public boolean isOnTableFilterRow()
    '''
def setOnTableTitleRow():
    '''public void setOnTableTitleRow()
    '''
def isOnTableTitleRow():
    '''public boolean isOnTableTitleRow()
    '''
def cleanup():
    '''public void cleanup()
    '''
def isSelected():
    '''public boolean isSelected()
    '''
def setSelected():
    '''public void setSelected(final boolean selected)
    '''
def isVisible():
    '''public boolean isVisible()
    '''
def hasVisibleChildren():
    '''public boolean hasVisibleChildren()
    '''
def isFirstChildVisible():
    '''public boolean isFirstChildVisible()
    '''
def launchexternal():
    '''public int launchexternal()
    '''
def isMasked():
    '''public boolean isMasked()
    '''
def isDisabled():
    '''public boolean isDisabled()
    '''
def setVisibility():
    '''public void setVisibility(final boolean visible)
    '''
def hasMaskedChanged():
    '''public boolean hasMaskedChanged()
    '''
def setGeneratedControl():
    '''public void setGeneratedControl(final ControlInstance generated)
    '''
def getGeneratedControl():
    '''public ControlInstance getGeneratedControl()
    '''
def setOriginalControl():
    '''public void setOriginalControl(final ControlInstance original)
    '''
def getOriginalControl():
    '''public ControlInstance getOriginalControl()
    '''
def setDesignerSelected():
    '''public ControlInstance setDesignerSelected(final boolean selected)
    '''
def getDesignerSelected():
    '''public boolean getDesignerSelected()
    '''
def getDesignerSelectedControl():
    '''public ControlInstance getDesignerSelectedControl()
    '''
def canInsert():
    '''public boolean canInsert(final ControlInstance newControl)
    public boolean canInsert()
    '''
def canRemove():
    '''public boolean canRemove()
    '''
def getDescriptorControl():
    '''public ControlInstance getDescriptorControl()
    '''
def instantiatedatasrc():
    '''public void instantiatedatasrc()
    '''
def isReInitialize():
    '''public boolean isReInitialize()
    '''
def setReInitialize():
    '''public void setReInitialize(final boolean reInitialize)
    '''
def removeChild():
    '''public void removeChild(final ControlInstance child)
    '''
def moveChild():
    '''public void moveChild(final ControlInstance child, int index)
    '''
def isGenerated():
    '''public boolean isGenerated()
    '''
def setGenerated():
    '''public void setGenerated(final boolean generated)
    '''
def addChild():
    '''public void addChild(final ControlInstance child, final int index)
    '''
def getSkipPreRender():
    '''public boolean getSkipPreRender()
    '''
def setSkipPreRender():
    '''public void setSkipPreRender(final boolean skip)
    '''
def resolveParams():
    '''public String resolveParams(String value)
    '''
def resolveParam():
    '''public String resolveParam(String param)
    '''
def walkForId():
    '''public String walkForId(final String baseType)
    public String walkForId(final String baseType, final String prop, final String proValue)
    '''
def quickinsert():
    '''public int quickinsert()
    '''
def isToBeDisplayedOnCurrentTab():
    '''public boolean isToBeDisplayedOnCurrentTab(final String tabDisplay)
    '''
def isToBeDisplayedOnTab():
    '''public static boolean isToBeDisplayedOnTab(final String tabToCheck, String tabDisplay)
    '''
def setBoundComponent():
    '''public void setBoundComponent(final BoundComponentInstance boundComponent)
    '''
def getBoundComponent():
    '''public BoundComponentInstance getBoundComponent()
    '''
def setReRenderFlags():
    '''public void setReRenderFlags()
    '''
def getProperties():
    '''public ControlProperties getProperties()
    '''
def getDataSource():
    '''public String getDataSource()
    '''
def resetDataSource():
    '''public void resetDataSource(final String value)
    '''
def getDataBean():
    '''public DataBean getDataBean()
    '''
def setIncluded():
    '''public void setIncluded()
    public void setIncluded(final boolean included)
    '''
def isIncluded():
    '''public boolean isIncluded()
    '''
def getPropertyUncle():
    '''public ControlInstance getPropertyUncle()
    '''
def isHiddenByLicense():
    '''public boolean isHiddenByLicense()
    '''
def isLastChild():
    '''public boolean isLastChild(final ControlInstance child)
    '''
def setAttributeError():
    '''public void setAttributeError(final UIERMBoundControl boundControl, final ERMAttributeError error)
    '''
def childHasError():
    '''public void childHasError(final BoundComponentInstance childWIthError, final SetValueError newError)
    '''
def getErrorLevel():
    '''public int getErrorLevel()
    '''
def clearErrors():
    '''public void clearErrors()
    '''
def childHasErrorFocus():
    '''public void childHasErrorFocus()
    '''
def setErrorFocusOnControl():
    '''public void setErrorFocusOnControl(final UIERMBoundControl ermControl, final int mboIndex)
    '''
def hasChangedConditionally():
    '''public boolean hasChangedConditionally(final String property)
    '''
def stopRender():
    '''public boolean stopRender()
    '''
def setPropertyOriginator():
    '''public void setPropertyOriginator(final ControlInstance control)
    '''
def getPropertyOriginator():
    '''public ControlInstance getPropertyOriginator()
    '''
def getTakesValueComponent():
    '''public BoundComponentInstance getTakesValueComponent(final String attribute)
    '''
def findComponentByDescriptorId():
    '''public ComponentInstance findComponentByDescriptorId(final String componentId)
    '''
def findUseForLablledByComponent():
    '''public ComponentInstance findUseForLablledByComponent()
    '''
def getRecordHover():
    '''public Element getRecordHover()
    '''
def hasRecordHover():
    '''public boolean hasRecordHover(final ComponentInstance component)
    '''
def isMainrecActionMenu():
    '''public boolean isMainrecActionMenu()
    '''
def createRenderId():
    '''public String createRenderId(final String id, final PageInstance page)
    '''
def isFocusable():
    '''public boolean isFocusable()
    '''
def setFocusable():
    '''public void setFocusable(final boolean focusable)
    '''
def getConditonallyChanged():
    '''public ArrayList<String> getConditonallyChanged()
    '''
