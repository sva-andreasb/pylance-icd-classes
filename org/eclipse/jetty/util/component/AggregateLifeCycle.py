def AggregateLifeCycle():
    '''    public AggregateLifeCycle()
    '''
def destroy():
    '''    public void destroy()
    '''
def contains():
    '''    public boolean contains(final Object bean)
    '''
def isManaged():
    '''    public boolean isManaged(final Object bean)
    '''
def addBean():
    '''    public boolean addBean(final Object o)
    public boolean addBean(final Object o, final boolean managed)
    '''
def manage():
    '''    public void manage(final Object bean)
    '''
def unmanage():
    '''    public void unmanage(final Object bean)
    '''
def getBeans():
    '''    public Collection<Object> getBeans()
    public <T> List<T> getBeans(final Class<T> clazz)
    '''
def getBean():
    '''    public <T> T getBean(final Class<T> clazz)
    '''
def removeBeans():
    '''    public void removeBeans()
    '''
def removeBean():
    '''    public boolean removeBean(final Object o)
    '''
def dumpStdErr():
    '''    public void dumpStdErr()
    '''
def dump():
    '''    public String dump()
    public static String dump(final Dumpable dumpable)
    public void dump(final Appendable out)
    public void dump(final Appendable out, final String indent)
    public static void dump(final Appendable out, final String indent, final Collection<?>... collections)
    '''
def dumpObject():
    '''    public static void dumpObject(final Appendable out, final Object o)
    '''
