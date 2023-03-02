.. _bigdata_Ep_09_druid:

Big Data Ep 09: Apache Druid
---------------------------------------------------------------------

    .. code:: bash

            docker run --rm -it \
                --name druid \
                -p 50070:50070 \
                -p 8088:8088 \
                -p 8888:8888 \
                -p 9999:9999 \
                -v "$PWD":/workspace \
                jdvelasq/druid:0.22.1
      

    .. toctree::
        :titlesonly:
        :glob:

        notebooks/*
