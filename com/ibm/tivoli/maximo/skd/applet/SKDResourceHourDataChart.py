def ():
    '''returns WOActivity\n\n
    (final IlvChart chart, final IlvStairChartRenderer chartRenderder, final ResourceHourViewStyleResolver rhViewStyleResolver)\n
    (final IlvResource resource)\n
    (Date shiftStartDate, Date shiftEndDate)\n
    (final Date activityStartDate, final Date activityEndDate, final double hours, final boolean interruptibleFlag)\n
    '''
def setAppletGanttModel():
    '''returns None\n\n
    setAppletGanttModel(final AppletGanttModel model)\n
    '''
def createDataSet():
    '''returns IlvResourceDataSet\n\n
    createDataSet(final IlvResource resource, final IlvReservationDataPolicy dataPolicy)\n
    '''
def getResourceHourDataSet():
    '''returns ArrayList<IlvDefaultDataSet>\n\n
    getResourceHourDataSet(final IlvResource resource, final IlvDataPoints resourceLoadDataPoints)\n
    '''
def syncGanttModel():
    '''returns None\n\n
    syncGanttModel(final IlvScheduleChart scheduleChart, final int resourceDisplayMode)\n
    '''
def unsyncGanttModel():
    '''returns None\n\n
    unsyncGanttModel()\n
    '''
def getAvailabilityDataSet():
    '''returns ArrayList<IlvDefaultDataSet>\n\n
    getAvailabilityDataSet(final IlvResource resource)\n
    '''
def getActivityResourceMap():
    '''returns IlvDoublePoints\n\n
    getActivityResourceMap(final IlvResource resource)\n
    '''
def isOverlaping():
    '''returns boolean\n\n
    isOverlaping(final WOActivity activity, final Shift shift)\n
    '''
def dataSetContentsChanged():
    '''returns None\n\n
    dataSetContentsChanged(final DataSetContentsEvent dataSetContentsEvent)\n
    '''
def dataSetPropertyChanged():
    '''returns None\n\n
    dataSetPropertyChanged(final DataSetPropertyEvent arg0)\n
    '''
def selectionChanged():
    '''returns None\n\n
    selectionChanged(final SelectionEvent event)\n
    '''
def getShiftStartDate():
    '''returns Date\n\n
    getShiftStartDate()\n
    '''
def setShiftStartDate():
    '''returns None\n\n
    setShiftStartDate(final Date shiftStartDate)\n
    '''
def getShiftEndDate():
    '''returns Date\n\n
    getShiftEndDate()\n
    '''
def setShiftEndDate():
    '''returns None\n\n
    setShiftEndDate(final Date shiftEndDate)\n
    '''
def compareTo():
    '''returns int\n\n
    compareTo(final Object obj)\n
    compareTo(final Object obj)\n
    '''
def getOverlappingShifts():
    '''returns ArrayList<Shift>\n\n
    getOverlappingShifts()\n
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
def getHours():
    '''returns double\n\n
    getHours()\n
    '''
def getHoursInShift():
    '''returns double\n\n
    getHoursInShift(final Date shiftStartDate)\n
    '''
def setHours():
    '''returns None\n\n
    setHours(final double hours)\n
    '''
def addOverlappingShifts():
    '''returns None\n\n
    addOverlappingShifts(final Shift shift)\n
    '''
def getShifts():
    '''returns ArrayList<Shift>\n\n
    getShifts(final Date shiftStartDate)\n
    '''
def getFractionOverlap():
    '''returns double\n\n
    getFractionOverlap(final Date shiftStartDate)\n
    '''
