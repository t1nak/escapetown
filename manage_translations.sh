#!/bin/bash

# Languages to create translations for
LANGUAGES=("en" "de" "es" "fr" "pt" "zh-CN" "nl")

# Create translation files for specified languages
for lang in "${LANGUAGES[@]}"
do
   poetry run django-admin makemessages -l $lang
done


# Array of paths to process
LOCALE_PATHS=("dashboard/locale" "products/locale" "accounts/locale" "landing_page/locale" "things_to_do/locale")

# Loop through each path and run the translation script
for path in "${LOCALE_PATHS[@]}"; do
    echo "Processing $path..."
    poetry run python translate_po_files.py "$path"
done


# Compile translation files
poetry run django-admin compilemessages

echo "Translations have been created and compiled."