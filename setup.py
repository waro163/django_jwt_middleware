from setuptools import find_packages, setup

version = "v0.0.1"

def read(f):
    return open(f, 'r', encoding='utf-8').read()

setup(
    name='django_jwt_middleware',
    version=version,
    license='MIT',
    description='',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    author='waro163',
    author_email='waro163@163.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'asgiref==3.2.7',
        'Django==3.0.7',
        'PyJWT==2.4.0',
        'pytz==2019.3',
        'sqlparse==0.3.1',
    ],
    python_requires=">=3.5",
    zip_safe=False,
    classifiers=[
        'Development Status :: 1 - Beta',
        'Environment :: Web Environment',
        # 'Framework :: Django',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 2.2',
        # 'Intended Audience :: Developers',
        # 'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
    ],
)