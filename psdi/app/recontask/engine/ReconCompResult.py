BOTH_DATASETS = "int  0"
DATASET1_ONLY = "int  1"
DATASET2_ONLY = "int  2"
OBJECT_NAME = "String  _Object Name""
MAIN_ATTRIBUTE_NAME = "String  _Attribute Name""
MAIN_ATTRIBUTE_VALUE = "String  _Attribute Value""
MAIN_ATTRIBUTE_DATETIME_VALUE = "String  _Attribute Datetime Value""
MAIN_ATTRIBUTE_MEASURE_UNIT = "String  _Attribute Measure Unit""
def ReconCompResult():
'''public ReconCompResult(final ReconInfo reconInfo, final String dataSet1ObjectName, final String dataSet2ObjectName)
public ReconCompResult(final ReconInfo reconInfo, final String dataSet1ObjectName, final String dataSet2ObjectName, final int resultType)
public ReconCompResult(final ReconInfo reconInfo, final String objectName, final int resultType)
'''
pass
def getResultType():
'''public int getResultType()
'''
pass
def getCode():
'''public String getCode()
'''
pass
def setCode():
'''public void setCode(final String code)
'''
pass
def getRuleName():
'''public String getRuleName()
'''
pass
def setRuleName():
'''public void setRuleName(final String ruleName)
'''
pass
def isSuccessful():
'''public boolean isSuccessful()
'''
pass
def setSuccessful():
'''public void setSuccessful(final boolean successful)
'''
pass
def addDataSet1Attribute():
'''public void addDataSet1Attribute(final String attributeName, final Object attributeValue)
'''
pass
def getDataSet1Attribute():
'''public Object getDataSet1Attribute(final String attributeName)
'''
pass
def addDataSet2Attribute():
'''public void addDataSet2Attribute(final String attributeName, final Object attributeValue)
'''
pass
def getDataSet2Attribute():
'''public Object getDataSet2Attribute(final String attributeName)
'''
pass
def joinUsingAnd():
'''public static ReconCompResult joinUsingAnd(final ReconCompResult r1, final ReconCompResult r2)
'''
pass
def joinUsingOr():
'''public static ReconCompResult joinUsingOr(final ReconCompResult r1, final ReconCompResult r2)
'''
pass
def resolveItem():
'''public static Object resolveItem(final Object item1, final Object item2)
'''
pass
def prepare():
'''public void prepare(final Map linkValue1, final Map linkValue2)
'''
pass
def setIDAndKeys():
'''public void setIDAndKeys(final Map idKey1, final Map idKey2, final boolean isRoot)
public void setIDAndKeys(final ResultTableAttributes attributes, final Map idKey, final boolean isRoot, final boolean isDataSet1)
'''
pass
def setVoid():
'''public void setVoid(final boolean isVoid)
'''
pass
def isVoid():
'''public boolean isVoid()
'''
pass
def getRootValue1():
'''public Map getRootValue1()
'''
pass
def setRootValue1():
'''public void setRootValue1(final Map rootValue1)
'''
pass
def getRootValue2():
'''public Map getRootValue2()
'''
pass
def setRootValue2():
'''public void setRootValue2(final Map rootValue2)
'''
pass
def isSameAs():
'''public boolean isSameAs(final ReconCompResult anotherResult)
'''
pass
def sameValue():
'''public boolean sameValue(final Object o1, final Object o2)
'''
pass
def isSupersede():
'''public boolean isSupersede(final ReconCompResult anotherResult)
'''
pass
