def setLogger():
    '''public static void setLogger(final MXLogger logger)
    '''
def getLogger():
    '''public static MXLogger getLogger()
    '''
def isTodayCalendarHoliday():
    '''public static boolean isTodayCalendarHoliday(final Date now, final ReferencePointData refPointData)
    public static boolean isTodayCalendarHoliday(final Date now, final EscalationData escalationData, final MboRemote escalationMbo)
    '''
def isRefPointEscalationWithinCalendarBoundary():
    '''public static boolean isRefPointEscalationWithinCalendarBoundary(final Date now, final ReferencePointData refPointData)
    '''
def isInBoundary():
    '''public static boolean isInBoundary(final MboRemote workPeriod, final Date now)
    '''
def isCalendarBasedRefPointReadyToFire():
    '''public static boolean isCalendarBasedRefPointReadyToFire(final Date now, final ReferencePointData refPointData)
    '''
def getRealEndCalendar():
    '''public static Calendar getRealEndCalendar(final MboRemote workPeriod)
    '''
