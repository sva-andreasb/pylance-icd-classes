def ():
    '''returns SKDActivityDuration\n\n
    (final UserInfo userInfo, final IMXGanttModel model)\n
    '''
def getActivityDuration():
    '''returns Object[]\n\n
    getActivityDuration(final Date startDate, Date endDate, final boolean isInterruptable)\n
    '''
def durationBetweenTwoDates():
    '''returns double\n\n
    durationBetweenTwoDates(final Date startTime, final Date endTime)\n
    '''
def getWorkingHoursBetweenStartAndEndDates():
    '''returns double\n\n
    getWorkingHoursBetweenStartAndEndDates(final Date startDate, final Date endDate)\n
    '''
def getWorkingHoursBetweenStartAndEndDatesForShift():
    '''returns double\n\n
    getWorkingHoursBetweenStartAndEndDatesForShift(final String shift, final Date startDate, final Date endDate)\n
    '''
def getNonWorkingHoursBetweenStartAndEndDates():
    '''returns double\n\n
    getNonWorkingHoursBetweenStartAndEndDates(final Date startDate, final Date endDate)\n
    '''
def getNonWorkingHoursBetweenStartAndEndDatesForShift():
    '''returns double\n\n
    getNonWorkingHoursBetweenStartAndEndDatesForShift(final String shift, final Date startDate, final Date endDate)\n
    '''
def getNonWorkingHours():
    '''returns double\n\n
    getNonWorkingHours(final ArrayList<Date> mergedNonWorkPeriods, final Date startDate, final Date endDate)\n
    '''
def getNWDateListBetweenDates():
    '''returns LinkedHashSet<TreeSet<Date>>\n\n
    getNWDateListBetweenDates(final Date startDate, final Date endDate)\n
    '''
def getNWDateRangeListBetweenDates():
    '''returns List<Range<Date>>\n\n
    getNWDateRangeListBetweenDates(final Date startDate, final Date endDate)\n
    '''
def getNWDateRangeListBetweenDatesForShift():
    '''returns List<Range<Date>>\n\n
    getNWDateRangeListBetweenDatesForShift(final String shiftnum, final Date startDate, final Date endDate)\n
    '''
def getNWDateRangeList():
    '''returns List<Range<Date>>\n\n
    getNWDateRangeList(final ArrayList<Date> nonWorkPeriods, final Date startDate, final Date endDate)\n
    '''
def getActivityStartAndEndDates():
    '''returns IlvTimeInterval\n\n
    getActivityStartAndEndDates(final Date startDate, final Date endDate, final double duration, final boolean isInterruptable, final String intshift)\n
    getActivityStartAndEndDates(Date startDate, Date endDate, double duration, final boolean isInterruptable, final ArrayList<Date> mergedNonWorkPeriods)\n
    '''
def getFirstAvailableWorkingDate():
    '''returns Date\n\n
    getFirstAvailableWorkingDate(final Date scheduleDate)\n
    getFirstAvailableWorkingDate(final Date scheduleDate, final String intShift)\n
    '''
def getPreviousAvailableWorkingDate():
    '''returns Date\n\n
    getPreviousAvailableWorkingDate(final Date scheduleDate)\n
    getPreviousAvailableWorkingDate(final Date scheduleDate, final String intShift)\n
    '''
def getShiftEnd():
    '''returns Date\n\n
    getShiftEnd(final Date scheduleDate)\n
    getShiftEnd(final Date scheduleDate, final String intShift)\n
    '''
def getNextShift():
    '''returns Date\n\n
    getNextShift(final Date scheduleDate)\n
    getNextShift(final Date scheduleDate, final String intShift)\n
    '''
def getActivityLatestStartAndFinishDates():
    '''returns IlvTimeInterval\n\n
    getActivityLatestStartAndFinishDates(final Date startDate, final Date endDate, final double duration, final boolean isInterruptable, final String intshift)\n
    getActivityLatestStartAndFinishDates(Date startDate, Date endDate, double duration, final boolean isInterruptable, final ArrayList<Date> mergedNonWorkPeriods)\n
    '''
def getShiftWorkPeriod():
    '''returns ArrayList<Date>\n\n
    getShiftWorkPeriod(final String shift, final IMXGanttModel model)\n
    '''
def getNonInterruptableActivitiesCalendarBreaksDuration():
    '''returns double\n\n
    getNonInterruptableActivitiesCalendarBreaksDuration()\n
    '''
def isWorkingDate():
    '''returns boolean\n\n
    isWorkingDate(final Date scheduleDate, final String intShift)\n
    isWorkingDate(final Date scheduleDate)\n
    '''
def addWorkingHours():
    '''returns Date\n\n
    addWorkingHours(final Date date, final double workingHours, final boolean isInterruptible)\n
    addWorkingHours(Date date, final double workingHours, final boolean isInterruptible, final boolean convertUserTimeZone)\n
    addWorkingHours(final Date date, final double workingHours, final boolean isInterruptible, final String intShift)\n
    addWorkingHours(Date date, final double workingHours, final boolean isInterruptible, final String intShift, final boolean convertUserTimeZone)\n
    '''
def subtractWorkingHours():
    '''returns Date\n\n
    subtractWorkingHours(final Date date, final double workingHours, final boolean isInterruptible, final String intShift)\n
    subtractWorkingHours(Date date, final double workingHours, final boolean isInterruptible, final String intShift, final boolean convertUserTimeZone)\n
    subtractWorkingHours(final Date date, final double workingHours, final boolean isInterruptible)\n
    subtractWorkingHours(Date date, final double workingHours, final boolean isInterruptible, final boolean convertUserTimeZone)\n
    '''
