def LatLonDocValuesField():
'''public LatLonDocValuesField(final String name, final double latitude, final double longitude)
'''
pass
def setLocationValue():
'''public void setLocationValue(final double latitude, final double longitude)
'''
pass
def toString():
'''public String toString()
'''
pass
def newDistanceSort():
'''public static SortField newDistanceSort(final String field, final double latitude, final double longitude)
'''
pass
def newSlowBoxQuery():
'''public static Query newSlowBoxQuery(final String field, final double minLatitude, final double maxLatitude, double minLongitude, final double maxLongitude)
'''
pass
def newSlowDistanceQuery():
'''public static Query newSlowDistanceQuery(final String field, final double latitude, final double longitude, final double radiusMeters)
'''
pass
def newSlowPolygonQuery():
'''public static Query newSlowPolygonQuery(final String field, final Polygon... polygons)
'''
pass
