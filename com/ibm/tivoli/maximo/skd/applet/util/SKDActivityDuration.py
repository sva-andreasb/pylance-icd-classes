def SKDActivityDuration():
'''public SKDActivityDuration()
'''
pass
def getSKDActivityDuration():
'''public static synchronized SKDActivityDuration getSKDActivityDuration()
'''
pass
def getActivityDuration():
'''public Object[] getActivityDuration(final Date startDate, Date endDate, final boolean isInterruptable)
'''
pass
def durationBetweenTwoDates():
'''public double durationBetweenTwoDates(final Date startDate, final Date endDate, final SKDFormat skdf, final Locale l)
'''
pass
def getWorkingHoursBetweenStartAndEndDates():
'''public double getWorkingHoursBetweenStartAndEndDates(final Date startDate, final Date endDate)
'''
pass
def getNonWorkingHoursBetweenStartAndEndDates():
'''public double getNonWorkingHoursBetweenStartAndEndDates(final Date startDate, final Date endDate)
'''
pass
def getNWDateListBetweenDates():
'''public LinkedHashSet<TreeSet<Date>> getNWDateListBetweenDates(final Date startDate, final Date endDate)
'''
pass
def getActivityStartAndEndDates():
'''public IlvTimeInterval getActivityStartAndEndDates(Date startDate, Date endDate, double duration, final boolean isInterruptable)
'''
pass
def getActivityLatestStartAndFinishDates():
'''public IlvTimeInterval getActivityLatestStartAndFinishDates(Date startDate, Date endDate, double duration, final boolean isInterruptable)
'''
pass
def getStartEndMap():
'''public static TreeMap<Date, Date> getStartEndMap(final Locale l, final TimeZone tz, final ArrayList<Date> mergedNonWorkPeriods)
'''
pass
def convertDateToUserTZ():
'''public static Date convertDateToUserTZ(final Date d, final Locale userLocale, final TimeZone userTimeZone)
'''
pass
def isWorkingDate():
'''public boolean isWorkingDate(final Date scheduleDate, final boolean isStartTime)
'''
pass
def getFirstAvailableWorkingDate():
'''public Date getFirstAvailableWorkingDate(final Date scheduleDate)
'''
pass
