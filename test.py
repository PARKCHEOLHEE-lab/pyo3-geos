from shapely import BufferCapStyle, geometry, wkt, BufferJoinStyle
from shapely.geometry.base import BaseGeometry as Geometry


def buffer_erosion_and_dilation_py(geometry_wkt: str, distance: float) -> str:

    geometry: Geometry = wkt.loads(geometry_wkt)
    
    quadsegs: int = 16
    cap_style: BufferCapStyle = BufferCapStyle.flat
    join_style: BufferJoinStyle = BufferJoinStyle.mitre
    mitre_limit: float = 5.0
    
    eroded: Geometry = geometry.buffer(
        -distance, 
        quad_segs=quadsegs, 
        cap_style=cap_style, 
        join_style=join_style, 
        mitre_limit=mitre_limit
    )
    
    dilated: Geometry = eroded.buffer(
        distance, 
        quad_segs=quadsegs, 
        cap_style=cap_style, 
        join_style=join_style, 
        mitre_limit=mitre_limit
    )
    
    return dilated.wkt



if __name__ == "__main__":
    
    rectangle = geometry.Polygon(
        [
            [0, 0], 
            [1, 0], 
            [1, 1], 
            [0, 1]
        ]
    )
    
    import time
    import math
    
    start = time.time()
    for _ in range(100000):
        g = buffer_erosion_and_dilation_py(rectangle.wkt, 0.1)

    duration_py = time.time() - start
    print(f"duration_py: {duration_py:.5f}")

    assert math.isclose(wkt.loads(g).area, 1.0) 
    assert (rectangle - wkt.loads(g)).is_empty
    
    from rust_geos import buffer_erosion_and_dilation_rs

    start = time.time()
    for _ in range(100000):
        g = buffer_erosion_and_dilation_rs(rectangle.wkt, 0.1)

    duration_rs = time.time() - start
    print(f"duration_rs: {duration_rs:.5f}")
    
    assert math.isclose(wkt.loads(g).area, 1.0) 
    assert (rectangle - wkt.loads(g)).is_empty
    
    speedup_ratio = duration_py / duration_rs
    print(f"speedup_ratio: {speedup_ratio:.5f}")