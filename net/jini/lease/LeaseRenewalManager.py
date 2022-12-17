def ():
    '''returns Entry\n\n
    ()\n
    (final Configuration configuration)\n
    (final Lease lease, final long n, final LeaseListener leaseListener)\n
    (final Lease lease, final long expiration, final long renewDuration, final LeaseListener listener)\n
    (final long renew)\n
    '''
def renewUntil():
    '''returns None\n\n
    renewUntil(final Lease lease, final long n, final LeaseListener leaseListener)\n
    renewUntil(final Lease lease, final long n, final long n2, final LeaseListener leaseListener)\n
    '''
def renewFor():
    '''returns None\n\n
    renewFor(final Lease lease, final long n, final LeaseListener leaseListener)\n
    renewFor(final Lease lease, final long n, final long n2, final LeaseListener leaseListener)\n
    '''
def cancel():
    '''returns None\n\n
    cancel(final Lease lease)\n
    '''
def run():
    '''returns None\n\n
    run()\n
    run()\n
    '''
def runAfter():
    '''returns boolean\n\n
    runAfter(final List list, final int n)\n
    runAfter(final List list, final int n)\n
    '''
def getRenewDuration():
    '''returns long\n\n
    getRenewDuration(final long n)\n
    '''
def calcRenew():
    '''returns None\n\n
    calcRenew(final long n)\n
    '''
def delayRenew():
    '''returns None\n\n
    delayRenew()\n
    '''
def compareTo():
    '''returns int\n\n
    compareTo(final Object o)\n
    '''
def canBatch():
    '''returns boolean\n\n
    canBatch(final Entry entry)\n
    '''
def desiredExpirationListener():
    '''returns DesiredExpirationListener\n\n
    desiredExpirationListener()\n
    '''
def renewalsDone():
    '''returns boolean\n\n
    renewalsDone()\n
    '''
