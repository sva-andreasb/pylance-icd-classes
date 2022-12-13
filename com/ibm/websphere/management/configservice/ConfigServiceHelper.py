def getConfigDataId():
'''public static ConfigDataId getConfigDataId(final AttributeList attrList)
public static ConfigDataId getConfigDataId(final ObjectName objName)
'''
pass
def getAttributeValue():
'''public static Object getAttributeValue(final AttributeList attrList, final String name)
'''
pass
def setAttributeValue():
'''public static void setAttributeValue(final AttributeList attrList, final String name, final Object value)
'''
pass
def removeAttribute():
'''public static Object removeAttribute(final AttributeList attrList, final String name)
'''
pass
def lookup():
'''public static AttributeList lookup(final AttributeList attrList, final ConfigDataId id)
'''
pass
def createObjectName():
'''public static ObjectName createObjectName(final AttributeList attrList)
public static ObjectName createObjectName(final ConfigDataId id)
public static ObjectName createObjectName(final ConfigDataId id, final String type)
public static ObjectName createObjectName(final ConfigDataId id, final String type, final String displayName)
public static ObjectName createObjectName(final Properties props)
public static ObjectName createObjectName(final String domain, final Properties props)
'''
pass
def getConfigDataType():
'''public static String getConfigDataType(final ObjectName objName)
'''
pass
def getDisplayName():
'''public static String getDisplayName(final ObjectName objName)
'''
pass
def checkIfNameValid():
'''public static boolean checkIfNameValid(final String aName)
'''
pass
def getObjectLocation():
'''public static Properties getObjectLocation(final ObjectName objName)
'''
pass
def convertObjectNameToConfigDataId():
'''public static ConfigDataId convertObjectNameToConfigDataId(final ObjectName on)
'''
pass
