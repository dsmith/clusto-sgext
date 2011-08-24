from setuptools import setup

__version__ = file('VERSION', 'r').read().strip('\r\n\t ')

setup(name='clusto-sgext',
      version=__version__,
      packages=['sgext'],
      install_requires=[
        'clusto',
        'IPy',
        'boto',
        'kombu',
        'eventlet',
        'PyYAML',
      ], 
      entry_points={
        'console_scripts': [
            'clusto-puppet-node2 = sgext.commands.puppet_node2:main',
            'clusto-barker-consumer = sgext.commands.barker_consumer:main',
            'clusto-ec2-report = sgext.commands.ec2_report:main',
        ]
      })
