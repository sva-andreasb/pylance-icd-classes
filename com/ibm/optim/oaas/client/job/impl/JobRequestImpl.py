def ():
    '''returns JobRequestImpl\n\n
    (final JobClientImpl client, final JobCreationDataImpl data, final List<JobInput> input, final List<JobOutput> output, final List<JobLogOutputImpl> logoutput, final boolean delete, final long timeout, final OutputStream livelog, final DateFormat livelogDateFormat, final String copy, final boolean shallow, final String recreate, final boolean batchSubmitMode)\n
    '''
def getClient():
    '''returns JobClientImpl\n\n
    getClient()\n
    '''
def getData():
    '''returns JobCreationDataImpl\n\n
    getData()\n
    '''
def getInput():
    '''returns List<JobInput>\n\n
    getInput()\n
    '''
def getOutput():
    '''returns List<JobOutput>\n\n
    getOutput()\n
    '''
def getLogOutput():
    '''returns List<JobLogOutputImpl>\n\n
    getLogOutput()\n
    '''
def isDeleteOnCompletion():
    '''returns boolean\n\n
    isDeleteOnCompletion()\n
    '''
def getTimeout():
    '''returns long\n\n
    getTimeout()\n
    '''
def getLivelog():
    '''returns OutputStream\n\n
    getLivelog()\n
    '''
def execute():
    '''returns Future<JobResponse>\n\n
    execute(final JobExecutor executor)\n
    '''
def create():
    '''returns Future<JobResponse>\n\n
    create(final JobExecutor executor)\n
    '''
def getJobId():
    '''returns String\n\n
    getJobId()\n
    '''
def setJobId():
    '''returns None\n\n
    setJobId(final String jobid)\n
    '''
def getLivelogDateFormat():
    '''returns DateFormat\n\n
    getLivelogDateFormat()\n
    '''
def getCopyJobId():
    '''returns String\n\n
    getCopyJobId()\n
    '''
def getShallowCopy():
    '''returns boolean\n\n
    getShallowCopy()\n
    '''
def getRecreateJobId():
    '''returns String\n\n
    getRecreateJobId()\n
    '''
def isBatchSubmitMode():
    '''returns boolean\n\n
    isBatchSubmitMode()\n
    '''
