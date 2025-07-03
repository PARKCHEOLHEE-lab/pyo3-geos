# Installation

This repository uses the [image](/.devcontainer/Dockerfile) named `rust:1.82` for running devcontainer.

1. Ensure you have Docker and Visual Studio Code with the Remote - Containers extension installed.
2. Clone the repository.

    ```
    git clone https://github.com/PARKCHEOLHEE-lab/pyo3-geos.git
    ```

3. Open the project with VSCode.
4. When prompted at the bottom left on the VSCode, click `Reopen in Container` or use the command palette (F1) and select `Remote-Containers: Reopen in Container`.
5. VS Code will build the Docker container and set up the environment.
6. Once the container is built and running, you're ready to start working with the project.

<br>

# Building Rust Code
After running the container, use the following command to compile the Rust code. The compiled code is generated in the target/wheels directory in \*.whl format, which can be installed using pip. For automation, the build.sh script includes `pip install target/wheels/"$NAME"-*.whl`.
```sh
sh build.sh rust_geos --release

  Updating crates.io index
  Downloaded unindent v0.2.4
  Downloaded num v0.4.3
  Downloaded pyo3-macros v0.25.1
  Downloaded c_vec v2.0.0
  Downloaded pkg-config v0.3.32
  Downloaded indoc v2.0.6
  Downloaded num-iter v0.1.45
  Downloaded heck v0.5.0
  Downloaded memoffset v0.9.1
  Downloaded num-integer v0.1.46
  Downloaded autocfg v1.5.0
  Downloaded num-complex v0.4.6
  Downloaded num-rational v0.4.2
  Downloaded once_cell v1.21.3
  Downloaded pyo3-build-config v0.25.1
  Downloaded geos-sys v2.0.6
  Downloaded quote v1.0.40
  Downloaded target-lexicon v0.13.2
  Downloaded semver v1.0.26
  Downloaded num-traits v0.2.19
  Downloaded proc-macro2 v1.0.95
  Downloaded unicode-ident v1.0.18
  Downloaded pyo3-macros-backend v0.25.1
  Downloaded pyo3-ffi v0.25.1
  Downloaded num-bigint v0.4.6
  Downloaded portable-atomic v1.11.1
  Downloaded syn v2.0.104
  Downloaded geos v10.0.0
  Downloaded libc v0.2.174
  Downloaded pyo3 v0.25.1
  Downloaded 30 crates (3.5 MB) in 8.48s (largest was `pyo3` at 1.1 MB)
🔗 Found pyo3 bindings
🐍 Found CPython 3.11 at /opt/venv/bin/python3
📡 Using build options features from pyproject.toml
   Compiling rust_geos v0.1.0 (/workspaces/pyo3-geos/rust_geos)
    Finished `release` profile [optimized] target(s) in 9.25s
🖨  Copied external shared libraries to package rust_geos.libs directory:
    /usr/lib/x86_64-linux-gnu/libgeos_c.so.1.17.1
    /usr/lib/x86_64-linux-gnu/libgeos.so.3.11.1
📦 Built wheel for CPython 3.11 to /workspaces/pyo3-geos/rust_geos/target/wheels/rust_geos-0.1.0-cp311-cp311-manylinux_2_34_x86_64.whl
Processing ./target/wheels/rust_geos-0.1.0-cp311-cp311-manylinux_2_34_x86_64.whl
Installing collected packages: rust-geos
Successfully installed rust-geos-0.1.0
```

<br>

# Testing

`test.py` tests a simple performance and accuracy test for the `buffer_erosion_and_dilation()` geometry operation using [python](./test.py) and [rust](./rust_geos/src/lib.rs).
Both Python's shapely library and Rust's geos library are based on the C GEOS library, and this test measures both implementations using the same parameters for the erode and dilate operations.

```sh
python test.py

  duration_py: 10.06878
  duration_rs: 4.41597
  speedup_ratio: 2.28008
```