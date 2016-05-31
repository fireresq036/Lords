# web-python-gae-simple

Python GAE Sample Application

# Developer Workspace
[![Contribute](http://beta.codenvy.com/factory/resources/codenvy-contribute.svg)](http://beta.codenvy.com/f?id=w8y6pvoqv145r3pc)

# Stack to use

FROM [codenvy/ubuntu_python:gae_python2.7](https://hub.docker.com/r/codenvy/ubuntu_python/)

# How to run

| #       | Description           | Command  |
| :------------- |:-------------| :-----|
| 1      | Run | `cd ${GAE} && ./dev_appserver.py 2>&1 --skip_sdk_update_check true --host=0.0.0.0 --admin_host=0.0.0.0 ${current.project.path}` |