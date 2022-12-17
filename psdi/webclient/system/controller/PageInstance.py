def get():
    '''returns Object\n\n
    get(final Object key)\n
    '''
def render():
    '''returns int\n\n
    render()\n
    '''
def clearMenus():
    '''returns None\n\n
    clearMenus()\n
    '''
def togglewebreplay():
    '''returns int\n\n
    togglewebreplay()\n
    '''
def showWebReplay():
    '''returns int\n\n
    showWebReplay()\n
    '''
def hideWebReplay():
    '''returns int\n\n
    hideWebReplay()\n
    '''
def put():
    '''returns Object\n\n
    put(final Object key, final Object value)\n
    '''
def remove():
    '''returns Object\n\n
    remove(final Object key)\n
    '''
def setReloadAutoFillInfo():
    '''returns None\n\n
    setReloadAutoFillInfo(final boolean bool)\n
    '''
def shouldReloadAutoFillInfo():
    '''returns boolean\n\n
    shouldReloadAutoFillInfo()\n
    '''
def containsKey():
    '''returns boolean\n\n
    containsKey(final Object key)\n
    '''
def ():
    '''returns PageInstance\n\n
    ()\n
    '''
def initialize():
    '''returns None\n\n
    initialize(final WebClientSession wcs, final AppInstance ai, final Element page)\n
    '''
def addSharedAttributes():
    '''returns String\n\n
    addSharedAttributes(final UIERMAttribute ermAttr, final String renderId)\n
    '''
def getIndexForErmName():
    '''returns Integer\n\n
    getIndexForErmName(final UIERMAttribute ermAttr)\n
    '''
def getAutoFillInfo():
    '''returns JSONObject\n\n
    getAutoFillInfo()\n
    '''
def processTabs():
    '''returns None\n\n
    processTabs(final WebClientSession wcs, final Element tabs, final String tabName, final DatasrcInstance parent, final boolean init)\n
    '''
def isThisTabProcessed():
    '''returns boolean\n\n
    isThisTabProcessed(final String tabName)\n
    '''
def gotoTab():
    '''returns int\n\n
    gotoTab(final String tabType)\n
    '''
def getBeans():
    '''returns ArrayList<DataBean>\n\n
    getBeans()\n
    '''
def getPageId():
    '''returns String\n\n
    getPageId()\n
    '''
def getAppInstance():
    '''returns AppInstance\n\n
    getAppInstance()\n
    '''
def createControlInstances():
    '''returns None\n\n
    createControlInstances(final Element element, final ControlInstance parent)\n
    createControlInstances(final Element element, final ControlInstance parent, final int index)\n
    '''
def createRuntimeControlInstance():
    '''returns ControlInstance\n\n
    createRuntimeControlInstance(final String id, final String type, final ControlInstance parent)\n
    '''
def createDesignerControlInstances():
    '''returns String\n\n
    createDesignerControlInstances(final Element element, final ControlInstance parent)\n
    createDesignerControlInstances(final Element element, final ControlInstance parent, final int idx)\n
    '''
def copyDesignerControlInstances():
    '''returns String\n\n
    copyDesignerControlInstances(final ControlInstance original, final ControlInstance parent, final int idx)\n
    '''
def createControlInstance():
    '''returns ControlInstance\n\n
    createControlInstance(final Element element, final ControlInstance parent)\n
    createControlInstance(final Element element, final ControlInstance parent, final int index)\n
    '''
def getControlInstance():
    '''returns ControlInstance\n\n
    getControlInstance(final String id)\n
    '''
def setControlInstance():
    '''returns None\n\n
    setControlInstance(final String id, final BaseInstance ci)\n
    '''
def getComponentInstance():
    '''returns ComponentInstance\n\n
    getComponentInstance(final String id)\n
    '''
def setComponentInstance():
    '''returns None\n\n
    setComponentInstance(final String id, final BaseInstance coi)\n
    '''
def stopFocus():
    '''returns None\n\n
    stopFocus()\n
    '''
def focus():
    '''returns boolean\n\n
    focus()\n
    '''
def focusOnLast():
    '''returns None\n\n
    focusOnLast()\n
    '''
def removeControl():
    '''returns boolean\n\n
    removeControl(final String id)\n
    '''
def setMarkForDesigner():
    '''returns None\n\n
    setMarkForDesigner(final boolean flag)\n
    '''
def cleanup():
    '''returns None\n\n
    cleanup()\n
    '''
def addControlInstanceToIndex():
    '''returns None\n\n
    addControlInstanceToIndex(final String id, final ControlInstance controlInst)\n
    '''
def getMenuHandlerId():
    '''returns String\n\n
    getMenuHandlerId()\n
    '''
def getFocusableList():
    '''returns ArrayList<ComponentInstance>\n\n
    getFocusableList()\n
    '''
def getFocusRenderId():
    '''returns String\n\n
    getFocusRenderId()\n
    getFocusRenderId(final boolean last)\n
    '''
def resetwizard():
    '''returns int\n\n
    resetwizard()\n
    '''
def toggleViewport():
    '''returns None\n\n
    toggleViewport()\n
    '''
def showViewport():
    '''returns boolean\n\n
    showViewport()\n
    '''
def removeAttributeError():
    '''returns None\n\n
    removeAttributeError(final ERMAttributeError attributeError)\n
    '''
def setAttributeError():
    '''returns None\n\n
    setAttributeError(final ERMAttributeError attributeError)\n
    '''
def getErrorLevel():
    '''returns int\n\n
    getErrorLevel()\n
    '''
def addChangedErrorContainer():
    '''returns None\n\n
    addChangedErrorContainer(final String id, final String errorType)\n
    '''
def clearChangedErrorContainers():
    '''returns None\n\n
    clearChangedErrorContainers()\n
    '''
def addDataStoreForAutoFill():
    '''returns None\n\n
    addDataStoreForAutoFill(final DataStoreInfo dataStoreInfo)\n
    '''
def getPageAutoFillId():
    '''returns String\n\n
    getPageAutoFillId()\n
    '''
def setPageAutoFillId():
    '''returns None\n\n
    setPageAutoFillId(final String autoFillId)\n
    '''
def addDataBeanToSiteOrgList():
    '''returns None\n\n
    addDataBeanToSiteOrgList(final DataBean dataBean)\n
    '''
def setMainTab():
    '''returns None\n\n
    setMainTab(final String tabGroupId)\n
    '''
def getMainTabId():
    '''returns String\n\n
    getMainTabId()\n
    '''
def setDialogDataStores():
    '''returns None\n\n
    setDialogDataStores(final List<DataStoreInfo> createdDataStores)\n
    '''
def getDialogDataStores():
    '''returns List<DataStoreInfo>\n\n
    getDialogDataStores()\n
    '''
def isLookup():
    '''returns boolean\n\n
    isLookup()\n
    '''
def clearFocusContainer():
    '''returns None\n\n
    clearFocusContainer()\n
    '''
