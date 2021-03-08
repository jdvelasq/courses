Instalación de Vagrant y Docker
======================================================================================================

Como actividades previas al inicio del curso, se debe instalar y configurar el software utilizado. 

**Actividad 1.---** Creación de una cuenta en Github. 

  Realice los siguientes pasos:

    **Paso 1**

      Cree una **cuenta gratuita** en `GitHub <https://github.com>`__ con su correo electrónico de la universidad. Siga las instrucciones dadas en https://help.github.com/articles/signing-up-for-a-new-github-account/.

    **Paso 2**

      Configure la autenticación de dos factores https://help.github.com/articles/configuring-two-factor-authentication/.

    **Paso 3** 

      Modifique su perfil https://help.github.com/articles/personalizing-your-profile/, incluyendo nombre completo y fotografía para facilitar su identificación durante la calificación de los laboratios.

    **Paso 4**

      Instale y configure GitHub Desktop (windows y Mac OS) https://desktop.github.com/


**Actividad 2.---** Creación de una máquina virtual usando Vagrant.

  Siga las instrucciones dadas en el repo https://github.com/jdvelasq/vagrant4docker.


**Actividad 3.---** Apertura de un contenedor con una configuración mínima de Python.

  **Paso 1**

    Abra  **Terminal** y vaya a la carpeta donde configuró Vagrant. Inice la máquna virtual (VM)
    con 

    .. code:: bash

      vagrant up

  **Paso 2**
    
    Entre en la VM con:

    .. code:: bash

      vagrant ssh

    El prompt de **Terminal** cambiará a:

    .. code::

       $ vagrant ssh
       Welcome to Ubuntu 18.04.1 LTS (GNU/Linux 4.15.0-47-generic x86_64)

        * Documentation:  https://help.ubuntu.com
        * Management:     https://landscape.canonical.com
        * Support:        https://ubuntu.com/advantage

         System information as of Fri May  3 15:45:15 UTC 2019

         System load:  0.0                Processes:             97
         Usage of /:   79.2% of 11.57GB   Users logged in:       1
         Memory usage: 11%                IP address for enp0s3: 10.0.2.15
         Swap usage:   0%

        * Ubuntu's Kubernetes 1.14 distributions can bypass Docker and use containerd
          directly, see https://bit.ly/ubuntu-containerd or try it now with

            snap install microk8s --classic

         Get cloud support with Ubuntu Advantage Cloud Guest:
           http://www.ubuntu.com/business/services/cloud

        * Canonical Livepatch is available for installation.
          - Reduce system reboots and improve kernel security. Activate at:
            https://ubuntu.com/livepatch

       164 packages can be updated.
       39 updates are security updates.

       Last login: Wed May  1 22:20:14 2019 from 10.0.2.2
       vagrant@ubuntu-bionic:~$ 


  **Paso 3**

    Vaya a la carpeta compartida entre su VM y el sistema operativo anfitrión:

    .. code:: bash

      cd /vagrant

  **Paso 4** 
    
    En el prompt digite:

    .. code:: bash  

      docker run --rm -it -v "$PWD":/datalake -p 8888:8888 jdvelasq/python:3.6.9-minimal

    La prompt de comandos cambiará a algo similar a lo siguiente:

    .. code:: bash

      root@1e988d73e631:/datalake#

    En este momento, usted se encuentra trabajando dentro del contenedor.

  **Paso 5**

    Para cerrar el contendor y retornar a la máquina virtual use:

    .. code:: bash

      root@1e988d73e631:/datalake# exit
      vagrant@ubuntu-bionic:~$ 
