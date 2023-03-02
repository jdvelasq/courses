.. _bigdata_Ep_05_mariadb:

Big Data Ep 05: Maria DB
---------------------------------------------------------------------

    .. code:: bash

            docker run --rm -it \
                --name mariadb \
                -p 50070:50070 \
                -p 8088:8088 \
                -p 8888:8888 \
                -v "$PWD":/workspace \
                jdvelasq/mariadb:10.3.34

    .. toctree::
        :titlesonly:
        :glob:

        notebooks/*


