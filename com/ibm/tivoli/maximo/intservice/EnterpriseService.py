def ():
    '''returns EnterpriseService\n\n
    ()\n
    '''
def processExternalDataSync():
    '''returns byte[]\n\n
    processExternalDataSync(final byte[] extData, final String serviceName, final String sender)\n
    '''
def secureProcessExternalDataSync():
    '''returns byte[]\n\n
    secureProcessExternalDataSync(final byte[] extData, final String serviceName, final String sender, final Principal principal)\n
    '''
def maxSecureProcessExternalDataSync():
    '''returns byte[]\n\n
    maxSecureProcessExternalDataSync(final String loginid, final String password, final byte[] extData, final String serviceName, final String sender)\n
    '''
def maxAPIKeySecureProcessExternalDataSync():
    '''returns byte[]\n\n
    maxAPIKeySecureProcessExternalDataSync(final String apikey, final byte[] extData, final String serviceName, final String sender)\n
    '''
def secureProcessExternalDataAsync():
    '''returns byte[]\n\n
    secureProcessExternalDataAsync(final byte[] extData, final String serviceName, final String sender, final Principal principal)\n
    '''
def maxSecureProcessExternalDataAsync():
    '''returns byte[]\n\n
    maxSecureProcessExternalDataAsync(final String loginid, final String password, final byte[] extData, final String serviceName, final String sender)\n
    '''
def maxAPIKeySecureProcessExternalDataAsync():
    '''returns byte[]\n\n
    maxAPIKeySecureProcessExternalDataAsync(final String apikey, final byte[] extData, final String serviceName, final String sender)\n
    '''
def processExternalDataAsync():
    '''returns byte[]\n\n
    processExternalDataAsync(final byte[] extData, final String serviceName, final String sender)\n
    '''
def wsProcessExternalData():
    '''returns byte[]\n\n
    wsProcessExternalData(final byte[] extData, final String wsName)\n
    '''
def wsSecureProcessExternalData():
    '''returns byte[]\n\n
    wsSecureProcessExternalData(final byte[] extData, final String wsName, final Principal principal)\n
    '''
def wsMaxSecureProcessExternalData():
    '''returns byte[]\n\n
    wsMaxSecureProcessExternalData(final String loginid, final String password, final byte[] extData, final String wsName)\n
    '''
def wsMaxAPIKeySecureProcessExternalData():
    '''returns byte[]\n\n
    wsMaxAPIKeySecureProcessExternalData(final String apikey, final byte[] extData, final String wsName)\n
    '''
