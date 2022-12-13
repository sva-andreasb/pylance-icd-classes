def SKDResourceHourDataChart():
'''public SKDResourceHourDataChart(final IlvChart chart, final IlvStairChartRenderer chartRenderder, final ResourceHourViewStyleResolver rhViewStyleResolver)
'''
pass
def setAppletGanttModel():
'''public void setAppletGanttModel(final AppletGanttModel model)
'''
pass
def createDataSet():
'''public IlvResourceDataSet createDataSet(final IlvResource resource, final IlvReservationDataPolicy dataPolicy)
'''
pass
def getResourceHourDataSet():
'''public ArrayList<IlvDefaultDataSet> getResourceHourDataSet(final IlvResource resource, final IlvDataPoints resourceLoadDataPoints)
'''
pass
def syncGanttModel():
'''public void syncGanttModel(final IlvScheduleChart scheduleChart, final int resourceDisplayMode)
'''
pass
def unsyncGanttModel():
'''public void unsyncGanttModel()
'''
pass
def getAvailabilityDataSet():
'''public ArrayList<IlvDefaultDataSet> getAvailabilityDataSet(final IlvResource resource)
'''
pass
def getActivityResourceMap():
'''public IlvDoublePoints getActivityResourceMap(final IlvResource resource)
'''
pass
def isOverlaping():
'''public boolean isOverlaping(final WOActivity activity, final Shift shift)
'''
pass
def ResourceDataSetListener():
'''public ResourceDataSetListener(final IlvResource resource)
'''
pass
def dataSetContentsChanged():
'''public void dataSetContentsChanged(final DataSetContentsEvent dataSetContentsEvent)
'''
pass
def dataSetPropertyChanged():
'''public void dataSetPropertyChanged(final DataSetPropertyEvent arg0)
'''
pass
def selectionChanged():
'''public void selectionChanged(final SelectionEvent event)
'''
pass
def Shift():
'''public Shift(Date shiftStartDate, Date shiftEndDate)
'''
pass
def getShiftStartDate():
'''public Date getShiftStartDate()
'''
pass
def setShiftStartDate():
'''public void setShiftStartDate(final Date shiftStartDate)
'''
pass
def getShiftEndDate():
'''public Date getShiftEndDate()
'''
pass
def setShiftEndDate():
'''public void setShiftEndDate(final Date shiftEndDate)
'''
pass
def compareTo():
'''public int compareTo(final Object obj)
public int compareTo(final Object obj)
'''
pass
def getOverlappingShifts():
'''public ArrayList<Shift> getOverlappingShifts()
'''
pass
def WOActivity():
'''public WOActivity(final Date activityStartDate, final Date activityEndDate, final double hours, final boolean interruptibleFlag)
'''
pass
def getInterruptible():
'''public boolean getInterruptible()
'''
pass
def getActivityStartDate():
'''public Date getActivityStartDate()
'''
pass
def setActivityStartDate():
'''public void setActivityStartDate(final Date activityStartDate)
'''
pass
def getActivityEndDate():
'''public Date getActivityEndDate()
'''
pass
def setActivityEndDate():
'''public void setActivityEndDate(final Date activityEndDate)
'''
pass
def getHours():
'''public double getHours()
'''
pass
def getHoursInShift():
'''public double getHoursInShift(final Date shiftStartDate)
'''
pass
def setHours():
'''public void setHours(final double hours)
'''
pass
def addOverlappingShifts():
'''public void addOverlappingShifts(final Shift shift)
'''
pass
def getShifts():
'''public ArrayList<Shift> getShifts(final Date shiftStartDate)
'''
pass
def getFractionOverlap():
'''public double getFractionOverlap(final Date shiftStartDate)
'''
pass
