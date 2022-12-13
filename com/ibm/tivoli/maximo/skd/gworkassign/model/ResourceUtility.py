MODAVAIL_WORK_COLOR = "String  \"#FFA500\""
MODAVAIL_NONWORK_COLOR = "String  \"#B4CDD6\""
MODAVAIL_NONWORK_FONTCOLOR = "String  \"#00008B\""
def ResourceUtility():
    '''public ResourceUtility()
    '''
def calculateCrewWeekData():
    '''public void calculateCrewWeekData(final IWeekGanttModel schedule, final IMXResource resource, final Date firstDayWeek, final AMCrewRemote crew, final WeekUtility weekUtility, final int week)
    '''
def calculateLaborWeekData():
    '''public void calculateLaborWeekData(final IWeekGanttModel schedule, final IMXResource resource, final Date firstDayWeek, final LaborRemote labor, final WeekUtility weekUtility, final int week)
    '''
def loadCrewPrimaryAndSecondaryCrafts():
    '''public static void loadCrewPrimaryAndSecondaryCrafts(final IMXResource resource, final MboRemote crewType)
    '''
def loadLaborPrimaryAndSecondaryCrafts():
    '''public static void loadLaborPrimaryAndSecondaryCrafts(final IMXResource resource, final MboRemote labor)
    '''
def calculateUnassignWeekData():
    '''public void calculateUnassignWeekData(final GWASchedule schedule, final IMXResource resource, final Date firstDayWeek, final WeekUtility weekUtility, final int week)
    '''
def getUnAssignedHours():
    '''public static double getUnAssignedHours(final boolean insideCurrentDateWorkingTime, final Date rangeStartDateTime, final Date rangeFinishDateTime, final HashMap<String, Activity> unassignactivitiesForResource)
    '''
def getDateTime():
    '''public static Date getDateTime(final Date workdt, final Date sttime)
    '''
