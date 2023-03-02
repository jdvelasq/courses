.. _terminal_de_linux_Ep_01_comandos_basicos_1:

Terminal de Linux Ep 01: Comandos básicos (1)
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
