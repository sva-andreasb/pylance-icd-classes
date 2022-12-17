def ():
    '''returns QNameSetBuilder\n\n
    ()\n
    (final QNameSetSpecification set)\n
    (final Set excludedURIs, final Set includedURIs, final Set excludedQNamesInIncludedURIs, final Set includedQNamesInExcludedURIs)\n
    (String str, final String targetURI)\n
    '''
def contains():
    '''returns boolean\n\n
    contains(final QName name)\n
    '''
def isAll():
    '''returns boolean\n\n
    isAll()\n
    '''
def isEmpty():
    '''returns boolean\n\n
    isEmpty()\n
    '''
def intersect():
    '''returns QNameSet\n\n
    intersect(final QNameSetSpecification set)\n
    '''
def union():
    '''returns QNameSet\n\n
    union(final QNameSetSpecification set)\n
    '''
def inverse():
    '''returns QNameSet\n\n
    inverse()\n
    '''
def containsAll():
    '''returns boolean\n\n
    containsAll(final QNameSetSpecification set)\n
    '''
def isDisjoint():
    '''returns boolean\n\n
    isDisjoint(final QNameSetSpecification set)\n
    '''
def clear():
    '''returns None\n\n
    clear()\n
    '''
def invert():
    '''returns None\n\n
    invert()\n
    '''
def add():
    '''returns None\n\n
    add(final QName qname)\n
    '''
def addNamespace():
    '''returns None\n\n
    addNamespace(final String uri)\n
    '''
def addAll():
    '''returns None\n\n
    addAll(final QNameSetSpecification set)\n
    '''
def remove():
    '''returns None\n\n
    remove(final QName qname)\n
    '''
def removeNamespace():
    '''returns None\n\n
    removeNamespace(final String uri)\n
    '''
def removeAll():
    '''returns None\n\n
    removeAll(final QNameSetSpecification set)\n
    '''
def restrict():
    '''returns None\n\n
    restrict(final QNameSetSpecification set)\n
    '''
def excludedURIs():
    '''returns Set\n\n
    excludedURIs()\n
    '''
def includedURIs():
    '''returns Set\n\n
    includedURIs()\n
    '''
def excludedQNamesInIncludedURIs():
    '''returns Set\n\n
    excludedQNamesInIncludedURIs()\n
    '''
def includedQNamesInExcludedURIs():
    '''returns Set\n\n
    includedQNamesInExcludedURIs()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def toQNameSet():
    '''returns QNameSet\n\n
    toQNameSet()\n
    '''
