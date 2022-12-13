PROPER_SUBSET = "int  1"
EQUAL = "int  2"
NO_SUBSET = "int  3"
SIGNED_APPLET_DBNAME = "int  4"
TEMP_FILENAME = "int  5"
def checkPrivilegeEnabled():
'''public void checkPrivilegeEnabled(final Target target)
public void checkPrivilegeEnabled(final Target target, final Object o)
'''
pass
def enablePrivilege():
'''public static void enablePrivilege(final String s)
public void enablePrivilege(final Target target)
public void enablePrivilege(final Target target, final Principal principal)
public void enablePrivilege(final Target target, final Principal principal, final Object o)
'''
pass
def revertPrivilege():
'''public void revertPrivilege(final Target target)
public static void revertPrivilege(final String s)
'''
pass
def disablePrivilege():
'''public void disablePrivilege(final Target target)
public void disablePrivilege(final String s)
'''
pass
def checkPrivilegeGranted():
'''public static void checkPrivilegeGranted(final String s)
public void checkPrivilegeGranted(final Target target)
public void checkPrivilegeGranted(final Target target, final Object o)
public void checkPrivilegeGranted(final Target target, final Principal principal, final Object o)
'''
pass
def isCalledByPrincipal():
'''public boolean isCalledByPrincipal(final Principal principal, final int n)
public boolean isCalledByPrincipal(final Principal principal)
'''
pass
def getSystemPrincipal():
'''public static Principal getSystemPrincipal()
'''
pass
def getPrivilegeManager():
'''public static PrivilegeManager getPrivilegeManager()
'''
pass
def hasPrincipal():
'''public boolean hasPrincipal(final Class clazz, final Principal principal)
'''
pass
def comparePrincipalArray():
'''public int comparePrincipalArray(final Principal[] array, final Principal[] array2)
'''
pass
def checkMatchPrincipal():
'''public boolean checkMatchPrincipal(final Class clazz, final int n)
public boolean checkMatchPrincipal(final Principal principal, final int n)
public boolean checkMatchPrincipal(final Class clazz)
'''
pass
def checkMatchPrincipalAlways():
'''public boolean checkMatchPrincipalAlways()
'''
pass
def getClassPrincipalsFromStack():
'''public Principal[] getClassPrincipalsFromStack(final int n)
'''
pass
def getPrivilegeTableFromStack():
'''public PrivilegeTable getPrivilegeTableFromStack()
'''
pass
