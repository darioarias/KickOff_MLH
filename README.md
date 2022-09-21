# KickOff_MLH

## Setting up using MacOS with Apple M1 chip

1. Clone this repository
2. Install TensorFlow and the tensorflow-metal PluggableDevice on your machine following [these instructions](https://developer.apple.com/metal/tensorflow-plugin/)
3. In the terminal, `cd` to this project's directory
4. Create a conda environment from `environment.yml`: `conda env create -f environment.yml`
5. Activate the environment: `conda activate tensorflow_m1`
6. Verify that the new environment was installed correctly: `conda env list` or `conda info --envs`
7. In VS Code, open the `model.ipynb` file and change to the kernel associated with conda environment `tensorflow_m1`
8. When running the first block that imports packages, you may get a prompt that asks you to install supporting jupyter extensions. Click "Install" and restart VS Code

**Note:** If the `environment.yml` file is missing or need to be refreshed, do the following:

1. In the terminal, run `while read requirement; do conda install --yes $requirement || pip install $requirement; done < requirements.txt`. This command will install all the packages listed in `requirements.txt` using conda if possible, otherwise it will use pip
2. Delete the outdated `environment.yml` file: `rm environment.yml`
3. Create a new version: `conda env export > environment.yml`
