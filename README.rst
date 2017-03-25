.. image:: https://img.shields.io/pypi/v/wagtailfacelift.svg
   :target: https://pypi.python.org/pypi/wagtailfacelift

Wagtail Facelift
================

    Drop-in CSS enhancements for Wagtail's Streamfield. Pure CSS overrides, there's no extra configuration.
    
Check out `Awesome Wagtail <https://github.com/springload/awesome-wagtail>`_ for more awesome packages and resources from the Wagtail community.

Installation
------------

.. code:: sh

    pip install wagtailfacelift


Add the application to your installed apps:

.. code:: python

    INSTALLED_APPS = [
        'wagtail',
        'wagtailfacelift'
    ]


---

Extra theming
-------------

`.multi-field-dark`

Apply this class to your widget for a subtle background shift, eg:

.. code:: python

    MultiFieldPanel([
        StreamFieldPanel('heroes'),
        ],
        heading="Homepage Heroes",
        classname="collapsible collapsed multi-field-dark"
    )


Enjoy!

