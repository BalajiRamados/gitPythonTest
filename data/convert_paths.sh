paths=(
    "data/new1.py",
    "data/new2.sql",
    "data/newData/new3.sql"
    "new4.sql",
    "newData/newData2/newData3/new5.py"
)

convert_paths() {
    local paths=("$@")
    for path in "${paths[@]}"; do
        base_name="${path%.*}"
        
        converted_path="${base_name//\//.}"

        echo "$converted_path"
    done
}

convert_paths "${paths[@]}"
