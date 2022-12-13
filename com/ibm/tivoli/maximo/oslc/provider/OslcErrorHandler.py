def OslcErrorHandler():
    '''public OslcErrorHandler(final UserInfo userInfo)
    '''
def setNoErrorTracking():
    '''public void setNoErrorTracking(final boolean noErrTracking)
    '''
def errorToJson():
    '''public static void errorToJson(final Map<String, Exception> errors, final Mbo mbo)
    '''
def serializeError():
    '''public static JSONObject serializeError(final String attr, final Throwable e, final Mbo mbo, final boolean ignoreApiErrs)
    '''
def setForErrorSerialization():
    '''public void setForErrorSerialization(final boolean errser)
    '''
def serializeExtendedError():
    '''public byte[] serializeExtendedError(final String bmxId, final Map<String, String> headers, final OslcRequest request)
    '''
def getExtendedErrorURL():
    '''public String getExtendedErrorURL(final MXException me)
    '''
def getErrorId():
    '''public String getErrorId(final MXException me)
    '''
def sendJsonError():
    '''public void sendJsonError(final OslcErrorResponse osr, final HttpServletRequest request, final HttpServletResponse resp, final int errorcode, final JSONObject optionsJo, final JSONArray params)
    '''
def handleError():
    '''public OslcErrorResponse handleError(Throwable t, final HttpServletRequest request, final HttpServletResponse resp)
    '''
