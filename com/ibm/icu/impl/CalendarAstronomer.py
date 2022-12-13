SIDEREAL_DAY = "double  23.93446960027"
SOLAR_DAY = "double  24.065709816"
SYNODIC_MONTH = "double  29.530588853"
SIDEREAL_MONTH = "double  27.32166"
TROPICAL_YEAR = "double  365.242191"
SIDEREAL_YEAR = "double  365.25636"
SECOND_MS = "int  1000"
MINUTE_MS = "int  60000"
HOUR_MS = "int  3600000"
DAY_MS = "long  86400000L"
JULIAN_EPOCH_MS = "long  -210866760000000L"
def CalendarAstronomer():
    '''public CalendarAstronomer()
    public CalendarAstronomer(final Date d)
    public CalendarAstronomer(final long aTime)
    public CalendarAstronomer(final double longitude, final double latitude)
    '''
def setTime():
    '''public void setTime(final long aTime)
    '''
def setDate():
    '''public void setDate(final Date date)
    '''
def setJulianDay():
    '''public void setJulianDay(final double jdn)
    '''
def getTime():
    '''public long getTime()
    '''
def getDate():
    '''public Date getDate()
    '''
def getJulianDay():
    '''public double getJulianDay()
    '''
def getJulianCentury():
    '''public double getJulianCentury()
    '''
def getGreenwichSidereal():
    '''public double getGreenwichSidereal()
    '''
def getLocalSidereal():
    '''public double getLocalSidereal()
    '''
def eclipticToEquatorial():
    '''public final Equatorial eclipticToEquatorial(final Ecliptic ecliptic)
    public final Equatorial eclipticToEquatorial(final double eclipLong, final double eclipLat)
    public final Equatorial eclipticToEquatorial(final double eclipLong)
    '''
def eclipticToHorizon():
    '''public Horizon eclipticToHorizon(final double eclipLong)
    '''
def getSunLongitude():
    '''public double getSunLongitude()
    '''
def getSunPosition():
    '''public Equatorial getSunPosition()
    '''
def getSunTime():
    '''public long getSunTime(final double desired, final boolean next)
    public long getSunTime(final SolarLongitude desired, final boolean next)
    '''
def eval():
    '''public double eval()
    public Equatorial eval()
    public double eval()
    public Equatorial eval()
    '''
def getSunRiseSet():
    '''public long getSunRiseSet(final boolean rise)
    '''
def getMoonPosition():
    '''public Equatorial getMoonPosition()
    '''
def getMoonAge():
    '''public double getMoonAge()
    '''
def getMoonPhase():
    '''public double getMoonPhase()
    '''
def getMoonTime():
    '''public long getMoonTime(final double desired, final boolean next)
    public long getMoonTime(final MoonAge desired, final boolean next)
    '''
def getMoonRiseSet():
    '''public long getMoonRiseSet(final boolean rise)
    '''
def local():
    '''public String local(final long localMillis)
    '''
def Ecliptic():
    '''public Ecliptic(final double lat, final double lon)
    '''
def toString():
    '''public String toString()
    public String toString()
    public String toString()
    '''
def Equatorial():
    '''public Equatorial(final double asc, final double dec)
    '''
def toHmsString():
    '''public String toHmsString()
    '''
def Horizon():
    '''public Horizon(final double alt, final double azim)
    '''
