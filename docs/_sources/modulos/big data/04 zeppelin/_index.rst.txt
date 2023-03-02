.. _bigdata_Ep_04_zeppelin:

Big Data Ep 04: Procesamiento de datos en Python y Bash con Apache Zeppelin
-------------------------------------------------------------------------------

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
        :titlesonly:
        :glob:

        notebooks/*

