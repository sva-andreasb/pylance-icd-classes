def ():
    '''returns ActivityIterator\n\n
    (final int n, final int o, final int p5, final int q, final float m)\n
    (final int n, final int n2, final int n3, final int n4)\n
    ()\n
    (final IlvResource key)\n
    ()\n
    (final IlvActivity key)\n
    '''
def contains():
    '''returns boolean\n\n
    contains(final IlvHierarchyNode ilvHierarchyNode)\n
    contains(final IlvConstraint o)\n
    contains(final IlvReservation o)\n
    '''
def getRootActivity():
    '''returns IlvActivity\n\n
    getRootActivity()\n
    '''
def setRootActivity():
    '''returns None\n\n
    setRootActivity(final IlvActivity c)\n
    '''
def childActivityIterator():
    '''returns Iterator<IlvActivity>\n\n
    childActivityIterator(final IlvActivity ilvActivity)\n
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
    addActivity(final IlvActivity key, final IlvActivity a, final int a2)\n
    '''
def removeActivity():
    '''returns None\n\n
    removeActivity(final IlvActivity ilvActivity, final int n)\n
    removeActivity(final IlvActivity obj)\n
    '''
def moveActivity():
    '''returns None\n\n
    moveActivity(final IlvActivity key, final IlvActivity ilvActivity, int min)\n
    '''
def getRootResource():
    '''returns IlvResource\n\n
    getRootResource()\n
    '''
def setRootResource():
    '''returns None\n\n
    setRootResource(final IlvResource e)\n
    '''
def childResourceIterator():
    '''returns Iterator<IlvResource>\n\n
    childResourceIterator(final IlvResource ilvResource)\n
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
    addResource(final IlvResource key, final IlvResource a, final int a2)\n
    '''
def removeResource():
    '''returns None\n\n
    removeResource(final IlvResource ilvResource, final int n)\n
    removeResource(final IlvResource obj)\n
    '''
def moveResource():
    '''returns None\n\n
    moveResource(final IlvResource key, final IlvResource ilvResource, int min)\n
    '''
def constraintIteratorToActivity():
    '''returns Iterator<IlvConstraint>\n\n
    constraintIteratorToActivity(final IlvActivity key)\n
    '''
def addConstraint():
    '''returns None\n\n
    addConstraint(final IlvConstraint e)\n
    '''
def removeConstraint():
    '''returns None\n\n
    removeConstraint(final IlvConstraint ilvConstraint)\n
    '''
def evaluate():
    '''returns boolean\n\n
    evaluate(final IlvReservation ilvReservation)\n
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
