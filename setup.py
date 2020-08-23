import setuptools

setuptools.setup(
    name="basic_graph"
    ,version="0.0.1"
    ,author="Nicolas Judd"
    ,author_email="Nicolas.Judd@gmail.com"
    ,description="Just a basic graph setup"
    ,packages=['basic_graph']
    ,package_dir={'':'src'}
    ,classifiers=[
        "Programming Language :: Python :: 3"
        ,"License :: OSI Approved :: MIT License"
        ,"Operating System :: OS Independent"
    ]
    ,python_requires='>=3.8',
)
