def BasicFuture():
'''public BasicFuture(final FutureCallback<T> callback)
'''
pass
def isCancelled():
'''public boolean isCancelled()
'''
pass
def isDone():
'''public boolean isDone()
'''
pass
def get():
'''public synchronized T get()
public synchronized T get(final long timeout, final TimeUnit unit)
'''
pass
def completed():
'''public boolean completed(final T result)
'''
pass
def failed():
'''public boolean failed(final Exception exception)
'''
pass
def cancel():
'''public boolean cancel(final boolean mayInterruptIfRunning)
public boolean cancel()
'''
pass
