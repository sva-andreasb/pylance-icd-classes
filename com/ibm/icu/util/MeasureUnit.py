def getType():
'''public String getType()
'''
pass
def getSubtype():
'''public String getSubtype()
'''
pass
def hashCode():
'''public int hashCode()
'''
pass
def equals():
'''public boolean equals(final Object rhs)
'''
pass
def toString():
'''public String toString()
'''
pass
def getAvailableTypes():
'''public static synchronized Set<String> getAvailableTypes()
'''
pass
def getAvailable():
'''public static synchronized Set<MeasureUnit> getAvailable(final String type)
public static synchronized Set<MeasureUnit> getAvailable()
'''
pass
def internalGetInstance():
'''public static MeasureUnit internalGetInstance(final String type, final String subType)
'''
pass
def parseCoreUnitIdentifier():
'''public static MeasureUnit[] parseCoreUnitIdentifier(final String coreUnitIdentifier)
'''
pass
def resolveUnitPerUnit():
'''public static MeasureUnit resolveUnitPerUnit(final MeasureUnit unit, final MeasureUnit perUnit)
'''
pass
def create():
'''public MeasureUnit create(final String type, final String subType)
public MeasureUnit create(final String unusedType, final String subType)
public MeasureUnit create(final String type, final String subType)
public MeasureUnit create(final String type, final String subType)
'''
pass
def put():
'''public void put(final UResource.Key key, final UResource.Value value, final boolean noFallback)
public void put(final UResource.Key key, final UResource.Value value, final boolean noFallback)
'''
pass
def MeasureUnitProxy():
'''public MeasureUnitProxy(final String type, final String subType)
public MeasureUnitProxy()
'''
pass
def writeExternal():
'''public void writeExternal(final ObjectOutput out)
'''
pass
def readExternal():
'''public void readExternal(final ObjectInput in)
'''
pass
