from setuptools import find_packages,setup

def get_data(file_name):
    requirements=[]

    with open(file_name) as f:
        requirements=f.readlines()

        requirements=[file.replace("\n","") for file in requirements]

        if("-e ." in requirements):
            requirements.remove("-e .")
    return requirements


setup(
   name='Data Gathering',
   version='0.0.1',
   description='Gatherring the world international news data and news headlines',
   author='Sami-Ullah',
   author_email='sami606713@gmail.com',
   packages=find_packages(),
   install_requires=get_data('requirements.txt') #external packages as dependencies
)
