Introducción a Bash
===================

* *5 min*.

El proceso de transformación de datos se refiere a la tarea de convertir los datos de un formato a otro [#f1]_, el cual incluye las fases de:

*	Inspección – determinación de las características como el formato y otras propiedades.
*	Lectura – carga correcta de los datos.
*	Filtrado – selección del subconjunto de datos de interés.
*	Transformación – modificación de los datos como tal.

La transformación de datos es una de las fases principales en la ciencia de los datos y la analítica, y está directamente vinculada a los procesos ETL (Extract-Transform-Load).  Por ETL se hace referencia los procesos requeridos para la extracción de datos provenientes de diferentes fuentes y con distintos formatos, la transformación para su unificación en un solo formato estándar y la carga a un sistema de información (que usualmente es una base de datos).

El proceso de transformación de datos incluye, entre otras, las siguientes actividades [#f2]_:

*	Remoción de datos innecesarios o repetidos.
*	Reducción del número de filas o registros por eliminación o por agregación.
*	Reducción del número de campos o columnas.
*	Reemplazo o construcción de claves.
*	Creación de nuevos campos o columnas.

Estos procesos suelen ser repetitivos e involucran, usualmente, una cantidad importante de datos, de tal forma que pueden resultar muy dispendiosos, tediosos o prácticamente imposibles de realizar manualmente. Es así como una tarea tan simple como renombrar un archivo se vuelve abrumadora cuando se deben renombrar 1.000 o 10.000 archivos. En este sentido, la automatización de estas tareas trae múltiples beneficios al usuario, entre los que se encuentran [#f3]_:

*	El agilizar tareas simples que consumen una gran cantidad de tiempo.
*	La eliminación de la posibilidad de errores debidos a la ejecución manual de un proceso (por un humano).
*	Una mayor cantidad de tiempo para realizar otras actividades de corte intelectual.

Este documento aborda la transformación de datos almacenados en archivos de texto mediante el uso de la consola de comandos o shell, la cual es una interfaz para dar comandos al sistema operativo Unix (incluyendo Linux y OS X) [#f4]_ digitando texto. La idoneidad de la shell para la transformación de archivos de texto proviene de la filosofía de diseño del sistema operativo Unix, según la cual, el sistema operativo debe estar conformado por una gran cantidad de pequeños programas con objetivos bien definidos y por el intercambio de información entre programas a través de texto plano [#f5]_. Ya que el texto plano es el lenguaje universal entre programas escritos en diferentes lenguajes, las herramientas del sistema operativo operan limpiamente entre si. Adicionalmente, el diseño de una gran cantidad de herramientas del sistema operativo fue realizado para leer una porción de la entrada (por ejemplo, una línea de un archivo de texto) y procesarla, sin tener que cargar todo el archivo en memoria; eso hace, que se puedan procesar archivos con millones de registros sin problemas.

Bash es en si mismo tanto una shell de comandos como un lenguaje de programación para la automatización de procesos [#f4]_.  En el contexto de la ciencia de los datos resulta particularmente interesante, ya que:

* Permite la gestión de archivos planos de texto (creación, transformación y borrado) en el contexto de los procesos ETL (extracción, transformación y carga de datos).
* Permite la creación de herramientas  ETL escritas en lenguajes de programación de alto nivel (como Perl, Python, Ruby o R) que pueden integrarse directamente con otras herramientas del sistema operativo.
* Sistemas como Hadoop corren sobre Unix, y por tanto, el usuario requiere unos conocimientos mínimos sobre Bash para interactuar con estos sistemas.
* La línea de comandos es fácilmente programable y permite hacer tareas complejas usando comandos simples; en oposición, programas equivalentes en los lenguajes R o Python que hagan las mismas tareas podrían tener muchas más líneas de código.

Para ejemplificar el tipo de tareas que se pueden realizar fácilmente en la línea de comandos, suponga que tiene un archivo separado por comas (CSV) llamado datos.csv con dos millones de filas cuya cabecera se presenta a continuación: ::

    fecha,placa,ciudad,valor
    2015-05-03,IAY184,medellin,20040
    2016-01-03,TYE765,medellin,75645
    2014-03-25,RET145,cali,472277
    2014-03-23,IAY184,cali,28848
    2013-05-23,UYA435,cali,284663
    2010-02-26,TTE234,manizales,3456

Entre las tareas comunes de extracción, transformación y carga de datos que pueden realizarse se encuentran las siguientes:

* Contar la cantidad de registros por año.
* Calcular los subtotales por año y mes de la columna valor.
* Extraer los registros para una determinada ciudad a otro archivo.
* Generar una lista ordenada de las ciudades que aparecen en el archivo.
* Determinar entre que fechas se encuentra la muestra.
* Ordenar el archivo por fecha.
* (y muchas otras preguntas posibles)

Estas tareas son fácilmente realizables usando la línea de comandos de Linux. Por ejemplo, el comando::

    grep ^2015 datos.csv


permite imprimir en pantalla los registros del año 2015; para grabar los resultados en el archivo 2015.csv  solo es necesario modificar ligeramente el comando anterior: ::

    grep ^2015 datos.csv > 2015.csv

El objetivo de las Secciones 2 y 3 es presentar y ejemplificar los principales comandos del sistema operativo Unix para la transformación de archivos de texto y la automatización de estas tareas mediante el uso de scripts. Este documento difiere en gran medida de muchos otros textos sobre Bash en que está orientado a la transformación de datos, mientras que la gran cantidad de literatura existente se focaliza mayormente en tareas de gestión y administración del sistema operativo [#f6]_ [#f7]_.

Al finalizar este documento, el lector estará en capacidad de:

*	Visualizar una porción o el total de un archivo.
*	Renombrar, copiar y mover archivos.
*	Generar nuevos archivos a partir del contenido de otros archivos.
*	Escribir programas en Bash de complejidad baja y media.

**Recursos adicionales de aprendizaje**

  * `The Command Line Crash Course <http://cli.learncodethehardway.org/book/>`__.
  * `The Linux Command Line <http://linuxcommand.org/tlcl.php>`__ por William Shotts.
  * `Learn Enough Command Line to Be Dangerous <https://www.learnenough.com/command-line-tutorial#sec-grepping>`__    por Michael Hart.
  * `Data Science at the Command Line <http://datascienceatthecommandline.com>`__ por Jeroen Janssens.
  * `The Mac OS X Command Line: Unix Under the Hood      <http://www.wiley.com/WileyCDA/WileyTitle/productCd-0782143547.html>`__ por Kirk McElhearn


**Referencias**

.. [#f1] D. Cross. Data Munging with Perl. Maning Publications Co. 2001
.. [#f2] S. Redmond. Mastering QlikView. Packs Publishing, 2014.
.. [#f3] T. Meyr. Apple® Automator with AppleScript® Bible. Wiley Publishing, Inc., Indianapolis, Indiana, 2010.
.. [#f4] C. Albing, JP Vossen and C. Newham. Bash cookbook. O'Reilly, Media Inc. 2007.
.. [#f5] E. S. Raymond, The Art of Unix Programming. Addison-Wesley, 2004.
.. [#f6] K. McElhearn. The Mac OS X Command Line: Unix under the hood. Ibex, 2005.
.. [#f7] R. K. Michael. Mastering Unix Shell Scripting. Wiley, 2003.







