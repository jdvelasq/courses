.. _bigdata_Ep_10_hive:

Big Data Ep 10: Apache Hive
---------------------------------------------------------------------

    .. code:: bash

            docker run --rm -it \
                -v "$PWD":/workspace \
                --name hive \
                -p 50070:50070 \
                -p 8088:8088 \
                -p 8888:8888 \
                jdvelasq/hive:2.3.9            

      

    .. toctree::
        :titlesonly:
        :glob:

        notebooks/*