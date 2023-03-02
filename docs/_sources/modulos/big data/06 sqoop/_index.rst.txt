.. _bigdata_Ep_06_sqoop:

Big Data Ep 06: Intercambio de datos con Apache Sqoop
---------------------------------------------------------------------

    .. code:: bash

            docker run --rm -it \
                --name sqoop \
                -p 50070:50070 \
                -p 8088:8088 \
                -p 8888:8888 \
                -v "$PWD":/workspace \
                jdvelasq/sqoop:1.4.7            

    .. toctree::
        :titlesonly:
        :glob:

        notebooks/*

