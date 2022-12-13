def AggregateLifeCycle():
'''public AggregateLifeCycle()
'''
pass
def destroy():
'''public void destroy()
'''
pass
def contains():
'''public boolean contains(final Object bean)
'''
pass
def isManaged():
'''public boolean isManaged(final Object bean)
'''
pass
def addBean():
'''public boolean addBean(final Object o)
public boolean addBean(final Object o, final boolean managed)
'''
pass
def manage():
'''public void manage(final Object bean)
'''
pass
def unmanage():
'''public void unmanage(final Object bean)
'''
pass
def getBeans():
'''public Collection<Object> getBeans()
public <T> List<T> getBeans(final Class<T> clazz)
'''
pass
def getBean():
'''public <T> T getBean(final Class<T> clazz)
'''
pass
def removeBeans():
'''public void removeBeans()
'''
pass
def removeBean():
'''public boolean removeBean(final Object o)
'''
pass
def dumpStdErr():
'''public void dumpStdErr()
'''
pass
def dump():
'''public String dump()
public static String dump(final Dumpable dumpable)
public void dump(final Appendable out)
public void dump(final Appendable out, final String indent)
public static void dump(final Appendable out, final String indent, final Collection<?>... collections)
'''
pass
def dumpObject():
'''public static void dumpObject(final Appendable out, final Object o)
'''
pass
