HEIRARCHY_LEVEL = "String  \"_LEVEL\""
def ():
    '''returns MaxActivityModelProcessor\n\n
    (final Schedule schedule)\n
    '''
def getModel():
    '''returns IMXGanttModel\n\n
    getModel()\n
    '''
def getRootActivity():
    '''returns IMXActivity\n\n
    getRootActivity()\n
    '''
def activityPreorderIterator():
    '''returns Iterator<IMXActivity>\n\n
    activityPreorderIterator()\n
    activityPreorderIterator(final IMXActivity activity)\n
    '''
def childActivityIterator():
    '''returns Iterator<IMXActivity>\n\n
    childActivityIterator(final IMXActivity activity)\n
    '''
def getChildActivityCount():
    '''returns int\n\n
    getChildActivityCount(final IMXActivity activity)\n
    '''
def constraintIteratorFromActivity():
    '''returns Iterator\n\n
    constraintIteratorFromActivity(final IMXActivity activity)\n
    '''
def constraintIteratorToActivity():
    '''returns Iterator\n\n
    constraintIteratorToActivity(final IMXActivity activity)\n
    '''
def constraintIterator():
    '''returns Iterator\n\n
    constraintIterator(final IMXActivity activity)\n
    '''
def getActivityByID():
    '''returns IMXActivity\n\n
    getActivityByID(final String activityID)\n
    '''
def recalculateParentActivity():
    '''returns boolean\n\n
    recalculateParentActivity(final IMXActivity parent)\n
    '''
def getItemById():
    '''returns IMXActivity\n\n
    getItemById(final String id)\n
    '''
