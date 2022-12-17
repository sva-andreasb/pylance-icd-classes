def ():
    '''returns WOActivity\n\n
    (final Date activityStartDate, final Date activityEndDate, final double hours, final double resource_qty, final boolean interruptibleFlag, final boolean useOverlappingShifts, final String intShift)\n
    (final Date activityStartDate, final Date activityEndDate, final double hours, final double resource_qty, final boolean interruptibleFlag, final boolean useOverlappingShifts, final Date intShiftStartTime, final Date intShiftEndTime, final String intShift)\n
    '''
def getInterruptible():
    '''returns boolean\n\n
    getInterruptible()\n
    '''
def getActivityStartDate():
    '''returns Date\n\n
    getActivityStartDate()\n
    '''
def setActivityStartDate():
    '''returns None\n\n
    setActivityStartDate(final Date activityStartDate)\n
    '''
def getActivityEndDate():
    '''returns Date\n\n
    getActivityEndDate()\n
    '''
def setActivityEndDate():
    '''returns None\n\n
    setActivityEndDate(final Date activityEndDate)\n
    '''
def getHoursInShift():
    '''returns double\n\n
    getHoursInShift(final Date shiftStartDate, final UserInfo userInfo, final IMXGanttModel model)\n
    '''
def addOverlappingShifts():
    '''returns None\n\n
    addOverlappingShifts(final Shift shift)\n
    '''
def getOverlappingShiftsCount():
    '''returns int\n\n
    getOverlappingShiftsCount()\n
    '''
def getClosestShiftStart():
    '''returns Shift\n\n
    getClosestShiftStart(final Date date)\n
    '''
def compareTo():
    '''returns int\n\n
    compareTo(final WOActivity obj)\n
    '''
def getShifts():
    '''returns ArrayList<Shift>\n\n
    getShifts(final Date shiftStartDate)\n
    '''
def getFractionOverlap():
    '''returns double\n\n
    getFractionOverlap(final Date shiftStartDate, final UserInfo userInfo, final IMXGanttModel model)\n
    '''
