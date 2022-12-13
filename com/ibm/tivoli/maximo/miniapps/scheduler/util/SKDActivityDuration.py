def SKDActivityDuration():
    '''public SKDActivityDuration(final UserInfo userInfo, final IMXGanttModel model)
    '''
def getActivityDuration():
    '''public Object[] getActivityDuration(final Date startDate, Date endDate, final boolean isInterruptable)
    '''
def durationBetweenTwoDates():
    '''public double durationBetweenTwoDates(final Date startTime, final Date endTime)
    '''
def getWorkingHoursBetweenStartAndEndDates():
    '''public double getWorkingHoursBetweenStartAndEndDates(final Date startDate, final Date endDate)
    '''
def getWorkingHoursBetweenStartAndEndDatesForShift():
    '''public double getWorkingHoursBetweenStartAndEndDatesForShift(final String shift, final Date startDate, final Date endDate)
    '''
def getNonWorkingHoursBetweenStartAndEndDates():
    '''public double getNonWorkingHoursBetweenStartAndEndDates(final Date startDate, final Date endDate)
    '''
def getNonWorkingHoursBetweenStartAndEndDatesForShift():
    '''public double getNonWorkingHoursBetweenStartAndEndDatesForShift(final String shift, final Date startDate, final Date endDate)
    '''
def getNonWorkingHours():
    '''public double getNonWorkingHours(final ArrayList<Date> mergedNonWorkPeriods, final Date startDate, final Date endDate)
    '''
def getNWDateListBetweenDates():
    '''public LinkedHashSet<TreeSet<Date>> getNWDateListBetweenDates(final Date startDate, final Date endDate)
    '''
def getNWDateRangeListBetweenDates():
    '''public List<Range<Date>> getNWDateRangeListBetweenDates(final Date startDate, final Date endDate)
    '''
def getNWDateRangeListBetweenDatesForShift():
    '''public List<Range<Date>> getNWDateRangeListBetweenDatesForShift(final String shiftnum, final Date startDate, final Date endDate)
    '''
def getNWDateRangeList():
    '''public List<Range<Date>> getNWDateRangeList(final ArrayList<Date> nonWorkPeriods, final Date startDate, final Date endDate)
    '''
def getActivityStartAndEndDates():
    '''public IlvTimeInterval getActivityStartAndEndDates(final Date startDate, final Date endDate, final double duration, final boolean isInterruptable, final String intshift)
    public IlvTimeInterval getActivityStartAndEndDates(Date startDate, Date endDate, double duration, final boolean isInterruptable, final ArrayList<Date> mergedNonWorkPeriods)
    '''
def getFirstAvailableWorkingDate():
    '''public Date getFirstAvailableWorkingDate(final Date scheduleDate)
    public Date getFirstAvailableWorkingDate(final Date scheduleDate, final String intShift)
    '''
def getPreviousAvailableWorkingDate():
    '''public Date getPreviousAvailableWorkingDate(final Date scheduleDate)
    public Date getPreviousAvailableWorkingDate(final Date scheduleDate, final String intShift)
    '''
def getShiftEnd():
    '''public Date getShiftEnd(final Date scheduleDate)
    public Date getShiftEnd(final Date scheduleDate, final String intShift)
    '''
def getNextShift():
    '''public Date getNextShift(final Date scheduleDate)
    public Date getNextShift(final Date scheduleDate, final String intShift)
    '''
def getActivityLatestStartAndFinishDates():
    '''public IlvTimeInterval getActivityLatestStartAndFinishDates(final Date startDate, final Date endDate, final double duration, final boolean isInterruptable, final String intshift)
    public IlvTimeInterval getActivityLatestStartAndFinishDates(Date startDate, Date endDate, double duration, final boolean isInterruptable, final ArrayList<Date> mergedNonWorkPeriods)
    '''
def getShiftWorkPeriod():
    '''public ArrayList<Date> getShiftWorkPeriod(final String shift, final IMXGanttModel model)
    '''
def getNonInterruptableActivitiesCalendarBreaksDuration():
    '''public double getNonInterruptableActivitiesCalendarBreaksDuration()
    '''
def isWorkingDate():
    '''public boolean isWorkingDate(final Date scheduleDate, final String intShift)
    public boolean isWorkingDate(final Date scheduleDate)
    '''
def addWorkingHours():
    '''public Date addWorkingHours(final Date date, final double workingHours, final boolean isInterruptible)
    public Date addWorkingHours(Date date, final double workingHours, final boolean isInterruptible, final boolean convertUserTimeZone)
    public Date addWorkingHours(final Date date, final double workingHours, final boolean isInterruptible, final String intShift)
    public Date addWorkingHours(Date date, final double workingHours, final boolean isInterruptible, final String intShift, final boolean convertUserTimeZone)
    '''
def subtractWorkingHours():
    '''public Date subtractWorkingHours(final Date date, final double workingHours, final boolean isInterruptible, final String intShift)
    public Date subtractWorkingHours(Date date, final double workingHours, final boolean isInterruptible, final String intShift, final boolean convertUserTimeZone)
    public Date subtractWorkingHours(final Date date, final double workingHours, final boolean isInterruptible)
    public Date subtractWorkingHours(Date date, final double workingHours, final boolean isInterruptible, final boolean convertUserTimeZone)
    '''
