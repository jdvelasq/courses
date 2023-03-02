.. _bigdata_Ep_11_hbase:

Big Data Ep 11: Apache HBase
---------------------------------------------------------------------

    .. code:: bash

            docker run --rm -it \
                --name hbase \
                -p 16010:16010 \
                -p 50070:50070 \
                -p 8088:8088 \
                -p 8888:8888 \
                -v "$PWD":/workspace \
                jdvelasq/hbase:2.3.0

      

    .. toctree::
        :titlesonly:
        :glob:

        notebooks/*