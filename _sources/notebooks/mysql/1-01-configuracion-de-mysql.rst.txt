Configuración de MySQL
============================

* *5 min*  | Última modificación: Junio 22, 2019

La VM suministrada con Vagrant, ya tiene instalado MySQL 5.7 y no requiere password 
para su uso.


**Shell de MySSL**.

Para iniciar la consola de comandos de MySQL en Terminal digite:

.. code::
    
   sudo mysql 


Seguidamente, en Terminal se solicitará el password. Si el resultado es exitoso,
la salida será similar a la siguiente:

.. code::

   vagrant@ubuntu-bionic:~$ mysql
   Welcome to the MySQL monitor.  Commands end with ; or \g.
   Your MySQL connection id is 6
   Server version: 5.7.25-0ubuntu0.18.04.2 (Ubuntu)

   Copyright (c) 2000, 2019, Oracle and/or its affiliates. All rights reserved.

   Oracle is a registered trademark of Oracle Corporation and/or its
   affiliates. Other names may be trademarks of their respective
   owners.

   Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

   mysql> quit
   Bye
   vagrant@ubuntu-bionic:~$


