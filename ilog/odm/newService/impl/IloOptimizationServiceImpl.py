COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def IloOptimizationServiceImpl():
    '''public IloOptimizationServiceImpl(final IloOPLIDEInterface ideInterface, final IloApplicationContext applicationContext)
    '''
def setSolveEngineFactory():
    '''public void setSolveEngineFactory(final IloOplDecisionEngineFactory engineFactory)
    '''
def solve():
    '''public boolean solve(final IloScenario scenario, final int timeLimit, final boolean withRelaxation)
    '''
def execute():
    '''public boolean execute(final IloEnginePilot enginePilot, final IloOplDecisionEngine engine, final IloScenario scenario, final IloIssueReporter issueReporter)
    public boolean execute(final IloEnginePilot enginePilot, final IloOplDecisionEngine engine, final IloScenario scenario, final IloIssueReporter issueReporter)
    '''
def findGoalBounds():
    '''public boolean findGoalBounds(final IloScenario scenario, final String goalId, final String ignoredPriorityLevel, final int timeLimit)
    '''
def generateRequirementsPreview():
    '''public IloTable generateRequirementsPreview(final IloScenario scenario, final boolean solve)
    '''
def getIssueReporter():
    '''public IloReportHandler getIssueReporter()
    '''
def abort():
    '''public void abort()
    '''
def acceptCurrentSolution():
    '''public void acceptCurrentSolution()
    '''
def sendControllingOrder():
    '''public void sendControllingOrder(final long orderId, final String orderType, final Serializable[] orderParameter)
    '''
def skipCurrentGoalBoundSearch():
    '''public void skipCurrentGoalBoundSearch()
    '''
def skipRelaxationMinimization():
    '''public void skipRelaxationMinimization()
    '''
def skipRelaxationPriority():
    '''public void skipRelaxationPriority()
    '''
def setProgressObserver():
    '''public void setProgressObserver(final OptimProgressObserver observer)
    '''
def getProgressObserver():
    '''public OptimProgressObserver getProgressObserver()
    '''
def end():
    '''public void end()
    '''
def isAborted():
    '''public boolean isAborted()
    '''
