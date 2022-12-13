COPYRIGHT_NOTICE = "String  Copyright IBM Corporation 2005,2012""
DO_NOTHING_REQUEST = "int  0"
SOLVE_REQUEST = "int  1"
SOLVE_ANYWAY_REQUEST = "int  2"
FIND_GOAL_BOUNDS_REQUEST = "int  4"
def IloEngineRequest():
'''public IloEngineRequest(final int requestType)
public IloEngineRequest(final IloTable table)
'''
pass
def isEqualWith():
'''public boolean isEqualWith(final IloComparable oth)
'''
pass
def getType():
'''public int getType()
'''
pass
def setType():
'''public void setType(final int engineRequestType)
'''
pass
def getGoalId():
'''public String getGoalId()
'''
pass
def setGoalId():
'''public void setGoalId(final String goalId)
'''
pass
def findBestGoalBound():
'''public boolean findBestGoalBound()
'''
pass
def setFindBestGoalBound():
'''public void setFindBestGoalBound(final boolean isFindMaxGoalBound)
'''
pass
def setSolvingTimeLimit():
'''public void setSolvingTimeLimit(final int timeInSecond)
'''
pass
def getSolvingTimeLimit():
'''public int getSolvingTimeLimit()
'''
pass
def getTable():
'''public IloTable getTable()
'''
pass
def getIgnoredPriority():
'''public String getIgnoredPriority()
'''
pass
def setIgnoredPriority():
'''public void setIgnoredPriority(final String priorty)
'''
pass
def isSearchBoundsRequest():
'''public boolean isSearchBoundsRequest()
'''
pass
