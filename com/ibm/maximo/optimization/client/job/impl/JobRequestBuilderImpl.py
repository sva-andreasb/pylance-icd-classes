def JobRequestBuilderImpl():
'''public JobRequestBuilderImpl(final JobClientImpl client)
'''
pass
def modelName():
'''public JobRequestBuilderImpl modelName(final String modelName)
'''
pass
def modelVersion():
'''public JobRequestBuilderImpl modelVersion(final int modelVersion)
'''
pass
def userName():
'''public JobRequestBuilderImpl userName(final String userName)
'''
pass
def userEmail():
'''public JobRequestBuilderImpl userEmail(final String userEmail)
'''
pass
def scenarioName():
'''public JobRequestBuilderImpl scenarioName(final String scenarioName)
'''
pass
def input():
'''public JobRequestBuilderImpl input(final File file)
public JobRequestBuilderImpl input(final String name, final File file)
public JobRequestBuilderImpl input(final String name, final URL url)
public JobRequestBuilderImpl input(final String name, final InputStream stream)
public JobRequestBuilderImpl input(final String name, final ObjectMapper mapper, final Object obj)
public JobRequestBuilder input(final JobInput input)
'''
pass
def output():
'''public JobRequestBuilder output(final File file)
public JobRequestBuilder output(final OutputStream stream)
public <T> JobRequestBuilder output(final ObjectMapper mapper, final TypeReference<T> type)
public <T> JobRequestBuilder output(final ObjectMapper mapper, final Class<T> type)
public JobRequestBuilder output(final JobOutput output)
public JobRequestBuilder output(final String attid, final File file)
public <T> JobRequestBuilder output(final String attid, final ObjectMapper mapper, final Class<T> type)
public <T> JobRequestBuilder output(final String attid, final ObjectMapper mapper, final TypeReference<T> type)
public JobRequestBuilder output(final String attid, final OutputStream stream)
'''
pass
def log():
'''public JobRequestBuilder log(final File file)
public JobRequestBuilder log(final OutputStream stream)
'''
pass
def deleteOnCompletion():
'''public JobRequestBuilder deleteOnCompletion(final boolean delete)
'''
pass
def parameter():
'''public JobRequestBuilderImpl parameter(final String name, final Object value)
'''
pass
def timeout():
'''public JobRequestBuilder timeout(final long timeout, final TimeUnit unit)
'''
pass
def build():
'''public JobRequest build()
'''
pass
def execute():
'''public Future<JobResponse> execute(final JobExecutor executor)
'''
pass
def create():
'''public Future<JobResponse> create(final JobExecutor executor)
'''
pass
def livelog():
'''public JobRequestBuilder livelog(final OutputStream stream)
public JobRequestBuilder livelog(final OutputStream stream, final DateFormat format)
'''
pass
def copy():
'''public JobRequestBuilder copy(final String jobId)
public JobRequestBuilder copy(final String jobId, final boolean shallow)
'''
pass
def recreate():
'''public JobRequestBuilder recreate(final String jobId)
'''
pass
def useBatchSubmitMode():
'''public JobRequestBuilder useBatchSubmitMode()
'''
pass
