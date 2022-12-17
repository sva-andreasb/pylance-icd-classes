def ():
    '''returns IEMAPIs\n\n
    (final String userName, final String password, final String server, final int port)\n
    (final String userName, final String password, final String baseUrl)\n
    '''
def getTasksForSWPackage():
    '''returns List<ScopedFixlet>\n\n
    getTasksForSWPackage(final String softwarePackageId)\n
    '''
def getFixlets():
    '''returns List<ScopedFixlet>\n\n
    getFixlets(final String name, final String siteName, final long maxrows)\n
    '''
def getSWPackages():
    '''returns List<SoftwarePackage>\n\n
    getSWPackages(final String nameFilter, final String versionFilter, final String vendorFilter, final String descriptionFilter, final boolean matchAll)\n
    '''
