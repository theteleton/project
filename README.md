# How to automatically compare two ![Power Bi](https://img.shields.io/badge/power_bi-F2C811?style=for-the-badge&logo=powerbi&logoColor=black) reports? 

The PowerBI is one of the most popular software for creating and manipulating with reports, which can be used for many advanced statistical analyses, which can solve or more importantly show many problems related to our business. One type of problems that we want to find out about is the correctness of a migration of a database and,since the databases are usually too large for checking each value separately, a solution is proposed to generate two structurally identical PowerBI reports and compare them in order to find out about differences in the databases. 

## Installation

For this setup you need to have installed Anaconda (https://www.anaconda.com/products/distribution) and Git (https://git-scm.com/).

```
# install Anaconda

cd your_favourite_directory
git clone <this_repository>
cd project
conda env create -f src/environment.yml

# press y

conda activate ids
```
## Usage
Once you have installed the environment you can use the comparator with the following commands:
```
cd src
python main.py --email <your_powerbi_email> --password <your_powerbi_password> --group_id1 <group_or_workspace_id_of_the_first_report> --group_id2 <group_or_workspace_id_of_the_first_report> --report_id1 <first_report_id> --report_id2 <second_report_id> --data_folder <location_of_your_favourite_folder> 
```
After you start the comparator, if your account needs two-factor authentication to be logged in, the comparator will ask you to insert you 2FA authenticator. The comparison will be created in the ```<data_folder>``` that you chosed.  

**WARNING! If the comparator did not run successfuly, it is most probably due to a window that is appearing from powerbi for whether do you like this app or not. This is for first time users of Power BI application, it will be showed only one time.**

*ATTENTION! For the usage of this application you will need to have Linux operating system installed. If you are using for Windows, you will need to download the windows driver and in addition to have set some permissions so the files could be downloaded with the driver. I strongly recommend to use Linux for now. The next version would be more Windows friendly.*

*ATTENTION! Currently the application is developed only for Google Chrome.*

If you want to see how the test cases looked like, in each ```<data_folder>```  there is a folder of screenshots of the Power BI reports.
## Technologies used

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)![Selenium](https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white)![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white)![Power Bi](https://img.shields.io/badge/power_bi-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)![Microsoft Excel](https://img.shields.io/badge/Microsoft_Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white)

## Environtment
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)![Google Chrome](https://img.shields.io/badge/Google%20Chrome-4285F4?style=for-the-badge&logo=GoogleChrome&logoColor=white)