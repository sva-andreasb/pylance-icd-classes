def JobRequestBuilderImpl():
    '''    public JobRequestBuilderImpl(final JobClientImpl client)
    '''
def application():
    '''    public JobRequestBuilderImpl application(final String applicationId)
    '''
def input():
    '''    public JobRequestBuilderImpl input(final File file)
    public JobRequestBuilderImpl input(final String name, final File file)
    public JobRequestBuilderImpl input(final String name, final URL url)
    public JobRequestBuilderImpl input(final String name, final InputStream stream)
    public JobRequestBuilderImpl input(final String name, final ObjectMapper mapper, final Object obj)
    public JobRequestBuilder input(final JobInput input)
    '''
def output():
    '''    public JobRequestBuilder output(final File file)
    public JobRequestBuilder output(final OutputStream stream)
    public <T> JobRequestBuilder output(final ObjectMapper mapper, final TypeReference<T> type)
    public <T> JobRequestBuilder output(final ObjectMapper mapper, final Class<T> type)
    public JobRequestBuilder output(final JobOutput output)
    public JobRequestBuilder output(final String attid, final File file)
    public <T> JobRequestBuilder output(final String attid, final ObjectMapper mapper, final Class<T> type)
    public <T> JobRequestBuilder output(final String attid, final ObjectMapper mapper, final TypeReference<T> type)
    public JobRequestBuilder output(final String attid, final OutputStream stream)
    '''
def log():
    '''    public JobRequestBuilder log(final File file)
    public JobRequestBuilder log(final OutputStream stream)
    '''
def deleteOnCompletion():
    '''    public JobRequestBuilder deleteOnCompletion(final boolean delete)
    '''
def version():
    '''    public JobRequestBuilderImpl version(final String version)
    '''
def parameter():
    '''    public JobRequestBuilderImpl parameter(final String name, final Object value)
    '''
def timeout():
    '''    public JobRequestBuilder timeout(final long timeout, final TimeUnit unit)
    '''
def build():
    '''    public JobRequest build()
    '''
def execute():
    '''    public Future<JobResponse> execute(final JobExecutor executor)
    '''
def create():
    '''    public Future<JobResponse> create(final JobExecutor executor)
    '''
def livelog():
    '''    public JobRequestBuilder livelog(final OutputStream stream)
    public JobRequestBuilder livelog(final OutputStream stream, final DateFormat format)
    '''
def clientName():
    '''    public JobRequestBuilder clientName(final String name)
    '''
def clientEmail():
    '''    public JobRequestBuilder clientEmail(final String email)
    '''
def copy():
    '''    public JobRequestBuilder copy(final String jobId)
    public JobRequestBuilder copy(final String jobId, final boolean shallow)
    '''
def recreate():
    '''    public JobRequestBuilder recreate(final String jobId)
    '''
def useBatchSubmitMode():
    '''    public JobRequestBuilder useBatchSubmitMode()
    '''
