def ():
    '''returns Heartbeat\n\n
    (final long sessionTimeout, final long heartbeatInterval, final long maxPollInterval, final long retryBackoffMs)\n
    '''
def poll():
    '''returns None\n\n
    poll(final long now)\n
    '''
def sentHeartbeat():
    '''returns None\n\n
    sentHeartbeat(final long now)\n
    '''
def failHeartbeat():
    '''returns None\n\n
    failHeartbeat()\n
    '''
def receiveHeartbeat():
    '''returns None\n\n
    receiveHeartbeat(final long now)\n
    '''
def shouldHeartbeat():
    '''returns boolean\n\n
    shouldHeartbeat(final long now)\n
    '''
def lastHeartbeatSend():
    '''returns long\n\n
    lastHeartbeatSend()\n
    '''
def timeToNextHeartbeat():
    '''returns long\n\n
    timeToNextHeartbeat(final long now)\n
    '''
def sessionTimeoutExpired():
    '''returns boolean\n\n
    sessionTimeoutExpired(final long now)\n
    '''
def interval():
    '''returns long\n\n
    interval()\n
    '''
def resetTimeouts():
    '''returns None\n\n
    resetTimeouts(final long now)\n
    '''
def pollTimeoutExpired():
    '''returns boolean\n\n
    pollTimeoutExpired(final long now)\n
    '''
