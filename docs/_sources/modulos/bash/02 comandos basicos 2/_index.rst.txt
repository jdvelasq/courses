.. _terminal_de_linux_Ep_02_comandos_basicos_2:

Terminal de Linux Ep 02: Comandos básicos (2)
---------------------------------------------------------------------

    .. code:: bash

            docker run --rm -it \
                --name ubuntu \
                -v "$PWD":/workspace \
                jdvelasq/ubuntu:20.04

    .. toctree::
        :titlesonly:
        :glob:

        notebooks/*
