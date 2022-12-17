COBIE_JOB_TYPE_ADJUSTMENT = "String  \"Adjustment\""
COBIE_JOB_TYPE_CALIBRATION = "String  \"Calibration\""
COBIE_JOB_TYPE_EMERGENCY = "String  \"Emergency\""
COBIE_JOB_TYPE_INSPECTION = "String  \"Inspection\""
COBIE_JOB_TYPE_OPERATION = "String  \"Operation\""
COBIE_JOB_TYPE_PM = "String  \"PM\""
COBIE_JOB_TYPE_SAFTY = "String  \"Safety\""
COBIE_JOB_TYPE_SHUTDOWN = "String  \"ShutDown\""
COBIE_JOB_TYPE_STARTUP = "String  \"StartUp\""
COBIE_JOB_TYPE_TESTING = "String  \"Testing\""
COBIE_JOB_TYPE_TROUBLE = "String  \"Trouble\""
JOB_TYPE_UNKNOWN = "int  0"
JOB_TYPE_ADJUSTMENT = "int  1"
JOB_TYPE_CALIBRATION = "int  2"
JOB_TYPE_EMERGENCY = "int  3"
JOB_TYPE_INSPECTION = "int  4"
JOB_TYPE_OPERATION = "int  5"
JOB_TYPE_PM = "int  6"
JOB_TYPE_SAFTY = "int  7"
JOB_TYPE_SHUTDOWN = "int  8"
JOB_TYPE_STARTUP = "int  9"
JOB_TYPE_TESTING = "int  10"
JOB_TYPE_TROUBLE = "int  11"
JOB_DURATION_UNKNOWN = "int  0"
JOB_DURATION_SECOND = "int  1"
JOB_DURATION_MINUTE = "int  2"
JOB_DURATION_HOUR = "int  3"
JOB_DURATION_DAY = "int  4"
def ():
    '''returns ItemJOB\n\n
    ()\n
    '''
def isDuplicat():
    '''returns boolean\n\n
    isDuplicat(final Parser parser, final Item item)\n
    '''
def resolveRerefences():
    '''returns None\n\n
    resolveRerefences(final Parser project, final long flags)\n
    '''
def addTask():
    '''returns None\n\n
    addTask(final JobTask task)\n
    '''
def getPageId():
    '''returns String\n\n
    getPageId()\n
    '''
def findTaskByName():
    '''returns JobTask\n\n
    findTaskByName(final String name)\n
    '''
def getJobType():
    '''returns int\n\n
    getJobType()\n
    '''
def addResource():
    '''returns None\n\n
    addResource(final ItemRESOURCE resource)\n
    '''
def resources():
    '''returns Enumeration<ItemRESOURCE>\n\n
    resources()\n
    '''
def getStatus():
    '''returns String\n\n
    getStatus()\n
    '''
def setStatus():
    '''returns None\n\n
    setStatus(final String status)\n
    '''
def getTypeName():
    '''returns String\n\n
    getTypeName()\n
    '''
def setTypeName():
    '''returns None\n\n
    setTypeName(String typeName)\n
    '''
def getTypeReference():
    '''returns ItemTYPE[]\n\n
    getTypeReference()\n
    '''
def setTypeReference():
    '''returns None\n\n
    setTypeReference(final ItemTYPE[] typeReferences)\n
    '''
def getDuration():
    '''returns String\n\n
    getDuration()\n
    '''
def setDuration():
    '''returns None\n\n
    setDuration(final String duration)\n
    '''
def getDurationUnit():
    '''returns String\n\n
    getDurationUnit()\n
    '''
def getDurationUnitType():
    '''returns int\n\n
    getDurationUnitType()\n
    '''
def setDurationUnit():
    '''returns None\n\n
    setDurationUnit(final String durationUnit)\n
    '''
def getStart():
    '''returns String\n\n
    getStart()\n
    '''
def setStart():
    '''returns None\n\n
    setStart(final String start)\n
    '''
def getTaskStartUnit():
    '''returns String\n\n
    getTaskStartUnit()\n
    '''
def setTaskStartUnit():
    '''returns None\n\n
    setTaskStartUnit(final String taskStartUnit)\n
    '''
def getFrequency():
    '''returns String\n\n
    getFrequency()\n
    '''
def setFrequency():
    '''returns None\n\n
    setFrequency(final String frequency)\n
    '''
def getFrequencyUnit():
    '''returns String\n\n
    getFrequencyUnit()\n
    '''
def setFrequencyUnit():
    '''returns None\n\n
    setFrequencyUnit(final String frequencyUnit)\n
    '''
def getTaskNumber():
    '''returns String\n\n
    getTaskNumber()\n
    '''
def setTaskNumber():
    '''returns None\n\n
    setTaskNumber(final String taskNumber)\n
    '''
def getPriors():
    '''returns String\n\n
    getPriors()\n
    '''
def setPriors():
    '''returns None\n\n
    setPriors(String priors)\n
    '''
def getResource():
    '''returns Enumeration<ItemRESOURCE>\n\n
    getResource()\n
    '''
def getResourceNames():
    '''returns String\n\n
    getResourceNames()\n
    '''
def setResourceNames():
    '''returns None\n\n
    setResourceNames(final String resourceNames)\n
    '''
def addResourceNames():
    '''returns None\n\n
    addResourceNames(String resourceNames)\n
    '''
def skip():
    '''returns boolean\n\n
    skip(final Parser parser, final long flags)\n
    '''
def tasks():
    '''returns Iterator<JobTask>\n\n
    tasks()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def export():
    '''returns None\n\n
    export(final Exporter exporter)\n
    '''
