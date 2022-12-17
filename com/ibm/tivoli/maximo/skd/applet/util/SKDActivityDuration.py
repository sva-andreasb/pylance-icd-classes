def ():
    '''returns SKDActivityDuration\n\n
    ()\n
    '''
def getActivityDuration():
    '''returns Object[]\n\n
    getActivityDuration(final Date startDate, Date endDate, final boolean isInterruptable)\n
    '''
def durationBetweenTwoDates():
    '''returns double\n\n
    durationBetweenTwoDates(final Date startDate, final Date endDate, final SKDFormat skdf, final Locale l)\n
    '''
def getWorkingHoursBetweenStartAndEndDates():
    '''returns double\n\n
    getWorkingHoursBetweenStartAndEndDates(final Date startDate, final Date endDate)\n
    '''
def getNonWorkingHoursBetweenStartAndEndDates():
    '''returns double\n\n
    getNonWorkingHoursBetweenStartAndEndDates(final Date startDate, final Date endDate)\n
    '''
def getNWDateListBetweenDates():
    '''returns LinkedHashSet<TreeSet<Date>>\n\n
    getNWDateListBetweenDates(final Date startDate, final Date endDate)\n
    '''
def getActivityStartAndEndDates():
    '''returns IlvTimeInterval\n\n
    getActivityStartAndEndDates(Date startDate, Date endDate, double duration, final boolean isInterruptable)\n
    '''
def getActivityLatestStartAndFinishDates():
    '''returns IlvTimeInterval\n\n
    getActivityLatestStartAndFinishDates(Date startDate, Date endDate, double duration, final boolean isInterruptable)\n
    '''
def isWorkingDate():
    '''returns boolean\n\n
    isWorkingDate(final Date scheduleDate, final boolean isStartTime)\n
    '''
def getFirstAvailableWorkingDate():
    '''returns Date\n\n
    getFirstAvailableWorkingDate(final Date scheduleDate)\n
    '''
