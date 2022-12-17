def ():
    '''returns NioEventLoopGroup\n\n
    ()\n
    (final int nThreads)\n
    (final ThreadFactory threadFactory)\n
    (final int nThreads, final ThreadFactory threadFactory)\n
    (final int nThreads, final Executor executor)\n
    (final int nThreads, final ThreadFactory threadFactory, final SelectorProvider selectorProvider)\n
    (final int nThreads, final ThreadFactory threadFactory, final SelectorProvider selectorProvider, final SelectStrategyFactory selectStrategyFactory)\n
    (final int nThreads, final Executor executor, final SelectorProvider selectorProvider)\n
    (final int nThreads, final Executor executor, final SelectorProvider selectorProvider, final SelectStrategyFactory selectStrategyFactory)\n
    (final int nThreads, final Executor executor, final EventExecutorChooserFactory chooserFactory, final SelectorProvider selectorProvider, final SelectStrategyFactory selectStrategyFactory)\n
    (final int nThreads, final Executor executor, final EventExecutorChooserFactory chooserFactory, final SelectorProvider selectorProvider, final SelectStrategyFactory selectStrategyFactory, final RejectedExecutionHandler rejectedExecutionHandler)\n
    (final int nThreads, final Executor executor, final EventExecutorChooserFactory chooserFactory, final SelectorProvider selectorProvider, final SelectStrategyFactory selectStrategyFactory, final RejectedExecutionHandler rejectedExecutionHandler, final EventLoopTaskQueueFactory taskQueueFactory)\n
    '''
def setIoRatio():
    '''returns None\n\n
    setIoRatio(final int ioRatio)\n
    '''
def rebuildSelectors():
    '''returns None\n\n
    rebuildSelectors()\n
    '''
