use pyo3::prelude::*;
use geos::{Geometry, Geom, Error, CapStyle, JoinStyle};


fn _pyerr(e: String) -> PyErr {
    // PyO3 uses PyResult<T> which is an alias for Result<T, PyErr>
    // This allows functions to return either a successful value T or a Python exception PyErr
    // 
    // GEOS uses GResult<T> which is an alias for Result<T, Error> 
    // This allows geometry operations to return either a successful value T or a GEOS-specific Error
    
    PyErr::new::<pyo3::exceptions::PyValueError, _>(e.to_string())
}

#[pyfunction]
fn buffer_erosion_and_dilation_rs(geometry_wkt: &str, distance: f64) -> PyResult<String> {

    let geometry: Geometry = Geometry::new_from_wkt(geometry_wkt)
        .map_err(|e: Error| _pyerr(e.to_string()))?;

    let quadsegs: i32 = 16;
    let cap_style: CapStyle = CapStyle::Flat;
    let join_style: JoinStyle = JoinStyle::Mitre;
    let mitre_limit: f64 = 5.0;

    let eroded: Geometry = geometry.buffer_with_style(
        -distance, 
        quadsegs, 
        cap_style, 
        join_style, 
        mitre_limit,
    ).map_err(|e: Error| _pyerr(e.to_string()))?;

    let dilated: Geometry = eroded.buffer_with_style(
        distance, 
        quadsegs, 
        cap_style, 
        join_style, 
        mitre_limit,
    ).map_err(|e: Error| _pyerr(e.to_string()))?;
    
    Ok(dilated.to_wkt()
        .map_err(|e: Error| _pyerr(e.to_string()))?)
}


#[pymodule]
fn rust_geos(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(buffer_erosion_and_dilation_rs, m)?)?;
    Ok(())
}
