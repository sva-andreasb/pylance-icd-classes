def QNameSetBuilder():
    '''    public QNameSetBuilder()
    public QNameSetBuilder(final QNameSetSpecification set)
    public QNameSetBuilder(final Set excludedURIs, final Set includedURIs, final Set excludedQNamesInIncludedURIs, final Set includedQNamesInExcludedURIs)
    public QNameSetBuilder(String str, final String targetURI)
    '''
def contains():
    '''    public boolean contains(final QName name)
    '''
def isAll():
    '''    public boolean isAll()
    '''
def isEmpty():
    '''    public boolean isEmpty()
    '''
def intersect():
    '''    public QNameSet intersect(final QNameSetSpecification set)
    '''
def union():
    '''    public QNameSet union(final QNameSetSpecification set)
    '''
def inverse():
    '''    public QNameSet inverse()
    '''
def containsAll():
    '''    public boolean containsAll(final QNameSetSpecification set)
    '''
def isDisjoint():
    '''    public boolean isDisjoint(final QNameSetSpecification set)
    '''
def clear():
    '''    public void clear()
    '''
def invert():
    '''    public void invert()
    '''
def add():
    '''    public void add(final QName qname)
    '''
def addNamespace():
    '''    public void addNamespace(final String uri)
    '''
def addAll():
    '''    public void addAll(final QNameSetSpecification set)
    '''
def remove():
    '''    public void remove(final QName qname)
    '''
def removeNamespace():
    '''    public void removeNamespace(final String uri)
    '''
def removeAll():
    '''    public void removeAll(final QNameSetSpecification set)
    '''
def restrict():
    '''    public void restrict(final QNameSetSpecification set)
    '''
def excludedURIs():
    '''    public Set excludedURIs()
    '''
def includedURIs():
    '''    public Set includedURIs()
    '''
def excludedQNamesInIncludedURIs():
    '''    public Set excludedQNamesInIncludedURIs()
    '''
def includedQNamesInExcludedURIs():
    '''    public Set includedQNamesInExcludedURIs()
    '''
def toString():
    '''    public String toString()
    '''
def toQNameSet():
    '''    public QNameSet toQNameSet()
    '''
