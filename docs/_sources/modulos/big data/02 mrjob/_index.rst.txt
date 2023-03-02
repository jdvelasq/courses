.. _bigdata_Ep_02_mrjob:

Big Data Ep 02: Orquestación de tareas con mrjob
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
