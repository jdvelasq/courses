.. _bigdata_Ep_12_phoenix:

Big Data Ep 12: Apache Phoenix
---------------------------------------------------------------------

    .. code:: bash

            docker run --rm -it \
                --name phoenix \
                -p 16010:16010 \
                -p 50070:50070 \
                -p 8088:8088 \
                -p 8888:8888 \
                -v "$PWD":/workspace \
                jdvelasq/phoenix:5.1.2
      

    .. toctree::
        :titlesonly:
        :glob:

        notebooks/*