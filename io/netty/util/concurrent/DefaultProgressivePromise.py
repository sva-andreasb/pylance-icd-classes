def DefaultProgressivePromise():
    '''    public DefaultProgressivePromise(final EventExecutor executor)
    '''
def setProgress():
    '''    public ProgressivePromise<V> setProgress(final long progress, long total)
    '''
def tryProgress():
    '''    public boolean tryProgress(final long progress, long total)
    '''
def addListener():
    '''    public ProgressivePromise<V> addListener(final GenericFutureListener<? extends Future<? super V>> listener)
    '''
def addListeners():
    '''    public ProgressivePromise<V> addListeners(final GenericFutureListener<? extends Future<? super V>>... listeners)
    '''
def removeListener():
    '''    public ProgressivePromise<V> removeListener(final GenericFutureListener<? extends Future<? super V>> listener)
    '''
def removeListeners():
    '''    public ProgressivePromise<V> removeListeners(final GenericFutureListener<? extends Future<? super V>>... listeners)
    '''
def sync():
    '''    public ProgressivePromise<V> sync()
    '''
def syncUninterruptibly():
    '''    public ProgressivePromise<V> syncUninterruptibly()
    '''
def await():
    '''    public ProgressivePromise<V> await()
    '''
def awaitUninterruptibly():
    '''    public ProgressivePromise<V> awaitUninterruptibly()
    '''
def setSuccess():
    '''    public ProgressivePromise<V> setSuccess(final V result)
    '''
def setFailure():
    '''    public ProgressivePromise<V> setFailure(final Throwable cause)
    '''
