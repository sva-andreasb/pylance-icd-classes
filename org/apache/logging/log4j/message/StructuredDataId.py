RESERVED = "int  -1"
def StructuredDataId():
    '''    public StructuredDataId(final String name)
    public StructuredDataId(final String name, final int maxLength)
    public StructuredDataId(final String name, final String[] required, final String[] optional)
    public StructuredDataId(final String name, final String[] required, final String[] optional, int maxLength)
    public StructuredDataId(final String name, final int enterpriseNumber, final String[] required, final String[] optional)
    public StructuredDataId(final String name, final int enterpriseNumber, final String[] required, final String[] optional, final int maxLength)
    '''
def makeId():
    '''    public StructuredDataId makeId(final StructuredDataId id)
    public StructuredDataId makeId(final String defaultId, final int anEnterpriseNumber)
    '''
def getRequired():
    '''    public String[] getRequired()
    '''
def getOptional():
    '''    public String[] getOptional()
    '''
def getName():
    '''    public String getName()
    '''
def getEnterpriseNumber():
    '''    public int getEnterpriseNumber()
    '''
def isReserved():
    '''    public boolean isReserved()
    '''
def toString():
    '''    public String toString()
    '''
def formatTo():
    '''    public void formatTo(final StringBuilder buffer)
    '''
