import os
import shutil

# Paths
names_file = 'names.txt'
source_dir = 'C:/Users/felip/OneDrive/Documentos/JSEx/spell_images'
destination_dir = 'C:/Users/felip/OneDrive/Documentos/JSEx/matching_images'

# Create the destination directory if it doesn't exist
if not os.path.exists(destination_dir):
    os.makedirs(destination_dir)

# Read the names from the file
with open(names_file, 'r') as file:
    names = file.read().splitlines()

# Process each name
for name in names:
    # Remove any quotes
    name = name.strip('"')
    # Construct the full image filename
    image_filename = f"{name}.png"
    
    # Check if the image exists in the source directory
    source_path = os.path.join(source_dir, image_filename)
    if os.path.exists(source_path):
        # Copy the image to the destination directory
        shutil.copy(source_path, destination_dir)
        print(f"Copied: {image_filename}")
    else:
        print(f"Image not found: {image_filename}")

print("Copy process completed.")
