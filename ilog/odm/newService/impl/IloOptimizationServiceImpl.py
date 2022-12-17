COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def ():
    '''returns IloOptimizationServiceImpl\n\n
    (final IloOPLIDEInterface ideInterface, final IloApplicationContext applicationContext)\n
    '''
def setSolveEngineFactory():
    '''returns None\n\n
    setSolveEngineFactory(final IloOplDecisionEngineFactory engineFactory)\n
    '''
def solve():
    '''returns boolean\n\n
    solve(final IloScenario scenario, final int timeLimit, final boolean withRelaxation)\n
    '''
def execute():
    '''returns boolean\n\n
    execute(final IloEnginePilot enginePilot, final IloOplDecisionEngine engine, final IloScenario scenario, final IloIssueReporter issueReporter)\n
    execute(final IloEnginePilot enginePilot, final IloOplDecisionEngine engine, final IloScenario scenario, final IloIssueReporter issueReporter)\n
    '''
def findGoalBounds():
    '''returns boolean\n\n
    findGoalBounds(final IloScenario scenario, final String goalId, final String ignoredPriorityLevel, final int timeLimit)\n
    '''
def generateRequirementsPreview():
    '''returns IloTable\n\n
    generateRequirementsPreview(final IloScenario scenario, final boolean solve)\n
    '''
def getIssueReporter():
    '''returns IloReportHandler\n\n
    getIssueReporter()\n
    '''
def abort():
    '''returns None\n\n
    abort()\n
    '''
def acceptCurrentSolution():
    '''returns None\n\n
    acceptCurrentSolution()\n
    '''
def sendControllingOrder():
    '''returns None\n\n
    sendControllingOrder(final long orderId, final String orderType, final Serializable[] orderParameter)\n
    '''
def skipCurrentGoalBoundSearch():
    '''returns None\n\n
    skipCurrentGoalBoundSearch()\n
    '''
def skipRelaxationMinimization():
    '''returns None\n\n
    skipRelaxationMinimization()\n
    '''
def skipRelaxationPriority():
    '''returns None\n\n
    skipRelaxationPriority()\n
    '''
def setProgressObserver():
    '''returns None\n\n
    setProgressObserver(final OptimProgressObserver observer)\n
    '''
def getProgressObserver():
    '''returns OptimProgressObserver\n\n
    getProgressObserver()\n
    '''
def end():
    '''returns None\n\n
    end()\n
    '''
def isAborted():
    '''returns boolean\n\n
    isAborted()\n
    '''
