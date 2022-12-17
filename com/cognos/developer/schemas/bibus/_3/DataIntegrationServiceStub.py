def ():
    '''returns DataIntegrationServiceStub\n\n
    ()\n
    (final URL endpointURL, final Service service)\n
    (final Service service)\n
    '''
def cancel():
    '''returns None\n\n
    cancel(final AsynchRequest conversation)\n
    '''
def release():
    '''returns None\n\n
    release(final AsynchRequest conversation)\n
    '''
def run():
    '''returns AsynchReply\n\n
    run(final SearchPathSingleObject objectPath, final ParameterValue[] parameterValues, final Option[] options)\n
    '''
def runSpecification():
    '''returns AsynchReply\n\n
    runSpecification(final AsynchSpecification specification, final ParameterValue[] parameterValues, final Option[] options)\n
    '''
def wait():
    '''returns AsynchReply\n\n
    wait(final AsynchRequest conversation, final ParameterValue[] parameterValues, final Option[] options)\n
    '''
