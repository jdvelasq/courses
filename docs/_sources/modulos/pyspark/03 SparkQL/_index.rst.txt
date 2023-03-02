.. _pyspark_Ep_03_SparkQL:

DA con PySpark Ep 03: SparkQL
---------------------------------------------------------------------

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
        :titlesonly:
        :glob:

        notebooks/*

