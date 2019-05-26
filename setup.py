from setuptools import setup, find_packages

setup(
    name="OpenMiner",
    description="Miner for python",
    long_description="Miner software for zcash by multi process and gpu",
    author="winter",
    author_email="785576549@qq.com",
    packages=find_packages(),
    zip_safe=False,
    keywords=("zcash", "miner", "scrypt", "Equihash", "GPU", "cuda"),
    license="MIT Licence",
    include_package_data=True,
    platforms="any",
    install_requires=[
        "numba"
    ],
    scripts=[],
    entry_points={
        "console_scripts": [
            "openminer=openminer.entry:main"
        ]
    },
    classifiers=[
        "Development Status :: Develop",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Topic: mine, bitcoin, zcash"
    ],
)
