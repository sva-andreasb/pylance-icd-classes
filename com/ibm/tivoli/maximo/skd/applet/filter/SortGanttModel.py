def ():
    '''returns CustomActivityComparator\n\n
    (final IlvGanttModel filteredModel, final IlvFilter activityFilter, final IlvFilter resourceFilter)\n
    ()\n
    (final String attrName)\n
    '''
def initSKDUtil():
    '''returns None\n\n
    initSKDUtil()\n
    '''
def setFilteredModel():
    '''returns None\n\n
    setFilteredModel(final IlvGanttModel model)\n
    '''
def activityPreorderIterator():
    '''returns Iterator\n\n
    activityPreorderIterator()\n
    activityPreorderIterator(final IlvActivity activity)\n
    '''
def reInitCache():
    '''returns None\n\n
    reInitCache()\n
    '''
def getActivityComparator():
    '''returns ActivityComparator\n\n
    getActivityComparator()\n
    '''
def setActivityComparator():
    '''returns None\n\n
    setActivityComparator(final ActivityComparator activityComparator)\n
    '''
def addActivity():
    '''returns None\n\n
    addActivity(final IlvActivity newActivity, final IlvActivity parent, final int index)\n
    '''
def removeActivity():
    '''returns None\n\n
    removeActivity(final IlvActivity parent, final int index)\n
    removeActivity(final IlvActivity activity)\n
    '''
def moveActivity():
    '''returns None\n\n
    moveActivity(final IlvActivity activity, final IlvActivity newParent, final int newIndex)\n
    '''
def getParentActivityIndex():
    '''returns int\n\n
    getParentActivityIndex(final IlvActivity activity)\n
    '''
def getParentActivity():
    '''returns IlvActivity\n\n
    getParentActivity(final IlvActivity activity)\n
    '''
def contains():
    '''returns boolean\n\n
    contains(final IlvHierarchyNode arg0)\n
    '''
def getChildActivity():
    '''returns IlvActivity\n\n
    getChildActivity(final IlvActivity parent, final int index)\n
    '''
def getChildActivityIndex():
    '''returns int\n\n
    getChildActivityIndex(final IlvActivity parent, final IlvActivity child)\n
    '''
def reservationIterator():
    '''returns Iterator<IlvReservation>\n\n
    reservationIterator(final IlvActivity arg0)\n
    '''
def compare():
    '''returns int\n\n
    compare(final IlvActivity a1, final IlvActivity a2)\n
    compare(final IlvActivity a1, final IlvActivity a2)\n
    compare(final IlvActivity a1, final IlvActivity a2)\n
    compare(final IlvActivity a1, final IlvActivity a2)\n
    '''
def changesSortOrder():
    '''returns boolean\n\n
    changesSortOrder(final ActivityPropertyEvent event)\n
    changesSortOrder(final ActivityPropertyEvent event)\n
    changesSortOrder(final ActivityPropertyEvent event)\n
    changesSortOrder(final ActivityPropertyEvent event)\n
    '''
def activityChanged():
    '''returns None\n\n
    activityChanged(final ActivityEvent event)\n
    '''
def activitiesInserted():
    '''returns None\n\n
    activitiesInserted(final ActivitiesInsertedEvent event)\n
    '''
def activitiesRemoved():
    '''returns None\n\n
    activitiesRemoved(final ActivitiesRemovedEvent event)\n
    '''
def activityMoved():
    '''returns None\n\n
    activityMoved(final ActivityMovedEvent event)\n
    '''
