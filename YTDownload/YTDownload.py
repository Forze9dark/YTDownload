import pytube
import os
import subprocess

while True:
    # Nombre de la carpeta donde se descargaran los ficheros.
    folder_to_download = "YTDescargas"

    # Obtenemos la url por parte del usuario y la buscamos en Youtube para obtener todos sus datos.
    video_url = input(
        "Ingresa la URL del video o escriba 'salir' para cerrar el programa: "
    )
    if video_url == "salir":
        break

    yt = pytube.YouTube(video_url)
    streams = yt.streams.filter(progressive=True).order_by("resolution").desc()

    # Imprimir lista de resoluciones y seleccionar una.
    print("Lista de resoluciones disponibles:")
    for i, stream in enumerate(streams):
        print(f"{i+1}. {stream.resolution}")
    choice = int(input("Ingrese el numero de la resolucion que desea bajar el video: "))

    stream = streams[choice - 1]

    # Nombre del archivo a guardar.
    filename = stream.default_filename

    if not os.path.exists(folder_to_download):
        os.makedirs(folder_to_download)

    # Ruta completa del archivo a guardar
    output_path = os.path.join(folder_to_download, filename)

    # Descargar el archivo y guardarlo en la carpeta de la variable folder_to_download
    print("Descargando...")
    stream.download(output_path=output_path)
    print("Descarga completada.")

    # Abrir la carpeta donde se descargó el video y limpiar la consola
    os.startfile(folder_to_download)
