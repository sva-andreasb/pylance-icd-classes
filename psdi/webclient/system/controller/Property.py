TRANSLATE_FLAG = "int  1"
GLOBAL_FLAG = "int  2"
FORMAT_FLAG = "int  16"
FINAL = "int  32"
SYSTEM = "int  64"
NONCONDITIONAL = "int  128"
RENDERID = "int  256"
LABEL_SOURCE_ID = "String  id""
def Property():
'''public Property(final String name)
public Property(final String name, final String value)
public Property(final Property prop)
'''
pass
def setFlag():
'''public void setFlag(final long index)
'''
pass
def setFlags():
'''public void setFlags(final long flags)
'''
pass
def setValue():
'''public void setValue(final String value)
'''
pass
def getValue():
'''public String getValue()
public String getValue(final List<String> paramValues)
'''
pass
def setDetaultValue():
'''public void setDetaultValue(final String val)
'''
pass
def getDefaultValue():
'''public String getDefaultValue()
'''
pass
def setName():
'''public void setName(final String name)
'''
pass
def getName():
'''public String getName()
'''
pass
def clearFlags():
'''public void clearFlags()
'''
pass
def clearFlag():
'''public void clearFlag(final long index)
'''
pass
def getFlag():
'''public boolean getFlag(final long index)
'''
pass
def getFlags():
'''public long getFlags()
'''
pass
def clone():
'''public Object clone()
'''
pass
def setFlagsFromString():
'''public void setFlagsFromString(final String flags)
'''
pass
def setFlagFromString():
'''public void setFlagFromString(final String flag)
'''
pass
def isParameterized():
'''public boolean isParameterized()
'''
pass
def getParameterList():
'''public List<String> getParameterList()
'''
pass
def setRegexPattern():
'''public void setRegexPattern(final String regex)
'''
pass
def getTranslatable():
'''public String getTranslatable(final WebClientSession sc, final String controlId, final String property)
public String getTranslatable(final WebClientSession sc, final String controlId, final String property, final String defaultValue)
'''
pass
def getString():
'''public String getString(final String property)
'''
pass
def toString():
'''public String toString()
'''
pass
