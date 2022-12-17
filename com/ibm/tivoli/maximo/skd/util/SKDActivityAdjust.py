def ():
    '''returns SKDActivityAdjust\n\n
    (final Locale l, final TimeZone tz)\n
    '''
def adjustActivityForMergedShiftList():
    '''returns None\n\n
    adjustActivityForMergedShiftList(final MXActivity activity, final MXGanttModel model)\n
    adjustActivityForMergedShiftList(final Activity activity, final Schedule schedule)\n
    '''
def getActivityStartAndEndDates():
    '''returns IlvTimeInterval\n\n
    getActivityStartAndEndDates(Date startDate, Date endDate, double duration, final ArrayList<Date> mergedNonWorkPeriods)\n
    '''
def getShiftWorkPeriod():
    '''returns ArrayList<Date>\n\n
    getShiftWorkPeriod(final String shift, final MXGanttModel model, final boolean shiftDate)\n
    getShiftWorkPeriod(final String shift, final Schedule schedule, final boolean shiftDate)\n
    '''
def getNonWorkingHours():
    '''returns double\n\n
    getNonWorkingHours(final ArrayList<Date> mergedNonWorkPeriods, final Date startDate, final Date endDate)\n
    '''
def getShiftEnd():
    '''returns Date\n\n
    getShiftEnd(final Date scheduleDate, final Schedule schedule)\n
    '''
def addWorkingHours():
    '''returns Date\n\n
    addWorkingHours(final Schedule schedule, Date date, final double workingHours, final boolean isInterruptible)\n
    '''
def subtractWorkingHours():
    '''returns Date\n\n
    subtractWorkingHours(final Schedule schedule, Date date, final double workingHours, final boolean isInterruptible)\n
    '''
def getFirstAvailableWorkingDate():
    '''returns Date\n\n
    getFirstAvailableWorkingDate(final Date scheduleDate, final Schedule schedule)\n
    '''
def getPreviousAvailableWorkingDate():
    '''returns Date\n\n
    getPreviousAvailableWorkingDate(final Date scheduleDate, final Schedule schedule)\n
    '''
def isWorkingDate():
    '''returns boolean\n\n
    isWorkingDate(final Date scheduleDate, final Schedule schedule)\n
    '''
def getWorkingHoursBetweenStartAndEndDates():
    '''returns double\n\n
    getWorkingHoursBetweenStartAndEndDates(final Schedule schedule, final Date startDate, final Date endDate)\n
    '''
def getNonWorkingHoursBetweenStartAndEndDates():
    '''returns double\n\n
    getNonWorkingHoursBetweenStartAndEndDates(final Schedule schedule, final Date startDate, final Date endDate)\n
    '''
