def ():
    '''returns IlvSimpleActivity\n\n
    (final String b, final String c, final IlvTimeInterval d)\n
    (final String s, final String s2, final Date date, final Date date2)\n
    (final String s, final String s2, final Date date, final IlvDuration ilvDuration)\n
    '''
def getID():
    '''returns String\n\n
    getID()\n
    '''
def setID():
    '''returns None\n\n
    setID(final String anObject)\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def setName():
    '''returns None\n\n
    setName(final String anObject)\n
    '''
def getTimeInterval():
    '''returns IlvTimeInterval\n\n
    getTimeInterval()\n
    '''
def setTimeInterval():
    '''returns None\n\n
    setTimeInterval(final IlvTimeInterval ilvTimeInterval)\n
    '''
def getAutoCalcTimeIntervalFromChildren():
    '''returns boolean\n\n
    getAutoCalcTimeIntervalFromChildren()\n
    '''
def setAutoCalcTimeIntervalFromChildren():
    '''returns None\n\n
    setAutoCalcTimeIntervalFromChildren(final boolean e)\n
    '''
def getChildEventFilter():
    '''returns IlvUnaryPredicate<ActivityEvent>\n\n
    getChildEventFilter()\n
    '''
def processChildEvent():
    '''returns None\n\n
    processChildEvent(final ActivityEvent activityEvent)\n
    '''
def setGanttModelImpl():
    '''returns None\n\n
    setGanttModelImpl(final IlvGanttModel key)\n
    '''
def evaluate():
    '''returns boolean\n\n
    evaluate(final ActivityEvent activityEvent)\n
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
