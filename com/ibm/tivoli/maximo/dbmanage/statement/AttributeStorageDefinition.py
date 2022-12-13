def AttributeStorageDefinition():
    '''    public AttributeStorageDefinition(final String[] names, AttributeClass[] storage)
    public AttributeStorageDefinition(final String... names)
    '''
def getStorageClass():
    '''    public AttributeClass getStorageClass(final String attrName)
    '''
def hasAttribute():
    '''    public boolean hasAttribute(final String attrName)
    '''
def getNameIterator():
    '''    public Iterator<String> getNameIterator()
    '''
def getNames():
    '''    public String[] getNames()
    '''
def getClasses():
    '''    public AttributeClass[] getClasses()
    '''
def addDefinition():
    '''    public void addDefinition(final String name, final AttributeClass storage)
    '''
def getSelectColumns():
    '''    public String getSelectColumns()
    '''
def toString():
    '''    public String toString()
    '''
def expand():
    '''    public static AttributeStorageDefinition expand(final AttributeStorageDefinition asd, final String addCol, final AttributeClass addClass)
    '''
def reduce():
    '''    public static AttributeStorageDefinition reduce(final AttributeStorageDefinition asd, final String... removeAttrs)
    '''
def equals():
    '''    public boolean equals(final Object o)
    '''
def getTableASD():
    '''    public static AttributeStorageDefinition getTableASD(final Connection con, final String tablename)
    '''
def createTableSubsetDefinition():
    '''    public AttributeStorageDefinition createTableSubsetDefinition(final List<String> wantedColumns)
    '''
