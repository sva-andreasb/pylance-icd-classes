COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def ():
    '''returns IloProcessingServiceImpl\n\n
    (final SolveQueue solveQueue, final IloApplicationContext applicationContext, final IloODMConfigElements odmCfgElts, final IloReportHandler reportHandler)\n
    '''
def getSolveQueue():
    '''returns SolveQueue\n\n
    getSolveQueue()\n
    '''
def getReportHandler():
    '''returns IloReportHandler\n\n
    getReportHandler()\n
    '''
def createSolveInputOutput():
    '''returns IloSolveInputOutput\n\n
    createSolveInputOutput(final IloScenario scenario)\n
    '''
def createFindGoalBoundsInputOutput():
    '''returns IloFindGoalBoundsInputOutput\n\n
    createFindGoalBoundsInputOutput(final IloScenario scenario, final String goalName)\n
    '''
def notifyNoMoreInSync():
    '''returns None\n\n
    notifyNoMoreInSync(final IloRepositoryChangeEvent evt)\n
    '''
def submitJob():
    '''returns IloJobController\n\n
    submitJob(final IloJobInputOutput jobIO)\n
    '''
def dispose():
    '''returns None\n\n
    dispose()\n
    '''
def initialize():
    '''returns None\n\n
    initialize()\n
    '''
def queueContentChanged():
    '''returns None\n\n
    queueContentChanged(final QueueContentChangeEvent event)\n
    '''
def startingNewOptimTask():
    '''returns None\n\n
    startingNewOptimTask(final OptimTaskInfo info, final RunningOptimTaskInteractor interactor)\n
    '''
def newTask():
    '''returns IloTaskController\n\n
    newTask(final IloTaskConfig config, final IloExecutionScope scope)\n
    '''
def call():
    '''returns Boolean\n\n
    call()\n
    call()\n
    '''
def addProcessingServiceListener():
    '''returns None\n\n
    addProcessingServiceListener(final IloProcessingServiceListener listener)\n
    '''
def removeProcessingServiceListener():
    '''returns None\n\n
    removeProcessingServiceListener(final IloProcessingServiceListener listener)\n
    '''
def getConfiguration():
    '''returns IloDecisionProcessConfiguration\n\n
    getConfiguration()\n
    '''
def getSubmittedTasks():
    '''returns List<IloTaskController>\n\n
    getSubmittedTasks(final IloExecutionScope scope)\n
    '''
def log():
    '''returns None\n\n
    log(final Level level, final String message)\n
    log(final Level level, final String message, final Throwable t)\n
    '''
def newScope():
    '''returns IloScenarioExecutionScope\n\n
    newScope(final IloScenario scenario)\n
    '''
def getDataService():
    '''returns IloDataService\n\n
    getDataService()\n
    '''
def getAppInputTableIds():
    '''returns List<String>\n\n
    getAppInputTableIds(final IloRelationalTaskConfig config)\n
    '''
def getAppOutputTableIds():
    '''returns List<String>\n\n
    getAppOutputTableIds(final IloRelationalTaskConfig config)\n
    '''
def isInputTable():
    '''returns boolean\n\n
    isInputTable(final IloRelationalTaskConfig config, final String tableId)\n
    '''
def isOutputTable():
    '''returns boolean\n\n
    isOutputTable(final IloRelationalTaskConfig config, final String tableId)\n
    '''
def getLogger():
    '''returns Logger\n\n
    getLogger()\n
    '''
def isUsingOptimizationServer():
    '''returns boolean\n\n
    isUsingOptimizationServer()\n
    '''
def getOdmConfigElements():
    '''returns IloODMConfigElements\n\n
    getOdmConfigElements()\n
    '''
