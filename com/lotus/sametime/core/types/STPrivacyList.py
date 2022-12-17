def ():
    '''returns STPrivacyList\n\n
    (final NdrInputStream ndrInputStream)\n
    (final NdrInputStream ndrInputStream, final boolean b)\n
    (final boolean excluding, final Hashtable people, final Hashtable targets, final Hashtable requestors)\n
    (final boolean excluding)\n
    '''
def isExcluding():
    '''returns boolean\n\n
    isExcluding()\n
    '''
def setExcluding():
    '''returns None\n\n
    setExcluding(final boolean excluding)\n
    '''
def isSeenBy():
    '''returns boolean\n\n
    isSeenBy(final STUser stUser)\n
    '''
def addUser():
    '''returns None\n\n
    addUser(final STUser value)\n
    '''
def removeUser():
    '''returns None\n\n
    removeUser(final STUser stUser)\n
    '''
def addGroup():
    '''returns None\n\n
    addGroup(final STGroup value)\n
    '''
def removeGroup():
    '''returns None\n\n
    removeGroup(final STGroup stGroup)\n
    '''
def getPeople():
    '''returns Hashtable\n\n
    getPeople()\n
    '''
def getGroups():
    '''returns Hashtable\n\n
    getGroups()\n
    '''
def getTargets():
    '''returns Hashtable\n\n
    getTargets()\n
    '''
def getRequestors():
    '''returns Hashtable\n\n
    getRequestors()\n
    '''
def elements():
    '''returns Enumeration\n\n
    elements()\n
    '''
def getPeopleEnumeration():
    '''returns Enumeration\n\n
    getPeopleEnumeration()\n
    '''
def getGroupEnumeration():
    '''returns Enumeration\n\n
    getGroupEnumeration()\n
    '''
def getTargetElements():
    '''returns Enumeration\n\n
    getTargetElements()\n
    '''
def getRequestorElements():
    '''returns Enumeration\n\n
    getRequestorElements()\n
    '''
def dump():
    '''returns None\n\n
    dump(final NdrOutputStream ndrOutputStream, final boolean b)\n
    '''
def load():
    '''returns None\n\n
    load(final NdrInputStream ndrInputStream)\n
    '''
def loadPeople():
    '''returns None\n\n
    loadPeople(final NdrInputStream ndrInputStream)\n
    '''
def loadRequestors():
    '''returns boolean\n\n
    loadRequestors(final NdrInputStream ndrInputStream)\n
    '''
def clone():
    '''returns Object\n\n
    clone()\n
    '''
def newDump():
    '''returns None\n\n
    newDump(final NdrOutputStream ndrOutputStream, final boolean b)\n
    '''
