def ():
    '''returns OslcErrorHandler\n\n
    (final UserInfo userInfo)\n
    '''
def setNoErrorTracking():
    '''returns None\n\n
    setNoErrorTracking(final boolean noErrTracking)\n
    '''
def setForErrorSerialization():
    '''returns None\n\n
    setForErrorSerialization(final boolean errser)\n
    '''
def serializeExtendedError():
    '''returns byte[]\n\n
    serializeExtendedError(final String bmxId, final Map<String, String> headers, final OslcRequest request)\n
    '''
def getExtendedErrorURL():
    '''returns String\n\n
    getExtendedErrorURL(final MXException me)\n
    '''
def getErrorId():
    '''returns String\n\n
    getErrorId(final MXException me)\n
    '''
def sendJsonError():
    '''returns None\n\n
    sendJsonError(final OslcErrorResponse osr, final HttpServletRequest request, final HttpServletResponse resp, final int errorcode, final JSONObject optionsJo, final JSONArray params)\n
    '''
def handleError():
    '''returns OslcErrorResponse\n\n
    handleError(Throwable t, final HttpServletRequest request, final HttpServletResponse resp)\n
    '''
