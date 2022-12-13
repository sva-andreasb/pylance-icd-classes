def JobExecutorImpl():
    '''public JobExecutorImpl(final ExecutorService service, final long interval, final long timeout, final int retry, final long retryDelay)
    '''
def getExecutionDetails():
    '''public JobExecutionDetails getExecutionDetails()
    '''
def setExecutionDetails():
    '''public void setExecutionDetails(final JobExecutionDetails executionDetails)
    '''
def start():
    '''public void start()
    '''
def shutdown():
    '''public void shutdown()
    '''
def create():
    '''public Future<JobResponse> create(final JobRequest request, final JobCallback callback)
    '''
def submit():
    '''public Future<JobResponse> submit(final JobRequest request, final JobCallback callback)
    '''
def monitor():
    '''public Future<JobResponse> monitor(final JobRequest request, final String jobid, final JobCallback callback)
    '''
def execute():
    '''public Future<JobResponse> execute(final JobRequest request, final JobCallback callback)
    public Future<JobResponse> execute(final JobRequest request)
    '''
def executeMain():
    '''public Future<JobResponse> executeMain(final JobRequest request, final JobCallback callback, final boolean create, final boolean submit, final boolean monitor)
    '''
def call():
    '''public JobResponse call()
    '''
def RetryLoop():
    '''public RetryLoop()
    '''
def next():
    '''public void next()
    '''
def exception():
    '''public void exception(final OperationException e)
    '''
