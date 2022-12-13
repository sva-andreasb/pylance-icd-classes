def authenticate():
'''public static boolean authenticate(final HttpServletRequest request, final String mxToken, final String userId, final String tenantCode)
public static boolean authenticate(final HttpServletRequest request, final String mxToken, final String userId, final String tenantCode, final boolean isDirectPrint)
'''
pass
def isAuthenticatedSession():
'''public static boolean isAuthenticatedSession(final HttpServletRequest request)
'''
pass
def encodeForSecureAttachment():
'''public static void encodeForSecureAttachment(final Vector attVec, final Vector securedAttachFlags, final WebClientSession clientSession, final String tenantCode)
public static void encodeForSecureAttachment(final Vector attVec, final Vector securedAttachFlags, final WebClientSession clientSession, final String tenantCode, final HttpServletRequest requ)
'''
pass
def getRequestParameterValue():
'''public static String getRequestParameterValue(final HttpServletRequest request, final String paramName)
'''
pass
def getRequestParameterValues():
'''public static String[] getRequestParameterValues(final HttpServletRequest request, final String paramName)
public static String[] getRequestParameterValues(final HttpServletRequest request, final String paramName, final boolean convertToUft8)
'''
pass
def convertSafeToOriginalValue():
'''public static String[] convertSafeToOriginalValue(final String[] paramValues)
'''
pass
