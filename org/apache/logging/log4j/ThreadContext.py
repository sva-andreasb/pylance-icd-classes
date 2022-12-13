def put():
    '''public static void put(final String key, final String value)
    '''
def putIfNull():
    '''public static void putIfNull(final String key, final String value)
    '''
def putAll():
    '''public static void putAll(final Map<String, String> m)
    '''
def get():
    '''public static String get(final String key)
    '''
def remove():
    '''public static void remove(final String key)
    public void remove()
    '''
def removeAll():
    '''public static void removeAll(final Iterable<String> keys)
    public boolean removeAll(final Collection<?> c)
    '''
def clearMap():
    '''public static void clearMap()
    '''
def clearAll():
    '''public static void clearAll()
    '''
def containsKey():
    '''public static boolean containsKey(final String key)
    '''
def getContext():
    '''public static Map<String, String> getContext()
    '''
def getImmutableContext():
    '''public static Map<String, String> getImmutableContext()
    '''
def getThreadContextMap():
    '''public static ReadOnlyThreadContextMap getThreadContextMap()
    '''
def isEmpty():
    '''public static boolean isEmpty()
    '''
def clearStack():
    '''public static void clearStack()
    '''
def cloneStack():
    '''public static ContextStack cloneStack()
    '''
def getImmutableStack():
    '''public static ContextStack getImmutableStack()
    '''
def setStack():
    '''public static void setStack(final Collection<String> stack)
    '''
def getDepth():
    '''public static int getDepth()
    public int getDepth()
    '''
def pop():
    '''public static String pop()
    public String pop()
    '''
def peek():
    '''public static String peek()
    public String peek()
    '''
def push():
    '''public static void push(final String message)
    public static void push(final String message, final Object... args)
    public void push(final String message)
    '''
def removeStack():
    '''public static void removeStack()
    '''
def trim():
    '''public static void trim(final int depth)
    public void trim(final int depth)
    '''
def asList():
    '''public List<String> asList()
    '''
def equals():
    '''public boolean equals(final Object o)
    '''
def hashCode():
    '''public int hashCode()
    '''
def copy():
    '''public ContextStack copy()
    '''
def toArray():
    '''public <T> T[] toArray(final T[] a)
    '''
def add():
    '''public boolean add(final String e)
    '''
def containsAll():
    '''public boolean containsAll(final Collection<?> c)
    '''
def addAll():
    '''public boolean addAll(final Collection<? extends String> c)
    '''
def retainAll():
    '''public boolean retainAll(final Collection<?> c)
    '''
def iterator():
    '''public Iterator<String> iterator()
    '''
def size():
    '''public int size()
    '''
def getImmutableStackOrNull():
    '''public ContextStack getImmutableStackOrNull()
    '''
def hasNext():
    '''public boolean hasNext()
    '''
def next():
    '''public E next()
    '''
