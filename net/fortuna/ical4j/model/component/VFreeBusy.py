def VFreeBusy():
    '''    public VFreeBusy()
    public VFreeBusy(final boolean initialise)
    public VFreeBusy(final PropertyList properties)
    public VFreeBusy(final DateTime start, final DateTime end)
    public VFreeBusy(final DateTime start, final DateTime end, final TemporalAmount duration)
    public VFreeBusy(final VFreeBusy request, final ComponentList<CalendarComponent> components)
    '''
def validate():
    '''    public final void validate(final boolean recurse)
    '''
def getContact():
    '''    public final Contact getContact()
    '''
def getStartDate():
    '''    public final DtStart getStartDate()
    '''
def getEndDate():
    '''    public final DtEnd getEndDate()
    '''
def getDuration():
    '''    public final Duration getDuration()
    '''
def getDateStamp():
    '''    public final DtStamp getDateStamp()
    '''
def getOrganizer():
    '''    public final Organizer getOrganizer()
    '''
def getUrl():
    '''    public final Url getUrl()
    '''
def getUid():
    '''    public final Uid getUid()
    '''
def start():
    '''    public BusyTimeBuilder start(final DateTime start)
    public FreeTimeBuilder start(final DateTime start)
    '''
def end():
    '''    public BusyTimeBuilder end(final DateTime end)
    public FreeTimeBuilder end(final DateTime end)
    '''
def components():
    '''    public BusyTimeBuilder components(final ComponentList<CalendarComponent> components)
    public FreeTimeBuilder components(final ComponentList<CalendarComponent> components)
    '''
def build():
    '''    public FreeBusy build()
    public FreeBusy build()
    '''
def Factory():
    '''    public Factory()
    '''
def createComponent():
    '''    public VFreeBusy createComponent()
    public VFreeBusy createComponent(final PropertyList properties)
    public VFreeBusy createComponent(final PropertyList properties, final ComponentList subComponents)
    '''
