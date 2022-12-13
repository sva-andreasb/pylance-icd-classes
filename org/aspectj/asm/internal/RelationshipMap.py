def get():
    '''public List<IRelationship> get(final String handle)
    public List<IRelationship> get(final IProgramElement source)
    public IRelationship get(final String source, final IRelationship.Kind kind, final String relationshipName, final boolean runtimeTest, final boolean createIfMissing)
    public IRelationship get(final IProgramElement source, final IRelationship.Kind kind, final String relationshipName, final boolean runtimeTest, final boolean createIfMissing)
    public IRelationship get(final IProgramElement source, final IRelationship.Kind kind, final String relationshipName)
    '''
def remove():
    '''public boolean remove(final String source, final IRelationship relationship)
    '''
def removeAll():
    '''public void removeAll(final String source)
    '''
def put():
    '''public void put(final String source, final IRelationship relationship)
    public void put(final IProgramElement source, final IRelationship relationship)
    '''
def clear():
    '''public void clear()
    '''
def getEntries():
    '''public Set<String> getEntries()
    '''
