def DefaultProgressivePromise():
'''public DefaultProgressivePromise(final EventExecutor executor)
'''
pass
def setProgress():
'''public ProgressivePromise<V> setProgress(final long progress, long total)
'''
pass
def tryProgress():
'''public boolean tryProgress(final long progress, long total)
'''
pass
def addListener():
'''public ProgressivePromise<V> addListener(final GenericFutureListener<? extends Future<? super V>> listener)
'''
pass
def addListeners():
'''public ProgressivePromise<V> addListeners(final GenericFutureListener<? extends Future<? super V>>... listeners)
'''
pass
def removeListener():
'''public ProgressivePromise<V> removeListener(final GenericFutureListener<? extends Future<? super V>> listener)
'''
pass
def removeListeners():
'''public ProgressivePromise<V> removeListeners(final GenericFutureListener<? extends Future<? super V>>... listeners)
'''
pass
def sync():
'''public ProgressivePromise<V> sync()
'''
pass
def syncUninterruptibly():
'''public ProgressivePromise<V> syncUninterruptibly()
'''
pass
def await():
'''public ProgressivePromise<V> await()
'''
pass
def awaitUninterruptibly():
'''public ProgressivePromise<V> awaitUninterruptibly()
'''
pass
def setSuccess():
'''public ProgressivePromise<V> setSuccess(final V result)
'''
pass
def setFailure():
'''public ProgressivePromise<V> setFailure(final Throwable cause)
'''
pass
