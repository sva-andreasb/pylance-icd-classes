def ():
    '''returns KafkaFutureImpl\n\n
    ()\n
    '''
def whenComplete():
    '''returns KafkaFuture<T>\n\n
    whenComplete(final BiConsumer<? super T, ? super Throwable> biConsumer)\n
    '''
def completeExceptionally():
    '''returns boolean\n\n
    completeExceptionally(final Throwable newException)\n
    '''
def get():
    '''returns T\n\n
    get()\n
    get(final long timeout, final TimeUnit unit)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def accept():
    '''returns None\n\n
    accept(final A a, final Throwable exception)\n
    accept(final T val, Throwable exception)\n
    '''
