def extractCause():
    '''public static ConcurrentException extractCause(final ExecutionException ex)
    '''
def extractCauseUnchecked():
    '''public static ConcurrentRuntimeException extractCauseUnchecked(final ExecutionException ex)
    '''
def handleCause():
    '''public static void handleCause(final ExecutionException ex)
    '''
def handleCauseUnchecked():
    '''public static void handleCauseUnchecked(final ExecutionException ex)
    '''
def initialize():
    '''public static <T> T initialize(final ConcurrentInitializer<T> initializer)
    '''
def initializeUnchecked():
    '''public static <T> T initializeUnchecked(final ConcurrentInitializer<T> initializer)
    '''
def putIfAbsent():
    '''public static <K, V> V putIfAbsent(final ConcurrentMap<K, V> map, final K key, final V value)
    '''
def createIfAbsent():
    '''public static <K, V> V createIfAbsent(final ConcurrentMap<K, V> map, final K key, final ConcurrentInitializer<V> init)
    '''
def createIfAbsentUnchecked():
    '''public static <K, V> V createIfAbsentUnchecked(final ConcurrentMap<K, V> map, final K key, final ConcurrentInitializer<V> init)
    '''
def constantFuture():
    '''public static <T> Future<T> constantFuture(final T value)
    '''
def isDone():
    '''public boolean isDone()
    '''
def get():
    '''public T get()
    public T get(final long timeout, final TimeUnit unit)
    '''
def isCancelled():
    '''public boolean isCancelled()
    '''
def cancel():
    '''public boolean cancel(final boolean mayInterruptIfRunning)
    '''
