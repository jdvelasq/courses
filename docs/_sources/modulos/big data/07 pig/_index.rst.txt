.. _bigdata_Ep_07_pig:

Big Data Ep 07: Gestión de datos con Apache Pig
---------------------------------------------------------------------

    .. code:: bash

            docker run --rm -it \
                --name pig \
                -p 50070:50070 \
                -p 8088:8088 \
                -p 8888:8888 \
                -v "$PWD":/workspace  \
                jdvelasq/pig:0.17.0          

    .. toctree::
        :titlesonly:
        :glob:

        notebooks/*


