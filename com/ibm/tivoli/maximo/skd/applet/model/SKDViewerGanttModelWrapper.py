def SKDViewerGanttModelWrapper():
'''public SKDViewerGanttModelWrapper(final IlvDefaultGanttModel ganttModel)
'''
pass
def activityPreorderIterator():
'''public Iterator activityPreorderIterator(final IlvActivity activity)
'''
pass
def addActivity():
'''public void addActivity(final IlvActivity newActivity, final IlvActivity parentActivity)
public void addActivity(final IlvActivity newActivity, final IlvActivity parentActivity, final int index)
'''
pass
def addActivityHierarchyListener():
'''public void addActivityHierarchyListener(final ActivityHierarchyListener listener)
'''
pass
def addActivityListener():
'''public void addActivityListener(final ActivityListener listener)
'''
pass
def addConstraint():
'''public void addConstraint(final IlvConstraint constraint)
'''
pass
def addConstraintListener():
'''public void addConstraintListener(final ConstraintListener listener)
'''
pass
def addGanttModelPropertyListener():
'''public void addGanttModelPropertyListener(final GanttModelPropertyListener listener)
'''
pass
def addReservation():
'''public void addReservation(final IlvReservation reservation)
'''
pass
def addReservationListener():
'''public void addReservationListener(final ReservationListener listener)
'''
pass
def addResource():
'''public void addResource(final IlvResource newResource, final IlvResource parentResource)
public void addResource(final IlvResource newResource, final IlvResource parentResource, final int index)
'''
pass
def addResourceHierarchyListener():
'''public void addResourceHierarchyListener(final ResourceHierarchyListener listener)
'''
pass
def addResourceListener():
'''public void addResourceListener(final ResourceListener listener)
'''
pass
def childActivityIterator():
'''public Iterator childActivityIterator(final IlvActivity parentActivity)
'''
pass
def childResourceIterator():
'''public Iterator childResourceIterator(final IlvResource parentResource)
'''
pass
def constraintIterator():
'''public Iterator constraintIterator()
'''
pass
def constraintIteratorFromActivity():
'''public Iterator constraintIteratorFromActivity(final IlvActivity activity)
'''
pass
def constraintIteratorToActivity():
'''public Iterator constraintIteratorToActivity(final IlvActivity activity)
'''
pass
def contains():
'''public boolean contains(final IlvHierarchyNode node)
public boolean contains(final IlvConstraint constraint)
public boolean contains(final IlvReservation reservation)
'''
pass
def fireActivityEvent():
'''public void fireActivityEvent(final ActivityEvent event)
'''
pass
def fireConstraintEvent():
'''public void fireConstraintEvent(final ConstraintEvent event)
'''
pass
def fireReservationEvent():
'''public void fireReservationEvent(final ReservationEvent event)
'''
pass
def fireResourceEvent():
'''public void fireResourceEvent(final ResourceEvent event)
'''
pass
def getChild():
'''public IlvHierarchyNode getChild(final IlvHierarchyNode parent, final int index)
'''
pass
def getChildActivity():
'''public IlvActivity getChildActivity(final IlvActivity parentActivity, final int index)
'''
pass
def getChildActivityCount():
'''public int getChildActivityCount(final IlvActivity parentActivity)
'''
pass
def getChildActivityIndex():
'''public int getChildActivityIndex(final IlvActivity parentActivity, final IlvActivity childActivity)
'''
pass
def getChildCount():
'''public int getChildCount(final IlvHierarchyNode parent)
'''
pass
def getChildIndex():
'''public int getChildIndex(final IlvHierarchyNode parent, final IlvHierarchyNode child)
'''
pass
def getChildResource():
'''public IlvResource getChildResource(final IlvResource parent, final int index)
'''
pass
def getChildResourceCount():
'''public int getChildResourceCount(final IlvResource parent)
'''
pass
def getChildResourceIndex():
'''public int getChildResourceIndex(final IlvResource parent, final IlvResource index)
'''
pass
def getParent():
'''public IlvHierarchyNode getParent(final IlvHierarchyNode node)
'''
pass
def getParentActivity():
'''public IlvActivity getParentActivity(final IlvActivity activity)
'''
pass
def getParentActivityIndex():
'''public int getParentActivityIndex(final IlvActivity activity)
'''
pass
def getParentIndex():
'''public int getParentIndex(final IlvHierarchyNode node)
'''
pass
def getParentResource():
'''public IlvResource getParentResource(final IlvResource resource)
'''
pass
def getParentResourceIndex():
'''public int getParentResourceIndex(final IlvResource resource)
'''
pass
def getRootActivity():
'''public IlvActivity getRootActivity()
'''
pass
def getRootResource():
'''public IlvResource getRootResource()
'''
pass
def isAdjusting():
'''public boolean isAdjusting()
'''
pass
def moveActivity():
'''public void moveActivity(final IlvActivity activity1, final IlvActivity activity2, final int index)
'''
pass
def moveResource():
'''public void moveResource(final IlvResource resource1, final IlvResource resource2, final int index)
'''
pass
def removeActivity():
'''public void removeActivity(final IlvActivity activity)
public void removeActivity(final IlvActivity activity, final int index)
'''
pass
def removeActivityHierarchyListener():
'''public void removeActivityHierarchyListener(final ActivityHierarchyListener listener)
'''
pass
def removeActivityListener():
'''public void removeActivityListener(final ActivityListener listener)
'''
pass
def removeConstraint():
'''public void removeConstraint(final IlvConstraint constraint)
'''
pass
def removeConstraintListener():
'''public void removeConstraintListener(final ConstraintListener listener)
'''
pass
def removeGanttModelPropertyListener():
'''public void removeGanttModelPropertyListener(final GanttModelPropertyListener listener)
'''
pass
def removeReservation():
'''public void removeReservation(final IlvReservation reservation)
'''
pass
def removeReservationListener():
'''public void removeReservationListener(final ReservationListener listener)
'''
pass
def removeResource():
'''public void removeResource(final IlvResource resource)
public void removeResource(final IlvResource resource, final int index)
'''
pass
def removeResourceHierarchyListener():
'''public void removeResourceHierarchyListener(final ResourceHierarchyListener listener)
'''
pass
def removeResourceListener():
'''public void removeResourceListener(final ResourceListener listener)
'''
pass
def reservationIterator():
'''public Iterator reservationIterator()
public Iterator reservationIterator(final IlvActivity activity)
public Iterator reservationIterator(final IlvResource resource)
public Iterator reservationIterator(final IlvResource resource, final IlvTimeInterval timeInterval)
'''
pass
def resourcePreorderIterator():
'''public Iterator resourcePreorderIterator(final IlvResource resource)
'''
pass
def setAdjusting():
'''public void setAdjusting(final boolean adjusting)
'''
pass
def setRootActivity():
'''public void setRootActivity(final IlvActivity activity)
'''
pass
def setRootResource():
'''public void setRootResource(final IlvResource resource)
'''
pass
def isBatching():
'''public boolean isBatching()
'''
pass
def setBatching():
'''public void setBatching(final boolean arg0)
'''
pass
