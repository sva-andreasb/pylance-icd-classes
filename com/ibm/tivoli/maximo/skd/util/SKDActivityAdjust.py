def SKDActivityAdjust():
'''public SKDActivityAdjust(final Locale l, final TimeZone tz)
'''
pass
def adjustActivityForMergedShiftList():
'''public void adjustActivityForMergedShiftList(final MXActivity activity, final MXGanttModel model)
public void adjustActivityForMergedShiftList(final Activity activity, final Schedule schedule)
'''
pass
def getActivityStartAndEndDates():
'''public IlvTimeInterval getActivityStartAndEndDates(Date startDate, Date endDate, double duration, final ArrayList<Date> mergedNonWorkPeriods)
'''
pass
def getShiftWorkPeriod():
'''public ArrayList<Date> getShiftWorkPeriod(final String shift, final MXGanttModel model, final boolean shiftDate)
public ArrayList<Date> getShiftWorkPeriod(final String shift, final Schedule schedule, final boolean shiftDate)
'''
pass
def getNonWorkingHours():
'''public double getNonWorkingHours(final ArrayList<Date> mergedNonWorkPeriods, final Date startDate, final Date endDate)
'''
pass
def getShiftEnd():
'''public Date getShiftEnd(final Date scheduleDate, final Schedule schedule)
'''
pass
def addWorkingHours():
'''public Date addWorkingHours(final Schedule schedule, Date date, final double workingHours, final boolean isInterruptible)
'''
pass
def subtractWorkingHours():
'''public Date subtractWorkingHours(final Schedule schedule, Date date, final double workingHours, final boolean isInterruptible)
'''
pass
def getFirstAvailableWorkingDate():
'''public Date getFirstAvailableWorkingDate(final Date scheduleDate, final Schedule schedule)
'''
pass
def getPreviousAvailableWorkingDate():
'''public Date getPreviousAvailableWorkingDate(final Date scheduleDate, final Schedule schedule)
'''
pass
def isWorkingDate():
'''public boolean isWorkingDate(final Date scheduleDate, final Schedule schedule)
'''
pass
def getWorkingHoursBetweenStartAndEndDates():
'''public double getWorkingHoursBetweenStartAndEndDates(final Schedule schedule, final Date startDate, final Date endDate)
'''
pass
def getNonWorkingHoursBetweenStartAndEndDates():
'''public double getNonWorkingHoursBetweenStartAndEndDates(final Schedule schedule, final Date startDate, final Date endDate)
'''
pass
