import kagglehub

# Download latest version
path = kagglehub.dataset_download("cbxkgl/uefa-champions-league-2016-2022-data")

print("Path to dataset files:", path)
