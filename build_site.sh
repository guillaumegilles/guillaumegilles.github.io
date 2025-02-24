#!/bin/bash

# Exit on error
set -e

# Step 1: Render the Quarto project
echo "Rendering Quarto project..."
quarto render

# Step 2: Create up to two levels of subdirectories inside docs/, removing `_`
echo "Creating directory structure in docs/..."
for dir in teaching projects; do
    find "$dir" -maxdepth 1 -type d | while read -r subdir; do
        # Remove any leading `_` from each directory name
        clean_subdir=$(echo "$subdir" | sed 's|/_|/|g' | sed 's|^_||')

        # Construct the corresponding directory inside docs/
        newdir="docs/$clean_subdir"
        mkdir -p "$newdir"
        echo "Created: $newdir"
    done
done

echo "Directory structure created successfully!"

# Step 3: Copy files from `teaching/*/docs/` and `projects/*/docs/` to `docs/teaching/*` and `docs/projects/*`
echo "Copying files..."
find teaching projects -maxdepth 2 -type d -name "docs" | while read -r source_dir; do
    # Determine the parent directory (e.g., teaching/_data-analysis/docs → teaching/_data-analysis)
    parent_dir=$(dirname "$source_dir")

    # Remove leading `_` from parent directory name
    clean_subdir=$(echo "$parent_dir" | sed 's|/_|/|g' | sed 's|^_||')

    # Define the target directory in `docs/`
    target_dir="docs/$clean_subdir"

    # Copy files if the source directory is not empty
    if [ -d "$source_dir" ]; then
        cp -r "$source_dir"/* "$target_dir"/ 2>/dev/null || true
        echo "Copied files from $source_dir to $target_dir"
    fi
done

echo "Build process completed successfully!"
