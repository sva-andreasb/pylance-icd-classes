def ():
    '''returns AttributeStorageDefinition\n\n
    (final String[] names, AttributeClass[] storage)\n
    (final String... names)\n
    '''
def getStorageClass():
    '''returns AttributeClass\n\n
    getStorageClass(final String attrName)\n
    '''
def hasAttribute():
    '''returns boolean\n\n
    hasAttribute(final String attrName)\n
    '''
def getNameIterator():
    '''returns Iterator<String>\n\n
    getNameIterator()\n
    '''
def getNames():
    '''returns String[]\n\n
    getNames()\n
    '''
def getClasses():
    '''returns AttributeClass[]\n\n
    getClasses()\n
    '''
def addDefinition():
    '''returns None\n\n
    addDefinition(final String name, final AttributeClass storage)\n
    '''
def getSelectColumns():
    '''returns String\n\n
    getSelectColumns()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object o)\n
    '''
def createTableSubsetDefinition():
    '''returns AttributeStorageDefinition\n\n
    createTableSubsetDefinition(final List<String> wantedColumns)\n
    '''
