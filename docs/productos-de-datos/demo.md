INTRODUCCIÓN


Cada día los expertos en análisis de datos son profesionales muy demandados en los diferentes estados del arte de nuestra sociedad. El uso constante y creciente de la tecnología e internet, genera grandes cantidades de información. Extraer el valor de todos esos datos y volverlos conocimiento es el gran reto de cualquier empresa o institución que desee estar a la vanguardia y crear nuevas experiencias de a nivel de servicio y negocio.

Manejar datos a una escala empresarial, requiere desarrollar una serie de habilidades, así como el manejo de diferentes herramientas; lo cual este curso no es ajeno a estas necesidad, por esta razón fue diseñada esta guia para ofrecer un punto de partida para realizar las configuraciones de sus máquina personales o la que destinen para este curso,  con el fin de que puedan avanzar sin contratiempos en las actividades y explicaciones del curso.
































1. CONFIGURACIÓN DE DOCKER

Docker es un conjunto de productos de plataforma como servicio (PaaS) que utilizan la virtualización a nivel de sistema operativo para entregar software en paquetes llamados contenedores. Los contenedores están aislados entre sí y agrupan su propio software, pueden comunicarse entre ellos a través de canales bien definidos y utilizan menos recursos que las máquinas virtuales.

A continuación se listan los pasos dependiendo del sistema operativo, para realizar su respectiva configuración


1.1. CONFIGURACION MAC


Ingresar a la página https://www.docker.com/products/docker-desktop , seleccionar productos >  Docker Desktop



Selecciona Descarga para Mac



Una vez finalice la descarga, se visualizará un archivo como este



Dar click sobre el archivo, se iniciará el proceso de descompresión


Finalizada la descompresión se abrirá la ventana de instalación, seleccionar el icono de docker y soltarlo en la carpeta de aplicaciones


	
Si no hay novedades, iniciará la instalación



Finalizada la instalación, ir a launchpad y buscar el icono de docker


Se generará una serie de alertas de seguridad, a las cuales deberá aceptar y  acreditar mediante clave de usuario







Si todos los datos ingresados fueron correctos, podrás ver una pantalla como esta



Docker quedará completamente configurado cuando en la barra superior puedas ver el icono de la ballena de manera estático 



 Realizaremos una última prueba, ingresamos a  launchpad  y buscamos la terminal


	
	Ejecutar docker versión, se deberá mostrarse algo como esto:




1.2. CONFIGURACION WINDOWS


Ingresar a la pagina https://www.docker.com/products/docker-desktop , seleccionar productos >  Docker Desktop



Selecciona Descarga para Windows


Una vez finalice la descarga, se visualizará un archivo como este







Dar click sobre el archivo, se iniciará el proceso de instalación, oprimir el botón Ok



Si no hay contratiempos en la máquina, inicia la instalación






Si todo instalo correctamente, sacara esta ventana de confirmación, la cual deberá dar click en cierre y reinicio

Nota: no deberá tener cambios pendientes en documentos o etc, para no perder información



Una vez que la máquina reinicie nuevamente, buscar el icono de Docker y dar click. Esto abrirá la ventana del programa, dar click en omitir tutorial




Podrás ver una pantalla como esta, la ballena deberá estar en color verde, si esta en roja, deberá reiniciar la maquina nuevamente



Realizaremos una última prueba, ingresar a la barra de búsqueda y se debe digitar PowerShell






Ejecutar docker versión, se deberá mostrarse algo como esto:




1.2.1. POSIBLES ERRORES WINDOWS


Dependiendo de la configuración por defecto que tenga la máquina o las actualizaciones incompletas del sistema, se pueden generar varios errores al intentar abrir docker, a continuación, se lista una serie de errores comunes, los cuales se explicaran paso a paso cómo solucionarlos

 
1.2.1.1 ERROR DE BIOS

Si intenta abrir la aplicación y le genera el siguiente error :



probablemente,puede ser que no tenga habilitada la opción de virtualización, para lo cual se deben seguir los siguientes pasos descritos en el siguiente link https://docs.docker.com/docker-for-windows/troubleshoot/#virtualization, o descritos a continuación:

Realizar la combinación de teclas Control + Shift + Esc, la cual abrirá el administrador de tareas, dar Click en la pestaña de Rendimiento > validar que la opción de virtualización está activada



Si la opción no se encuentra o no habilitada, deberá realizar la validación de la configuración requerida para la virtualización, para ello deberá ingresar la combinación de teclas Windows + R > ingresar la palabra control > Presionar Enter > Seleccionar Programas y Caracteristicas > Activar o desactivar las características de Windows




Se deberá verificar que las siguientes opciones están habilitadas




Si alguna de las opciones no se encuentra habilitada, se deberá realizar activación y reinicia nuevamente la máquina he intentar abrir Docker 

En caso de que tenga seleccionada las opciones,  y aun siga apareciendo el error 1.2.1.1, se deberán ejecutar las siguientes acciones

Abrir una consola de PowerShell como administrador y ejecutar bcdedit /set hypervisorlaunchtype auto , luego intentar abrir Docker


Si la opción anterior no funciona, abrir una consola de PowerShell como administrador y ejecutar :  dism.exe /Online /Enable-Feature:Microsoft-Hyper-V /All , luego intentar abrir Docker

Si la opción anterior no funciona,  deberá ingresar la combinación de teclas Windows + R > ingresar la palabra control > Presionar Enter > Seleccionar Programas y Caracteristicas > Activar o desactivar las características de Windows > Deshabilitar Hyper-V, reiniciar la maquina he intentar abrir Docker nuevamente
Si el paso anterior no funciona, deberá validar la configuración de virtualización a nivel de BIOS, para ello se recomienda seguir el siguiente video https://www.youtube.com/watch?v=OwNqlicoAu8&ab_channel=AlkaJuggerProyecto-C

1.2.1.2 ERROR DE WSL

Si intenta abrir la aplicación y le genera el siguiente error :



Deberá descargar el archivo https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi , una vez descargado el archivo:



 deberá instalarlo y reiniciar la máquina, luego abrir Docker nuevamente.
1.3. CONFIGURACIÓN LINUX

Este tutorial está diseñado para las versiones de Ubuntu 18 y 20, si está usando otra distribución diferente sea Fedora, Centos, RedHat, Suse, deberá verificar los paquetes en el repositorio de la distribución oficial. 

Actualizar los repositorios de Software  
sudo apt-get update
Desinstalar cualquier paquete viejo 
sudo apt-get remove docker docker-engine docker.io
Instalar Docker
sudo apt install docker.io
Iniciar el servicio de docker, configurarlo para que arranque en modo daemon
sudo systemctl start docker
sudo systemctl enable docker

	Si la configuración fue aplicada correctamente, se deberá ver algo como esto:



 Realizar una última prueba, ejecutar docker versión, se deberá ver algo como esto:

1.3.1. REFERENCIAS LINUX

https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-18-04

https://phoenixnap.com/kb/how-to-install-docker-on-ubuntu-18-04

