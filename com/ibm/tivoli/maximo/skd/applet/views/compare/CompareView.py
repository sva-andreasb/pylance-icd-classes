PROPERTY_COMPARE_NEW = "String  \"__COMPARE_NEW\""
PROPERTY_COMPARE_MODIFIED = "String  \"__COMPARE_MODIFIED\""
COMPARE_SCENARIOS_EVENT_NAME = "String  \"compare_scenarios\""
def ():
    '''returns Entry\n\n
    (final Viewer viewer)\n
    (final Class viewClass, final String label)\n
    (final IlvHierarchyChart chart1, final IlvHierarchyChart chart2)\n
    (final IlvHierarchyChart chart2, final IlvHierarchyNode node2)\n
    '''
def selectionChanged():
    '''returns None\n\n
    selectionChanged(final SelectionEvent evt)\n
    '''
def currentViewChanged():
    '''returns None\n\n
    currentViewChanged(final CurrentViewChangedEvent event)\n
    '''
def handleMessage():
    '''returns None\n\n
    handleMessage(final String msgId, final Object... args)\n
    handleMessage(final String msgId, final Object... args)\n
    '''
def setAsCurrentView():
    '''returns None\n\n
    setAsCurrentView()\n
    '''
def doInBackground():
    '''returns Void\n\n
    doInBackground()\n
    '''
def runOnUI():
    '''returns None\n\n
    runOnUI(final Void nothing)\n
    '''
def insertUpdate():
    '''returns None\n\n
    insertUpdate(final DocumentEvent e)\n
    '''
def removeUpdate():
    '''returns None\n\n
    removeUpdate(final DocumentEvent e)\n
    '''
def changedUpdate():
    '''returns None\n\n
    changedUpdate(final DocumentEvent e)\n
    '''
def actionPerformed():
    '''returns None\n\n
    actionPerformed(final ActionEvent e)\n
    actionPerformed(final ActionEvent e)\n
    actionPerformed(final ActionEvent e)\n
    actionPerformed(final ActionEvent e)\n
    actionPerformed(final ActionEvent e)\n
    '''
def stateChanged():
    '''returns None\n\n
    stateChanged(final ChangeEvent e)\n
    '''
def componentResized():
    '''returns None\n\n
    componentResized(final ComponentEvent e)\n
    '''
def onSuccess():
    '''returns None\n\n
    onSuccess(final IlvGanttModel data)\n
    '''
def run():
    '''returns None\n\n
    run()\n
    run()\n
    '''
def onError():
    '''returns None\n\n
    onError(final Throwable t)\n
    '''
def performAction():
    '''returns None\n\n
    performAction(final ViewerAbstractAction action, final ActionEvent event)\n
    '''
def getInterval():
    '''returns IlvTimeInterval\n\n
    getInterval(final IlvGanttModel paramIlvGanttModel)\n
    '''
def getSecondaryComponent():
    '''returns JComponent\n\n
    getSecondaryComponent()\n
    '''
def compare():
    '''returns None\n\n
    compare(final String p1id, final String p1name, final String p2id, final String p2name, final Class compareItemType)\n
    '''
def swapCharts():
    '''returns None\n\n
    swapCharts()\n
    '''
def previous():
    '''returns None\n\n
    previous()\n
    '''
def next():
    '''returns None\n\n
    next()\n
    '''
def isChartsLoaded():
    '''returns boolean\n\n
    isChartsLoaded()\n
    '''
def navigate():
    '''returns None\n\n
    navigate(final int dir)\n
    '''
def getNode():
    '''returns Entry\n\n
    getNode(final IlvHierarchyNode node)\n
    '''
def getOtherNode():
    '''returns Entry\n\n
    getOtherNode(final IlvHierarchyNode node)\n
    '''
