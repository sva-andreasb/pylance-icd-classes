def get():
    '''returns IRelationship\n\n
    get(final String handle)\n
    get(final IProgramElement source)\n
    get(final String source, final IRelationship.Kind kind, final String relationshipName, final boolean runtimeTest, final boolean createIfMissing)\n
    get(final IProgramElement source, final IRelationship.Kind kind, final String relationshipName, final boolean runtimeTest, final boolean createIfMissing)\n
    get(final IProgramElement source, final IRelationship.Kind kind, final String relationshipName)\n
    '''
def remove():
    '''returns boolean\n\n
    remove(final String source, final IRelationship relationship)\n
    '''
def removeAll():
    '''returns None\n\n
    removeAll(final String source)\n
    '''
def put():
    '''returns None\n\n
    put(final String source, final IRelationship relationship)\n
    put(final IProgramElement source, final IRelationship relationship)\n
    '''
def clear():
    '''returns None\n\n
    clear()\n
    '''
def getEntries():
    '''returns Set<String>\n\n
    getEntries()\n
    '''
