def SKDViewerGanttModelWrapper():
    '''    public SKDViewerGanttModelWrapper(final IlvDefaultGanttModel ganttModel)
    '''
def activityPreorderIterator():
    '''    public Iterator activityPreorderIterator(final IlvActivity activity)
    '''
def addActivity():
    '''    public void addActivity(final IlvActivity newActivity, final IlvActivity parentActivity)
    public void addActivity(final IlvActivity newActivity, final IlvActivity parentActivity, final int index)
    '''
def addActivityHierarchyListener():
    '''    public void addActivityHierarchyListener(final ActivityHierarchyListener listener)
    '''
def addActivityListener():
    '''    public void addActivityListener(final ActivityListener listener)
    '''
def addConstraint():
    '''    public void addConstraint(final IlvConstraint constraint)
    '''
def addConstraintListener():
    '''    public void addConstraintListener(final ConstraintListener listener)
    '''
def addGanttModelPropertyListener():
    '''    public void addGanttModelPropertyListener(final GanttModelPropertyListener listener)
    '''
def addReservation():
    '''    public void addReservation(final IlvReservation reservation)
    '''
def addReservationListener():
    '''    public void addReservationListener(final ReservationListener listener)
    '''
def addResource():
    '''    public void addResource(final IlvResource newResource, final IlvResource parentResource)
    public void addResource(final IlvResource newResource, final IlvResource parentResource, final int index)
    '''
def addResourceHierarchyListener():
    '''    public void addResourceHierarchyListener(final ResourceHierarchyListener listener)
    '''
def addResourceListener():
    '''    public void addResourceListener(final ResourceListener listener)
    '''
def childActivityIterator():
    '''    public Iterator childActivityIterator(final IlvActivity parentActivity)
    '''
def childResourceIterator():
    '''    public Iterator childResourceIterator(final IlvResource parentResource)
    '''
def constraintIterator():
    '''    public Iterator constraintIterator()
    '''
def constraintIteratorFromActivity():
    '''    public Iterator constraintIteratorFromActivity(final IlvActivity activity)
    '''
def constraintIteratorToActivity():
    '''    public Iterator constraintIteratorToActivity(final IlvActivity activity)
    '''
def contains():
    '''    public boolean contains(final IlvHierarchyNode node)
    public boolean contains(final IlvConstraint constraint)
    public boolean contains(final IlvReservation reservation)
    '''
def fireActivityEvent():
    '''    public void fireActivityEvent(final ActivityEvent event)
    '''
def fireConstraintEvent():
    '''    public void fireConstraintEvent(final ConstraintEvent event)
    '''
def fireReservationEvent():
    '''    public void fireReservationEvent(final ReservationEvent event)
    '''
def fireResourceEvent():
    '''    public void fireResourceEvent(final ResourceEvent event)
    '''
def getChild():
    '''    public IlvHierarchyNode getChild(final IlvHierarchyNode parent, final int index)
    '''
def getChildActivity():
    '''    public IlvActivity getChildActivity(final IlvActivity parentActivity, final int index)
    '''
def getChildActivityCount():
    '''    public int getChildActivityCount(final IlvActivity parentActivity)
    '''
def getChildActivityIndex():
    '''    public int getChildActivityIndex(final IlvActivity parentActivity, final IlvActivity childActivity)
    '''
def getChildCount():
    '''    public int getChildCount(final IlvHierarchyNode parent)
    '''
def getChildIndex():
    '''    public int getChildIndex(final IlvHierarchyNode parent, final IlvHierarchyNode child)
    '''
def getChildResource():
    '''    public IlvResource getChildResource(final IlvResource parent, final int index)
    '''
def getChildResourceCount():
    '''    public int getChildResourceCount(final IlvResource parent)
    '''
def getChildResourceIndex():
    '''    public int getChildResourceIndex(final IlvResource parent, final IlvResource index)
    '''
def getParent():
    '''    public IlvHierarchyNode getParent(final IlvHierarchyNode node)
    '''
def getParentActivity():
    '''    public IlvActivity getParentActivity(final IlvActivity activity)
    '''
def getParentActivityIndex():
    '''    public int getParentActivityIndex(final IlvActivity activity)
    '''
def getParentIndex():
    '''    public int getParentIndex(final IlvHierarchyNode node)
    '''
def getParentResource():
    '''    public IlvResource getParentResource(final IlvResource resource)
    '''
def getParentResourceIndex():
    '''    public int getParentResourceIndex(final IlvResource resource)
    '''
def getRootActivity():
    '''    public IlvActivity getRootActivity()
    '''
def getRootResource():
    '''    public IlvResource getRootResource()
    '''
def isAdjusting():
    '''    public boolean isAdjusting()
    '''
def moveActivity():
    '''    public void moveActivity(final IlvActivity activity1, final IlvActivity activity2, final int index)
    '''
def moveResource():
    '''    public void moveResource(final IlvResource resource1, final IlvResource resource2, final int index)
    '''
def removeActivity():
    '''    public void removeActivity(final IlvActivity activity)
    public void removeActivity(final IlvActivity activity, final int index)
    '''
def removeActivityHierarchyListener():
    '''    public void removeActivityHierarchyListener(final ActivityHierarchyListener listener)
    '''
def removeActivityListener():
    '''    public void removeActivityListener(final ActivityListener listener)
    '''
def removeConstraint():
    '''    public void removeConstraint(final IlvConstraint constraint)
    '''
def removeConstraintListener():
    '''    public void removeConstraintListener(final ConstraintListener listener)
    '''
def removeGanttModelPropertyListener():
    '''    public void removeGanttModelPropertyListener(final GanttModelPropertyListener listener)
    '''
def removeReservation():
    '''    public void removeReservation(final IlvReservation reservation)
    '''
def removeReservationListener():
    '''    public void removeReservationListener(final ReservationListener listener)
    '''
def removeResource():
    '''    public void removeResource(final IlvResource resource)
    public void removeResource(final IlvResource resource, final int index)
    '''
def removeResourceHierarchyListener():
    '''    public void removeResourceHierarchyListener(final ResourceHierarchyListener listener)
    '''
def removeResourceListener():
    '''    public void removeResourceListener(final ResourceListener listener)
    '''
def reservationIterator():
    '''    public Iterator reservationIterator()
    public Iterator reservationIterator(final IlvActivity activity)
    public Iterator reservationIterator(final IlvResource resource)
    public Iterator reservationIterator(final IlvResource resource, final IlvTimeInterval timeInterval)
    '''
def resourcePreorderIterator():
    '''    public Iterator resourcePreorderIterator(final IlvResource resource)
    '''
def setAdjusting():
    '''    public void setAdjusting(final boolean adjusting)
    '''
def setRootActivity():
    '''    public void setRootActivity(final IlvActivity activity)
    '''
def setRootResource():
    '''    public void setRootResource(final IlvResource resource)
    '''
def isBatching():
    '''    public boolean isBatching()
    '''
def setBatching():
    '''    public void setBatching(final boolean arg0)
    '''
