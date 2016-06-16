Wagtail Facelift
================

Provides some visual enhancements to Streamfield components.

Pure CSS overrides, there's no extra configuration.

Installation.
-------------

::
    pip install wagtailfacelift


Add the application to your installed apps:

::
    INSTALLED_APPS = [
        'wagtail',
        'wagtailfacelift'
    ]


---

Extra theming
-------------

`.multi-field-dark`

Apply this class to your widget for a subtle background shift, eg:

::
    MultiFieldPanel([
        StreamFieldPanel('heroes'),
        ],
        heading="Homepage Heroes",
        classname="collapsible collapsed multi-field-dark"
    )


Enjoy!

