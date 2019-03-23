from distutils.core import setup

setup(
    name='twitter_requests',
    packages=['twitter_requests'],
    version='0.1',
    license='MIT',
    description='Simple python lib for acquire your twitter data',
    author='ebysofyan',
    author_email='eby.sofyan@gmail.com',
    url='https://github.com/ebysofyan',
    download_url='',
    keywords=['twitter-lib', 'simple api', 'twitter requests'],
    install_requires=[
        'requests',
        'requests_oauthlib',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
)
