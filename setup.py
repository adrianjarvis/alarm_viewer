from distutils.core import setup

requires = ['pyramid', 'pyramid_chameleon', 'sqlalchemy', 'psycopg2']

setup(
    name='alarm_viewer',
    version='0.0',
    packages=['alarm'],
    url='',
    license='',
    author='Adrian Jarvis',
    author_email='adrian.jarvis@clear.net.nz',
    description='',
    install_requires=requires
)
