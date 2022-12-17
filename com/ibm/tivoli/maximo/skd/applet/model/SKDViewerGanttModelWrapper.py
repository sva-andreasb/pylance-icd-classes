def ():
    '''returns SKDViewerGanttModelWrapper\n\n
    (final IlvDefaultGanttModel ganttModel)\n
    '''
def activityPreorderIterator():
    '''returns Iterator\n\n
    activityPreorderIterator(final IlvActivity activity)\n
    '''
def addActivity():
    '''returns None\n\n
    addActivity(final IlvActivity newActivity, final IlvActivity parentActivity)\n
    addActivity(final IlvActivity newActivity, final IlvActivity parentActivity, final int index)\n
    '''
def addActivityHierarchyListener():
    '''returns None\n\n
    addActivityHierarchyListener(final ActivityHierarchyListener listener)\n
    '''
def addActivityListener():
    '''returns None\n\n
    addActivityListener(final ActivityListener listener)\n
    '''
def addConstraint():
    '''returns None\n\n
    addConstraint(final IlvConstraint constraint)\n
    '''
def addConstraintListener():
    '''returns None\n\n
    addConstraintListener(final ConstraintListener listener)\n
    '''
def addGanttModelPropertyListener():
    '''returns None\n\n
    addGanttModelPropertyListener(final GanttModelPropertyListener listener)\n
    '''
def addReservation():
    '''returns None\n\n
    addReservation(final IlvReservation reservation)\n
    '''
def addReservationListener():
    '''returns None\n\n
    addReservationListener(final ReservationListener listener)\n
    '''
def addResource():
    '''returns None\n\n
    addResource(final IlvResource newResource, final IlvResource parentResource)\n
    addResource(final IlvResource newResource, final IlvResource parentResource, final int index)\n
    '''
def addResourceHierarchyListener():
    '''returns None\n\n
    addResourceHierarchyListener(final ResourceHierarchyListener listener)\n
    '''
def addResourceListener():
    '''returns None\n\n
    addResourceListener(final ResourceListener listener)\n
    '''
def childActivityIterator():
    '''returns Iterator\n\n
    childActivityIterator(final IlvActivity parentActivity)\n
    '''
def childResourceIterator():
    '''returns Iterator\n\n
    childResourceIterator(final IlvResource parentResource)\n
    '''
def constraintIterator():
    '''returns Iterator\n\n
    constraintIterator()\n
    '''
def constraintIteratorFromActivity():
    '''returns Iterator\n\n
    constraintIteratorFromActivity(final IlvActivity activity)\n
    '''
def constraintIteratorToActivity():
    '''returns Iterator\n\n
    constraintIteratorToActivity(final IlvActivity activity)\n
    '''
def contains():
    '''returns boolean\n\n
    contains(final IlvHierarchyNode node)\n
    contains(final IlvConstraint constraint)\n
    contains(final IlvReservation reservation)\n
    '''
def fireActivityEvent():
    '''returns None\n\n
    fireActivityEvent(final ActivityEvent event)\n
    '''
def fireConstraintEvent():
    '''returns None\n\n
    fireConstraintEvent(final ConstraintEvent event)\n
    '''
def fireReservationEvent():
    '''returns None\n\n
    fireReservationEvent(final ReservationEvent event)\n
    '''
def fireResourceEvent():
    '''returns None\n\n
    fireResourceEvent(final ResourceEvent event)\n
    '''
def getChild():
    '''returns IlvHierarchyNode\n\n
    getChild(final IlvHierarchyNode parent, final int index)\n
    '''
def getChildActivity():
    '''returns IlvActivity\n\n
    getChildActivity(final IlvActivity parentActivity, final int index)\n
    '''
def getChildActivityCount():
    '''returns int\n\n
    getChildActivityCount(final IlvActivity parentActivity)\n
    '''
def getChildActivityIndex():
    '''returns int\n\n
    getChildActivityIndex(final IlvActivity parentActivity, final IlvActivity childActivity)\n
    '''
def getChildCount():
    '''returns int\n\n
    getChildCount(final IlvHierarchyNode parent)\n
    '''
def getChildIndex():
    '''returns int\n\n
    getChildIndex(final IlvHierarchyNode parent, final IlvHierarchyNode child)\n
    '''
def getChildResource():
    '''returns IlvResource\n\n
    getChildResource(final IlvResource parent, final int index)\n
    '''
def getChildResourceCount():
    '''returns int\n\n
    getChildResourceCount(final IlvResource parent)\n
    '''
def getChildResourceIndex():
    '''returns int\n\n
    getChildResourceIndex(final IlvResource parent, final IlvResource index)\n
    '''
def getParent():
    '''returns IlvHierarchyNode\n\n
    getParent(final IlvHierarchyNode node)\n
    '''
def getParentActivity():
    '''returns IlvActivity\n\n
    getParentActivity(final IlvActivity activity)\n
    '''
def getParentActivityIndex():
    '''returns int\n\n
    getParentActivityIndex(final IlvActivity activity)\n
    '''
def getParentIndex():
    '''returns int\n\n
    getParentIndex(final IlvHierarchyNode node)\n
    '''
def getParentResource():
    '''returns IlvResource\n\n
    getParentResource(final IlvResource resource)\n
    '''
def getParentResourceIndex():
    '''returns int\n\n
    getParentResourceIndex(final IlvResource resource)\n
    '''
def getRootActivity():
    '''returns IlvActivity\n\n
    getRootActivity()\n
    '''
def getRootResource():
    '''returns IlvResource\n\n
    getRootResource()\n
    '''
def isAdjusting():
    '''returns boolean\n\n
    isAdjusting()\n
    '''
def moveActivity():
    '''returns None\n\n
    moveActivity(final IlvActivity activity1, final IlvActivity activity2, final int index)\n
    '''
def moveResource():
    '''returns None\n\n
    moveResource(final IlvResource resource1, final IlvResource resource2, final int index)\n
    '''
def removeActivity():
    '''returns None\n\n
    removeActivity(final IlvActivity activity)\n
    removeActivity(final IlvActivity activity, final int index)\n
    '''
def removeActivityHierarchyListener():
    '''returns None\n\n
    removeActivityHierarchyListener(final ActivityHierarchyListener listener)\n
    '''
def removeActivityListener():
    '''returns None\n\n
    removeActivityListener(final ActivityListener listener)\n
    '''
def removeConstraint():
    '''returns None\n\n
    removeConstraint(final IlvConstraint constraint)\n
    '''
def removeConstraintListener():
    '''returns None\n\n
    removeConstraintListener(final ConstraintListener listener)\n
    '''
def removeGanttModelPropertyListener():
    '''returns None\n\n
    removeGanttModelPropertyListener(final GanttModelPropertyListener listener)\n
    '''
def removeReservation():
    '''returns None\n\n
    removeReservation(final IlvReservation reservation)\n
    '''
def removeReservationListener():
    '''returns None\n\n
    removeReservationListener(final ReservationListener listener)\n
    '''
def removeResource():
    '''returns None\n\n
    removeResource(final IlvResource resource)\n
    removeResource(final IlvResource resource, final int index)\n
    '''
def removeResourceHierarchyListener():
    '''returns None\n\n
    removeResourceHierarchyListener(final ResourceHierarchyListener listener)\n
    '''
def removeResourceListener():
    '''returns None\n\n
    removeResourceListener(final ResourceListener listener)\n
    '''
def reservationIterator():
    '''returns Iterator\n\n
    reservationIterator()\n
    reservationIterator(final IlvActivity activity)\n
    reservationIterator(final IlvResource resource)\n
    reservationIterator(final IlvResource resource, final IlvTimeInterval timeInterval)\n
    '''
def resourcePreorderIterator():
    '''returns Iterator\n\n
    resourcePreorderIterator(final IlvResource resource)\n
    '''
def setAdjusting():
    '''returns None\n\n
    setAdjusting(final boolean adjusting)\n
    '''
def setRootActivity():
    '''returns None\n\n
    setRootActivity(final IlvActivity activity)\n
    '''
def setRootResource():
    '''returns None\n\n
    setRootResource(final IlvResource resource)\n
    '''
def isBatching():
    '''returns boolean\n\n
    isBatching()\n
    '''
def setBatching():
    '''returns None\n\n
    setBatching(final boolean arg0)\n
    '''
