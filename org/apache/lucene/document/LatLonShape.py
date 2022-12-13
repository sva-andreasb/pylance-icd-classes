def createIndexableFields():
'''public static Field[] createIndexableFields(final String fieldName, final Polygon polygon)
public static Field[] createIndexableFields(final String fieldName, final Line line)
public static Field[] createIndexableFields(final String fieldName, final double lat, final double lon)
'''
pass
def newBoxQuery():
'''public static Query newBoxQuery(final String field, final ShapeField.QueryRelation queryRelation, final double minLatitude, final double maxLatitude, final double minLongitude, final double maxLongitude)
'''
pass
def newLineQuery():
'''public static Query newLineQuery(final String field, final ShapeField.QueryRelation queryRelation, final Line... lines)
'''
pass
def newPolygonQuery():
'''public static Query newPolygonQuery(final String field, final ShapeField.QueryRelation queryRelation, final Polygon... polygons)
'''
pass
def newPointQuery():
'''public static Query newPointQuery(final String field, final ShapeField.QueryRelation queryRelation, final double[]... points)
'''
pass
def newDistanceQuery():
'''public static Query newDistanceQuery(final String field, final ShapeField.QueryRelation queryRelation, final Circle... circle)
'''
pass
def newGeometryQuery():
'''public static Query newGeometryQuery(final String field, final ShapeField.QueryRelation queryRelation, final LatLonGeometry... latLonGeometries)
'''
pass
