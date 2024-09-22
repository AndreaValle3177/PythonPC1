mime_types = {
    '.gif': 'image/gif',
    '.jpg': 'image/jpeg',
    '.jpeg': 'image/jpeg',
    '.png': 'image/png',
    '.pdf': 'application/pdf',
    '.txt': 'text/plain',
    '.zip': 'application/zip'
}
nombre_archivo = input("Ingrese el nombre del archivo: ")
nombre_archivo_lower = nombre_archivo.lower()
tipo_mime = 'application/octet-stream'
for extension in mime_types:
    if nombre_archivo_lower.endswith(extension):
        tipo_mime = mime_types[extension]
        break
print(f"El tipo MIME del archivo es: {tipo_mime}")
