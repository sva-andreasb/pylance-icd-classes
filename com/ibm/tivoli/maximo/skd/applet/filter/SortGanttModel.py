def SortGanttModel():
    '''public SortGanttModel(final IlvGanttModel filteredModel, final IlvFilter activityFilter, final IlvFilter resourceFilter)
    '''
def initSKDUtil():
    '''public void initSKDUtil()
    '''
def setFilteredModel():
    '''public void setFilteredModel(final IlvGanttModel model)
    '''
def activityPreorderIterator():
    '''public Iterator activityPreorderIterator()
    public Iterator activityPreorderIterator(final IlvActivity activity)
    '''
def reInitCache():
    '''public void reInitCache()
    '''
def getActivityComparator():
    '''public ActivityComparator getActivityComparator()
    '''
def setActivityComparator():
    '''public void setActivityComparator(final ActivityComparator activityComparator)
    '''
def addActivity():
    '''public void addActivity(final IlvActivity newActivity, final IlvActivity parent, final int index)
    '''
def removeActivity():
    '''public void removeActivity(final IlvActivity parent, final int index)
    public void removeActivity(final IlvActivity activity)
    '''
def moveActivity():
    '''public void moveActivity(final IlvActivity activity, final IlvActivity newParent, final int newIndex)
    '''
def getParentActivityIndex():
    '''public int getParentActivityIndex(final IlvActivity activity)
    '''
def getParentActivity():
    '''public IlvActivity getParentActivity(final IlvActivity activity)
    '''
def contains():
    '''public boolean contains(final IlvHierarchyNode arg0)
    '''
def getChildActivity():
    '''public IlvActivity getChildActivity(final IlvActivity parent, final int index)
    '''
def getChildActivityIndex():
    '''public int getChildActivityIndex(final IlvActivity parent, final IlvActivity child)
    '''
def reservationIterator():
    '''public Iterator<IlvReservation> reservationIterator(final IlvActivity arg0)
    '''
def ActivityNameComparator():
    '''public ActivityNameComparator()
    '''
def compare():
    '''public int compare(final IlvActivity a1, final IlvActivity a2)
    public int compare(final IlvActivity a1, final IlvActivity a2)
    public int compare(final IlvActivity a1, final IlvActivity a2)
    public int compare(final IlvActivity a1, final IlvActivity a2)
    '''
def changesSortOrder():
    '''public boolean changesSortOrder(final ActivityPropertyEvent event)
    public boolean changesSortOrder(final ActivityPropertyEvent event)
    public boolean changesSortOrder(final ActivityPropertyEvent event)
    public boolean changesSortOrder(final ActivityPropertyEvent event)
    '''
def CustomActivityComparator():
    '''public CustomActivityComparator(final String attrName)
    '''
def activityChanged():
    '''public void activityChanged(final ActivityEvent event)
    '''
def activitiesInserted():
    '''public void activitiesInserted(final ActivitiesInsertedEvent event)
    '''
def activitiesRemoved():
    '''public void activitiesRemoved(final ActivitiesRemovedEvent event)
    '''
def activityMoved():
    '''public void activityMoved(final ActivityMovedEvent event)
    '''
