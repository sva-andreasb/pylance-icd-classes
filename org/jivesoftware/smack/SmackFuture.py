def cancel():
    '''    public final synchronized boolean cancel(final boolean mayInterruptIfRunning)
    '''
def isCancelled():
    '''    public final synchronized boolean isCancelled()
    '''
def isDone():
    '''    public final synchronized boolean isDone()
    '''
def onSuccess():
    '''    public CallbackRecipient<V, E> onSuccess(final SuccessCallback<V> successCallback)
    '''
def onError():
    '''    public CallbackRecipient<V, E> onError(final ExceptionCallback<E> exceptionCallback)
    '''
def get():
    '''    public final synchronized V get()
    public final synchronized V get(final long timeout, final TimeUnit unit)
    '''
def getOrThrow():
    '''    public final synchronized V getOrThrow()
    '''
def run():
    '''    public void run()
    public void run()
    public void run()
    '''
def from():
    '''    public static <V, E extends Exception> SmackFuture<V, E> from(final V result)
    '''
def setResult():
    '''    public final synchronized void setResult(final V result)
    '''
def setException():
    '''    public final synchronized void setException(final E exception)
    '''
def SocketFuture():
    '''    public SocketFuture(final SocketFactory socketFactory)
    '''
def connectAsync():
    '''    public void connectAsync(final SocketAddress socketAddress, final int timeout)
    '''
def processException():
    '''    public final synchronized void processException(final E exception)
    '''
def processStanza():
    '''    public final synchronized void processStanza(final Stanza stanza)
    '''
