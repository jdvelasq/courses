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


    **Uso del Terminal para el Procesamiento de Datos**

        .. note::

            Los participantes con sistema opeartivo *Windows* deben tener instalar Docker. El Terminal ya se 
            encuentra disponible en los sistemas operativos *Linux* y *Mac OS X*.

            Para tener acceso al Terminal (Windows) use el siguiente comando en el símbolo del sistema:

            .. code:: bash
            
                $ docker run --rm -it -v "$PWD":/workspace --name hadoop -p 8888:8888 -p 50070:50070 -p 8088:8088 jdvelasq/hadoop:2.8.5
            

            Para cerrar el Terminal use el siguiente comando:

            .. code:: bash
            
                $ exit
            


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

            /notebooks/bash/6-*


        .. toctree::
            :maxdepth: 1
            :glob:

            /notebooks/bash/7-*


        .. toctree::
            :maxdepth: 1
            :glob:

            /notebooks/bash/8-*


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

    **Manejo de datasets masivos en Python**

        .. toctree::
            :maxdepth: 1
            :glob:

            /notebooks/masive_datasets/1-*

    
    **Apache Hadoop (y Algoritmo MapReduce)**

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
..     #####  #####
..     #   #      #
..     #   #   ####
..     #   #      #
..     #####  #####

.. raw:: html

   <hr style="height:6px;border-width:0;color:gray;background-color:gray">

Sesión 03 --- 2022-05-27
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^




    **Limpieza de Datos con Apache Pig**


        .. toctree::
            :maxdepth: 1
            :glob:

            /notebooks/pig/1-*


        .. toctree::
            :maxdepth: 1
            :glob:


            /notebooks/pig/2-*

            


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

    

    **Gestión de Bases de Datos con Apache Hive**

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


    **Apache Spark RDD**
    

        **Programación funcional**

            .. toctree::
                :maxdepth: 1
                :glob:

                /notebooks/pyspark/1-*

        **Aprendizaje de Máquinas**

            .. toctree::
                :maxdepth: 1
                :glob:
        
                /notebooks/pyspark/2-*


    **Gestión de Bases de Datos con Apache Spark SQL**

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
    **2:18:10**

    **Redes Neuronales Artificiales con Keras y TensorFlow**

        **Fundamentos de ML con Keras --- 2:18:10**

            .. toctree::
                :maxdepth: 1
                :glob:

                /notebooks/tensorflow_02_ml_basics_with_keras/2-*




    * **Evaluación y Cierre**



