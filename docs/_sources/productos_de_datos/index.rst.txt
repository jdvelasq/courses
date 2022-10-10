Productos de Datos
=========================================================================================





**Nota** Incluir https://github.com/evidentlyai/evidently

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

   **Presentación del curso**

        .. toctree::
            :maxdepth: 1
            :glob:

            course-info



   **Simulación de las etapas de evolución de un sistema de PQRS en una empresa** --- Parte 1

      .. code:: bash

               docker run --rm -it \
                  --name ubuntu \
                  -v "$PWD":/workspace \
                  jdvelasq/ubuntu:20.04
    

      .. toctree::
            :maxdepth: 1
            :glob:

            /notebooks/dataops_pqrs/1-*


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

   **Simulación de las etapas de evolución de un sistema de PQRS en una empresa** --- Parte 2.

      .. toctree::
            :maxdepth: 1
            :glob:

            /notebooks/dataops_pqrs/2-*




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

   **MLOps: Manejo del ciclo de vida de ML con MLflow --- Parte 1**


      * `Intrdoucción a MLOps --07-- <https://jdvelasq.github.io/mlops_01_intro//>`_ 


      **Introducción a MLFlow**

         .. code:: bash

               docker run --rm -it \
                  --name sklearn \
                  -p 5001:5000 \
                  -p 8082:8082 \
                  -p 8888:8888 \
                  -v "$PWD":/workspace \
                  jdvelasq/sklearn:1.0.2


         .. toctree::
               :maxdepth: 1
               :glob:

               /notebooks/mlflow/1-*


      **Model Tracking**

         .. toctree::
               :maxdepth: 1
               :glob:

               /notebooks/mlflow/2-01*
         
         
         .. code:: bash

               docker run --rm -it \
                  -v "$PWD":/workspace \
                  --name tensorflow \
                  -p 5001:5000 \
                  -p 6006:6006 \
                  -p 8888:8888 \
                  jdvelasq/tensorflow:2.9.1

         .. toctree::
               :maxdepth: 1
               :glob:

               /notebooks/mlflow/2-02*


         .. code:: bash

               docker run --rm -it \
                  --name spark \
                  -p 4040:4040 \
                  -p 5001:5000 \    
                  -p 50070:50070 \
                  -p 8088:8088 \
                  -p 8888:8888 \
                  -v "$PWD":/workspace \
                  jdvelasq/spark:3.1.3

         .. toctree::
               :maxdepth: 1
               :glob:

               /notebooks/mlflow/2-03*


         .. toctree::
               :maxdepth: 1
               :glob:

               /notebooks/mlflow/2-04*



      **Projects**

         .. toctree::
               :maxdepth: 1
               :glob:

               /notebooks/mlflow/3-*


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

   **MLOps: Manejo del ciclo de vida de ML con MLflow --- Parte 2**

      **Models**

         .. toctree::
               :maxdepth: 1
               :glob:

               /notebooks/mlflow/4-*


      **Registry**

         .. toctree::
               :maxdepth: 1
               :glob:

               /notebooks/mlflow/5-*


   **MLOps: Despliegue de modelos de ML y dashboards en Python**


         .. toctree::
               :maxdepth: 1
               :glob:

               /notebooks/html/1-*







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

   **MLOps: Despliegue de modelos de ML y dashboards en Python**

         .. toctree::
               :maxdepth: 1
               :glob:

               /notebooks/flask/1-*


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


   **DataOps: Introducción**


      * `El problema con Data Analytics --10-- <https://jdvelasq.github.io/dataops_01_problem//>`_ 

      * `Qué es DataOps? --20-- <https://jdvelasq.github.io/dataops_02_what_is_dataops/>`_ 


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



   **DataOps: Paso 0.--- Escriba código de nivel industrial**


      **Revisión de conceptos de programación en Python.**

         .. toctree::
               :maxdepth: 1
               :glob:

               /notebooks/the_python_tutorial_06_modules/1-*


         .. toctree::
               :maxdepth: 1
               :glob:

               /notebooks/the_python_tutorial_08_errors_and_exceptions/1-*


         .. toctree::
               :maxdepth: 1
               :glob:

               /notebooks/the_python_tutorial_09_clases/1-*


         .. toctree::
               :maxdepth: 1
               :glob:


               /notebooks/the_python_tutorial_10_brief_tour_of_the_standard_library/1-04*


         .. toctree::
               :maxdepth: 1
               :glob:

               /notebooks/the_python_tutorial_10_brief_tour_of_the_standard_library/1-07*
               /notebooks/the_python_tutorial_10_brief_tour_of_the_standard_library/1-08*
               /notebooks/the_python_tutorial_10_brief_tour_of_the_standard_library/1-09*
               /notebooks/the_python_tutorial_10_brief_tour_of_the_standard_library/1-10*
               /notebooks/the_python_tutorial_10_brief_tour_of_the_standard_library/1-11*
               /notebooks/the_python_tutorial_10_brief_tour_of_the_standard_library/1-12*


         .. toctree::
               :maxdepth: 1
               :glob:

               /notebooks/the_python_tutorial_10_brief_tour_of_the_standard_library/1-14*


      **Código Limpio**

         .. toctree::
               :maxdepth: 1
               :glob:

               /notebooks/clean_code/1-*





   **DataOps: Paso 1.--- Adicione tests de lógica y datos**


      * **Escriba tests de lógica de negocio**

         .. toctree::
               :maxdepth: 1
               :glob:

               /notebooks/doctest/1-*
               /notebooks/unittest/1-*
               /notebooks/pytest/1-*


      * **Genere ddatos para sus tests de lógica de negocio**

         .. toctree::
               :maxdepth: 1
               :glob:

               /notebooks/faker/1-*


      * **Escriba tests de datos con datatest**

         .. toctree::
            :maxdepth: 1
            :glob:

            /notebooks/datatest/1-*

      * **Escriba tests de datos con Great Expectations (PENDIENTE)**      

         .. toctree::
            :maxdepth: 1
            :glob:

            /notebooks/great_expectations/1-*





   **DataOps: Paso 1.--- Adicione tests de lógica y datos (Continuación)**

         * **Orqueste sus pipelines con Luigi**

            .. toctree::
               :maxdepth: 1
               :glob:

               /notebooks/luigi/1-*


         * **Orqueste pipelines con Apache Airflow** (PENDIENTE)


   **DataOps: Paso 2.--- Use un sistema de control de versiones**

      * **Realice el control de cambios de código con Git**

         .. toctree::
               :maxdepth: 1
               :glob:

               /notebooks/git/1-*


      * **Realice control de versiones de datos con DVC**
      
         .. toctree::
               :maxdepth: 1
               :glob:

               /notebooks/dvc/1-*


   **DataOps: Paso 3.--- Ramifique y fusione**

      * **Gestione sus ramas de testing y development con Git**

         .. toctree::
               :maxdepth: 1
               :glob:

               /notebooks/git/2-*


      *  **Gestione su codebase con GitHub**

            .. toctree::
                  :maxdepth: 1
                  :glob:

                  /notebooks/github/1-*


            .. toctree::
                  :maxdepth: 1
                  :glob:

                  /notebooks/github/5-*








   **DataOps: Paso 4.--- Use múltiples ambientes**

      * **Gestione ambientes locales de desarrollo con ambientes virtuales**

         .. toctree::
               :maxdepth: 1
               :glob:

               /notebooks/the_python_tutorial_12_virtual_environments_and_packages/1-*

      * **Cree máquinas virtuales locales con Vagrant**
      
         .. toctree::
               :maxdepth: 1
               :glob:

               /notebooks/vagrant/1-*

      * **Comparta ambientes complejos de desarrollo con contenedores**

         * Contenedores de desarrollo en VS Code:  https://code.visualstudio.com/docs/remote/containers


   **DataOps: Paso 5.--- Reuse y contenerize el código**

      * **Desarrolle y comparta paquetes en Python**

         * https://github.com/jdvelasq/package_demo


      * **Contenerize su código con Docker**

         .. toctree::
            :maxdepth: 1
            :glob:

            /notebooks/docker/1-*
 
         * Apps de ML en Docker: https://github.com/jdvelasq/iris-app-in-docker

         * Jupyter Lab in Docker:  https://github.com/jdvelasq/jupyter_in_docker

            






   **DataOps: Paso 6.--- Parametrice el procesamiento**

      * **Parametrice su procesamiento usando archivos de configuración**

         .. toctree::
               :maxdepth: 1
               :glob:

               /notebooks/config_files/1-*


         .. toctree::
               :maxdepth: 1
               :glob:

               /notebooks/the_python_tutorial_10_brief_tour_of_the_standard_library/1-13*
               

   **DataOps: Paso 7.--- Trabaje sin miedo o heroísmo**

      Revisión de conceptos


   **DataOps: Fundamentación filosófica**
   

      * `DataOps para el Chief Data Officer --12-- <https://jdvelasq.github.io/dataops_03_for_the_chief_data_officer/>`_    

      * `DataOps para el Data Engineer y el Data Scientist --13-- <https://jdvelasq.github.io/dataops_04_for_the_data_scientist/>`_ 

      * `DataOps para calidad de datos --06-- <https://jdvelasq.github.io/dataops_05_for_data_quality/>`_ 

      * `Estructura organizacional para DataOps --09-- <https://jdvelasq.github.io/dataops_06_organizing_for_dataops/>`_    



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

   **DataOps: Fundamentación filosófica**

      * `Estrategia de datos --11-- <https://jdvelasq.github.io/dataops_07_data_strategy/>`_    

      * `Lean thinking --12-- <https://jdvelasq.github.io/dataops_08_lean_thinking/>`_ 

      * `Agile Collaboration --15-- <https://jdvelasq.github.io/dataops_09_agile_collaboration/>`_ 




























