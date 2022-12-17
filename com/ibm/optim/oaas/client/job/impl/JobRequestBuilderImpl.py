def ():
    '''returns JobRequestBuilderImpl\n\n
    (final JobClientImpl client)\n
    '''
def application():
    '''returns JobRequestBuilderImpl\n\n
    application(final String applicationId)\n
    '''
def input():
    '''returns JobRequestBuilder\n\n
    input(final File file)\n
    input(final String name, final File file)\n
    input(final String name, final URL url)\n
    input(final String name, final InputStream stream)\n
    input(final String name, final ObjectMapper mapper, final Object obj)\n
    input(final JobInput input)\n
    '''
def output():
    '''returns JobRequestBuilder\n\n
    output(final File file)\n
    output(final OutputStream stream)\n
    output(final JobOutput output)\n
    output(final String attid, final File file)\n
    output(final String attid, final OutputStream stream)\n
    '''
def log():
    '''returns JobRequestBuilder\n\n
    log(final File file)\n
    log(final OutputStream stream)\n
    '''
def deleteOnCompletion():
    '''returns JobRequestBuilder\n\n
    deleteOnCompletion(final boolean delete)\n
    '''
def version():
    '''returns JobRequestBuilderImpl\n\n
    version(final String version)\n
    '''
def parameter():
    '''returns JobRequestBuilderImpl\n\n
    parameter(final String name, final Object value)\n
    '''
def timeout():
    '''returns JobRequestBuilder\n\n
    timeout(final long timeout, final TimeUnit unit)\n
    '''
def build():
    '''returns JobRequest\n\n
    build()\n
    '''
def execute():
    '''returns Future<JobResponse>\n\n
    execute(final JobExecutor executor)\n
    '''
def create():
    '''returns Future<JobResponse>\n\n
    create(final JobExecutor executor)\n
    '''
def livelog():
    '''returns JobRequestBuilder\n\n
    livelog(final OutputStream stream)\n
    livelog(final OutputStream stream, final DateFormat format)\n
    '''
def clientName():
    '''returns JobRequestBuilder\n\n
    clientName(final String name)\n
    '''
def clientEmail():
    '''returns JobRequestBuilder\n\n
    clientEmail(final String email)\n
    '''
def copy():
    '''returns JobRequestBuilder\n\n
    copy(final String jobId)\n
    copy(final String jobId, final boolean shallow)\n
    '''
def recreate():
    '''returns JobRequestBuilder\n\n
    recreate(final String jobId)\n
    '''
def useBatchSubmitMode():
    '''returns JobRequestBuilder\n\n
    useBatchSubmitMode()\n
    '''
