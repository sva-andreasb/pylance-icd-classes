PROCESS_NEXT_EVENT = "int  1"
CANCEL_ALL = "int  0"
def ():
    '''returns EventQueue\n\n
    ()\n
    '''
def push():
    '''returns None\n\n
    push(final WebClientEvent event)\n
    '''
def pop():
    '''returns WebClientEvent\n\n
    pop()\n
    '''
def hasMoreEvents():
    '''returns boolean\n\n
    hasMoreEvents()\n
    '''
def peek():
    '''returns WebClientEvent\n\n
    peek()\n
    '''
def removeEventFromQueue():
    '''returns boolean\n\n
    removeEventFromQueue(final String eventType, final String targetID)\n
    '''
def clear():
    '''returns None\n\n
    clear()\n
    '''
