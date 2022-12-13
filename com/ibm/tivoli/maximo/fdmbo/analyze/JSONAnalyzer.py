def JSONAnalyzer():
'''public JSONAnalyzer()
'''
pass
def ingest():
'''public JSONResourceInfo ingest(final byte[] jsonData, final byte[] schemaData, final String resourceName, final String collectionProp, final String dateType, final String dateFormat, final boolean optimize)
'''
pass
def isDateTime():
'''public boolean isDateTime(final String dateType, final String dateFormat, final String data)
'''
pass
def isDateTimeInMiliSec():
'''public boolean isDateTimeInMiliSec(final String dateType, final String propName, final long data)
'''
pass
def getMappedName():
'''public static String getMappedName(String propName, final boolean isObject)
'''
pass
def getResolvedName():
'''public static String getResolvedName(final String origPropName, String propName, int start)
'''
pass
def optimize():
'''public void optimize(final JSONResourceInfo resInfo)
'''
pass
def getResolvedAttrName():
'''public static String getResolvedAttrName(final String origAttrName, String attrName, final Set<String> props, int start)
'''
pass
def replaceInvalidChar():
'''public static String replaceInvalidChar(final String checkString)
'''
pass
def formatParameter():
'''public String formatParameter(final String url, final String paramter, final String whereClause)
'''
pass
def findParamters():
'''public String findParamters(final String paramName, final String whereClause, final boolean isRequired)
'''
pass
def licenseCheck():
'''public boolean licenseCheck(final String productName)
'''
pass
def logAPICall():
'''public void logAPICall(final String productName, final String resourceName, final UserInfo userInfo)
'''
pass
