OSLC_CONTEXT = "String  \"oslc\""
def authenticateRequest():
    '''returns MXSession\n\n
    authenticateRequest(final OslcRequest request)\n
    '''
def setMXToken():
    '''returns String\n\n
    setMXToken(final MXSession mxSession)\n
    '''
def isSupportedLangCode():
    '''returns boolean\n\n
    isSupportedLangCode(final String langCode)\n
    '''
def verifySignature():
    '''returns boolean\n\n
    verifySignature(final HttpServletRequest request, final MboSetRemote msr, final String username, final String password, final String reason)\n
    '''
def logSignatureVerification():
    '''returns None\n\n
    logSignatureVerification(final MboSetRemote msr, final String username, final String reason, final boolean authenticated)\n
    '''
