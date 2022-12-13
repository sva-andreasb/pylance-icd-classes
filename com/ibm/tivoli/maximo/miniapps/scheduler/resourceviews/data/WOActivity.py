def WOActivity():
    '''    public WOActivity(final Date activityStartDate, final Date activityEndDate, final double hours, final double resource_qty, final boolean interruptibleFlag, final boolean useOverlappingShifts, final String intShift)
    public WOActivity(final Date activityStartDate, final Date activityEndDate, final double hours, final double resource_qty, final boolean interruptibleFlag, final boolean useOverlappingShifts, final Date intShiftStartTime, final Date intShiftEndTime, final String intShift)
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
def getHoursInShift():
    '''    public double getHoursInShift(final Date shiftStartDate, final UserInfo userInfo, final IMXGanttModel model)
    '''
def addOverlappingShifts():
    '''    public void addOverlappingShifts(final Shift shift)
    '''
def getOverlappingShiftsCount():
    '''    public int getOverlappingShiftsCount()
    '''
def getClosestShiftStart():
    '''    public Shift getClosestShiftStart(final Date date)
    '''
def compareTo():
    '''    public int compareTo(final WOActivity obj)
    '''
def getShifts():
    '''    public ArrayList<Shift> getShifts(final Date shiftStartDate)
    '''
def getFractionOverlap():
    '''    public double getFractionOverlap(final Date shiftStartDate, final UserInfo userInfo, final IMXGanttModel model)
    '''
