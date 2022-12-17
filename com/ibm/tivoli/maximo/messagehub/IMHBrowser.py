def ():
    '''returns IMHBrowser\n\n
    (final Properties consumerProperties)\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def position():
    '''returns Long\n\n
    position(final int partition)\n
    '''
def seek():
    '''returns None\n\n
    seek(final int partition, final long offset)\n
    '''
def browseMessages():
    '''returns List<Message>\n\n
    browseMessages(final long maxCount, final long skipCount)\n
    '''
