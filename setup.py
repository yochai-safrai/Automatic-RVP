from setuptools import setup, find_packages

setup(
	name='automatic-rvp',
	version='1.0.0',
	description='RVP Program',
	packages=find_packages(),
	url='https://github.com/yochai-safrai/RVP',
	author='Yochai Safrai',
	author_email='yochai.safrai@gmail.com',
	py_modules=['rvp', 'makima', 'pade', 'clustering', 'stabilization'],
	maintainer='Idan Haritan',
	maintainer_email='idan.haritan@gmail.com',
	include_package_data=True,
	package_dir={'': 'src'},
	install_requires=['numpy', 'scipy', 'matplotlib', 'pandas', 'scikit-learn', 'sympy'],
	classifiers=[
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.7',
		],
	python_requires='>=3.7',
	zip_safe=False,
)
