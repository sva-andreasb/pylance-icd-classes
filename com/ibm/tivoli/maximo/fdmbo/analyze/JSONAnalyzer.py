def JSONAnalyzer():
    '''    public JSONAnalyzer()
    '''
def ingest():
    '''    public JSONResourceInfo ingest(final byte[] jsonData, final byte[] schemaData, final String resourceName, final String collectionProp, final String dateType, final String dateFormat, final boolean optimize)
    '''
def isDateTime():
    '''    public boolean isDateTime(final String dateType, final String dateFormat, final String data)
    '''
def isDateTimeInMiliSec():
    '''    public boolean isDateTimeInMiliSec(final String dateType, final String propName, final long data)
    '''
def getMappedName():
    '''    public static String getMappedName(String propName, final boolean isObject)
    '''
def getResolvedName():
    '''    public static String getResolvedName(final String origPropName, String propName, int start)
    '''
def optimize():
    '''    public void optimize(final JSONResourceInfo resInfo)
    '''
def getResolvedAttrName():
    '''    public static String getResolvedAttrName(final String origAttrName, String attrName, final Set<String> props, int start)
    '''
def replaceInvalidChar():
    '''    public static String replaceInvalidChar(final String checkString)
    '''
def formatParameter():
    '''    public String formatParameter(final String url, final String paramter, final String whereClause)
    '''
def findParamters():
    '''    public String findParamters(final String paramName, final String whereClause, final boolean isRequired)
    '''
def licenseCheck():
    '''    public boolean licenseCheck(final String productName)
    '''
def logAPICall():
    '''    public void logAPICall(final String productName, final String resourceName, final UserInfo userInfo)
    '''
