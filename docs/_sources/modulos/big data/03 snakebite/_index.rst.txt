.. _bigdata_Ep_03_snakebite:

Big Data Ep 03: Acceso al HDFS con snakebite
---------------------------------------------------------------------

    .. code:: bash

            docker run --rm -it \
                --name hadoop \
                -p 50070:50070 \
                -p 8088:8088 \
                -p 8888:8888 \
                -v "$PWD":/workspace \
                jdvelasq/hadoop:2.10.1

    .. toctree::
        :titlesonly:
        :glob:

        notebooks/*

