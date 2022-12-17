COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def ():
    '''returns IloOptimDecisionService\n\n
    (final IloODMConfigElements config, IloOPLIDEInterface ideInterface, final IloApplicationContext applicationContext, final boolean inServer)\n
    (final IloODMConfigElements config, final IloReportHandler reportHandler, final IloApplicationContext applicationContext, final boolean inServer)\n
    (final IloODMConfigElements config, final IloApplicationContext applicationContext, final boolean inServer)\n
    '''
def abort():
    '''returns None\n\n
    abort()\n
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
def acceptCurrentSolution():
    '''returns None\n\n
    acceptCurrentSolution()\n
    '''
def setProgressObserver():
    '''returns None\n\n
    setProgressObserver(final OptimProgressObserver listener)\n
    '''
def getProgressObserver():
    '''returns OptimProgressObserver\n\n
    getProgressObserver()\n
    '''
def getOptimizationDescription():
    '''returns IloOptimDesc\n\n
    getOptimizationDescription()\n
    '''
def end():
    '''returns None\n\n
    end()\n
    '''
def generateRequirementsPreview():
    '''returns IloTable\n\n
    generateRequirementsPreview(final boolean solve, final IloScenario scenario)\n
    '''
def getOptimizationService():
    '''returns IloOptimizationService\n\n
    getOptimizationService()\n
    '''
def getDataService():
    '''returns IloDataService\n\n
    getDataService()\n
    '''
def getIssueReporter():
    '''returns IloReportHandler\n\n
    getIssueReporter()\n
    '''
def getProfile():
    '''returns IloDecisionServiceProfile\n\n
    getProfile()\n
    '''
def getStyle():
    '''returns IloDecisionServiceStyle\n\n
    getStyle()\n
    '''
