from datetime import datetime
import os
import shutil
import logging

SOURCE_DIR = 'source_folder'
BACKUP_DIR = 'backup_folder'
LOG_FILE = 'log/backup_log.txt'

os.makedirs(SOURCE_DIR, exist_ok=True)
os.makedirs(BACKUP_DIR, exist_ok=True)
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

logging.basicConfig(filename=LOG_FILE, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
current_backup_dir = os.path.join(BACKUP_DIR, f'backup_{timestamp}')
os.makedirs(current_backup_dir, exist_ok=True)

try:
    files_copied = []
    for filename in os.listdir(SOURCE_DIR):
        source_path = os.path.join(SOURCE_DIR, filename)
        if os.path.isfile(source_path):
            dest_path = os.path.join(current_backup_dir, filename)
            shutil.copy2(source_path, dest_path)
            files_copied.append(filename)

    if files_copied:
        logging.info(f"Backup exitoso. Archivos copiados: {', '.join(files_copied)}")
        print(f"Backup completo. {len(files_copied)} archivo(s) copiado(s).")
    else:
        logging.warning("No se encontraron archivos para respaldar.")
        print("No se encontraron archivos para respaldar.")

except Exception as e:
    logging.error(f"Error durante el backup: {e}")
    print(f"Ocurrió un error: {e}")
