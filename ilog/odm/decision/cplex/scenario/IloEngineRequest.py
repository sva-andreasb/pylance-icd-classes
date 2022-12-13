COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
DO_NOTHING_REQUEST = "int  0"
SOLVE_REQUEST = "int  1"
SOLVE_ANYWAY_REQUEST = "int  2"
FIND_GOAL_BOUNDS_REQUEST = "int  4"
def IloEngineRequest():
    '''    public IloEngineRequest(final int requestType)
    public IloEngineRequest(final IloTable table)
    '''
def isEqualWith():
    '''    public boolean isEqualWith(final IloComparable oth)
    '''
def getType():
    '''    public int getType()
    '''
def setType():
    '''    public void setType(final int engineRequestType)
    '''
def getGoalId():
    '''    public String getGoalId()
    '''
def setGoalId():
    '''    public void setGoalId(final String goalId)
    '''
def findBestGoalBound():
    '''    public boolean findBestGoalBound()
    '''
def setFindBestGoalBound():
    '''    public void setFindBestGoalBound(final boolean isFindMaxGoalBound)
    '''
def setSolvingTimeLimit():
    '''    public void setSolvingTimeLimit(final int timeInSecond)
    '''
def getSolvingTimeLimit():
    '''    public int getSolvingTimeLimit()
    '''
def getTable():
    '''    public IloTable getTable()
    '''
def getIgnoredPriority():
    '''    public String getIgnoredPriority()
    '''
def setIgnoredPriority():
    '''    public void setIgnoredPriority(final String priorty)
    '''
def isSearchBoundsRequest():
    '''    public boolean isSearchBoundsRequest()
    '''
