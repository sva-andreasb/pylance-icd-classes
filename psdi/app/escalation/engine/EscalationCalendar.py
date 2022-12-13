def setLogger():
    '''    public static void setLogger(final MXLogger logger)
    '''
def getLogger():
    '''    public static MXLogger getLogger()
    '''
def calculateNewElapsedTime():
    '''    public static long calculateNewElapsedTime(final Date now, final ReferencePointData refPointData)
    '''
def getSLARefPointConditionPastTargetDate():
    '''    public static String getSLARefPointConditionPastTargetDate(final Date now, final ReferencePointData refPointData)
    '''
def getSLARefPointCondition():
    '''    public static String getSLARefPointCondition(final Date now, final ReferencePointData refPointData)
    '''
def isRefPointEscalationWithinCalendarBoundary():
    '''    public static boolean isRefPointEscalationWithinCalendarBoundary(final Date now, final ReferencePointData refPointData)
    '''
def isEscalationWithinCalendarBoundary():
    '''    public static boolean isEscalationWithinCalendarBoundary(final Date now, final EscalationData escalationData, final MboRemote escalationMbo)
    '''
def calculateTimeLeftForTodaysShift():
    '''    public static long calculateTimeLeftForTodaysShift(final MboRemote workPeriod, final Date now)
    '''
def calculateTimeLeftBeforeTarget():
    '''    public static long calculateTimeLeftBeforeTarget(final MboRemote workPeriod, final Date targetDate)
    '''
def isInBoundary():
    '''    public static boolean isInBoundary(final MboRemote workPeriod, final Date now)
    '''
def getShiftType():
    '''    public static int getShiftType(final MboRemote workPeriod)
    '''
