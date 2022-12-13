def BasicFuture():
    '''public BasicFuture(final FutureCallback<T> callback)
    '''
def isCancelled():
    '''public boolean isCancelled()
    '''
def isDone():
    '''public boolean isDone()
    '''
def get():
    '''public synchronized T get()
    public synchronized T get(final long timeout, final TimeUnit unit)
    '''
def completed():
    '''public boolean completed(final T result)
    '''
def failed():
    '''public boolean failed(final Exception exception)
    '''
def cancel():
    '''public boolean cancel(final boolean mayInterruptIfRunning)
    public boolean cancel()
    '''
