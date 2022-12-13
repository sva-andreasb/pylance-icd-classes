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
def ItemJOB():
    '''public ItemJOB()
    '''
def isDuplicat():
    '''public boolean isDuplicat(final Parser parser, final Item item)
    '''
def resolveRerefences():
    '''public void resolveRerefences(final Parser project, final long flags)
    '''
def addTask():
    '''public void addTask(final JobTask task)
    '''
def getPageId():
    '''public String getPageId()
    '''
def findTaskByName():
    '''public JobTask findTaskByName(final String name)
    '''
def getJobType():
    '''public int getJobType()
    '''
def addResource():
    '''public void addResource(final ItemRESOURCE resource)
    '''
def resources():
    '''public Enumeration<ItemRESOURCE> resources()
    '''
def getStatus():
    '''public String getStatus()
    '''
def setStatus():
    '''public void setStatus(final String status)
    '''
def getTypeName():
    '''public String getTypeName()
    '''
def setTypeName():
    '''public void setTypeName(String typeName)
    '''
def getTypeReference():
    '''public ItemTYPE[] getTypeReference()
    '''
def setTypeReference():
    '''public void setTypeReference(final ItemTYPE[] typeReferences)
    '''
def getDuration():
    '''public String getDuration()
    '''
def setDuration():
    '''public void setDuration(final String duration)
    '''
def getDurationUnit():
    '''public String getDurationUnit()
    '''
def getDurationUnitType():
    '''public int getDurationUnitType()
    '''
def setDurationUnit():
    '''public void setDurationUnit(final String durationUnit)
    '''
def getStart():
    '''public String getStart()
    '''
def setStart():
    '''public void setStart(final String start)
    '''
def getTaskStartUnit():
    '''public String getTaskStartUnit()
    '''
def setTaskStartUnit():
    '''public void setTaskStartUnit(final String taskStartUnit)
    '''
def getFrequency():
    '''public String getFrequency()
    '''
def setFrequency():
    '''public void setFrequency(final String frequency)
    '''
def getFrequencyUnit():
    '''public String getFrequencyUnit()
    '''
def setFrequencyUnit():
    '''public void setFrequencyUnit(final String frequencyUnit)
    '''
def getTaskNumber():
    '''public String getTaskNumber()
    '''
def setTaskNumber():
    '''public void setTaskNumber(final String taskNumber)
    '''
def getPriors():
    '''public String getPriors()
    '''
def setPriors():
    '''public void setPriors(String priors)
    '''
def getResource():
    '''public Enumeration<ItemRESOURCE> getResource()
    '''
def getResourceNames():
    '''public String getResourceNames()
    '''
def setResourceNames():
    '''public void setResourceNames(final String resourceNames)
    '''
def addResourceNames():
    '''public void addResourceNames(String resourceNames)
    '''
def skip():
    '''public boolean skip(final Parser parser, final long flags)
    '''
def tasks():
    '''public Iterator<JobTask> tasks()
    '''
def toString():
    '''public String toString()
    '''
def durationStringToUnits():
    '''public static int durationStringToUnits(final String duration)
    '''
def export():
    '''public void export(final Exporter exporter)
    '''
