hr
==

CLI for update hr databatabase based on an input json file.

Preparing the Development
-------------------------

To help someone onboarding
List of things that people need to have
1. Ensure ``pip`` and ``pipenv`` are installed.
2. Clone repository: ``git clone git@github.com:raminderis/hr``
3. ``cd`` into the repository
4. Fetch development dependencies ``make install``
5. Activate virtualenv: ``pipenv shell``

Usage
-----

Pass in the full path of the json file, and optionally an export flag.

Example without the export flag:

::

    $ hr /path/to/the/inventory.json

Example w/ export flag

::

   $ hr --export /path/to/the/inventory.json

Running Tests
-------------

Run tests locally using ``make`` if virtualenv is active:

::

    $ make

If virtualenv is not active then use:

::

    $ pipenv run make
