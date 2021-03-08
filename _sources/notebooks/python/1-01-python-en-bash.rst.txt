Creación y ejecución de programas de Python
=========================================================================================

* *30 min* | Última modificación: Diciembre 19, 2019.



Parte 1. Uso interactivo en Terminal
-----------------------------------------------------------------------------------------

  **Paso 1** 
  
    En Terminal, abra el interprete de Python con el comando:
    
    .. code::

        $ python3
    
    
    La salida será similar a la siguiente:

    .. code::

        Python 3.6.9 (default, Nov  7 2019, 10:44:02) 
        [GCC 8.3.0] on linux
        Type "help", "copyright", "credits" or "license" for more information.
        >>> 


  **Paso 2**

    En el prompt de Python (símbolo `>>>`) digite:
    
    .. code::

        >>> print('hola mundo')
        hola
    
    
  **Paso3**
  
    Salga del interprete de Python con
    
    .. code::

        >>> exit()

Parte 2. Uso interactivo de IPython
-----------------------------------------------------------------------------------------

  **Paso 1** 
  
    En Terminal, abra el interprete de Python con el comando:
    
    .. code::

        $ ipython
    
    
    La salida será similar a la siguiente:

    .. code::

        Python 3.6.9 (default, Nov  7 2019, 10:44:02) 
        Type 'copyright', 'credits' or 'license' for more information
        IPython 7.10.2 -- An enhanced Interactive Python. Type '?' for help.

        In [1]:    


  **Paso 2**

    En el prompt de IPython (símbolo `In [#]:`) digite:
    
    .. code::

        In [1]: print('hola mundo')
        hola
    
    
  **Paso3**
  
    Salga del interprete de IPython con
    
    .. code::

        >>> exit()

    
Parte 3. Creación y ejecución de archivos con código
-----------------------------------------------------------------------------------------

    **Paso 1**

      Use `nano` para crear un archivo llamado `hola.py`. Agregue el siguiente código al 
      archivo:

    .. code::

        print('hola mundo')


    **Paso 2**

      Cierre el editor de texto.

    **Paso 3**

      Ejecute `hola.py` con:

    .. code::

        $ python3 hola.py
        hola mundo
    
    


  
