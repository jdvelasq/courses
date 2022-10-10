Analítica de Grandes Datos
=========================================================================================

.. raw:: html

   <hr style="height:2px;border-width:0;color:gray;background-color:gray">


El concepto de Big Data Analytics está asociado al uso de herramientas y tecnologías para realizar cómputos de alto desempeño sobre grandes volúmenes de datos, con el fin de poder derivar conocimiento que pueda ser utilizado en procesos de toma de decisiones en contextos empresariales y de negocios usando Aprendizaje Estadístico y Aprendizaje Automático. Los retos relacionados con este nuevo paradigma están relacionados con la realización de tareas que hoy se realizan comúnmente en analítica descriptiva/diagnóstica, productiva y prescriptiva, como la extracción, limpieza y transformación de datos, o el cómputo de estadísticos básicos, pero en ambientes computacionales con millones de datos para procesar; esto implica, que el uso de paradigmas tradicionales se hace imposible o impráctico debido a los altos tiempos de cómputo requeridos para procesar la información. 

En este curso se abordan los elementos más básicos y fundamentales en Big Data Analytics y se busca que el estudiante tenga una primera experiencia que le permita desarrollar conocimientos, destrezas y habilidades básicas para la manipulación y modelado de grandes volúmenes de datos para la toma de decisiones. El curso provee al estudiante de una experiencia práctica en el correcto uso de herramientas computacionales comúnmente utilizadas en la analítica y el Big Data. Entre los temas tratados se encuentran: el paradigma de Map/Reduce, que es la base de la computación en paralelo en Big Data, lenguajes de manipulación de datos como Apache Pig, bases de datos como Apache Hive, Apache AsterisDB, lenguajes de consulta directa sobre archivos como Apache Drill, y finalmente, Apache Spark. Este curso no pretende enseñar todo sobre cada una de las herramientas, pero busca una comprensión profunda de los conceptos detrás de las tecnologías y su uso en la solución de problemas reales. Al final de este curso, el estudiante pueda continuar su formación de forma autónoma.

Véase:  :ref:`info_general_cursos`

.. raw:: html

   <hr style="height:2px;border-width:0;color:gray;background-color:gray">


Programa Calendario
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Sesión 01 --- **2022-05-13**


    * Presentación del curso.

    **Uso del Terminal para el Procesamiento de Datos --- Parte 1**

        .. code:: bash

                docker run --rm -it \
                    --name ubuntu \
                    -v "$PWD":/workspace \
                    jdvelasq/ubuntu:20.04


        * :ref:`bash_1`

        * :ref:`bash_2`

        * :ref:`bash_3`


.. ......................................................................................

* Sesión 02 --- **2022-05-20**

    **Uso del Terminal para el Procesamiento de Datos --- Parte 2**

        * :ref:`bash_4`

        * :ref:`bash_5`

        * :ref:`csvkit`

        * :ref:`bash_6`

        * :ref:`bash_7`

        * `LAB --- Limpieza de archivos con sed <https://classroom.github.com/a/2pSb_67S>`_.

.. ......................................................................................

* Sesión 03 --- **2022-05-27**

    * :ref:`masive_datasets`
    
    **Apache Hadoop y Algoritmo Map/Reduce**

        .. code:: bash

                docker run --rm -it \
                    --name hadoop \
                    -p 50070:50070 \
                    -p 8088:8088 \
                    -p 8888:8888 \
                    -v "$PWD":/workspace \
                    jdvelasq/hadoop:2.10.1

        * :ref:`hadoop`

        * :ref:`mrjob`

        * :ref:`snakebite`

        * `LAB --- Algoritmo MapReduce en Python <https://classroom.github.com/a/C1Ti2RTw>`_.

.. ......................................................................................

* Sesión 04 --- **2022-06-03**

    **Apache Zeppelin**

        .. code:: bash

                docker run --rm -it \
                    --name zeppelin \
                    -p 50070:50070 \
                    -p 8088:8088 \
                    -p 8888:8888 \
                    -p 8080:8080 \
                    -v "$PWD":/workspace  \
                    jdvelasq/zeppelin:0.10.1            


        * :ref:`zeppelin`


    
    **Maria DB**

        .. code:: bash

                docker run --rm -it \
                    --name mariadb \
                    -p 50070:50070 \
                    -p 8088:8088 \
                    -p 8888:8888 \
                    -v "$PWD":/workspace \
                    jdvelasq/mariadb:10.3.34

        .. toctree::
            :maxdepth: 1
            :glob:

            /notebooks/mariadb/1-*


    **Apache Sqoop**

        .. code:: bash

                docker run --rm -it \
                    --name sqoop \
                    -p 50070:50070 \
                    -p 8088:8088 \
                    -p 8888:8888 \
                    -v "$PWD":/workspace \
                    jdvelasq/sqoop:1.4.7            

        * :ref:`sqoop`


    **Apache Pig**

        .. code:: bash

                docker run --rm -it \
                    --name pig \
                    -p 50070:50070 \
                    -p 8088:8088 \
                    -p 8888:8888 \
                    -v "$PWD":/workspace  \
                    jdvelasq/pig:0.17.0


        * :ref:`pig`

        * `LAB --- Apache Pig <https://classroom.github.com/a/EjViQnqQ>`_.

.. ......................................................................................

* Sesión 05 --- **2022-06-10**

    **Apache Drill**

        .. code:: bash

            docker run --rm -it \
                --name drill \
                -p 31010:31010 \
                -p 50070:50070 \
                -p 8047:8047 \
                -p 8088:8088 \
                -p 8888:8888 \
                -v "$PWD":/workspace \
                jdvelasq/drill:1.19.0


        * :ref:`drill`


    **Apache Druid**

        .. code:: bash

                docker run --rm -it \
                    --name druid \
                    -p 50070:50070 \
                    -p 8088:8088 \
                    -p 8888:8888 \
                    -p 9999:9999 \
                    -v "$PWD":/workspace \
                    jdvelasq/druid:0.22.1


        * :ref:`druid`


    **Apache Hive**

        .. code:: bash

                docker run --rm -it \
                    -v "$PWD":/workspace \
                    --name hive \
                    -p 50070:50070 \
                    -p 8088:8088 \
                    -p 8888:8888 \
                    jdvelasq/hive:2.3.9            


        * :ref:`hive`

        * `LAB --- Apache Hive <https://classroom.github.com/a/XMSXISr5>`_.

.. ......................................................................................

* Sesión 06 --- 2022-06-17

    **Apache HBase**

        .. code:: bash

                docker run --rm -it \
                    --name hbase \
                    -p 16010:16010 \
                    -p 50070:50070 \
                    -p 8088:8088 \
                    -p 8888:8888 \
                    -v "$PWD":/workspace \
                    jdvelasq/hbase:2.3.0

        * :ref:`hbase`

    **Apache Phoenix**

        .. code:: bash

                docker run --rm -it \
                    --name phoenix \
                    -p 16010:16010 \
                    -p 50070:50070 \
                    -p 8088:8088 \
                    -p 8888:8888 \
                    -v "$PWD":/workspace \
                    jdvelasq/phoenix:5.1.2


        * :ref:`phoenix`


    **Apache Spark RDD**

        .. code:: bash

                docker run --rm -it \
                    --name spark \
                    -p 4040:4040 \
                    -p 50070:50070 \
                    -p 8088:8088 \
                    -p 8888:8888 \
                    -v "$PWD":/workspace \
                    jdvelasq/spark:3.1.3

        * :ref:`pyspark_intro`

    **Aprendizaje de Máquinas en Apache Spark RDD**

        * :ref:`pyspark_mllib_rdd`

.. ......................................................................................

* Sesión 07 --- **2022-06-24**

    **Apache Spark QL**

        * :ref:`pyspark_ql`

    **Aprendizaje de Máquinas con Apache Spark ML**

        * :ref:`pyspark_mllib_1`

        * :ref:`pyspark_mllib_2`

        * :ref:`pyspark_mllib_3`

        * :ref:`pyspark_streaming`


.. ......................................................................................
..
..     #####  #####
..     #   #  #   #
..     #   #  #####
..     #   #  #   #
..     #####  #####

.. raw:: html

   <hr style="height:6px;border-width:0;color:gray;background-color:gray">

* Sesión 08 --- **2022-07-01**

    * TensorFlow

