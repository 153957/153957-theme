from setuptools import setup, find_packages

setup(
    name="153957-theme",
    version="1.0.0",
    packages=find_packages(),
    url="http://github.com/153957/153957-theme/",
    bugtrack_url='http://github.com/153957/153957-theme/issues',
    license='MIT',
    author="Arne de Laat",
    author_email="arne@delaat.net",
    description="Theme for sigal generated photo albums",
    long_description=open('README.rst').read(),
    keywords=['photo album', 'theme', 'sigal', 'galleria'],
    classifiers=[
        'Environment :: Plugins',
        'Environment :: Web Environment',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Text Processing :: Markup :: HTML',
    ],
    install_requires=['sigal'],
    package_data={
        '153957_theme': [
            'templates/*.html',
            'static/*/*',
        ]
    },
)
