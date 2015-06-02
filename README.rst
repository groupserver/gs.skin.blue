=================
``gs.skin.blue``
=================
~~~~~~~~~~~~~~~~~~~~~~~~~~~
A blue skin for GroupServer
~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Author: `Michael JasonSmith`_
:Contact: Michael JasonSmith <mpj17@onlinegroups.net>
:Date: 2015-06-02
:Organization: `GroupServer.org`_
:Copyright: This document is licensed under a
  `Creative Commons Attribution-Share Alike 4.0 International License`_
  by `OnlineGroups.net`_.

..  _Creative Commons Attribution-Share Alike 4.0 International License:
    http://creativecommons.org/licenses/by-sa/4.0/

Introduction
============

This product provides a blue skin for GroupServer. The This skin
takes the typeset page, provided by ``gs.content.css``, and adds
colours_.

Colours
=======

The most prominent colour is **blue steel**, which is the
background of the page heading, and the text colour of all the
headers. The most *common* colour is **Bateman bold,** which is
the background of the page, followed by the body text, which is
**Garage patina** grey:

+-------------+-----+--------------------+-------------------------------------+
| Colour      | Eg. | Colour description | Use                                 |
+=============+=====+====================+=====================================+
| ``#fffffc`` | |0| | Bateman bond       |   ``<body>`` background             |
+-------------+-----+--------------------+-------------------------------------+
| ``#ffffff`` | |1| | White              |   ``<heading>`` title               |
|             |     |                    +-------------------------------------+
|             |     |                    |   Disabled ``<button>`` text        |
|             |     |                    +-------------------------------------+
|             |     |                    |   ``<button>`` borders              |
|             |     |                    +-------------------------------------+
|             |     |                    |   ``<button>`` text                 |
+-------------+-----+--------------------+-------------------------------------+
| ``#edf0f2`` | |2| | Shark underbelly   |   The ``<footer>`` background       |
+-------------+-----+--------------------+-------------------------------------+
| ``#d3d9df`` | |3| | Baskerville fog    |   ``<heading> <a>`` text            |
|             |     |                    +-------------------------------------+
|             |     |                    |   Borders between items             |
+-------------+-----+--------------------+-------------------------------------+
| ``#a6b3bf`` | |4| | Forlorn grey       |   Borders,                          |
|             |     |                    +-------------------------------------+
|             |     |                    |   Disabled ``<button>`` background  |
|             |     |                    +-------------------------------------+
|             |     |                    |   Muted ``<heading>`` text          |
+-------------+-----+--------------------+-------------------------------------+
| ``#556677`` | |5| | **Blue Steel**     |   ``<heading>`` background          |
|             |     |                    +-------------------------------------+
|             |     |                    |   ``<button>`` background           |
|             |     |                    +-------------------------------------+
|             |     |                    |   ``<h1>``, ``<h2>``, ``<h3>`` text |
|             |     |                    +-------------------------------------+
|             |     |                    |   ``<a>``                           |
+-------------+-----+--------------------+-------------------------------------+
| ``#506070`` | |6| | Thunderhead blue   |   ``<button>`` hover                |
+-------------+-----+--------------------+-------------------------------------+
| ``#3c4a5d`` | |7| | Abyss undershot    |   ``<heading> <button>`` background |
+-------------+-----+--------------------+-------------------------------------+
| ``#8c8d8d`` | |8| | Anarchy silence    |   Muted body text                   |
+-------------+-----+--------------------+-------------------------------------+
| ``#667366`` | |9| | Garage patina      |   ``<body>`` text                   |
+-------------+-----+--------------------+-------------------------------------+
| ``#3e4143`` | |a| | Umbra dreaming     |   ``<h4>`` text                     |
|             |     |                    +-------------------------------------+
|             |     |                    |   ``<strong>``                      |
+-------------+-----+--------------------+-------------------------------------+

.. |0| raw:: html

  <span style="background:#fffffc;">&#160;Sample&#160;</style>

.. |1| raw:: html

  <span style="background:#ffffff;">&#160;Sample&#160;</style>

.. |2| raw:: html

  <span style="background:#edf0f2;">&#160;Sample&#160;</style>

.. |3| raw:: html

  <span style="background:#d3d9df;">&#160;Sample&#160;</style>

.. |4| raw:: html

  <span style="background:#a6b3bf;">&#160;Sample&#160;</style>

.. |5| raw:: html

  <span style="background:#556677;color:white;">&#160;Sample&#160;</style>

.. |6| raw:: html

  <span style="background:#506070;color:white;">&#160;Sample&#160;</style>

.. |7| raw:: html

  <span style="background:#3c4a5d;color:white;">&#160;Sample&#160;</style>

.. |8| raw:: html

  <span style="background:#8c8d8d;">&#160;Sample&#160;</style>

.. |9| raw:: html

  <span style="background:#667366;color:white">&#160;Sample&#160;</style>

.. |a| raw:: html

  <span style="background:#3e4143;color:white;">&#160;Sample&#160;</style>

Authors
=======

Mike Harding from `Cactus Lab`_ performed the design work. The
CSS coding and egg creation, was by `Michael JasonSmith`_. Many
of the CSS classes are from `Twitter Bootstrap`_.

Resources
=========

- Code repository: https://github.com/groupserver/gs.skin.blue/
- Questions and comments to
  http://groupserver.org/groups/development
- Report bugs at https://redmine.iopen.net/projects/groupserver

.. _GroupServer: http://groupserver.org/
.. _GroupServer.org: http://groupserver.org/
.. _OnlineGroups.Net: https://onlinegroups.net/
.. _Michael JasonSmith: http://groupserver.org/p/mpj17/
.. _Creative Commons Attribution-Share Alike 3.0 New Zealand License:
   http://creativecommons.org/licenses/by-sa/3.0/nz/
.. _Dan: http://groupserver.org/p/danr/
.. _Cactus Lab: http://cactuslab.com/
.. _Twitter Bootstrap: http://getbootstrap.com/

..  LocalWords:  Bateman Baskerville
