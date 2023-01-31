# csv-flask-app

Flask app for csv manipulation

He optado por realizar una app con el siguiente **Stack**:

1. **Python** : Para el manejo de datos, aunque sea desde .csv, creo que Python es una opción muy flexible
2. **Flask** : Quería probar a utilizar Django, ya que creo que es una de las tecnologías principales que utilizais, pero me parecía "overkill" para este proyecto, mientras que Flask es ideal para este tipo de proyecto, así que he optado por él. Me ha servido consultar la documentación https://flask.palletsprojects.com/en/2.2.x/
3. **Bootstrap y Custom CSS** : Para darle una apariencia decente a las templates de html de flask he optado por añadir Bootstrap y alguna clase de CSS
4. **Pytest**: No lo había utilizado, al utilizar Python he decidido hacer uso y diseñar algunos tests. Me ha servido consultar la documentación https://docs.pytest.org/en/7.1.x/how-to/usage.html

# Ejecutar la solución

Hay varias formas de ejecutar la solución

## A) Descargando la Imagen desde DockerHub (Para usar)

La aplicación entera esta dockerizada y se puede acceder desde https://hub.docker.com/r/adrianmf06/acme-app para ello:

1. Si no tienes instalado Docker, puedes [instalarlo desde aquí](https://www.docker.com/)

2. Descargamos la imagen desde el repositorio

   ```bash
   $ docker pull adrianmf06/acme-app
   ```

3. Ejecutamos un contenedor, escuchando en el puerto 5000, a partir de la imagen

   ```bash
   $ docker run -p 5000:5000 adrianmf06/acme-app
   ```

4. Ir a la dirección donde se encuentra la app http://127.0.0.1:5000/

También podemos realizar de forma más sencilla, los pasos equivalentes desde Docker desktop

## B) Clonando el repositorio a Local (Para desarrollar)

1. Si no tienes Python instalado, puedes [instalarlo desde aquí](https://www.python.org/downloads/)

2. Si no tienes instalado Docker, puedes [instalarlo desde aquí](https://www.docker.com/)

3. Clone esta respositorio localmente

4. Colocate en el directorio

   ```bash
   $ cd csv-flask-app
   ```

5. Crea un nuevo virtual environment

   ```bash
   $ python -m venv .venv
   $ . .venv/Scripts/activate
   ```

6. Instala las dependencias

   ```bash
   $ pip install -r requirements.txt
   ```

7. Cambia al directorio de la app

   ```bash
   $ cd flaskr
   ```

8. Ejecuta la app localmente

   ```bash
   $ flask --debug run
   ```

9. Ir a la dirección donde se encuentra la app http://127.0.0.1:5000/

(Opcional) 10. En caso que hayamos hecho modificaciones y queramos construir una nueva imagen, en el directorio del Dockerfile

```bash
$ docker build -t acme-app .
```

(Opcional) 11. Nos logueamons en dockerhub

```bash
$ docker login
```

(Opcional) 12. Hacemos push de la imagen local al repositorio

```bash
$ docker push <docker_hub_username>/acme-app
```

## Para ejecutar los tests

En el directorio raíz, ejecutar

```bash
$ pytest
```

# Requisitos mínimos de la prueba

- Desarrolla una aplicación que utilizando como parámetros de entrada los tres ficheros suministrados customers.csv, products.csv y orders.csv genere los tres reportes solicitados.

  > ✔️ He desarrollado una aplicación que genera cada uno de los reportes, a partir de suministrarle los distintos ficheros necesarios, para cada uno de los reportes. Estos fichero suminstrado tienen que llamarse exactamente como se indica en el enunciado, esto puede resultar tedioso, pero a su vez ayuda a que sepamos que fichero y con que columas le estamos suministrando al programa.

- No es necesario que construyas un frontend, es una prueba de backend. Es suficiente con tener un comando en consola que recoja la entrada y genere los archivos de salida.

  > ✔️ Incialmente desarolle el código para generar los 3 ficheros de salida a partir de los 3 ficheros de entrada con un único comando. Pero al pasar a desarollar un API consideré que era mejor separar la generación de cada reporte.

- Decíamos en el primer apartado de la prueba que vamos a valorar como documentes la prueba, puedes crear un fichero readme.md con los pasos que tenemos que dar para ejecutar tu prueba en local.

  > ✔️ He aquí, _el Readme.md_

# Para nota

Además de los requisitos mínimos para la prueba, hemos definido una serie de requisitos adicionales para que puedas lucirte

- Testing. No es imprescindible, pero si vienes con nosotros vas a tener que aprender a testear tu código, puede ser un buen momento para empezar.

  > 🟢 He realizado testing, he utilizado Pytest. En la raíz del proyecto hay una carpeta _tests_ que contiene la configuración necesaria y el archivo _test_index.py_ que define 4 casos de test. El primero para comprobar que se muestra correctamente la página de Inicio y después 3 casos más que cada uno testea uno de los endpoints que generan los reportes. Para poder testear la API y los métodos de los reportes, es necesario suministrar los ficheros _.csv_ por lo que en el carpeta _tests_ disponesmos también de una carpeta resources con los ficheros de ejemplo que utilizamos para testear los endpoints añadiendolos a las peticiones de testing. También comprobamos que al respuesta es correcta y que somo redirigidos al endpoint de descaga del reporte.

- API. Implementar la aplicación como un API que permita subir los ficheros, generar los resultados y descargarlos.

  > 🟢 La API esta organizada en 3 endpoints en función del reporte que queramos generar, estos son _/upload_report_1_ _/upload_report_2_ _/upload_report_3_

  Aquí podemos ver como llamar a cada uno:

  ```bash
  curl --location --request POST 'http://127.0.0.1:5000/upload_report_1' \
  --form 'files=@"/C:/Users/adria/Desktop/orders.csv"' \
  --form 'files=@"/C:/Users/adria/Desktop/products.csv"' \
  ```

  ```bash
  curl --location --request POST 'http://127.0.0.1:5000/upload_report_2' \
  --form 'files=@"/C:/Users/adria/Desktop/orders.csv"' \
  ```

  ```bash
  curl --location --request POST 'http://127.0.0.1:5000/upload_report_3' \
  --form 'files=@"/C:/Users/adria/Desktop/orders.csv"' \
  --form 'files=@"/C:/Users/adria/Desktop/products.csv"' \
  --form 'files=@"/C:/Users/adria/Desktop/customers.csv"'
  ```

- Docker. Nos gustaría que toda la prueba y sus dependencias se ejecutaran dentro de un contenedor y así nuestros compañeros de departamento solo necesitarán Docker en su día a día.

  > 🟢 A partir de un Dockerfile accesible en el repositorio, he creado una imagen con todo el entorno y dependencias necesarias para ejecutar contenedores en cualquier máquina que tenga Docker instalado.

- Frontend. Cómo decíamos no es un requisito, pero si te animas seguro que para nuestros compañeros es más sencillo utilizar la aplicación a través de un formulario web.

  > 🟢 Para que la app se mínimamente amigable de utilizar he desarrollado un front a partir de templates de html y estilado con Bootstrap y CSS. El diseño es sencillo pero también considero que para una aplicación interna y puede que crítica es más importante la funcionalidad clara que un diseño vistoso.

# Recursos que he utilizado

[Este vídeo de youtube](https://youtu.be/BP8ulGbu1fc) me ha resultado muy útil para saber cómo implemnetar una API que acepte ficheros .csv en las peticiones, cosa que no había hecho hasta ahora.

[Este otro vídeo](https://www.youtube.com/watch?v=S7bwkys6D0E&ab_channel=Postman) de la documentaciónmnatción de Postman de como utilizar para enviar ficheros en peticiones rest

[Documentación de Bootstrap](https://getbootstrap.com/docs/4.0/components/buttons/)

Estos dos aparatados de la documenatción de Flask
sobre fileuploads y project layout

- https://flask.palletsprojects.com/en/2.2.x/patterns/fileuploads/

- https://flask.palletsprojects.com/en/2.2.x/tutorial/layout/

muy útil también este apartado sobre testing en flask

- https://flask.palletsprojects.com/en/2.2.x/testing/

[Documentación de Pytest](https://docs.pytest.org/en/7.1.x/how-to/usage.html)

# Explicaciones adicionales

Lo que más me ha costado ha sido implentar y que funcionasen correctamente los tests, así como estructurar el proyecto adecuadamente.

Lo que no tengo del todo claro es si el dockerfile debe estar en el nivel raíz de forma que cuando creamos la imagen, tanto tests como el readme, ficheros de configuración etc se añadan también. O si por el contrario sería más conveninete crear la imagen en el directorio flaskr para que contuviera únicamente la app.

Algo que debo investigar más es como desplegar en modo producción la app de flask ya que a pesar de indicar modo production y el debug estar en off. Indican que se deberí ahacer uso de un servidor WSGI.

> _Debug mode: off_ > _WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead._

# Herramientas que he utilizado y suelo utilizar

**Postman**, para probar los endpoints definidos en el backend

**Docker Desktop** para probar la imagen construida y lanzar contenedores

**DockerHub** como repositorio para subir las Imagenes de Docker y que sean accesibles públicamente

**Stack Overflow**

[**Code Grepper**](https://www.grepper.com/) : Extensión de navegador que te muestra snippets de código bajo la barra de búsqueda.

**Yotube**

**ChatGPT** : Recientemente también lo estoy utilizando, para código en general creo que esta bastante bien, pero hay que saber que preguntar por lo menos y tamb vigilar de cerca. Para debugear a veces también me funciona muy bien, pasandole logs de error.
