# Auto Backup Tool

Este es un script en Python que automatiza el respaldo de archivos desde una carpeta origen hacia una carpeta de respaldo, agregando una marca de tiempo y generando un registro detallado.

## ¿Para qué sirve?

Evita la pérdida de archivos importantes mediante backups automáticos organizados por fecha. Es útil para oficinas, estudiantes, desarrolladores y cualquier persona que necesite proteger sus documentos.

## ¿Qué hace el script?

- Copia todos los archivos desde `source_folder/` hacia una subcarpeta nueva dentro de `backup_folder/`, agregando la fecha y hora al nombre.
- Genera un archivo de log (`backup_log.txt`) con cada operación realizada.
- Omite carpetas vacías o archivos inexistentes sin generar errores.

## ¿Cómo usarlo?

1. Asegurate de tener Python 3 instalado.
2. Cloná este repositorio o descargá los archivos.
3. Colocá tus archivos importantes dentro de `source_folder/`.
4. Ejecutá el script:

```bash
python auto_backup.py
