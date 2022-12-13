def cancel():
'''public final synchronized boolean cancel(final boolean mayInterruptIfRunning)
'''
pass
def isCancelled():
'''public final synchronized boolean isCancelled()
'''
pass
def isDone():
'''public final synchronized boolean isDone()
'''
pass
def onSuccess():
'''public CallbackRecipient<V, E> onSuccess(final SuccessCallback<V> successCallback)
'''
pass
def onError():
'''public CallbackRecipient<V, E> onError(final ExceptionCallback<E> exceptionCallback)
'''
pass
def get():
'''public final synchronized V get()
public final synchronized V get(final long timeout, final TimeUnit unit)
'''
pass
def getOrThrow():
'''public final synchronized V getOrThrow()
'''
pass
def run():
'''public void run()
public void run()
public void run()
'''
pass
def from():
'''public static <V, E extends Exception> SmackFuture<V, E> from(final V result)
'''
pass
def setResult():
'''public final synchronized void setResult(final V result)
'''
pass
def setException():
'''public final synchronized void setException(final E exception)
'''
pass
def SocketFuture():
'''public SocketFuture(final SocketFactory socketFactory)
'''
pass
def connectAsync():
'''public void connectAsync(final SocketAddress socketAddress, final int timeout)
'''
pass
def processException():
'''public final synchronized void processException(final E exception)
'''
pass
def processStanza():
'''public final synchronized void processStanza(final Stanza stanza)
'''
pass
