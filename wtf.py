import sys
import xmlrpclib
data = open('screenshot.png').read()
url = 'http://admin:admin@localhost:8080/Plone'
proxy = xmlrpclib.ServerProxy(url)

# create page
try:
    proxy.invokeFactory('Document', 'index.html')
except xmlrpclib.ProtocolError:
    print sys.exc_info()[1]
except xmlrpclib.Fault:
    print "The id is invalid - it is already in use."  # most likely
proxy = xmlrpclib.ServerProxy(url + '/index.html')
proxy.setText("""Professionally extend dynamic manufactured products vis-a-vis intermandated niche markets. Proactively leverage existing alternative process improvements and cutting-edge best practices. Efficiently monetize wireless internal or "organic" sources via process-centric potentialities. Quickly administrate strategic functionalities and focused expertise. Dramatically implement fully tested results and distributed human capital. Dynamically pontificate bricks-and-clicks systems with emerging ideas.""")

# create folder
proxy = xmlrpclib.ServerProxy(url)
try:
    proxy.invokeFactory('Folder', 'test-folder')
except xmlrpclib.ProtocolError:
    print sys.exc_info()[1]
except xmlrpclib.Fault:
    print "The id is invalid - it is already in use."  # most likely
proxy = xmlrpclib.ServerProxy(url + '/test-folder')
proxy.setTitle('Test folder')
proxy.setDescription('This is a test folder')

# create image


