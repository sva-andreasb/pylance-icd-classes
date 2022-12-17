def getBlockMgr():
    '''returns BlockMgr\n\n
    getBlockMgr()\n
    '''
def allocateId():
    '''returns int\n\n
    allocateId()\n
    '''
def create():
    '''returns T\n\n
    create(final int id, final BlockType bType)\n
    '''
def get():
    '''returns T\n\n
    get(final int id)\n
    '''
def put():
    '''returns None\n\n
    put(final int id, final T page)\n
    put(final T page)\n
    '''
def release():
    '''returns None\n\n
    release(final int id)\n
    '''
def valid():
    '''returns boolean\n\n
    valid(final int id)\n
    '''
def dump():
    '''returns None\n\n
    dump()\n
    '''
def startUpdate():
    '''returns None\n\n
    startUpdate()\n
    '''
def finishUpdate():
    '''returns None\n\n
    finishUpdate()\n
    '''
def startRead():
    '''returns None\n\n
    startRead()\n
    '''
def finishRead():
    '''returns None\n\n
    finishRead()\n
    '''
