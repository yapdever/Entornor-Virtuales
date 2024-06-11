FROM python:3.8

#Crear una carptea de trabajo
WORKDIR /app
#Copiar el archivo requirements.txt a la carpeta de trabajo
COPY requirements.txt /app/requirements.txt

#Instalar las dependencias
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

#Copiar todo el contenido de la carpeta actual a la carpeta de trabajo
COPY . /app

#Ejecutar el comando para que la aplicacion se ejecute constantemente
CMD bash -c "while true; do sleep 1; done"

