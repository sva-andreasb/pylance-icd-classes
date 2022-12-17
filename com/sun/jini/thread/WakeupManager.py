def ():
    '''returns ThreadDesc\n\n
    ()\n
    (final ThreadDesc kickerDesc)\n
    ()\n
    (final ThreadGroup threadGroup, final boolean b)\n
    (final ThreadGroup group, final boolean daemon, final int priority)\n
    '''
def schedule():
    '''returns Ticket\n\n
    schedule(final long n, final Runnable runnable)\n
    schedule(final long n, final Runnable runnable, final ThreadDesc threadDesc)\n
    '''
def cancel():
    '''returns None\n\n
    cancel(final Ticket ticket)\n
    '''
def cancelAll():
    '''returns None\n\n
    cancelAll()\n
    '''
def isEmpty():
    '''returns boolean\n\n
    isEmpty()\n
    '''
def stop():
    '''returns None\n\n
    stop()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object o)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def compareTo():
    '''returns int\n\n
    compareTo(final Object o)\n
    '''
def run():
    '''returns None\n\n
    run()\n
    '''
