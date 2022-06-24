Analítica de Grandes Datos
=========================================================================================


.. .....................................................................................
..
..     #####  ###
..     #   #    #
..     #   #    #
..     #   #    #
..     #####  #####

.. raw:: html

   <hr style="height:6px;border-width:0;color:gray;background-color:gray">

Sesión 01 --- 2022-05-13
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    **Introducción al curso**

        .. toctree::
            :maxdepth: 1
            :glob:

            course-info


    **Uso del Terminal para el Procesamiento de Datos --- Parte 1**

        .. code:: bash

                docker run --rm -it \
                    --name ubuntu \
                    -v "$PWD":/workspace \
                    jdvelasq/ubuntu:20.04


        .. toctree::
            :maxdepth: 1
            :glob:

            /notebooks/bash/1-*


        .. toctree::
            :maxdepth: 1
            :glob:

            /notebooks/bash/2-*


        .. toctree::
            :maxdepth: 1
            :glob:

            /notebooks/bash/3-*


.. ......................................................................................
..
..     #####  #####
..     #   #      #
..     #   #  #####
..     #   #  #
..     #####  #####

.. raw:: html

   <hr style="height:6px;border-width:0;color:gray;background-color:gray">

Sesión 02 --- 2022-05-20
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



    **Uso del Terminal para el Procesamiento de Datos --- Parte 2**

        .. toctree::
            :maxdepth: 1
            :glob:

            /notebooks/bash/4-*

        .. toctree::
            :maxdepth: 1
            :glob:

            /notebooks/bash/5-*

        .. toctree::
            :maxdepth: 1
            :glob:

            /notebooks/csvkit/1-*

        .. toctree::
            :maxdepth: 1
            :glob:

            /notebooks/bash/6-*

        .. toctree::
            :maxdepth: 1
            :glob:

            /notebooks/bash/7-*


    `LAB --- Limpieza de archivos con sed <https://classroom.github.com/a/2pSb_67S>`_.

.. ......................................................................................
..
..     #####  #####
..     #   #      #
..     #   #   ####
..     #   #      #
..     #####  #####

.. raw:: html

   <hr style="height:6px;border-width:0;color:gray;background-color:gray">

Sesión 03 --- 2022-05-27
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    **Manejo de datasets masivos en Python**

        .. toctree::
            :maxdepth: 1
            :glob:

            /notebooks/masive_datasets/1-*

    
    **Apache Hadoop y Algoritmo Map/Reduce**

        .. code:: bash

                docker run --rm -it \
                    --name hadoop \
                    -p 50070:50070 \
                    -p 8088:8088 \
                    -p 8888:8888 \
                    -v "$PWD":/workspace \
                    jdvelasq/hadoop:2.10.1



        .. toctree::
            :maxdepth: 1
            :glob:

            /notebooks/hadoop/1-*

        .. toctree::
            :maxdepth: 1
            :glob:

            /notebooks/mrjob/1-*


        .. toctree::
            :maxdepth: 1
            :glob:

            /notebooks/snakebite/1-*


    `LAB --- Algoritmo MapReduce en Python <https://classroom.github.com/a/C1Ti2RTw>`_.

.. ......................................................................................
..
..     #####  #   #
..     #   #  #   #
..     #   #  #####
..     #   #      #
..     #####      #

.. raw:: html

   <hr style="height:6px;border-width:0;color:gray;background-color:gray">

Sesión 04 --- 2022-06-03
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

        .. toctree::
            :maxdepth: 1
            :glob:

            /notebooks/zeppelin/1-*


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

        .. toctree::
            :maxdepth: 1
            :glob:

            /notebooks/sqoop/1-*


    **Apache Pig**

        .. code:: bash

                docker run --rm -it \
                    --name pig \
                    -p 50070:50070 \
                    -p 8088:8088 \
                    -p 8888:8888 \
                    -v "$PWD":/workspace  \
                    jdvelasq/pig:0.17.0


        .. toctree::
            :maxdepth: 1
            :glob:

            /notebooks/pig/1-*


        .. toctree::
            :maxdepth: 1
            :glob:


            /notebooks/pig/2-*


    `LAB --- Apache Pig <https://classroom.github.com/a/EjViQnqQ>`_.

.. ......................................................................................
..
..     #####  #####
..     #   #  #   
..     #   #  #####
..     #   #      #
..     #####  #####

.. raw:: html

   <hr style="height:6px;border-width:0;color:gray;background-color:gray">

Sesión 05 --- 2022-06-10
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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


        .. toctree::
            :maxdepth: 1
            :glob:

            /notebooks/drill/1-*



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

        .. toctree::
            :maxdepth: 1
            :glob:

            /notebooks/druid/1-*



    **Apache Hive**

        .. code:: bash

                docker run --rm -it \
                    -v "$PWD":/workspace \
                    --name hive \
                    -p 50070:50070 \
                    -p 8088:8088 \
                    -p 8888:8888 \
                    jdvelasq/hive:2.3.9            


        .. toctree::
            :maxdepth: 1
            :glob:

            /notebooks/hive/1-*


        .. toctree::
            :maxdepth: 1
            :glob:

            /notebooks/hive/2-*        


    `LAB --- Apache Hive <https://classroom.github.com/a/XMSXISr5>`_.

.. ......................................................................................
..
..     #####  #####
..     #   #  #   
..     #   #  #####
..     #   #  #   #
..     #####  #####

.. raw:: html

   <hr style="height:6px;border-width:0;color:gray;background-color:gray">

Sesión 06 --- 2022-06-17
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


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

        .. toctree::
            :maxdepth: 1
            :glob:

            /notebooks/hbase/1-*

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

        .. toctree::
            :maxdepth: 1
            :glob:

            /notebooks/phoenix/1-*



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


        .. toctree::
            :maxdepth: 1
            :glob:

            /notebooks/pyspark/1-*

    **Aprendizaje de Máquinas en Apache Spark RDD**

        .. toctree::
            :maxdepth: 1
            :glob:
    
            /notebooks/pyspark/2-*

.. ......................................................................................
..
..     #####  #####
..     #   #      #   
..     #   #      #
..     #   #      #
..     #####      #

.. raw:: html

   <hr style="height:6px;border-width:0;color:gray;background-color:gray">

Sesión 07 --- 2022-06-24
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^




    **Apache Spark QL**

        .. toctree::
            :maxdepth: 1
            :glob:

            /notebooks/pyspark/3-*



    **Aprendizaje de Máquinas con Apache Spark ML**

        .. toctree::
            :maxdepth: 1
            :glob:

            /notebooks/pyspark/4-*


        .. toctree::
            :maxdepth: 1
            :glob:

            /notebooks/pyspark/5-*


        .. toctree::
            :maxdepth: 1
            :glob:

            /notebooks/pyspark/6-*


    **Apache Spark Streaming**

        .. toctree::
            :maxdepth: 1
            :glob:

            /notebooks/pyspark/7-*




.. ......................................................................................
..
..     #####  #####
..     #   #  #   #
..     #   #  #####
..     #   #  #   #
..     #####  #####

.. raw:: html

   <hr style="height:6px;border-width:0;color:gray;background-color:gray">

Sesión 08 --- 2022-07-01
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


            







    **2:18:10**


    **Redes Neuronales Artificiales con Keras y TensorFlow**

        **Introducción a Keras --- 35:36 min**

            .. toctree::
                :maxdepth: 1
                :glob:

                /notebooks/tensorflow_01_quickstart/1-*


        **Fundamentos de ML con Keras --- 90:54 min**

            .. toctree::
                :maxdepth: 1
                :glob:

                /notebooks/tensorflow_02_ml_basics_with_keras/1-*




    **Redes Neuronales Artificiales con Keras y TensorFlow**

        **Fundamentos de ML con Keras --- 2:18:10**

            .. toctree::
                :maxdepth: 1
                :glob:

                /notebooks/tensorflow_02_ml_basics_with_keras/2-*




    * **Evaluación y Cierre**



**Apache Zookeeper**

        .. code:: bash

            docker run --rm -it \
                --name zookeeper \
                -p 50070:50070 \
                -p 8088:8088 \
                -p 8888:8888 \
                -v "$PWD":/workspace  \
                jdvelasq/zookeeper:3.7.1


        .. toctree::
            :maxdepth: 1
            :glob:

            /notebooks/zookeeper/1-*