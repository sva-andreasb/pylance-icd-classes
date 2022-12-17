def ():
    '''returns BatchReportServiceStub\n\n
    ()\n
    (final URL endpointURL, final Service service)\n
    (final Service service)\n
    '''
def add():
    '''returns AuthoredReport\n\n
    add(final SearchPathSingleObject parentPath, final AuthoredReport object, final AddOptions options)\n
    '''
def addDrillPath():
    '''returns DrillPath\n\n
    addDrillPath(final SearchPathSingleObject parentPath, final DrillPath object, final AddOptions options)\n
    '''
def back():
    '''returns AsynchReply\n\n
    back(final AsynchRequest conversation, final ParameterValue[] parameterValues, final Option[] options)\n
    '''
def cancel():
    '''returns None\n\n
    cancel(final AsynchRequest conversation)\n
    '''
def collectParameterValues():
    '''returns AsynchReply\n\n
    collectParameterValues(final SearchPathSingleObject objectPath, final ParameterValue[] parameterValues, final Option[] options)\n
    '''
def collectParameterValuesSpecification():
    '''returns AsynchReply\n\n
    collectParameterValuesSpecification(final AsynchSpecification specification, final ParameterValue[] parameterValues, final Option[] options)\n
    '''
def convertDrillThroughContext():
    '''returns AsynchReply\n\n
    convertDrillThroughContext(final XmlEncodedXML inputContext, final ParameterValue[] parameterValues, final Option[] options)\n
    '''
def currentPage():
    '''returns AsynchReply\n\n
    currentPage(final AsynchRequest conversation, final ParameterValue[] parameterValues, final Option[] options)\n
    '''
def deliver():
    '''returns AsynchReply\n\n
    deliver(final AsynchRequest conversation, final ParameterValue[] parameterValues, final Option[] options)\n
    '''
def drill():
    '''returns AsynchReply\n\n
    drill(final AsynchRequest conversation, final ParameterValue[] parameterValues, final Option[] options)\n
    '''
def findDrillThroughPaths():
    '''returns AsynchReply\n\n
    findDrillThroughPaths(final SearchPathSingleObject objectPath, final ParameterValue[] parameterValues, final Option[] options)\n
    '''
def firstPage():
    '''returns AsynchReply\n\n
    firstPage(final AsynchRequest conversation, final ParameterValue[] parameterValues, final Option[] options)\n
    '''
def forward():
    '''returns AsynchReply\n\n
    forward(final AsynchRequest conversation, final ParameterValue[] parameterValues, final Option[] options)\n
    '''
def getContext():
    '''returns AsynchReply\n\n
    getContext(final AsynchRequest conversation, final ParameterValue[] parameterValues, final Option[] options)\n
    '''
def getObjectContext():
    '''returns AsynchReply\n\n
    getObjectContext(final SearchPathSingleObject objectPath, final ParameterValue[] parameterValues, final Option[] options)\n
    '''
def getOutput():
    '''returns AsynchReply\n\n
    getOutput(final AsynchRequest conversation, final ParameterValue[] parameterValues, final Option[] options)\n
    '''
def getParameters():
    '''returns AsynchReply\n\n
    getParameters(final SearchPathSingleObject objectPath, final ParameterValue[] parameterValues, final Option[] options)\n
    '''
def getParametersSpecification():
    '''returns AsynchReply\n\n
    getParametersSpecification(final AsynchSpecification specification, final ParameterValue[] parameterValues, final Option[] options)\n
    '''
def getPromptValues():
    '''returns AsynchReply\n\n
    getPromptValues(final AsynchRequest conversation, final ParameterValue[] parameterValues, final Option[] options)\n
    '''
def lastPage():
    '''returns AsynchReply\n\n
    lastPage(final AsynchRequest conversation, final ParameterValue[] parameterValues, final Option[] options)\n
    '''
def lineage():
    '''returns AsynchReply\n\n
    lineage(final AsynchRequest conversation, final ParameterValue[] parameterValues, final Option[] options)\n
    '''
def nextPage():
    '''returns AsynchReply\n\n
    nextPage(final AsynchRequest conversation, final ParameterValue[] parameterValues, final Option[] options)\n
    '''
def previousPage():
    '''returns AsynchReply\n\n
    previousPage(final AsynchRequest conversation, final ParameterValue[] parameterValues, final Option[] options)\n
    '''
def query():
    '''returns AsynchReply\n\n
    query(final SearchPathSingleObject objectPath, final ParameterValue[] parameterValues, final Option[] options)\n
    '''
def queryDrillPath():
    '''returns AsynchReply\n\n
    queryDrillPath(final SearchPathSingleObject objectPath, final ParameterValue[] parameterValues, final Option[] options)\n
    '''
def release():
    '''returns None\n\n
    release(final AsynchRequest conversation)\n
    '''
def render():
    '''returns AsynchReply\n\n
    render(final AsynchRequest conversation, final ParameterValue[] parameterValues, final Option[] options)\n
    '''
def run():
    '''returns AsynchReply\n\n
    run(final SearchPathSingleObject objectPath, final ParameterValue[] parameterValues, final Option[] options)\n
    '''
def runSpecification():
    '''returns AsynchReply\n\n
    runSpecification(final AsynchSpecification specification, final ParameterValue[] parameterValues, final Option[] options)\n
    '''
def testDataSourceConnection():
    '''returns None\n\n
    testDataSourceConnection(final String connectionString, final XmlEncodedXML credentials)\n
    '''
def update():
    '''returns AuthoredReport\n\n
    update(final AuthoredReport object, final UpdateOptions options)\n
    '''
def updateDrillPath():
    '''returns DrillPath\n\n
    updateDrillPath(final DrillPath object, final UpdateOptions options)\n
    '''
def validate():
    '''returns AsynchReply\n\n
    validate(final SearchPathSingleObject objectPath, final ParameterValue[] parameterValues, final Option[] options)\n
    '''
def validateSpecification():
    '''returns AsynchReply\n\n
    validateSpecification(final AsynchSpecification specification, final ParameterValue[] parameterValues, final Option[] options)\n
    '''
def wait():
    '''returns AsynchReply\n\n
    wait(final AsynchRequest conversation, final ParameterValue[] parameterValues, final Option[] options)\n
    '''
