NAME=$(jq -r '.name' .devcontainer/devcontainer.json)
if [ ! -d "$NAME" ]; then
    mkdir -p "$NAME"
    cd "$NAME"
    maturin init -b pyo3
    cargo add geos@10.0.0
else
    :
fi
