def ():
    '''returns FilteredActivityEventHandler\n\n
    ()\n
    (final IlvGanttModel ilvGanttModel)\n
    (final IlvGanttModel filteredModel, final IlvFilter<IlvActivity> activityFilter, final IlvFilter<IlvResource> resourceFilter)\n
    ()\n
    ()\n
    ()\n
    ()\n
    ()\n
    ()\n
    '''
def filterChanged():
    '''returns None\n\n
    filterChanged(final FilterEvent filterEvent)\n
    filterChanged(final FilterEvent filterEvent)\n
    '''
def evaluate():
    '''returns boolean\n\n
    evaluate(final IlvConstraint o)\n
    evaluate(final IlvReservation o)\n
    evaluate(final Object o)\n
    '''
def setFilteredModel():
    '''returns None\n\n
    setFilteredModel(final IlvGanttModel filteredModel)\n
    '''
def contains():
    '''returns boolean\n\n
    contains(final IlvHierarchyNode ilvHierarchyNode)\n
    contains(final IlvConstraint o)\n
    contains(final IlvReservation o)\n
    '''
def getActivityFilter():
    '''returns IlvFilter<IlvActivity>\n\n
    getActivityFilter()\n
    '''
def setActivityFilter():
    '''returns None\n\n
    setActivityFilter(final IlvFilter<IlvActivity> ilvFilter)\n
    '''
def getRootActivity():
    '''returns IlvActivity\n\n
    getRootActivity()\n
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
    removeActivity(final IlvActivity ilvActivity)\n
    removeActivity(final IlvActivity ilvActivity, final int n)\n
    '''
def moveActivity():
    '''returns None\n\n
    moveActivity(final IlvActivity ilvActivity, final IlvActivity ilvActivity2, final int n)\n
    '''
def getResourceFilter():
    '''returns IlvFilter<IlvResource>\n\n
    getResourceFilter()\n
    '''
def setResourceFilter():
    '''returns None\n\n
    setResourceFilter(final IlvFilter<IlvResource> ilvFilter)\n
    '''
def getRootResource():
    '''returns IlvResource\n\n
    getRootResource()\n
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
    removeResource(final IlvResource ilvResource)\n
    removeResource(final IlvResource ilvResource, final int n)\n
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
def reservationIterator():
    '''returns Iterator<IlvReservation>\n\n
    reservationIterator()\n
    reservationIterator(final IlvActivity ilvActivity)\n
    reservationIterator(final IlvResource ilvResource)\n
    reservationIterator(final IlvResource ilvResource, final IlvTimeInterval ilvTimeInterval)\n
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
