.. _mlops_Ep_02_model_tracking_en_mlflow:

MLOps Ep 02: Model tracking en MLflow
---------------------------------------------------------------------

    * Ejecución del contendor con sklearn:

        .. code:: bash

            docker run --rm -it \
                --name sklearn \
                -p 5001:5000 \
                -p 8082:8082 \
                -p 8888:8888 \
                -v "$PWD":/workspace \
                jdvelasq/sklearn:1.0.2

    * Ejecución del contendor con tensorflow:

        .. code:: bash

            docker run --rm -it \
                -v "$PWD":/workspace \
                --name tensorflow \
                -p 5001:5000 \
                -p 6006:6006 \
                -p 8888:8888 \
                jdvelasq/tensorflow:2.9.1

    * Ejecución del contendor con spark:

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
        :titlesonly:
        :glob:

        notebooks/*

