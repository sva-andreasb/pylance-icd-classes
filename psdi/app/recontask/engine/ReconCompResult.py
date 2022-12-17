BOTH_DATASETS = "int  0"
DATASET1_ONLY = "int  1"
DATASET2_ONLY = "int  2"
OBJECT_NAME = "String  \"_Object Name\""
MAIN_ATTRIBUTE_NAME = "String  \"_Attribute Name\""
MAIN_ATTRIBUTE_VALUE = "String  \"_Attribute Value\""
MAIN_ATTRIBUTE_DATETIME_VALUE = "String  \"_Attribute Datetime Value\""
MAIN_ATTRIBUTE_MEASURE_UNIT = "String  \"_Attribute Measure Unit\""
def ():
    '''returns ReconCompResult\n\n
    (final ReconInfo reconInfo, final String dataSet1ObjectName, final String dataSet2ObjectName)\n
    (final ReconInfo reconInfo, final String dataSet1ObjectName, final String dataSet2ObjectName, final int resultType)\n
    (final ReconInfo reconInfo, final String objectName, final int resultType)\n
    '''
def getResultType():
    '''returns int\n\n
    getResultType()\n
    '''
def getCode():
    '''returns String\n\n
    getCode()\n
    '''
def setCode():
    '''returns None\n\n
    setCode(final String code)\n
    '''
def getRuleName():
    '''returns String\n\n
    getRuleName()\n
    '''
def setRuleName():
    '''returns None\n\n
    setRuleName(final String ruleName)\n
    '''
def isSuccessful():
    '''returns boolean\n\n
    isSuccessful()\n
    '''
def setSuccessful():
    '''returns None\n\n
    setSuccessful(final boolean successful)\n
    '''
def addDataSet1Attribute():
    '''returns None\n\n
    addDataSet1Attribute(final String attributeName, final Object attributeValue)\n
    '''
def getDataSet1Attribute():
    '''returns Object\n\n
    getDataSet1Attribute(final String attributeName)\n
    '''
def addDataSet2Attribute():
    '''returns None\n\n
    addDataSet2Attribute(final String attributeName, final Object attributeValue)\n
    '''
def getDataSet2Attribute():
    '''returns Object\n\n
    getDataSet2Attribute(final String attributeName)\n
    '''
def prepare():
    '''returns None\n\n
    prepare(final Map linkValue1, final Map linkValue2)\n
    '''
def setIDAndKeys():
    '''returns None\n\n
    setIDAndKeys(final Map idKey1, final Map idKey2, final boolean isRoot)\n
    setIDAndKeys(final ResultTableAttributes attributes, final Map idKey, final boolean isRoot, final boolean isDataSet1)\n
    '''
def setVoid():
    '''returns None\n\n
    setVoid(final boolean isVoid)\n
    '''
def isVoid():
    '''returns boolean\n\n
    isVoid()\n
    '''
def getRootValue1():
    '''returns Map\n\n
    getRootValue1()\n
    '''
def setRootValue1():
    '''returns None\n\n
    setRootValue1(final Map rootValue1)\n
    '''
def getRootValue2():
    '''returns Map\n\n
    getRootValue2()\n
    '''
def setRootValue2():
    '''returns None\n\n
    setRootValue2(final Map rootValue2)\n
    '''
def isSameAs():
    '''returns boolean\n\n
    isSameAs(final ReconCompResult anotherResult)\n
    '''
def sameValue():
    '''returns boolean\n\n
    sameValue(final Object o1, final Object o2)\n
    '''
def isSupersede():
    '''returns boolean\n\n
    isSupersede(final ReconCompResult anotherResult)\n
    '''
