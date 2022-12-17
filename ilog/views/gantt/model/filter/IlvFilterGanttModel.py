def ():
    '''returns GanttModelPropertyEventHandler\n\n
    ()\n
    (final IlvGanttModel filteredModel)\n
    ()\n
    ()\n
    ()\n
    ()\n
    ()\n
    ()\n
    ()\n
    '''
def setFilteredModel():
    '''returns None\n\n
    setFilteredModel(final IlvGanttModel a)\n
    '''
def getFilteredModel():
    '''returns IlvGanttModel\n\n
    getFilteredModel()\n
    '''
def setAdjusting():
    '''returns None\n\n
    setAdjusting(final boolean adjusting)\n
    '''
def isAdjusting():
    '''returns boolean\n\n
    isAdjusting()\n
    '''
def setBatching():
    '''returns None\n\n
    setBatching(final boolean batching)\n
    '''
def isBatching():
    '''returns boolean\n\n
    isBatching()\n
    '''
def fireActivityEvent():
    '''returns None\n\n
    fireActivityEvent(final ActivityEvent activityEvent)\n
    '''
def fireResourceEvent():
    '''returns None\n\n
    fireResourceEvent(final ResourceEvent resourceEvent)\n
    '''
def contains():
    '''returns boolean\n\n
    contains(final IlvHierarchyNode ilvHierarchyNode)\n
    contains(final IlvConstraint ilvConstraint)\n
    contains(final IlvReservation ilvReservation)\n
    '''
def getRootActivity():
    '''returns IlvActivity\n\n
    getRootActivity()\n
    '''
def setRootActivity():
    '''returns None\n\n
    setRootActivity(final IlvActivity rootActivity)\n
    '''
def getParentActivity():
    '''returns IlvActivity\n\n
    getParentActivity(final IlvActivity ilvActivity)\n
    '''
def getParentActivityIndex():
    '''returns int\n\n
    getParentActivityIndex(final IlvActivity ilvActivity)\n
    '''
def getChildActivityCount():
    '''returns int\n\n
    getChildActivityCount(final IlvActivity ilvActivity)\n
    '''
def getChildActivity():
    '''returns IlvActivity\n\n
    getChildActivity(final IlvActivity ilvActivity, final int n)\n
    '''
def getChildActivityIndex():
    '''returns int\n\n
    getChildActivityIndex(final IlvActivity ilvActivity, final IlvActivity ilvActivity2)\n
    '''
def addActivity():
    '''returns None\n\n
    addActivity(final IlvActivity ilvActivity, final IlvActivity ilvActivity2, final int n)\n
    '''
def removeActivity():
    '''returns None\n\n
    removeActivity(final IlvActivity ilvActivity, final int n)\n
    removeActivity(final IlvActivity ilvActivity)\n
    '''
def moveActivity():
    '''returns None\n\n
    moveActivity(final IlvActivity ilvActivity, final IlvActivity ilvActivity2, final int n)\n
    '''
def getRootResource():
    '''returns IlvResource\n\n
    getRootResource()\n
    '''
def setRootResource():
    '''returns None\n\n
    setRootResource(final IlvResource rootResource)\n
    '''
def getParentResource():
    '''returns IlvResource\n\n
    getParentResource(final IlvResource ilvResource)\n
    '''
def getParentResourceIndex():
    '''returns int\n\n
    getParentResourceIndex(final IlvResource ilvResource)\n
    '''
def getChildResourceCount():
    '''returns int\n\n
    getChildResourceCount(final IlvResource ilvResource)\n
    '''
def getChildResource():
    '''returns IlvResource\n\n
    getChildResource(final IlvResource ilvResource, final int n)\n
    '''
def getChildResourceIndex():
    '''returns int\n\n
    getChildResourceIndex(final IlvResource ilvResource, final IlvResource ilvResource2)\n
    '''
def addResource():
    '''returns None\n\n
    addResource(final IlvResource ilvResource, final IlvResource ilvResource2, final int n)\n
    '''
def removeResource():
    '''returns None\n\n
    removeResource(final IlvResource ilvResource, final int n)\n
    removeResource(final IlvResource ilvResource)\n
    '''
def moveResource():
    '''returns None\n\n
    moveResource(final IlvResource ilvResource, final IlvResource ilvResource2, final int n)\n
    '''
def constraintIterator():
    '''returns Iterator<IlvConstraint>\n\n
    constraintIterator()\n
    '''
def constraintIteratorFromActivity():
    '''returns Iterator<IlvConstraint>\n\n
    constraintIteratorFromActivity(final IlvActivity ilvActivity)\n
    '''
def constraintIteratorToActivity():
    '''returns Iterator<IlvConstraint>\n\n
    constraintIteratorToActivity(final IlvActivity ilvActivity)\n
    '''
def addConstraint():
    '''returns None\n\n
    addConstraint(final IlvConstraint ilvConstraint)\n
    '''
def removeConstraint():
    '''returns None\n\n
    removeConstraint(final IlvConstraint ilvConstraint)\n
    '''
def reservationIterator():
    '''returns Iterator<IlvReservation>\n\n
    reservationIterator()\n
    reservationIterator(final IlvActivity ilvActivity)\n
    reservationIterator(final IlvResource ilvResource)\n
    reservationIterator(final IlvResource ilvResource, final IlvTimeInterval ilvTimeInterval)\n
    '''
def addReservation():
    '''returns None\n\n
    addReservation(final IlvReservation ilvReservation)\n
    '''
def removeReservation():
    '''returns None\n\n
    removeReservation(final IlvReservation ilvReservation)\n
    '''
def reservationChanged():
    '''returns None\n\n
    reservationChanged(final ReservationEvent reservationEvent)\n
    '''
def constraintChanged():
    '''returns None\n\n
    constraintChanged(final ConstraintEvent constraintEvent)\n
    '''
def resourcesInserted():
    '''returns None\n\n
    resourcesInserted(final ResourcesInsertedEvent resourcesInsertedEvent)\n
    '''
def resourcesRemoved():
    '''returns None\n\n
    resourcesRemoved(final ResourcesRemovedEvent resourcesRemovedEvent)\n
    '''
def resourceMoved():
    '''returns None\n\n
    resourceMoved(final ResourceMovedEvent resourceMovedEvent)\n
    '''
def resourceChanged():
    '''returns None\n\n
    resourceChanged(final ResourceEvent resourceEvent)\n
    '''
def activitiesInserted():
    '''returns None\n\n
    activitiesInserted(final ActivitiesInsertedEvent activitiesInsertedEvent)\n
    '''
def activitiesRemoved():
    '''returns None\n\n
    activitiesRemoved(final ActivitiesRemovedEvent activitiesRemovedEvent)\n
    '''
def activityMoved():
    '''returns None\n\n
    activityMoved(final ActivityMovedEvent activityMovedEvent)\n
    '''
def activityChanged():
    '''returns None\n\n
    activityChanged(final ActivityEvent activityEvent)\n
    '''
def propertyChanged():
    '''returns None\n\n
    propertyChanged(final GanttModelPropertyEvent ganttModelPropertyEvent)\n
    '''
