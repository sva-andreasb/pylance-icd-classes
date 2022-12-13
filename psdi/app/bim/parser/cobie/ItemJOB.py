COBIE_JOB_TYPE_ADJUSTMENT = "String  Adjustment""
COBIE_JOB_TYPE_CALIBRATION = "String  Calibration""
COBIE_JOB_TYPE_EMERGENCY = "String  Emergency""
COBIE_JOB_TYPE_INSPECTION = "String  Inspection""
COBIE_JOB_TYPE_OPERATION = "String  Operation""
COBIE_JOB_TYPE_PM = "String  PM""
COBIE_JOB_TYPE_SAFTY = "String  Safety""
COBIE_JOB_TYPE_SHUTDOWN = "String  ShutDown""
COBIE_JOB_TYPE_STARTUP = "String  StartUp""
COBIE_JOB_TYPE_TESTING = "String  Testing""
COBIE_JOB_TYPE_TROUBLE = "String  Trouble""
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
pass
def isDuplicat():
'''public boolean isDuplicat(final Parser parser, final Item item)
'''
pass
def resolveRerefences():
'''public void resolveRerefences(final Parser project, final long flags)
'''
pass
def addTask():
'''public void addTask(final JobTask task)
'''
pass
def getPageId():
'''public String getPageId()
'''
pass
def findTaskByName():
'''public JobTask findTaskByName(final String name)
'''
pass
def getJobType():
'''public int getJobType()
'''
pass
def addResource():
'''public void addResource(final ItemRESOURCE resource)
'''
pass
def resources():
'''public Enumeration<ItemRESOURCE> resources()
'''
pass
def getStatus():
'''public String getStatus()
'''
pass
def setStatus():
'''public void setStatus(final String status)
'''
pass
def getTypeName():
'''public String getTypeName()
'''
pass
def setTypeName():
'''public void setTypeName(String typeName)
'''
pass
def getTypeReference():
'''public ItemTYPE[] getTypeReference()
'''
pass
def setTypeReference():
'''public void setTypeReference(final ItemTYPE[] typeReferences)
'''
pass
def getDuration():
'''public String getDuration()
'''
pass
def setDuration():
'''public void setDuration(final String duration)
'''
pass
def getDurationUnit():
'''public String getDurationUnit()
'''
pass
def getDurationUnitType():
'''public int getDurationUnitType()
'''
pass
def setDurationUnit():
'''public void setDurationUnit(final String durationUnit)
'''
pass
def getStart():
'''public String getStart()
'''
pass
def setStart():
'''public void setStart(final String start)
'''
pass
def getTaskStartUnit():
'''public String getTaskStartUnit()
'''
pass
def setTaskStartUnit():
'''public void setTaskStartUnit(final String taskStartUnit)
'''
pass
def getFrequency():
'''public String getFrequency()
'''
pass
def setFrequency():
'''public void setFrequency(final String frequency)
'''
pass
def getFrequencyUnit():
'''public String getFrequencyUnit()
'''
pass
def setFrequencyUnit():
'''public void setFrequencyUnit(final String frequencyUnit)
'''
pass
def getTaskNumber():
'''public String getTaskNumber()
'''
pass
def setTaskNumber():
'''public void setTaskNumber(final String taskNumber)
'''
pass
def getPriors():
'''public String getPriors()
'''
pass
def setPriors():
'''public void setPriors(String priors)
'''
pass
def getResource():
'''public Enumeration<ItemRESOURCE> getResource()
'''
pass
def getResourceNames():
'''public String getResourceNames()
'''
pass
def setResourceNames():
'''public void setResourceNames(final String resourceNames)
'''
pass
def addResourceNames():
'''public void addResourceNames(String resourceNames)
'''
pass
def skip():
'''public boolean skip(final Parser parser, final long flags)
'''
pass
def tasks():
'''public Iterator<JobTask> tasks()
'''
pass
def toString():
'''public String toString()
'''
pass
def durationStringToUnits():
'''public static int durationStringToUnits(final String duration)
'''
pass
def export():
'''public void export(final Exporter exporter)
'''
pass
