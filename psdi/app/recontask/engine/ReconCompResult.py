BOTH_DATASETS = "int  0"
DATASET1_ONLY = "int  1"
DATASET2_ONLY = "int  2"
OBJECT_NAME = "String  \"_Object Name\""
MAIN_ATTRIBUTE_NAME = "String  \"_Attribute Name\""
MAIN_ATTRIBUTE_VALUE = "String  \"_Attribute Value\""
MAIN_ATTRIBUTE_DATETIME_VALUE = "String  \"_Attribute Datetime Value\""
MAIN_ATTRIBUTE_MEASURE_UNIT = "String  \"_Attribute Measure Unit\""
def ReconCompResult():
    '''public ReconCompResult(final ReconInfo reconInfo, final String dataSet1ObjectName, final String dataSet2ObjectName)
    public ReconCompResult(final ReconInfo reconInfo, final String dataSet1ObjectName, final String dataSet2ObjectName, final int resultType)
    public ReconCompResult(final ReconInfo reconInfo, final String objectName, final int resultType)
    '''
def getResultType():
    '''public int getResultType()
    '''
def getCode():
    '''public String getCode()
    '''
def setCode():
    '''public void setCode(final String code)
    '''
def getRuleName():
    '''public String getRuleName()
    '''
def setRuleName():
    '''public void setRuleName(final String ruleName)
    '''
def isSuccessful():
    '''public boolean isSuccessful()
    '''
def setSuccessful():
    '''public void setSuccessful(final boolean successful)
    '''
def addDataSet1Attribute():
    '''public void addDataSet1Attribute(final String attributeName, final Object attributeValue)
    '''
def getDataSet1Attribute():
    '''public Object getDataSet1Attribute(final String attributeName)
    '''
def addDataSet2Attribute():
    '''public void addDataSet2Attribute(final String attributeName, final Object attributeValue)
    '''
def getDataSet2Attribute():
    '''public Object getDataSet2Attribute(final String attributeName)
    '''
def joinUsingAnd():
    '''public static ReconCompResult joinUsingAnd(final ReconCompResult r1, final ReconCompResult r2)
    '''
def joinUsingOr():
    '''public static ReconCompResult joinUsingOr(final ReconCompResult r1, final ReconCompResult r2)
    '''
def resolveItem():
    '''public static Object resolveItem(final Object item1, final Object item2)
    '''
def prepare():
    '''public void prepare(final Map linkValue1, final Map linkValue2)
    '''
def setIDAndKeys():
    '''public void setIDAndKeys(final Map idKey1, final Map idKey2, final boolean isRoot)
    public void setIDAndKeys(final ResultTableAttributes attributes, final Map idKey, final boolean isRoot, final boolean isDataSet1)
    '''
def setVoid():
    '''public void setVoid(final boolean isVoid)
    '''
def isVoid():
    '''public boolean isVoid()
    '''
def getRootValue1():
    '''public Map getRootValue1()
    '''
def setRootValue1():
    '''public void setRootValue1(final Map rootValue1)
    '''
def getRootValue2():
    '''public Map getRootValue2()
    '''
def setRootValue2():
    '''public void setRootValue2(final Map rootValue2)
    '''
def isSameAs():
    '''public boolean isSameAs(final ReconCompResult anotherResult)
    '''
def sameValue():
    '''public boolean sameValue(final Object o1, final Object o2)
    '''
def isSupersede():
    '''public boolean isSupersede(final ReconCompResult anotherResult)
    '''
