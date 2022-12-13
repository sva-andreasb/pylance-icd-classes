def DataItem():
    '''    public DataItem(final String id, final String label, final Locale locale)
    public DataItem(final DataSet dataSet, final MboRemote mbo)
    '''
def updateFromMbo():
    '''    public void updateFromMbo(final DataSet dataSet, final MboRemote mbo)
    public void updateFromMbo(final DataSet dataSet, final MboRemote mbo, final String idSuffix)
    '''
def getId():
    '''    public String getId()
    '''
def getBaseId():
    '''    public String getBaseId()
    '''
def getLocale():
    '''    public Locale getLocale()
    '''
def getMbo():
    '''    public MboRemote getMbo()
    '''
def getElements():
    '''    public List<DataElement> getElements()
    '''
def cleanup():
    '''    public void cleanup()
    '''
def add():
    '''    public void add(final DataElement element)
    '''
def addElement():
    '''    public DataElement addElement(final DataSet dataSet, final MboRemote mbo, final CacheLvcMsgDesc lvcInfoMsgUtil)
    public DataElement addElement(final DataSet dataSet, final MboRemote mbo, final String startMAttr, final String endMAttr, final CacheLvcMsgDesc lvcInfoMsgUtil)
    '''
def toJSON():
    '''    public JSONObject toJSON()
    '''
def toString():
    '''    public String toString()
    '''
def hasOverlapWith():
    '''    public boolean hasOverlapWith(final DataSet dataSet, final MboRemote mbo)
    '''
def addRelated():
    '''    public synchronized void addRelated(final DataItem item)
    '''
def getRelated():
    '''    public synchronized DataItem[] getRelated()
    '''
