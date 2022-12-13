INPUTMODE = "String  inputmode""
DATASOURCE = "String  datasrc""
ONDATACAHNGE = "String  ondatachange""
PARAM_APP = "String  app""
PARAM_PAGE = "String  page""
PARAM_MODULE = "String  module""
PARAM_PARENTCOMPONENT = "String  parentcomponent""
PARAM_PARENTCONTROL = "String  parentcontrol""
PARAM_PRESENTATION = "String  presentation""
PARAM_TABGROUP = "String  tabgroup""
PARAM_TABGROUP_MAIN = "String  maintabgroup""
PARAM_TAB = "String  tab""
PARAM_TABLE = "String  table""
PARAM_APPTABTYPE = "String  apptabtype""
PARAM_USERINFO = "String  userinfo.""
PARAM_DESIGNMODE = "String  designmode""
PARAM_SKINNAME = "String  skinname""
PARAM_MOBILE = "String  mobile""
PARAM_SCREENREADER = "String  screenreader""
PARAM_VERTICALLABEL = "String  verticallabel""
PARAM_LIGHTNING = "String  lightningportalmode""
RERENDER_PROPERTY = "String  rerenderenabled""
def ControlInstance():
'''public ControlInstance()
'''
pass
def getAdaptorInstance():
'''public ControlHandler getAdaptorInstance()
'''
pass
def getElement():
'''public Element getElement()
'''
pass
def initialize():
'''public void initialize()
'''
pass
def parseParamvalues():
'''public Map<String, String> parseParamvalues()
'''
pass
def setElement():
'''public void setElement(final Element element)
'''
pass
def getProperty():
'''public String getProperty(final String key, final String defaultValue)
public String getProperty(final String key)
'''
pass
def getPropertyIgnoreFlags():
'''public String getPropertyIgnoreFlags(final String key)
'''
pass
def getOriginalProperty():
'''public String getOriginalProperty(final String key)
'''
pass
def findProperty():
'''public String findProperty(final String key)
'''
pass
def setPropertyUncle():
'''public ControlInstance setPropertyUncle(final ControlInstance newUncle)
'''
pass
def registerDesignerEditedProperty():
'''public void registerDesignerEditedProperty(final String propName)
'''
pass
def isDesignerEditedProperty():
'''public boolean isDesignerEditedProperty(final String propName)
'''
pass
def isPersistentProperty():
'''public boolean isPersistentProperty(final String propName)
'''
pass
def errorLevelChanged():
'''public boolean errorLevelChanged()
'''
pass
def hasChanged():
'''public boolean hasChanged()
'''
pass
def setChangedFlag():
'''public void setChangedFlag()
public void setChangedFlag(final boolean flag)
'''
pass
def getComponents():
'''public List<ComponentInstance> getComponents()
'''
pass
def addComponent():
'''public void addComponent(final ComponentInstance component)
'''
pass
def reInitialize():
'''public void reInitialize()
'''
pass
def preRender():
'''public boolean preRender()
'''
pass
def preRenderChecks():
'''public void preRenderChecks()
'''
pass
def render():
'''public int render()
'''
pass
def eventCheck():
'''public void eventCheck()
'''
pass
def setDisabled():
'''public void setDisabled(final boolean disabled)
'''
pass
def hasChildElements():
'''public boolean hasChildElements()
'''
pass
def handleEvent():
'''public int handleEvent(final WebClientEvent event)
'''
pass
def broadcastEvent():
'''public int broadcastEvent(final WebClientEvent event)
'''
pass
def getComponent():
'''public ComponentInstance getComponent(final String id)
'''
pass
def renderChildren():
'''public void renderChildren()
'''
pass
def setNeedsRender():
'''public void setNeedsRender(final boolean needsRender)
'''
pass
def needsRender():
'''public boolean needsRender()
'''
pass
def setFocus():
'''public void setFocus()
public void setFocus(final String id)
'''
pass
def setFocusTable():
'''public void setFocusTable()
'''
pass
def clearComponent():
'''public void clearComponent()
'''
pass
def copy():
'''public Object copy(final String newId)
'''
pass
def getDesignerProperty():
'''public String getDesignerProperty(final String key, final Element el)
'''
pass
def findDesignerProperty():
'''public String findDesignerProperty(final String key, final Element el)
'''
pass
def setTableControl():
'''public void setTableControl(final Table table)
'''
pass
def getTableControl():
'''public Table getTableControl()
'''
pass
def setOnTableRow():
'''public void setOnTableRow()
'''
pass
def setOnTableFilterRow():
'''public void setOnTableFilterRow()
'''
pass
def isOnTableFilterRow():
'''public boolean isOnTableFilterRow()
'''
pass
def setOnTableTitleRow():
'''public void setOnTableTitleRow()
'''
pass
def isOnTableTitleRow():
'''public boolean isOnTableTitleRow()
'''
pass
def cleanup():
'''public void cleanup()
'''
pass
def isSelected():
'''public boolean isSelected()
'''
pass
def setSelected():
'''public void setSelected(final boolean selected)
'''
pass
def isVisible():
'''public boolean isVisible()
'''
pass
def hasVisibleChildren():
'''public boolean hasVisibleChildren()
'''
pass
def isFirstChildVisible():
'''public boolean isFirstChildVisible()
'''
pass
def launchexternal():
'''public int launchexternal()
'''
pass
def isMasked():
'''public boolean isMasked()
'''
pass
def isDisabled():
'''public boolean isDisabled()
'''
pass
def setVisibility():
'''public void setVisibility(final boolean visible)
'''
pass
def hasMaskedChanged():
'''public boolean hasMaskedChanged()
'''
pass
def setGeneratedControl():
'''public void setGeneratedControl(final ControlInstance generated)
'''
pass
def getGeneratedControl():
'''public ControlInstance getGeneratedControl()
'''
pass
def setOriginalControl():
'''public void setOriginalControl(final ControlInstance original)
'''
pass
def getOriginalControl():
'''public ControlInstance getOriginalControl()
'''
pass
def setDesignerSelected():
'''public ControlInstance setDesignerSelected(final boolean selected)
'''
pass
def getDesignerSelected():
'''public boolean getDesignerSelected()
'''
pass
def getDesignerSelectedControl():
'''public ControlInstance getDesignerSelectedControl()
'''
pass
def canInsert():
'''public boolean canInsert(final ControlInstance newControl)
public boolean canInsert()
'''
pass
def canRemove():
'''public boolean canRemove()
'''
pass
def getDescriptorControl():
'''public ControlInstance getDescriptorControl()
'''
pass
def instantiatedatasrc():
'''public void instantiatedatasrc()
'''
pass
def isReInitialize():
'''public boolean isReInitialize()
'''
pass
def setReInitialize():
'''public void setReInitialize(final boolean reInitialize)
'''
pass
def removeChild():
'''public void removeChild(final ControlInstance child)
'''
pass
def moveChild():
'''public void moveChild(final ControlInstance child, int index)
'''
pass
def isGenerated():
'''public boolean isGenerated()
'''
pass
def setGenerated():
'''public void setGenerated(final boolean generated)
'''
pass
def addChild():
'''public void addChild(final ControlInstance child, final int index)
'''
pass
def getSkipPreRender():
'''public boolean getSkipPreRender()
'''
pass
def setSkipPreRender():
'''public void setSkipPreRender(final boolean skip)
'''
pass
def resolveParams():
'''public String resolveParams(String value)
'''
pass
def resolveParam():
'''public String resolveParam(String param)
'''
pass
def walkForId():
'''public String walkForId(final String baseType)
public String walkForId(final String baseType, final String prop, final String proValue)
'''
pass
def quickinsert():
'''public int quickinsert()
'''
pass
def isToBeDisplayedOnCurrentTab():
'''public boolean isToBeDisplayedOnCurrentTab(final String tabDisplay)
'''
pass
def isToBeDisplayedOnTab():
'''public static boolean isToBeDisplayedOnTab(final String tabToCheck, String tabDisplay)
'''
pass
def setBoundComponent():
'''public void setBoundComponent(final BoundComponentInstance boundComponent)
'''
pass
def getBoundComponent():
'''public BoundComponentInstance getBoundComponent()
'''
pass
def setReRenderFlags():
'''public void setReRenderFlags()
'''
pass
def getProperties():
'''public ControlProperties getProperties()
'''
pass
def getDataSource():
'''public String getDataSource()
'''
pass
def resetDataSource():
'''public void resetDataSource(final String value)
'''
pass
def getDataBean():
'''public DataBean getDataBean()
'''
pass
def setIncluded():
'''public void setIncluded()
public void setIncluded(final boolean included)
'''
pass
def isIncluded():
'''public boolean isIncluded()
'''
pass
def getPropertyUncle():
'''public ControlInstance getPropertyUncle()
'''
pass
def isHiddenByLicense():
'''public boolean isHiddenByLicense()
'''
pass
def isLastChild():
'''public boolean isLastChild(final ControlInstance child)
'''
pass
def setAttributeError():
'''public void setAttributeError(final UIERMBoundControl boundControl, final ERMAttributeError error)
'''
pass
def childHasError():
'''public void childHasError(final BoundComponentInstance childWIthError, final SetValueError newError)
'''
pass
def getErrorLevel():
'''public int getErrorLevel()
'''
pass
def clearErrors():
'''public void clearErrors()
'''
pass
def childHasErrorFocus():
'''public void childHasErrorFocus()
'''
pass
def setErrorFocusOnControl():
'''public void setErrorFocusOnControl(final UIERMBoundControl ermControl, final int mboIndex)
'''
pass
def hasChangedConditionally():
'''public boolean hasChangedConditionally(final String property)
'''
pass
def stopRender():
'''public boolean stopRender()
'''
pass
def setPropertyOriginator():
'''public void setPropertyOriginator(final ControlInstance control)
'''
pass
def getPropertyOriginator():
'''public ControlInstance getPropertyOriginator()
'''
pass
def getTakesValueComponent():
'''public BoundComponentInstance getTakesValueComponent(final String attribute)
'''
pass
def findComponentByDescriptorId():
'''public ComponentInstance findComponentByDescriptorId(final String componentId)
'''
pass
def findUseForLablledByComponent():
'''public ComponentInstance findUseForLablledByComponent()
'''
pass
def getRecordHover():
'''public Element getRecordHover()
'''
pass
def hasRecordHover():
'''public boolean hasRecordHover(final ComponentInstance component)
'''
pass
def isMainrecActionMenu():
'''public boolean isMainrecActionMenu()
'''
pass
def createRenderId():
'''public String createRenderId(final String id, final PageInstance page)
'''
pass
def isFocusable():
'''public boolean isFocusable()
'''
pass
def setFocusable():
'''public void setFocusable(final boolean focusable)
'''
pass
def getConditonallyChanged():
'''public ArrayList<String> getConditonallyChanged()
'''
pass
