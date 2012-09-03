from setuptools import setup, find_packages
setup(
    name='django-articles',
    version=__import__('articles').get_version(limit=3),
    description='A Django application to handle basic articles and link them to any page',
    author='Guillaume Esquevin',
    author_email='guillaume.esquevin@platypus-creation.com',
    url='http://code.google.com/p/django-articles/',
    license='MIT',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    install_requires=['pygments','BeautifulSoup'],
    include_package_data=True,
    zip_safe=False,
)
