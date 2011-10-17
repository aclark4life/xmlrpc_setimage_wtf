

Introduction
============

This repository showcases a bad interaction between Zope2's XML-RPC support and ATImage's setImage mutator.


Details
=======

``wtf.py`` contains code to create a *Document*, *Folder*, and *Image*. The Document and Folder code works fine, the Image code fails with a 500 status code (and no traceback).
