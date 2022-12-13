def STPrivacyList():
    '''    public STPrivacyList(final NdrInputStream ndrInputStream)
    public STPrivacyList(final NdrInputStream ndrInputStream, final boolean b)
    public STPrivacyList(final boolean excluding, final Hashtable people, final Hashtable targets, final Hashtable requestors)
    public STPrivacyList(final boolean excluding)
    '''
def loadNewList():
    '''    public static final STPrivacyList loadNewList(final NdrInputStream ndrInputStream)
    '''
def isExcluding():
    '''    public boolean isExcluding()
    '''
def setExcluding():
    '''    public void setExcluding(final boolean excluding)
    '''
def isSeenBy():
    '''    public boolean isSeenBy(final STUser stUser)
    '''
def addUser():
    '''    public void addUser(final STUser value)
    '''
def removeUser():
    '''    public void removeUser(final STUser stUser)
    '''
def addGroup():
    '''    public void addGroup(final STGroup value)
    '''
def removeGroup():
    '''    public void removeGroup(final STGroup stGroup)
    '''
def getPeople():
    '''    public Hashtable getPeople()
    '''
def getGroups():
    '''    public Hashtable getGroups()
    '''
def getTargets():
    '''    public Hashtable getTargets()
    '''
def getRequestors():
    '''    public Hashtable getRequestors()
    '''
def elements():
    '''    public Enumeration elements()
    '''
def getPeopleEnumeration():
    '''    public Enumeration getPeopleEnumeration()
    '''
def getGroupEnumeration():
    '''    public Enumeration getGroupEnumeration()
    '''
def getTargetElements():
    '''    public Enumeration getTargetElements()
    '''
def getRequestorElements():
    '''    public Enumeration getRequestorElements()
    '''
def dump():
    '''    public void dump(final NdrOutputStream ndrOutputStream, final boolean b)
    '''
def load():
    '''    public void load(final NdrInputStream ndrInputStream)
    '''
def loadPeople():
    '''    public void loadPeople(final NdrInputStream ndrInputStream)
    '''
def loadRequestors():
    '''    public boolean loadRequestors(final NdrInputStream ndrInputStream)
    '''
def clone():
    '''    public Object clone()
    '''
def newDump():
    '''    public void newDump(final NdrOutputStream ndrOutputStream, final boolean b)
    '''
