def SKDActivityDuration():
    '''public SKDActivityDuration()
    '''
def getSKDActivityDuration():
    '''public static synchronized SKDActivityDuration getSKDActivityDuration()
    '''
def getActivityDuration():
    '''public Object[] getActivityDuration(final Date startDate, Date endDate, final boolean isInterruptable)
    '''
def durationBetweenTwoDates():
    '''public double durationBetweenTwoDates(final Date startDate, final Date endDate, final SKDFormat skdf, final Locale l)
    '''
def getWorkingHoursBetweenStartAndEndDates():
    '''public double getWorkingHoursBetweenStartAndEndDates(final Date startDate, final Date endDate)
    '''
def getNonWorkingHoursBetweenStartAndEndDates():
    '''public double getNonWorkingHoursBetweenStartAndEndDates(final Date startDate, final Date endDate)
    '''
def getNWDateListBetweenDates():
    '''public LinkedHashSet<TreeSet<Date>> getNWDateListBetweenDates(final Date startDate, final Date endDate)
    '''
def getActivityStartAndEndDates():
    '''public IlvTimeInterval getActivityStartAndEndDates(Date startDate, Date endDate, double duration, final boolean isInterruptable)
    '''
def getActivityLatestStartAndFinishDates():
    '''public IlvTimeInterval getActivityLatestStartAndFinishDates(Date startDate, Date endDate, double duration, final boolean isInterruptable)
    '''
def getStartEndMap():
    '''public static TreeMap<Date, Date> getStartEndMap(final Locale l, final TimeZone tz, final ArrayList<Date> mergedNonWorkPeriods)
    '''
def convertDateToUserTZ():
    '''public static Date convertDateToUserTZ(final Date d, final Locale userLocale, final TimeZone userTimeZone)
    '''
def isWorkingDate():
    '''public boolean isWorkingDate(final Date scheduleDate, final boolean isStartTime)
    '''
def getFirstAvailableWorkingDate():
    '''public Date getFirstAvailableWorkingDate(final Date scheduleDate)
    '''
