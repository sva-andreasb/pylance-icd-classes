HasValue = "boolean  true"
NoValue = "boolean  false"
def ():
    '''returns ArgDecl\n\n
    (final boolean hasValue)\n
    (final boolean hasValue, final String name)\n
    (final boolean hasValue, final String name, final ArgHandler handler)\n
    (final boolean hasValue, final String name1, final String name2)\n
    (final boolean hasValue, final String name1, final String name2, final ArgHandler handler)\n
    (final boolean hasValue, final String name1, final String name2, final String name3)\n
    (final boolean hasValue, final String name1, final String name2, final String name3, final ArgHandler handler)\n
    (final boolean hasValue, final String name1, final String name2, final String name3, final String name4)\n
    (final boolean hasValue, final String name1, final String name2, final String name3, final String name4, final ArgHandler handler)\n
    (final boolean hasValue, final String name1, final String name2, final String name3, final String name4, final String name5, final ArgHandler handler)\n
    '''
def addName():
    '''returns None\n\n
    addName(String name)\n
    '''
def getNames():
    '''returns Set<String>\n\n
    getNames()\n
    '''
def names():
    '''returns Iterator<String>\n\n
    names()\n
    '''
def addHook():
    '''returns None\n\n
    addHook(final ArgHandler argHandler)\n
    '''
def takesValue():
    '''returns boolean\n\n
    takesValue()\n
    '''
def matches():
    '''returns boolean\n\n
    matches(final Arg a)\n
    matches(String arg)\n
    '''
