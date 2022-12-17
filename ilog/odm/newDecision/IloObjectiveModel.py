COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def ():
    '''returns IloObjectiveModel\n\n
    (final IloGoalsDesc descs)\n
    '''
def getModelGoalByName():
    '''returns IloGoalModel\n\n
    getModelGoalByName(final String id)\n
    '''
def hasGoals():
    '''returns boolean\n\n
    hasGoals()\n
    '''
def makeObjective():
    '''returns None\n\n
    makeObjective(final IloOplModel oplModel, final IloModeler modeler, final IloEngineRequest request, final IloScenario currentScenario, final IloIssueReporter reporter)\n
    '''
def updateOneGoal():
    '''returns None\n\n
    updateOneGoal(final String goalId, final Double newWeight, final Boolean newActive)\n
    '''
def getVisibleGoals():
    '''returns Iterator<IloGoalModel>\n\n
    getVisibleGoals()\n
    '''
def remove():
    '''returns None\n\n
    remove()\n
    '''
def hasNext():
    '''returns boolean\n\n
    hasNext()\n
    '''
def next():
    '''returns IloGoalModel\n\n
    next()\n
    '''
