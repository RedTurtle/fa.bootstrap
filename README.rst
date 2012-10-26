fa.bootstrap
============

Introduction
------------

This library packages `twitter bootstrap`_ for `pyramid_formalchemy`_ using `js.bootstrap`_.

.. _`pyramid_formalchemy`: http://docs.formalchemy.org/pyramid_formalchemy/
.. _`twitter bootstrap`: http://twitter.github.com/bootstrap/
.. _`js.bootstrap`: https://github.com/RedTurtle/js.bootstrap


It's right now in early development stage so you should know what you are doing. 
However most of the `pyramid_formalchemy`_ views/functionalites should be properly wrap 
with `js.bootstrap`_.

What you can get is:


.. image:: https://github.com/RedTurtle/fa.bootstrap/raw/master/docs/Screenshot01.png

.. image:: https://github.com/RedTurtle/fa.bootstrap/raw/master/docs/Screenshot02.png

.. image:: https://github.com/RedTurtle/fa.bootstrap/raw/master/docs/Screenshot03.png

.. image:: https://github.com/RedTurtle/fa.bootstrap/raw/master/docs/Screenshot04.png

.. image:: https://github.com/RedTurtle/fa.bootstrap/raw/master/docs/Screenshot05.png

.. image:: https://github.com/RedTurtle/fa.bootstrap/raw/master/docs/Screenshot06.png


Installation
------------

fa.bootstrap also provides a paster template. It can be used to
to create a new project. If you create a new project, you must first install 
fa.bootstrap in your python environment, either with pip::

  $ pip install fa.bootstrap

or with easy_install::

    $ easy_install fa.bootstrap

Then you should be able to run::

  $ paster create -t pyramid_fa_bootstrap myapp

and start your application by::

  $ cd myapp
  $ python setup.py develop
  $ paster serve development.ini


Contact
-------

.. image:: http://www.slowfoodbologna.it/redturtle_logo.png

* | Andrew Mleczko <``andrew.mleczko at redturtle.net``>
  | **RedTurtle Technology**, http://www.redturtle.net/
