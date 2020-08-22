153957 theme
============

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
   :target: https://github.com/153957/153957-theme/blob/master/LICENSE
.. image:: https://img.shields.io/github/workflow/status/153957/153957-theme/Build%20demo%20and%20check%20output
   :target: https://github.com/153957/153957-theme/actions

`View demo album here <https://153957.github.io/153957-theme/>`_


Photo gallery template
----------------------

Web photo gallery templates adapted to my personal preferences.


Usage
-----

This section describes how to install an use this theme.

Installation
~~~~~~~~~~~~

Install the ``153597-theme`` package::

    $ pip install 153957-theme


Configure
~~~~~~~~~

In ``sigal.conf.py`` configuration for an album the ``theme`` setting should be
a path to a theme directory. However, since this theme is provided as a Python
package its location might be harder to get. Two options are available for
configuration:

The theme can be configured as a plugin or you can get the path by importing
the package. By setting is as plugin the theme is automatically set.

Set ``theme`` to an empty string and add the theme and menu plugins::

    theme = ''
    plugins = ['153957_theme.theme', '153957_theme.full_menu', …]

The alternative::

    from 153957_theme import theme
    theme = theme.get_path()
    plugins = ['153957_theme.full_menu', …]


Sources
-------

Based on `sigal <http://sigal.saimon.org/>`_ version of Galleria theme, which is
distributed under the MIT License.

Theme based on `Galleria Classic <http://galleria.io/>`_, which is distributed under
the MIT License.
