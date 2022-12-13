def get():
    '''public Object get(final Object key)
    '''
def render():
    '''public int render()
    '''
def clearMenus():
    '''public void clearMenus()
    '''
def togglewebreplay():
    '''public int togglewebreplay()
    '''
def showWebReplay():
    '''public int showWebReplay()
    '''
def hideWebReplay():
    '''public int hideWebReplay()
    '''
def put():
    '''public Object put(final Object key, final Object value)
    '''
def remove():
    '''public Object remove(final Object key)
    '''
def setReloadAutoFillInfo():
    '''public void setReloadAutoFillInfo(final boolean bool)
    '''
def shouldReloadAutoFillInfo():
    '''public boolean shouldReloadAutoFillInfo()
    '''
def containsKey():
    '''public boolean containsKey(final Object key)
    '''
def PageInstance():
    '''public PageInstance()
    '''
def initialize():
    '''public void initialize(final WebClientSession wcs, final AppInstance ai, final Element page)
    '''
def addSharedAttributes():
    '''public String addSharedAttributes(final UIERMAttribute ermAttr, final String renderId)
    '''
def getIndexForErmName():
    '''public Integer getIndexForErmName(final UIERMAttribute ermAttr)
    '''
def getAutoFillInfo():
    '''public JSONObject getAutoFillInfo()
    '''
def processTabs():
    '''public void processTabs(final WebClientSession wcs, final Element tabs, final String tabName, final DatasrcInstance parent, final boolean init)
    '''
def isThisTabProcessed():
    '''public boolean isThisTabProcessed(final String tabName)
    '''
def gotoTab():
    '''public int gotoTab(final String tabType)
    '''
def getBeans():
    '''public ArrayList<DataBean> getBeans()
    '''
def getPageId():
    '''public String getPageId()
    '''
def getAppInstance():
    '''public AppInstance getAppInstance()
    '''
def createControlInstances():
    '''public void createControlInstances(final Element element, final ControlInstance parent)
    public void createControlInstances(final Element element, final ControlInstance parent, final int index)
    '''
def createRuntimeControlInstance():
    '''public ControlInstance createRuntimeControlInstance(final String id, final String type, final ControlInstance parent)
    '''
def createDesignerControlInstances():
    '''public void createDesignerControlInstances(final Element element, final ControlInstance parent)
    public String createDesignerControlInstances(final Element element, final ControlInstance parent, final int idx)
    '''
def copyDesignerControlInstances():
    '''public String copyDesignerControlInstances(final ControlInstance original, final ControlInstance parent, final int idx)
    '''
def createControlInstance():
    '''public ControlInstance createControlInstance(final Element element, final ControlInstance parent)
    public ControlInstance createControlInstance(final Element element, final ControlInstance parent, final int index)
    '''
def getControlInstance():
    '''public ControlInstance getControlInstance(final String id)
    '''
def setControlInstance():
    '''public void setControlInstance(final String id, final BaseInstance ci)
    '''
def getComponentInstance():
    '''public ComponentInstance getComponentInstance(final String id)
    '''
def setComponentInstance():
    '''public void setComponentInstance(final String id, final BaseInstance coi)
    '''
def stopFocus():
    '''public void stopFocus()
    '''
def focus():
    '''public boolean focus()
    '''
def focusOnLast():
    '''public void focusOnLast()
    '''
def removeControl():
    '''public boolean removeControl(final String id)
    '''
def setMarkForDesigner():
    '''public void setMarkForDesigner(final boolean flag)
    '''
def cleanup():
    '''public void cleanup()
    '''
def addControlInstanceToIndex():
    '''public void addControlInstanceToIndex(final String id, final ControlInstance controlInst)
    '''
def getMenuHandlerId():
    '''public String getMenuHandlerId()
    '''
def getFocusableList():
    '''public ArrayList<ComponentInstance> getFocusableList()
    '''
def getFocusRenderId():
    '''public String getFocusRenderId()
    public String getFocusRenderId(final boolean last)
    '''
def resetwizard():
    '''public int resetwizard()
    '''
def toggleViewport():
    '''public void toggleViewport()
    '''
def showViewport():
    '''public boolean showViewport()
    '''
def removeAttributeError():
    '''public void removeAttributeError(final ERMAttributeError attributeError)
    '''
def setAttributeError():
    '''public void setAttributeError(final ERMAttributeError attributeError)
    '''
def getErrorLevel():
    '''public int getErrorLevel()
    '''
def addChangedErrorContainer():
    '''public void addChangedErrorContainer(final String id, final String errorType)
    '''
def getChangedErrorContainers():
    '''public Map<String, String> getChangedErrorContainers()
    '''
def clearChangedErrorContainers():
    '''public void clearChangedErrorContainers()
    '''
def addDataStoreForAutoFill():
    '''public void addDataStoreForAutoFill(final DataStoreInfo dataStoreInfo)
    '''
def getPageAutoFillId():
    '''public String getPageAutoFillId()
    '''
def setPageAutoFillId():
    '''public void setPageAutoFillId(final String autoFillId)
    '''
def addDataBeanToSiteOrgList():
    '''public void addDataBeanToSiteOrgList(final DataBean dataBean)
    '''
def setMainTab():
    '''public void setMainTab(final String tabGroupId)
    '''
def getMainTabId():
    '''public String getMainTabId()
    '''
def setDialogDataStores():
    '''public void setDialogDataStores(final List<DataStoreInfo> createdDataStores)
    '''
def getDialogDataStores():
    '''public List<DataStoreInfo> getDialogDataStores()
    '''
def isLookup():
    '''public boolean isLookup()
    '''
def clearFocusContainer():
    '''public void clearFocusContainer()
    '''
