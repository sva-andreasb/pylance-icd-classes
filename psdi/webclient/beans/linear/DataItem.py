def DataItem():
'''public DataItem(final String id, final String label, final Locale locale)
public DataItem(final DataSet dataSet, final MboRemote mbo)
'''
pass
def updateFromMbo():
'''public void updateFromMbo(final DataSet dataSet, final MboRemote mbo)
public void updateFromMbo(final DataSet dataSet, final MboRemote mbo, final String idSuffix)
'''
pass
def getId():
'''public String getId()
'''
pass
def getBaseId():
'''public String getBaseId()
'''
pass
def getLocale():
'''public Locale getLocale()
'''
pass
def getMbo():
'''public MboRemote getMbo()
'''
pass
def getElements():
'''public List<DataElement> getElements()
'''
pass
def cleanup():
'''public void cleanup()
'''
pass
def add():
'''public void add(final DataElement element)
'''
pass
def addElement():
'''public DataElement addElement(final DataSet dataSet, final MboRemote mbo, final CacheLvcMsgDesc lvcInfoMsgUtil)
public DataElement addElement(final DataSet dataSet, final MboRemote mbo, final String startMAttr, final String endMAttr, final CacheLvcMsgDesc lvcInfoMsgUtil)
'''
pass
def toJSON():
'''public JSONObject toJSON()
'''
pass
def toString():
'''public String toString()
'''
pass
def hasOverlapWith():
'''public boolean hasOverlapWith(final DataSet dataSet, final MboRemote mbo)
'''
pass
def addRelated():
'''public synchronized void addRelated(final DataItem item)
'''
pass
def getRelated():
'''public synchronized DataItem[] getRelated()
'''
pass
