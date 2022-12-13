def AttributeStorageDefinition():
'''public AttributeStorageDefinition(final String[] names, AttributeClass[] storage)
public AttributeStorageDefinition(final String... names)
'''
pass
def getStorageClass():
'''public AttributeClass getStorageClass(final String attrName)
'''
pass
def hasAttribute():
'''public boolean hasAttribute(final String attrName)
'''
pass
def getNameIterator():
'''public Iterator<String> getNameIterator()
'''
pass
def getNames():
'''public String[] getNames()
'''
pass
def getClasses():
'''public AttributeClass[] getClasses()
'''
pass
def addDefinition():
'''public void addDefinition(final String name, final AttributeClass storage)
'''
pass
def getSelectColumns():
'''public String getSelectColumns()
'''
pass
def toString():
'''public String toString()
'''
pass
def expand():
'''public static AttributeStorageDefinition expand(final AttributeStorageDefinition asd, final String addCol, final AttributeClass addClass)
'''
pass
def reduce():
'''public static AttributeStorageDefinition reduce(final AttributeStorageDefinition asd, final String... removeAttrs)
'''
pass
def equals():
'''public boolean equals(final Object o)
'''
pass
def getTableASD():
'''public static AttributeStorageDefinition getTableASD(final Connection con, final String tablename)
'''
pass
def createTableSubsetDefinition():
'''public AttributeStorageDefinition createTableSubsetDefinition(final List<String> wantedColumns)
'''
pass
