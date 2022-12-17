def ():
    '''returns ActivityIterator\n\n
    ()\n
    (final IlvResource ilvResource)\n
    (final IlvResource a)\n
    (final IlvActivity ilvActivity)\n
    (final IlvActivity a)\n
    '''
def clear():
    '''returns None\n\n
    clear()\n
    '''
def setAdjusting():
    '''returns None\n\n
    setAdjusting(final boolean b)\n
    '''
def isAdjusting():
    '''returns boolean\n\n
    isAdjusting()\n
    '''
def setBatching():
    '''returns None\n\n
    setBatching(final boolean b)\n
    '''
def isBatching():
    '''returns boolean\n\n
    isBatching()\n
    '''
def addGanttModelPropertyListener():
    '''returns None\n\n
    addGanttModelPropertyListener(final GanttModelPropertyListener ganttModelPropertyListener)\n
    '''
def removeGanttModelPropertyListener():
    '''returns None\n\n
    removeGanttModelPropertyListener(final GanttModelPropertyListener ganttModelPropertyListener)\n
    '''
def getParent():
    '''returns IlvHierarchyNode\n\n
    getParent(final IlvHierarchyNode ilvHierarchyNode)\n
    '''
def getParentIndex():
    '''returns int\n\n
    getParentIndex(final IlvHierarchyNode ilvHierarchyNode)\n
    '''
def getChildCount():
    '''returns int\n\n
    getChildCount(final IlvHierarchyNode ilvHierarchyNode)\n
    '''
def getChild():
    '''returns IlvHierarchyNode\n\n
    getChild(final IlvHierarchyNode ilvHierarchyNode, final int n)\n
    '''
def getChildIndex():
    '''returns int\n\n
    getChildIndex(final IlvHierarchyNode ilvHierarchyNode, final IlvHierarchyNode ilvHierarchyNode2)\n
    '''
def addActivity():
    '''returns None\n\n
    addActivity(final IlvActivity ilvActivity, final IlvActivity ilvActivity2)\n
    '''
def childActivityIterator():
    '''returns Iterator<IlvActivity>\n\n
    childActivityIterator(final IlvActivity ilvActivity)\n
    '''
def activityPreorderIterator():
    '''returns Iterator<IlvActivity>\n\n
    activityPreorderIterator(final IlvActivity ilvActivity)\n
    activityPreorderIterator()\n
    '''
def addActivityHierarchyListener():
    '''returns None\n\n
    addActivityHierarchyListener(final ActivityHierarchyListener activityHierarchyListener)\n
    '''
def removeActivityHierarchyListener():
    '''returns None\n\n
    removeActivityHierarchyListener(final ActivityHierarchyListener activityHierarchyListener)\n
    '''
def addActivityListener():
    '''returns None\n\n
    addActivityListener(final ActivityListener activityListener)\n
    '''
def removeActivityListener():
    '''returns None\n\n
    removeActivityListener(final ActivityListener activityListener)\n
    '''
def fireActivityEvent():
    '''returns None\n\n
    fireActivityEvent(final ActivityEvent activityEvent)\n
    '''
def addResource():
    '''returns None\n\n
    addResource(final IlvResource ilvResource, final IlvResource ilvResource2)\n
    '''
def childResourceIterator():
    '''returns Iterator<IlvResource>\n\n
    childResourceIterator(final IlvResource ilvResource)\n
    '''
def resourcePreorderIterator():
    '''returns Iterator<IlvResource>\n\n
    resourcePreorderIterator(final IlvResource ilvResource)\n
    resourcePreorderIterator()\n
    '''
def addResourceHierarchyListener():
    '''returns None\n\n
    addResourceHierarchyListener(final ResourceHierarchyListener resourceHierarchyListener)\n
    '''
def removeResourceHierarchyListener():
    '''returns None\n\n
    removeResourceHierarchyListener(final ResourceHierarchyListener resourceHierarchyListener)\n
    '''
def addResourceListener():
    '''returns None\n\n
    addResourceListener(final ResourceListener resourceListener)\n
    '''
def removeResourceListener():
    '''returns None\n\n
    removeResourceListener(final ResourceListener resourceListener)\n
    '''
def fireResourceEvent():
    '''returns None\n\n
    fireResourceEvent(final ResourceEvent resourceEvent)\n
    '''
def addConstraintListener():
    '''returns None\n\n
    addConstraintListener(final ConstraintListener constraintListener)\n
    '''
def removeConstraintListener():
    '''returns None\n\n
    removeConstraintListener(final ConstraintListener constraintListener)\n
    '''
def fireConstraintEvent():
    '''returns None\n\n
    fireConstraintEvent(final ConstraintEvent constraintEvent)\n
    '''
def addReservationListener():
    '''returns None\n\n
    addReservationListener(final ReservationListener reservationListener)\n
    '''
def removeReservationListener():
    '''returns None\n\n
    removeReservationListener(final ReservationListener reservationListener)\n
    '''
def fireReservationEvent():
    '''returns None\n\n
    fireReservationEvent(final ReservationEvent reservationEvent)\n
    '''
def getChildren():
    '''returns Iterator<IlvActivity>\n\n
    getChildren(final IlvResource ilvResource)\n
    getChildren(final IlvActivity ilvActivity)\n
    '''
def hasNext():
    '''returns boolean\n\n
    hasNext()\n
    hasNext()\n
    '''
def next():
    '''returns IlvActivity\n\n
    next()\n
    next()\n
    '''
def remove():
    '''returns None\n\n
    remove()\n
    remove()\n
    '''
