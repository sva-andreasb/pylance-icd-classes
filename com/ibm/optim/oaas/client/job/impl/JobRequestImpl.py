def JobRequestImpl():
    '''    public JobRequestImpl(final JobClientImpl client, final JobCreationDataImpl data, final List<JobInput> input, final List<JobOutput> output, final List<JobLogOutputImpl> logoutput, final boolean delete, final long timeout, final OutputStream livelog, final DateFormat livelogDateFormat, final String copy, final boolean shallow, final String recreate, final boolean batchSubmitMode)
    '''
def getClient():
    '''    public JobClientImpl getClient()
    '''
def getData():
    '''    public JobCreationDataImpl getData()
    '''
def getInput():
    '''    public List<JobInput> getInput()
    '''
def getOutput():
    '''    public List<JobOutput> getOutput()
    '''
def getLogOutput():
    '''    public List<JobLogOutputImpl> getLogOutput()
    '''
def isDeleteOnCompletion():
    '''    public boolean isDeleteOnCompletion()
    '''
def getTimeout():
    '''    public long getTimeout()
    '''
def getLivelog():
    '''    public OutputStream getLivelog()
    '''
def execute():
    '''    public Future<JobResponse> execute(final JobExecutor executor)
    '''
def create():
    '''    public Future<JobResponse> create(final JobExecutor executor)
    '''
def getJobId():
    '''    public String getJobId()
    '''
def setJobId():
    '''    public void setJobId(final String jobid)
    '''
def getLivelogDateFormat():
    '''    public DateFormat getLivelogDateFormat()
    '''
def getCopyJobId():
    '''    public String getCopyJobId()
    '''
def getShallowCopy():
    '''    public boolean getShallowCopy()
    '''
def getRecreateJobId():
    '''    public String getRecreateJobId()
    '''
def isBatchSubmitMode():
    '''    public boolean isBatchSubmitMode()
    '''
