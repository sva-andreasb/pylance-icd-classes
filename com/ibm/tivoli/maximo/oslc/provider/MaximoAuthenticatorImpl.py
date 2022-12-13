OSLC_CONTEXT = "String  \"oslc\""
def authenticateRequest():
    '''public MXSession authenticateRequest(final OslcRequest request)
    '''
def setMXToken():
    '''public String setMXToken(final MXSession mxSession)
    '''
def isSupportedLangCode():
    '''public boolean isSupportedLangCode(final String langCode)
    '''
def verifySignature():
    '''public boolean verifySignature(final HttpServletRequest request, final MboSetRemote msr, final String username, final String password, final String reason)
    '''
def logSignatureVerification():
    '''public void logSignatureVerification(final MboSetRemote msr, final String username, final String reason, final boolean authenticated)
    '''
