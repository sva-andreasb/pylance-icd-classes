def ():
    '''returns RequestFuture\n\n
    ()\n
    '''
def isDone():
    '''returns boolean\n\n
    isDone()\n
    '''
def awaitDone():
    '''returns boolean\n\n
    awaitDone(final long timeout, final TimeUnit unit)\n
    '''
def value():
    '''returns T\n\n
    value()\n
    '''
def succeeded():
    '''returns boolean\n\n
    succeeded()\n
    '''
def failed():
    '''returns boolean\n\n
    failed()\n
    '''
def isRetriable():
    '''returns boolean\n\n
    isRetriable()\n
    '''
def exception():
    '''returns RuntimeException\n\n
    exception()\n
    '''
def complete():
    '''returns None\n\n
    complete(final T value)\n
    '''
def raise():
    '''returns None\n\n
    raise(final RuntimeException e)\n
    raise(final Errors error)\n
    '''
def addListener():
    '''returns None\n\n
    addListener(final RequestFutureListener<T> listener)\n
    '''
def onSuccess():
    '''returns None\n\n
    onSuccess(final T value)\n
    onSuccess(final T value)\n
    '''
def onFailure():
    '''returns None\n\n
    onFailure(final RuntimeException e)\n
    onFailure(final RuntimeException e)\n
    '''
def chain():
    '''returns None\n\n
    chain(final RequestFuture<T> future)\n
    '''
def shouldBlock():
    '''returns boolean\n\n
    shouldBlock()\n
    '''
