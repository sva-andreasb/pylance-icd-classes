COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
DO_NOTHING_REQUEST = "int  0"
SOLVE_REQUEST = "int  1"
SOLVE_ANYWAY_REQUEST = "int  2"
FIND_GOAL_BOUNDS_REQUEST = "int  4"
def ():
    '''returns IloEngineRequest\n\n
    (final int requestType)\n
    (final IloTable table)\n
    '''
def isEqualWith():
    '''returns boolean\n\n
    isEqualWith(final IloComparable oth)\n
    '''
def getType():
    '''returns int\n\n
    getType()\n
    '''
def setType():
    '''returns None\n\n
    setType(final int engineRequestType)\n
    '''
def getGoalId():
    '''returns String\n\n
    getGoalId()\n
    '''
def setGoalId():
    '''returns None\n\n
    setGoalId(final String goalId)\n
    '''
def findBestGoalBound():
    '''returns boolean\n\n
    findBestGoalBound()\n
    '''
def setFindBestGoalBound():
    '''returns None\n\n
    setFindBestGoalBound(final boolean isFindMaxGoalBound)\n
    '''
def setSolvingTimeLimit():
    '''returns None\n\n
    setSolvingTimeLimit(final int timeInSecond)\n
    '''
def getSolvingTimeLimit():
    '''returns int\n\n
    getSolvingTimeLimit()\n
    '''
def getTable():
    '''returns IloTable\n\n
    getTable()\n
    '''
def getIgnoredPriority():
    '''returns String\n\n
    getIgnoredPriority()\n
    '''
def setIgnoredPriority():
    '''returns None\n\n
    setIgnoredPriority(final String priorty)\n
    '''
def isSearchBoundsRequest():
    '''returns boolean\n\n
    isSearchBoundsRequest()\n
    '''
