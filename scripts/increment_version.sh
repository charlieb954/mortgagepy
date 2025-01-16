#!/bin/bash

# Function to increment version
increment_version() {
    local version=$1
    local level=$2

    IFS='.' read -ra parts <<< "$version"
    major=${parts[0]}
    minor=${parts[1]}
    patch=${parts[2]}

    case $level in
        major)
            major=$((major + 1))
            minor=0
            patch=0
            ;;
        minor)
            minor=$((minor + 1))
            patch=0
            ;;
        patch)
            patch=$((patch + 1))
            ;;
        *)
            echo "Invalid level. Use 'major', 'minor', or 'patch'."
            exit 1
            ;;
    esac

    echo "$major.$minor.$patch"
}

# Check if level argument is provided
if [ $# -eq 0 ]; then
    echo "Please specify the version level to increment: major, minor, or patch"
    exit 1
fi

level=$1

# Read current version from pyproject.toml
current_version=$(awk -F' *= *' '/version/ {gsub(/"/, "", $2); print $2}' pyproject.toml)

if [[ -z "$current_version" ]]; then
    echo "Failed to read the current version from pyproject.toml"
    exit 1
fi

# Increment version
new_version=$(increment_version "$current_version" "$level")

# Update pyproject.toml with new version
awk -v new_version="$new_version" -F' *= *' '/version/ {$2="\""new_version"\""}1' OFS=' = ' pyproject.toml > pyproject.toml.tmp && mv pyproject.toml.tmp pyproject.toml

echo "Version updated from $current_version to $new_version"