.. _bigdata_Ep_08_drill:

Big Data Ep 08: Apache Drill
---------------------------------------------------------------------

    .. code:: bash

        docker run --rm -it \
            --name drill \
            -p 31010:31010 \
            -p 50070:50070 \
            -p 8047:8047 \
            -p 8088:8088 \
            -p 8888:8888 \
            -v "$PWD":/workspace \
            jdvelasq/drill:1.19.0
      

    .. toctree::
        :titlesonly:
        :glob:

        notebooks/*




