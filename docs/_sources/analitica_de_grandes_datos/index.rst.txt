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

        .. note:: **Ubuntu 20.04 en Docker**

            * Windows / PowerShell: ::

                docker run --rm -it -v "${PWD}":/workspace  --name ubuntu jdvelasq/ubuntu:20.04
            

            * Windows / Símbolo del sistema: ::
                
                docker run --rm -it -v "%cd%":/workspace  --name ubuntu jdvelasq/ubuntu:20.04


            * Mac OS y **Linux: ::
 
                docker run --rm -it -v "$PWD":/workspace  --name ubuntu jdvelasq/ubuntu:20.04



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

    
    **Apache Hadoop (y Algoritmo MapReduce)**

        .. note:: **Apache Hadoop 2.10.1 en Docker**

            * Windows / PowerShell: ::

                docker run --rm -it -v "${PWD}":/workspace  --name hadoop -p 50070:50070 -p 8088:8088 -p 8888:8888 jdvelasq/hadoop:2.10.1
            

            * Windows / Símbolo del sistema: ::
                
                docker run --rm -it -v "%cd%":/workspace  --name hadoop -p 50070:50070 -p 8088:8088 -p 8888:8888 jdvelasq/hadoop:2.10.1


            * Mac OS y **Linux: ::
 
                docker run --rm -it -v "$PWD":/workspace  --name hadoop -p 50070:50070 -p 8088:8088 -p 8888:8888 jdvelasq/hadoop:2.10.1



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

    **Analíticas interactivas sobre grandes conjuntos de datos usando Apache Druid**

        .. toctree::
            :maxdepth: 1
            :glob:

            /notebooks/druid/1-*




    **Transferencia de datos con Apache Sqoop**

        .. toctree::
            :maxdepth: 1
            :glob:

            /notebooks/sqoop/1-*


    **Notebooks con Apache Zeppelin**


        .. note:: **Apache Zeppelin 0.10.1 en Docker**

            * Windows / PowerShell: ::

                docker run --rm -it -v "${PWD}":/workspace --name zeppelin -p 8080:8080 jdvelasq/zepppelin:0.10.1
            

            * Windows / Símbolo del sistema: ::
                
                docker run --rm -it -v "%cd%":/workspace  --name zeppelin -p 8080:8080 \ jdvelasq/zepppelin:0.10.1


            * Mac OS y **Linux: ::
 
                docker run --rm -it -v "$PWD":/workspace  --name zeppelin -p 8080:8080 jdvelasq/zepppelin:0.10.1

        .. toctree::
            :maxdepth: 1
            :glob:

            /notebooks/zeppelin/1-*



    **Gestión de Bases de Datos con Apache Hive**

        .. note:: **Apache Hive 2.3.9 en Docker**

            * Windows / PowerShell: ::

                docker run --rm -it -v "${PWD}":/workspace --name hive -p 50070:50070 -p 8088:8088 -p 8888:8888 jdvelasq/hive:2.3.9
    

            * Windows / Símbolo del sistema: ::
                
                docker run --rm -it -v "%cd%":/workspace  --name hive -p 50070:50070 -p 8088:8088 -p 8888:8888 jdvelasq/hive:2.3.9


            * Mac OS y **Linux: ::
 
                docker run --rm -it -v "$PWD":/workspace  --name hive -p 50070:50070 -p 8088:8088 -p 8888:8888 jdvelasq/hive:2.3.9


        .. toctree::
            :maxdepth: 1
            :glob:

            /notebooks/hive/1-*


        .. toctree::
            :maxdepth: 1
            :glob:

            /notebooks/hive/2-*        


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
            
    .. note:: **Apache Spark en Docker**

        * Windows / PowerShell: ::

            docker run --rm -it -v "${PWD}":/workspace --name spark -p 4040:4040 -p 5001:5000 -p 50070:50070 -p 8088:8088 -p 8888:8888 jdvelasq/spark:3.1.3
        

        * Windows / Símbolo del sistema: ::
            
            docker run --rm -it -v "%cd%":/workspace  --name spark -p 4040:4040 -p 5001:5000 -p 50070:50070 -p 8088:8088 -p 8888:8888 jdvelasq/spark:3.1.3


        * Mac OS y **Linux: ::

            docker run --rm -it -v "$PWD":/workspace --name spark -p 4040:4040 -p 5001:5000 -p 50070:50070 -p 8088:8088 -p 8888:8888 jdvelasq/spark:3.1.3


    **Programación funcional en Apache Spark RDD**

        .. toctree::
            :maxdepth: 1
            :glob:

            /notebooks/pyspark/1-*

    **Aprendizaje de Máquinas en Apache Spark RDD**

        .. toctree::
            :maxdepth: 1
            :glob:
    
            /notebooks/pyspark/2-*


    **Gestión de Bases de Datos con Apache Spark QL**

        .. toctree::
            :maxdepth: 1
            :glob:

            /notebooks/pyspark/3-*




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
..     #   #      #   
..     #   #      #
..     #   #      #
..     #####      #

.. raw:: html

   <hr style="height:6px;border-width:0;color:gray;background-color:gray">

Sesión 07 --- 2022-06-24
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


    **Redes Neuronales Artificiales con Keras y TensorFlow**

        **Fundamentos de ML con Keras --- 2:18:10**

            .. toctree::
                :maxdepth: 1
                :glob:

                /notebooks/tensorflow_02_ml_basics_with_keras/2-*




    * **Evaluación y Cierre**





.. raw:: html

   <hr style="height:6px;border-width:0;color:gray;background-color:gray">

Apache Pig
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    **Limpieza de Datos con Apache Pig** --- No se incluirá debido al decamimiento en su uso.


        .. note::
            
            * **Windows**:

                * PowerShell:

                .. code:: bash
                
                    docker run --rm -it -v "${PWD}":/workspace  --name pig -p 50070:50070 -p 8088:8088 -p 8888:8888 jdvelasq/pig:0.17.0
            

                * Símbolo del sistema:

                .. code:: bash
                
                    docker run --rm -it -v "%cd%":/workspace  --name pig -p 50070:50070 -p 8088:8088 -p 8888:8888 jdvelasq/pig:0.17.0


            * **Mac OS** y **Linux**:

                .. code:: bash
                
                    docker run --rm -it -v "$PWD":/workspace  --name pig -p 50070:50070 -p 8088:8088 -p 8888:8888 jdvelasq/pig:0.17.0


            Para cerrar el contendor use el siguiente comando:

            .. code:: bash
            
                exit


        .. toctree::
            :maxdepth: 1
            :glob:

            /notebooks/pig/1-*


        .. toctree::
            :maxdepth: 1
            :glob:


            /notebooks/pig/2-*