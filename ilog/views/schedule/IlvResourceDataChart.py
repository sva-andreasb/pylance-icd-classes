AUTO_RESOURCE_DISPLAY_DISABLED = "int  -1"
DISPLAY_SELECTED_RESOURCES = "int  0"
DISPLAY_SELECTED_SUBTREES = "int  1"
DISPLAY_SELECTED_LEAVES = "int  2"
DISPLAY_ALL_RESOURCES = "int  3"
DISPLAY_ALL_LEAVES = "int  4"
def ():
    '''returns ModelForDataSets\n\n
    (final IlvReservationDataPolicy a)\n
    ()\n
    (final IlvScheduleChart ilvScheduleChart, final IlvResourceDataChart ilvResourceDataChart, final int n)\n
    (final IlvGanttModel ilvGanttModel)\n
    '''
def getReservationDataPolicy():
    '''returns IlvReservationDataPolicy\n\n
    getReservationDataPolicy()\n
    '''
def setReservationDataPolicy():
    '''returns None\n\n
    setReservationDataPolicy(final IlvReservationDataPolicy a)\n
    '''
def syncGanttModel():
    '''returns None\n\n
    syncGanttModel(final IlvScheduleChart ilvScheduleChart)\n
    syncGanttModel(final IlvScheduleChart c, final int resourceDisplayMode)\n
    '''
def unsyncGanttModel():
    '''returns None\n\n
    unsyncGanttModel()\n
    '''
def getResourceDisplayMode():
    '''returns int\n\n
    getResourceDisplayMode()\n
    '''
def setResourceDisplayMode():
    '''returns None\n\n
    setResourceDisplayMode(final int f)\n
    '''
def isDisplayed():
    '''returns boolean\n\n
    isDisplayed(final IlvResource ilvResource)\n
    '''
def createDataSet():
    '''returns IlvResourceDataSet\n\n
    createDataSet(final IlvResource ilvResource, final IlvReservationDataPolicy ilvReservationDataPolicy)\n
    '''
def displayResource():
    '''returns None\n\n
    displayResource(final IlvResource ilvResource, final boolean b)\n
    '''
def clearAllDisplayedResources():
    '''returns None\n\n
    clearAllDisplayedResources()\n
    '''
def displayedResourcesIterator():
    '''returns Iterator<IlvResource>\n\n
    displayedResourcesIterator()\n
    '''
def connect():
    '''returns None\n\n
    connect(final IlvScheduleChart b, final IlvResourceDataChart a, final int c)\n
    '''
def disconnect():
    '''returns None\n\n
    disconnect()\n
    '''
def selectionChanged():
    '''returns None\n\n
    selectionChanged(final SelectionEvent selectionEvent)\n
    '''
def resourcesRemoved():
    '''returns None\n\n
    resourcesRemoved(final ResourcesRemovedEvent resourcesRemovedEvent)\n
    '''
def resourcesInserted():
    '''returns None\n\n
    resourcesInserted(final ResourcesInsertedEvent resourcesInsertedEvent)\n
    '''
def resourceMoved():
    '''returns None\n\n
    resourceMoved(final ResourceMovedEvent resourceMovedEvent)\n
    '''
def dispose():
    '''returns None\n\n
    dispose()\n
    '''
def reservationIterator():
    '''returns Iterator<IlvReservation>\n\n
    reservationIterator(final IlvActivity ilvActivity, final IlvResource ilvResource)\n
    '''
def hasReservation():
    '''returns boolean\n\n
    hasReservation(final IlvActivity ilvActivity, final IlvResource ilvResource)\n
    '''
def fireActivityEvent():
    '''returns None\n\n
    fireActivityEvent(final ActivityEvent activityEvent)\n
    '''
