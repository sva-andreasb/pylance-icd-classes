def extractCause():
'''public static ConcurrentException extractCause(final ExecutionException ex)
'''
pass
def extractCauseUnchecked():
'''public static ConcurrentRuntimeException extractCauseUnchecked(final ExecutionException ex)
'''
pass
def handleCause():
'''public static void handleCause(final ExecutionException ex)
'''
pass
def handleCauseUnchecked():
'''public static void handleCauseUnchecked(final ExecutionException ex)
'''
pass
def initialize():
'''public static <T> T initialize(final ConcurrentInitializer<T> initializer)
'''
pass
def initializeUnchecked():
'''public static <T> T initializeUnchecked(final ConcurrentInitializer<T> initializer)
'''
pass
def putIfAbsent():
'''public static <K, V> V putIfAbsent(final ConcurrentMap<K, V> map, final K key, final V value)
'''
pass
def createIfAbsent():
'''public static <K, V> V createIfAbsent(final ConcurrentMap<K, V> map, final K key, final ConcurrentInitializer<V> init)
'''
pass
def createIfAbsentUnchecked():
'''public static <K, V> V createIfAbsentUnchecked(final ConcurrentMap<K, V> map, final K key, final ConcurrentInitializer<V> init)
'''
pass
def constantFuture():
'''public static <T> Future<T> constantFuture(final T value)
'''
pass
def isDone():
'''public boolean isDone()
'''
pass
def get():
'''public T get()
public T get(final long timeout, final TimeUnit unit)
'''
pass
def isCancelled():
'''public boolean isCancelled()
'''
pass
def cancel():
'''public boolean cancel(final boolean mayInterruptIfRunning)
'''
pass
