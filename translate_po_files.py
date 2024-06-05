import os
import sys
import polib
from deep_translator import GoogleTranslator

# Map your directory language codes to GoogleTranslator language codes
LANGUAGE_CODE_MAP = {
    'en': 'en',    # English
    'de': 'de',    # German
    'es': 'es',    # Spanish
    'fr': 'fr',    # French
    'pt': 'pt',    # Portuguese
    'zh-cn': 'zh-CN',  # Simplified Chinese
    'nl': 'nl'     # Dutch
}

def translate_po_files(root_dir):
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if file == 'django.po':
                po_file_path = os.path.join(subdir, file)
                process_po_file(po_file_path, subdir)

def process_po_file(po_file_path, subdir):
    # Get the language code from the parent directory of LC_MESSAGES
    lang_code = os.path.basename(os.path.dirname(subdir))
    print(f"Detected language code: {lang_code}")
    target_lang = LANGUAGE_CODE_MAP.get(lang_code)
    
    if not target_lang:
        print(f"No support for the provided language: {lang_code}")
        return

    po = polib.pofile(po_file_path)

    for entry in po:
        if not entry.msgstr.strip():
            try:
                translation = GoogleTranslator(source='auto', target=target_lang).translate(entry.msgid)
                entry.msgstr = translation
            except Exception as e:
                print(f"Error translating '{entry.msgid}': {e}")

    processed_file_path = os.path.join(subdir, 'django.po')  # Save as django_processed.po to avoid overwriting
    po.save(processed_file_path)
    print(f"Processed and saved: {processed_file_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python translate_po_files.py <root_directory>")
        sys.exit(1)

    root_directory = sys.argv[1]
    translate_po_files(root_directory)