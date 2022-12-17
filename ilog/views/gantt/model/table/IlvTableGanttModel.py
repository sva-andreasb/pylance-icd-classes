def ():
    '''returns ActivityFactory\n\n
    ()\n
    (final TableModel tableModel, final TableModel tableModel2, final TableModel tableModel3, final TableModel tableModel4)\n
    (final IlvTableModelMapper v, final IlvTableModelMapper aa, final IlvTableModelMapper af, final IlvTableModelMapper al)\n
    ()\n
    ()\n
    (final boolean a)\n
    (final boolean a)\n
    '''
def configureHierarchyChart():
    '''returns None\n\n
    configureHierarchyChart(final IlvHierarchyChart ilvHierarchyChart)\n
    configureHierarchyChart(final IlvHierarchyChart ilvHierarchyChart, final boolean b)\n
    '''
def run():
    '''returns None\n\n
    run()\n
    run()\n
    run()\n
    run()\n
    run()\n
    run()\n
    run()\n
    run()\n
    run()\n
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
    setRootActivity(final IlvActivity ilvActivity)\n
    '''
def getParentActivity():
    '''returns IlvActivity\n\n
    getParentActivity(final IlvActivity ilvActivity)\n
    '''
def getParentActivityIndex():
    '''returns int\n\n
    getParentActivityIndex(final IlvActivity obj)\n
    '''
def getChildActivityCount():
    '''returns int\n\n
    getChildActivityCount(final IlvActivity obj)\n
    '''
def getChildActivity():
    '''returns IlvActivity\n\n
    getChildActivity(final IlvActivity obj, final int n)\n
    '''
def getChildActivityIndex():
    '''returns int\n\n
    getChildActivityIndex(final IlvActivity obj, final IlvActivity ilvActivity)\n
    '''
def addActivity():
    '''returns None\n\n
    addActivity(final IlvActivity ilvActivity, final IlvActivity obj, final int a)\n
    '''
def removeActivity():
    '''returns None\n\n
    removeActivity(final IlvActivity obj, final int n)\n
    removeActivity(final IlvActivity obj)\n
    '''
def moveActivity():
    '''returns None\n\n
    moveActivity(final IlvActivity ilvActivity, final IlvActivity ilvActivity2, int min)\n
    '''
def getRootResource():
    '''returns IlvResource\n\n
    getRootResource()\n
    '''
def setRootResource():
    '''returns None\n\n
    setRootResource(final IlvResource ilvResource)\n
    '''
def getParentResource():
    '''returns IlvResource\n\n
    getParentResource(final IlvResource ilvResource)\n
    '''
def getParentResourceIndex():
    '''returns int\n\n
    getParentResourceIndex(final IlvResource obj)\n
    '''
def getChildResourceCount():
    '''returns int\n\n
    getChildResourceCount(final IlvResource obj)\n
    '''
def getChildResource():
    '''returns IlvResource\n\n
    getChildResource(final IlvResource obj, final int n)\n
    '''
def getChildResourceIndex():
    '''returns int\n\n
    getChildResourceIndex(final IlvResource obj, final IlvResource ilvResource)\n
    '''
def addResource():
    '''returns None\n\n
    addResource(final IlvResource ilvResource, final IlvResource obj, final int a)\n
    '''
def removeResource():
    '''returns None\n\n
    removeResource(final IlvResource obj, final int n)\n
    removeResource(final IlvResource obj)\n
    '''
def moveResource():
    '''returns None\n\n
    moveResource(final IlvResource ilvResource, final IlvResource ilvResource2, int min)\n
    '''
def constraintIteratorToActivity():
    '''returns Iterator\n\n
    constraintIteratorToActivity(final IlvActivity key)\n
    '''
def addConstraint():
    '''returns None\n\n
    addConstraint(final IlvConstraint ilvConstraint)\n
    '''
def removeConstraint():
    '''returns None\n\n
    removeConstraint(final IlvConstraint ilvConstraint)\n
    '''
def evaluate():
    '''returns boolean\n\n
    evaluate(final Object o)\n
    '''
def addReservation():
    '''returns None\n\n
    addReservation(final IlvReservation ilvReservation)\n
    '''
def removeReservation():
    '''returns None\n\n
    removeReservation(final IlvReservation ilvReservation)\n
    '''
def fireReservationEvent():
    '''returns None\n\n
    fireReservationEvent(final ReservationEvent reservationEvent)\n
    '''
def tableChanged():
    '''returns None\n\n
    tableChanged(final TableModelEvent tableModelEvent)\n
    '''
def createResource():
    '''returns IlvResource\n\n
    createResource()\n
    '''
def createConstraint():
    '''returns IlvConstraint\n\n
    createConstraint(final IlvActivity ilvActivity, final IlvActivity ilvActivity2, final IlvConstraintType ilvConstraintType)\n
    '''
def createReservation():
    '''returns IlvReservation\n\n
    createReservation(final IlvResource ilvResource, final IlvActivity ilvActivity)\n
    '''
def createActivity():
    '''returns IlvActivity\n\n
    createActivity(final IlvTimeInterval ilvTimeInterval)\n
    '''
