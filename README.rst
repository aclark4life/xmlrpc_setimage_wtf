
Introduction
============

This repository showcases a bad interaction between Zope2's XML-RPC support and ATImage's setImage mutator.


Installation
============

How to reproduce this error::

    $ git clone git://github.com/aclark4life/xmlrpc_setimage_wtf.git
    $ cd xmlrpc_setimage_wtf
    $ python2.6 bootstrap.py -d
    $ bin/buildout
    $ bin/plone start
    $ python wtf.py

You should see results like below.


Error details
=============

``wtf.py`` contains code to create a *Document*, *Folder*, and *Image*. The Document and Folder code works fine, the Image code fails with a 500 status code (and no traceback).


First run output
----------------

Looks like this::

    $ python wtf.py                       
    <ProtocolError for admin:admin@localhost:8080/Plone: 302 Moved Temporarily>
    <ProtocolError for admin:admin@localhost:8080/Plone: 302 Moved Temporarily>
    <ProtocolError for admin:admin@localhost:8080/Plone: 302 Moved Temporarily>
    <ProtocolError for admin:admin@localhost:8080/Plone/screenshot.png: 500 Internal Server Error>

Since the transaction works fine, I ignore the 302s. The 4th error is the problem.

Second and later run output
---------------------------

Looks like this::

    $ python wtf.py
    The id is invalid - it is already in use.
    The id is invalid - it is already in use.
    The id is invalid - it is already in use.
    <ProtocolError for admin:admin@localhost:8080/Plone/screenshot.png: 500 Internal Server Error>

We can ignore the "id in use" messages because they are expected. setImage continues to fail. Weird. And hard to get more info.

Fix
===

Fixed by adding an adapter to plone.app.blob:

- https://github.com/aclark4life/plone.app.blob/blob/master/src/plone/app/blob/adapters/xmlrpc.py
