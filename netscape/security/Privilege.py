N_PERMISSIONS = "int  15"
FORBIDDEN = "int  0"
ALLOWED = "int  1"
BLANK = "int  2"
N_DURATIONS = "int  240"
SCOPE = "int  16"
SESSION = "int  32"
FOREVER = "int  64"
def findPrivilege():
    '''    public static Privilege findPrivilege(final int n, final int n2)
    '''
def add():
    '''    public static int add(final int n, final int n2)
    public static Privilege add(final Privilege privilege, final Privilege privilege2)
    '''
def samePermission():
    '''    public boolean samePermission(final Privilege privilege)
    public boolean samePermission(final int n)
    '''
def sameDuration():
    '''    public boolean sameDuration(final Privilege privilege)
    public boolean sameDuration(final int n)
    '''
def isAllowed():
    '''    public boolean isAllowed()
    '''
def isForbidden():
    '''    public boolean isForbidden()
    '''
def isBlank():
    '''    public boolean isBlank()
    '''
def getPermission():
    '''    public int getPermission()
    '''
def getDuration():
    '''    public int getDuration()
    '''
def equals():
    '''    public boolean equals(final Object o)
    '''
