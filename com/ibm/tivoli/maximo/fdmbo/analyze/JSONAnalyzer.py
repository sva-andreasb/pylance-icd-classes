def ():
    '''returns JSONAnalyzer\n\n
    ()\n
    '''
def ingest():
    '''returns JSONResourceInfo\n\n
    ingest(final byte[] jsonData, final byte[] schemaData, final String resourceName, final String collectionProp, final String dateType, final String dateFormat, final boolean optimize)\n
    '''
def isDateTime():
    '''returns boolean\n\n
    isDateTime(final String dateType, final String dateFormat, final String data)\n
    '''
def isDateTimeInMiliSec():
    '''returns boolean\n\n
    isDateTimeInMiliSec(final String dateType, final String propName, final long data)\n
    '''
def optimize():
    '''returns None\n\n
    optimize(final JSONResourceInfo resInfo)\n
    '''
def formatParameter():
    '''returns String\n\n
    formatParameter(final String url, final String paramter, final String whereClause)\n
    '''
def findParamters():
    '''returns String\n\n
    findParamters(final String paramName, final String whereClause, final boolean isRequired)\n
    '''
def licenseCheck():
    '''returns boolean\n\n
    licenseCheck(final String productName)\n
    '''
def logAPICall():
    '''returns None\n\n
    logAPICall(final String productName, final String resourceName, final UserInfo userInfo)\n
    '''
