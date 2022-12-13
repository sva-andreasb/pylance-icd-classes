def getType():
    '''    public String getType()
    '''
def getSubtype():
    '''    public String getSubtype()
    '''
def hashCode():
    '''    public int hashCode()
    '''
def equals():
    '''    public boolean equals(final Object rhs)
    '''
def toString():
    '''    public String toString()
    '''
def getAvailableTypes():
    '''    public static synchronized Set<String> getAvailableTypes()
    '''
def getAvailable():
    '''    public static synchronized Set<MeasureUnit> getAvailable(final String type)
    public static synchronized Set<MeasureUnit> getAvailable()
    '''
def internalGetInstance():
    '''    public static MeasureUnit internalGetInstance(final String type, final String subType)
    '''
def parseCoreUnitIdentifier():
    '''    public static MeasureUnit[] parseCoreUnitIdentifier(final String coreUnitIdentifier)
    '''
def resolveUnitPerUnit():
    '''    public static MeasureUnit resolveUnitPerUnit(final MeasureUnit unit, final MeasureUnit perUnit)
    '''
def create():
    '''    public MeasureUnit create(final String type, final String subType)
    public MeasureUnit create(final String unusedType, final String subType)
    public MeasureUnit create(final String type, final String subType)
    public MeasureUnit create(final String type, final String subType)
    '''
def put():
    '''    public void put(final UResource.Key key, final UResource.Value value, final boolean noFallback)
    public void put(final UResource.Key key, final UResource.Value value, final boolean noFallback)
    '''
def MeasureUnitProxy():
    '''    public MeasureUnitProxy(final String type, final String subType)
    public MeasureUnitProxy()
    '''
def writeExternal():
    '''    public void writeExternal(final ObjectOutput out)
    '''
def readExternal():
    '''    public void readExternal(final ObjectInput in)
    '''
