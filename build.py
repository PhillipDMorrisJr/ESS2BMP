from pybuilder.core import use_plugin
from pybuilder.core import init

# plugins for common tasks
use_plugin('python.core')
use_plugin('python.unittest')
use_plugin('python.install_dependencies')
use_plugin('python.distutils')

# the task run when pyb is executed
default_task = 'publish'

# extra configuration
@init
def initialize(project):
    # these attributes get added in the generated setup.py file
    project.version = '1.0'
    project.summary = 'Converts skyrim ess to bmp'
    project.name = 'Ess2Bmp'
    project.author = 'Phillip Morris'

@task
def convertAllIn(project):
    project.version = '1.0'
    project.summary = 'Converts all skyrim ess files in a directory to bmp files'
    project.name = 'Ess2Bmp'
    project.author = 'Phillip Morris'
