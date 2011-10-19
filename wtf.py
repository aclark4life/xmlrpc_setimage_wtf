from OFS.Image import File

import sys
import traceback
import xmlrpclib

url = 'http://admin:admin@localhost:8080/Plone/subsites'
proxy = xmlrpclib.ServerProxy(url)

# create page
try:
    proxy.invokeFactory('Document', 'index.html')
except xmlrpclib.ProtocolError:
    print sys.exc_info()[1]
except xmlrpclib.Fault:
    print "The id is invalid - it is already in use."  # most likely
proxy = xmlrpclib.ServerProxy(url + '/index.html')
proxy.setText("""Professionally extend dynamic manufactured products""") 

# create folder
proxy = xmlrpclib.ServerProxy(url)  # reset
try:
    proxy.invokeFactory('Section', 'test-folder')
except xmlrpclib.ProtocolError:
    print sys.exc_info()[1]
except xmlrpclib.Fault:
    print "The id is invalid - it is already in use."  # most likely
proxy = xmlrpclib.ServerProxy(url + '/test-folder')
proxy.setTitle('Test folder')
proxy.setDescription('This is a test folder')

# create image
proxy = xmlrpclib.ServerProxy(url)  # reset
#wrappedData = xmlrpclib.Binary(open('screenshot.png').read())
filename = 'screenshot.png'
data = open(filename).read()
fileData = File(filename, filename, data, 'application/octet-stream')
fileData.filename = filename
wrappedData = fileData
try:
    proxy.invokeFactory('Image', 'screenshot.png')
except xmlrpclib.ProtocolError:
    print sys.exc_info()[1]
except xmlrpclib.Fault:
    print "The id is invalid - it is already in use."  # most likely
proxy = xmlrpclib.ServerProxy(url + '/screenshot.png')
proxy.setTitle('This is an image')
try:
    proxy.setImage(wrappedData)  # XXX this fails
except:
    print sys.exc_info()[1]
