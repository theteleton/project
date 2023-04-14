# Project Competition Comparison of Power BI reports

This is the repository for the project competition of comparisons of Power BI reports.
## Instructions

Here is the overall enviroment setup, any additional setup for the jupyter notebook will be added there.
For this setup you need to have installed Anaconda (https://www.anaconda.com/products/distribution) and Git (https://git-scm.com/).

```
# install Anaconda

cd your_favourite_directory
git clone <this_repository>
cd project-1-theteleton
conda env create -f environment.yml

# press y

conda activate ids
jupyter notebook
```
Also if you want to just let your pc to run scripts all night using the screen software (https://www.gnu.org/software/screen/). They are also the same in the notebook but only for the validation purposes.

```
# These lines must follow the previous ones, after getting into repository's directory and activating the enviroment.
# create new screen
screen -S <your_screen_name>
python ./scripts/<the script you want to run>
# CTRL A + CTRL D
# Let the laptop work