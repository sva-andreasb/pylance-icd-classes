def OslcErrorHandler():
'''public OslcErrorHandler(final UserInfo userInfo)
'''
pass
def setNoErrorTracking():
'''public void setNoErrorTracking(final boolean noErrTracking)
'''
pass
def errorToJson():
'''public static void errorToJson(final Map<String, Exception> errors, final Mbo mbo)
'''
pass
def serializeError():
'''public static JSONObject serializeError(final String attr, final Throwable e, final Mbo mbo, final boolean ignoreApiErrs)
'''
pass
def setForErrorSerialization():
'''public void setForErrorSerialization(final boolean errser)
'''
pass
def serializeExtendedError():
'''public byte[] serializeExtendedError(final String bmxId, final Map<String, String> headers, final OslcRequest request)
'''
pass
def getExtendedErrorURL():
'''public String getExtendedErrorURL(final MXException me)
'''
pass
def getErrorId():
'''public String getErrorId(final MXException me)
'''
pass
def sendJsonError():
'''public void sendJsonError(final OslcErrorResponse osr, final HttpServletRequest request, final HttpServletResponse resp, final int errorcode, final JSONObject optionsJo, final JSONArray params)
'''
pass
def handleError():
'''public OslcErrorResponse handleError(Throwable t, final HttpServletRequest request, final HttpServletResponse resp)
'''
pass
