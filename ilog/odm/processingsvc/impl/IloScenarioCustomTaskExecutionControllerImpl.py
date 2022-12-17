COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def ():
    '''returns IloScenarioCustomTaskExecutionControllerImpl\n\n
    (final IloProcessingService ps, final IloExecutionScope scope, final IloTaskConfig config, final IloTaskInputOutput io, final List<IloTaskExecutionController> tasks)\n
    '''
def notifyProgress():
    '''returns None\n\n
    notifyProgress(final String phase, final int completion)\n
    notifyProgress(final String phase, final int completion)\n
    '''
def getInputOutput():
    '''returns IloScenarioCustomInputOutputImpl\n\n
    getInputOutput()\n
    getInputOutput()\n
    '''
def setupExecuteImpl():
    '''returns None\n\n
    setupExecuteImpl()\n
    '''
def tearDownExecuteImpl():
    '''returns None\n\n
    tearDownExecuteImpl()\n
    '''
def abort():
    '''returns None\n\n
    abort()\n
    '''
def interaction():
    '''returns None\n\n
    interaction(final String name, final Map<String, String> parameters)\n
    interaction(final String interaction, final Map<String, String> parameters)\n
    '''
def isAborted():
    '''returns boolean\n\n
    isAborted()\n
    isAborted()\n
    '''
def setup():
    '''returns None\n\n
    setup()\n
    '''
def tearDown():
    '''returns None\n\n
    tearDown()\n
    '''
def getProcessingService():
    '''returns IloScenarioProcessingService\n\n
    getProcessingService()\n
    '''
def getExecutionScope():
    '''returns IloScenarioExecutionScope\n\n
    getExecutionScope()\n
    '''
def getBooleanConfigParameter():
    '''returns boolean\n\n
    getBooleanConfigParameter(final String name, final boolean defaultValue)\n
    '''
def getStringConfigParameter():
    '''returns String\n\n
    getStringConfigParameter(final String name, final String defaultValue)\n
    '''
def getDoubleConfigParameter():
    '''returns double\n\n
    getDoubleConfigParameter(final String name, final double defaultValue)\n
    '''
def getIntegerConfigParameter():
    '''returns int\n\n
    getIntegerConfigParameter(final String name, final int defaultValue)\n
    '''
def getLogger():
    '''returns Logger\n\n
    getLogger()\n
    '''
def getInputTables():
    '''returns List<String>\n\n
    getInputTables()\n
    '''
def getOutputTables():
    '''returns List<String>\n\n
    getOutputTables()\n
    '''
def getBooleanRuntimeParameter():
    '''returns boolean\n\n
    getBooleanRuntimeParameter(final String name, final boolean defaultValue)\n
    '''
def getStringRuntimeParameter():
    '''returns String\n\n
    getStringRuntimeParameter(final String name, final String defaultValue)\n
    '''
def getDoubleRuntimeParameter():
    '''returns double\n\n
    getDoubleRuntimeParameter(final String name, final double defaultValue)\n
    '''
def getIntegerRuntimeParameter():
    '''returns int\n\n
    getIntegerRuntimeParameter(final String name, final int defaultValue)\n
    '''
def addOptimProgressObserver():
    '''returns None\n\n
    addOptimProgressObserver(final OptimProgressObserver observer)\n
    '''
def removeOptimProgressObserver():
    '''returns None\n\n
    removeOptimProgressObserver(final OptimProgressObserver observer)\n
    '''
def getLastOptimProgressUpdate():
    '''returns OptimProgressUpdate\n\n
    getLastOptimProgressUpdate()\n
    '''
def getCurrentEnginePhase():
    '''returns IloEnginePhase\n\n
    getCurrentEnginePhase()\n
    '''
def acceptCurrentSolution():
    '''returns None\n\n
    acceptCurrentSolution()\n
    '''
