.. _bigdata_Ep_01_hadoop_y_mapreduce:

Big Data Ep 01: Apache Hadoop y algoritmo MapReduce
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

