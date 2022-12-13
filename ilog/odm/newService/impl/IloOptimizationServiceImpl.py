COPYRIGHT_NOTICE = "String  Copyright IBM Corporation 2005,2012""
def IloOptimizationServiceImpl():
'''public IloOptimizationServiceImpl(final IloOPLIDEInterface ideInterface, final IloApplicationContext applicationContext)
'''
pass
def setSolveEngineFactory():
'''public void setSolveEngineFactory(final IloOplDecisionEngineFactory engineFactory)
'''
pass
def solve():
'''public boolean solve(final IloScenario scenario, final int timeLimit, final boolean withRelaxation)
'''
pass
def execute():
'''public boolean execute(final IloEnginePilot enginePilot, final IloOplDecisionEngine engine, final IloScenario scenario, final IloIssueReporter issueReporter)
public boolean execute(final IloEnginePilot enginePilot, final IloOplDecisionEngine engine, final IloScenario scenario, final IloIssueReporter issueReporter)
'''
pass
def findGoalBounds():
'''public boolean findGoalBounds(final IloScenario scenario, final String goalId, final String ignoredPriorityLevel, final int timeLimit)
'''
pass
def generateRequirementsPreview():
'''public IloTable generateRequirementsPreview(final IloScenario scenario, final boolean solve)
'''
pass
def getIssueReporter():
'''public IloReportHandler getIssueReporter()
'''
pass
def abort():
'''public void abort()
'''
pass
def acceptCurrentSolution():
'''public void acceptCurrentSolution()
'''
pass
def sendControllingOrder():
'''public void sendControllingOrder(final long orderId, final String orderType, final Serializable[] orderParameter)
'''
pass
def skipCurrentGoalBoundSearch():
'''public void skipCurrentGoalBoundSearch()
'''
pass
def skipRelaxationMinimization():
'''public void skipRelaxationMinimization()
'''
pass
def skipRelaxationPriority():
'''public void skipRelaxationPriority()
'''
pass
def setProgressObserver():
'''public void setProgressObserver(final OptimProgressObserver observer)
'''
pass
def getProgressObserver():
'''public OptimProgressObserver getProgressObserver()
'''
pass
def end():
'''public void end()
'''
pass
def isAborted():
'''public boolean isAborted()
'''
pass
