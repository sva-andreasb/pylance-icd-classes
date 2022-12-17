def maxSecureProcessWorkflow():
    '''returns byte[]\n\n
    maxSecureProcessWorkflow(final String loginid, final String password, final byte[] reqMosData, final String wfName)\n
    '''
def maxAPIKeySecureProcessWorkflow():
    '''returns byte[]\n\n
    maxAPIKeySecureProcessWorkflow(final String apikey, final byte[] reqMosData, final String wfName)\n
    '''
def processWorkflow():
    '''returns byte[]\n\n
    processWorkflow(final byte[] reqMosData, final String wfName)\n
    '''
def secureProcessWorkflow():
    '''returns byte[]\n\n
    secureProcessWorkflow(final byte[] reqMosData, final String wfName, final Principal principal)\n
    '''
def secureProcessWorkflowInternal():
    '''returns byte[]\n\n
    secureProcessWorkflowInternal(final UserInfo userInfo, final byte[] processData, String wfName)\n
    '''
