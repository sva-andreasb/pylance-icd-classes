def SKDResourceHourDataChart():
    '''    public SKDResourceHourDataChart(final IlvChart chart, final IlvStairChartRenderer chartRenderder, final ResourceHourViewStyleResolver rhViewStyleResolver)
    '''
def setAppletGanttModel():
    '''    public void setAppletGanttModel(final AppletGanttModel model)
    '''
def createDataSet():
    '''    public IlvResourceDataSet createDataSet(final IlvResource resource, final IlvReservationDataPolicy dataPolicy)
    '''
def getResourceHourDataSet():
    '''    public ArrayList<IlvDefaultDataSet> getResourceHourDataSet(final IlvResource resource, final IlvDataPoints resourceLoadDataPoints)
    '''
def syncGanttModel():
    '''    public void syncGanttModel(final IlvScheduleChart scheduleChart, final int resourceDisplayMode)
    '''
def unsyncGanttModel():
    '''    public void unsyncGanttModel()
    '''
def getAvailabilityDataSet():
    '''    public ArrayList<IlvDefaultDataSet> getAvailabilityDataSet(final IlvResource resource)
    '''
def getActivityResourceMap():
    '''    public IlvDoublePoints getActivityResourceMap(final IlvResource resource)
    '''
def isOverlaping():
    '''    public boolean isOverlaping(final WOActivity activity, final Shift shift)
    '''
def ResourceDataSetListener():
    '''    public ResourceDataSetListener(final IlvResource resource)
    '''
def dataSetContentsChanged():
    '''    public void dataSetContentsChanged(final DataSetContentsEvent dataSetContentsEvent)
    '''
def dataSetPropertyChanged():
    '''    public void dataSetPropertyChanged(final DataSetPropertyEvent arg0)
    '''
def selectionChanged():
    '''    public void selectionChanged(final SelectionEvent event)
    '''
def Shift():
    '''    public Shift(Date shiftStartDate, Date shiftEndDate)
    '''
def getShiftStartDate():
    '''    public Date getShiftStartDate()
    '''
def setShiftStartDate():
    '''    public void setShiftStartDate(final Date shiftStartDate)
    '''
def getShiftEndDate():
    '''    public Date getShiftEndDate()
    '''
def setShiftEndDate():
    '''    public void setShiftEndDate(final Date shiftEndDate)
    '''
def compareTo():
    '''    public int compareTo(final Object obj)
    public int compareTo(final Object obj)
    '''
def getOverlappingShifts():
    '''    public ArrayList<Shift> getOverlappingShifts()
    '''
def WOActivity():
    '''    public WOActivity(final Date activityStartDate, final Date activityEndDate, final double hours, final boolean interruptibleFlag)
    '''
def getInterruptible():
    '''    public boolean getInterruptible()
    '''
def getActivityStartDate():
    '''    public Date getActivityStartDate()
    '''
def setActivityStartDate():
    '''    public void setActivityStartDate(final Date activityStartDate)
    '''
def getActivityEndDate():
    '''    public Date getActivityEndDate()
    '''
def setActivityEndDate():
    '''    public void setActivityEndDate(final Date activityEndDate)
    '''
def getHours():
    '''    public double getHours()
    '''
def getHoursInShift():
    '''    public double getHoursInShift(final Date shiftStartDate)
    '''
def setHours():
    '''    public void setHours(final double hours)
    '''
def addOverlappingShifts():
    '''    public void addOverlappingShifts(final Shift shift)
    '''
def getShifts():
    '''    public ArrayList<Shift> getShifts(final Date shiftStartDate)
    '''
def getFractionOverlap():
    '''    public double getFractionOverlap(final Date shiftStartDate)
    '''
