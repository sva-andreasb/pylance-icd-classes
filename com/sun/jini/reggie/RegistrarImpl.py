def ():
    '''returns SnapshotThread\n\n
    (final ActivationID activationID, final MarshalledObject marshalledObject)\n
    (final ActivationID activationID, final MarshalledObject marshalledObject, final SharedActivation sharedActivationRef)\n
    (final Item item, final long leaseID, final long leaseExpiration)\n
    (final long eventID, final long leaseID, final Template tmpl, final int transitions, final RemoteEventListener listener, final MarshalledObject handback, final long leaseExpiration)\n
    (final SvcReg reg)\n
    (final ServiceID serviceID, final long leaseID, final EntryRep[] attrSets)\n
    (final ServiceID serviceID, final long leaseID, final EntryRep[] attrSetTmpls, final EntryRep[] attrSets)\n
    (final ServiceID serviceID, final long leaseID, final EntryRep[] attrSets)\n
    (final EventReg eventReg)\n
    (final ServiceID serviceID, final long leaseID)\n
    (final ServiceID serviceID, final long leaseID, final long leaseExpTime)\n
    (final long eventID, final long leaseID)\n
    (final long eventID, final long leaseID, final long leaseExpTime)\n
    (final Object[] regIDs, final long[] leaseIDs, final long[] leaseExpTimes)\n
    (final Object[] regIDs, final long[] leaseIDs)\n
    (final int newPort)\n
    (final long newLeaseDuration)\n
    (final long newLeaseDuration)\n
    (final long newRenewalInterval)\n
    (final float newWeight)\n
    (final String[] groups)\n
    (final LookupLocator[] locators)\n
    (final int newThreshold)\n
    (final String[] groups)\n
    ()\n
    ()\n
    (final Template template)\n
    (final Template template, final int n, final int n2)\n
    (final Template template, final EntryClass key)\n
    (final Template template)\n
    (final Template template)\n
    (final EventReg reg, final ServiceID sid, final Item item, final int transition)\n
    (final InetAddress addr, final int port)\n
    (final Socket socket)\n
    ()\n
    ()\n
    ()\n
    ()\n
    (final int port)\n
    ()\n
    ()\n
    '''
def addAttributes():
    '''returns None\n\n
    addAttributes(final ServiceID serviceID, final long n, final EntryRep[] array)\n
    '''
def addLookupAttributes():
    '''returns None\n\n
    addLookupAttributes(final Entry[] array)\n
    '''
def addLookupGroups():
    '''returns None\n\n
    addLookupGroups(final String[] array)\n
    '''
def addLookupLocators():
    '''returns None\n\n
    addLookupLocators(final LookupLocator[] array)\n
    '''
def addMemberGroups():
    '''returns None\n\n
    addMemberGroups(final String[] array)\n
    '''
def cancelEventLease():
    '''returns None\n\n
    cancelEventLease(final long n, final long n2)\n
    '''
def cancelLeases():
    '''returns Exception[]\n\n
    cancelLeases(final Object[] array, final long[] array2)\n
    '''
def cancelServiceLease():
    '''returns None\n\n
    cancelServiceLease(final ServiceID serviceID, final long n)\n
    '''
def destroy():
    '''returns None\n\n
    destroy()\n
    '''
def getAdmin():
    '''returns Object\n\n
    getAdmin()\n
    '''
def getEntryClasses():
    '''returns EntryClassBase[]\n\n
    getEntryClasses(final Template template)\n
    '''
def getFieldValues():
    '''returns Object[]\n\n
    getFieldValues(final Template template, final int n, final int n2)\n
    '''
def getLocator():
    '''returns LookupLocator\n\n
    getLocator()\n
    '''
def getLogToSnapshotThreshold():
    '''returns int\n\n
    getLogToSnapshotThreshold()\n
    '''
def getLookupAttributes():
    '''returns Entry[]\n\n
    getLookupAttributes()\n
    '''
def getLookupGroups():
    '''returns String[]\n\n
    getLookupGroups()\n
    '''
def getLookupLocators():
    '''returns LookupLocator[]\n\n
    getLookupLocators()\n
    '''
def getMemberGroups():
    '''returns String[]\n\n
    getMemberGroups()\n
    '''
def getMinMaxEventLease():
    '''returns long\n\n
    getMinMaxEventLease()\n
    '''
def getMinMaxServiceLease():
    '''returns long\n\n
    getMinMaxServiceLease()\n
    '''
def getMinRenewalInterval():
    '''returns long\n\n
    getMinRenewalInterval()\n
    '''
def getServiceID():
    '''returns ServiceID\n\n
    getServiceID()\n
    '''
def getServiceTypes():
    '''returns ServiceTypeBase[]\n\n
    getServiceTypes(final Template template, final String s)\n
    '''
def getSnapshotWeight():
    '''returns float\n\n
    getSnapshotWeight()\n
    '''
def getStorageLocation():
    '''returns String\n\n
    getStorageLocation()\n
    '''
def getUnicastPort():
    '''returns int\n\n
    getUnicastPort()\n
    '''
def lookup():
    '''returns Matches\n\n
    lookup(final Template template)\n
    lookup(final Template template, final int n)\n
    '''
def modifyAttributes():
    '''returns None\n\n
    modifyAttributes(final ServiceID serviceID, final long n, final EntryRep[] array, final EntryRep[] array2)\n
    '''
def modifyLookupAttributes():
    '''returns None\n\n
    modifyLookupAttributes(final Entry[] array, final Entry[] array2)\n
    '''
def notify():
    '''returns EventRegistration\n\n
    notify(final Template template, final int n, final RemoteEventListener remoteEventListener, final MarshalledObject marshalledObject, final long n2)\n
    '''
def register():
    '''returns ServiceRegistration\n\n
    register(final Item item, final long n)\n
    '''
def removeLookupGroups():
    '''returns None\n\n
    removeLookupGroups(final String[] array)\n
    '''
def removeLookupLocators():
    '''returns None\n\n
    removeLookupLocators(final LookupLocator[] array)\n
    '''
def removeMemberGroups():
    '''returns None\n\n
    removeMemberGroups(final String[] array)\n
    '''
def renewEventLease():
    '''returns long\n\n
    renewEventLease(final long n, final long n2, final long n3)\n
    '''
def renewLeases():
    '''returns RenewResults\n\n
    renewLeases(final Object[] array, final long[] array2, final long[] array3)\n
    '''
def renewServiceLease():
    '''returns long\n\n
    renewServiceLease(final ServiceID serviceID, final long n, final long n2)\n
    '''
def setAttributes():
    '''returns None\n\n
    setAttributes(final ServiceID serviceID, final long n, final EntryRep[] array)\n
    '''
def setLogToSnapshotThreshold():
    '''returns None\n\n
    setLogToSnapshotThreshold(final int logToSnapshotThresh)\n
    '''
def setLookupGroups():
    '''returns None\n\n
    setLookupGroups(final String[] groups)\n
    '''
def setLookupLocators():
    '''returns None\n\n
    setLookupLocators(final LookupLocator[] locators)\n
    '''
def setMemberGroups():
    '''returns None\n\n
    setMemberGroups(final String[] array)\n
    '''
def setMinMaxEventLease():
    '''returns None\n\n
    setMinMaxEventLease(final long minMaxEventLease)\n
    '''
def setMinMaxServiceLease():
    '''returns None\n\n
    setMinMaxServiceLease(final long minMaxServiceLease)\n
    '''
def setMinRenewalInterval():
    '''returns None\n\n
    setMinRenewalInterval(final long minRenewalInterval)\n
    '''
def setSnapshotWeight():
    '''returns None\n\n
    setSnapshotWeight(final float snapshotWt)\n
    '''
def setStorageLocation():
    '''returns None\n\n
    setStorageLocation(final String s)\n
    '''
def setUnicastPort():
    '''returns None\n\n
    setUnicastPort(final int n)\n
    '''
def compareTo():
    '''returns int\n\n
    compareTo(final Object o)\n
    compareTo(final Object o)\n
    '''
def apply():
    '''returns None\n\n
    apply(final RegistrarImpl registrarImpl)\n
    apply(final RegistrarImpl registrarImpl)\n
    apply(final RegistrarImpl registrarImpl)\n
    apply(final RegistrarImpl registrarImpl)\n
    apply(final RegistrarImpl registrarImpl)\n
    apply(final RegistrarImpl registrarImpl)\n
    apply(final RegistrarImpl registrarImpl)\n
    apply(final RegistrarImpl registrarImpl)\n
    apply(final RegistrarImpl registrarImpl)\n
    apply(final RegistrarImpl registrarImpl)\n
    apply(final RegistrarImpl registrarImpl)\n
    apply(final RegistrarImpl registrarImpl)\n
    apply(final RegistrarImpl registrarImpl)\n
    apply(final RegistrarImpl registrarImpl)\n
    apply(final RegistrarImpl registrarImpl)\n
    apply(final RegistrarImpl registrarImpl)\n
    apply(final RegistrarImpl registrarImpl)\n
    apply(final RegistrarImpl registrarImpl)\n
    apply(final RegistrarImpl registrarImpl)\n
    apply(final RegistrarImpl registrarImpl)\n
    '''
def applyUpdate():
    '''returns None\n\n
    applyUpdate(final Object o)\n
    '''
def recover():
    '''returns None\n\n
    recover(final InputStream inputStream)\n
    '''
def snapshot():
    '''returns None\n\n
    snapshot(final OutputStream outputStream)\n
    '''
def hasNext():
    '''returns boolean\n\n
    hasNext()\n
    '''
def next():
    '''returns Item\n\n
    next()\n
    '''
def nextReg():
    '''returns SvcReg\n\n
    nextReg()\n
    '''
def run():
    '''returns None\n\n
    run()\n
    run()\n
    run()\n
    run()\n
    run()\n
    run()\n
    run()\n
    run()\n
    run()\n
    '''
def runAfter():
    '''returns boolean\n\n
    runAfter(final List list, final int n)\n
    runAfter(final List list, final int n)\n
    runAfter(final List list, final int n)\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object o)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
