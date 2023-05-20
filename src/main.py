from crawler import Crawler
from comparator import PowerBIComparator
import os
import argparse

import shutil


if __name__ == "__main__":
    

    parser = argparse.ArgumentParser()
    parser.add_argument('--email')
    parser.add_argument('--password')
    parser.add_argument('--group_id')
    parser.add_argument('--report_id1')
    parser.add_argument('--report_id2')

    args = parser.parse_args()

    folder_path = './data_new/Pair1'
    file_list = os.listdir(folder_path)
    for file_name in file_list:
        file_path = os.path.join(folder_path, file_name)
        os.remove(file_path)

    folder_path = './data_new/Pair2'
    file_list = os.listdir(folder_path)
    for file_name in file_list:
        file_path = os.path.join(folder_path, file_name)
        os.remove(file_path)

    folder_path = './predictions'
    file_list = os.listdir(folder_path)
    for file_name in file_list:
        file_path = os.path.join(folder_path, file_name)
        os.remove(file_path)

    email = args.email
    password = args.password

    report_id1 = args.report_id1
    group_id = args.group_id
    report_id2 = args.report_id2

    crawl = Crawler(username=email, password=password, group_id=group_id, report_id=report_id2)

    crawl.crawl()
    source_dir = '../../Downloads'
    destination_dir = './data_new/Pair1'
    files = os.listdir(source_dir)
    for file in files:
        if "vegetables.csv" in file.split(" "):
            new_file = "Sales quantity by veggie.csv"
            os.rename(os.path.join(source_dir, file), os.path.join(source_dir, new_file))
    files = os.listdir(source_dir)
    for file in files:
        source_file = os.path.join(source_dir, file)
        destination_file = os.path.join(destination_dir, file)
        shutil.move(source_file, destination_file)

    crawl = Crawler(username=email, password=password, group_id=group_id, report_id=report_id1)

    crawl.crawl()
    


    
    source_dir = '../../Downloads'
    destination_dir = './data_new/Pair2'
    files = os.listdir(source_dir)
    for file in files:
        source_file = os.path.join(source_dir, file)
        destination_file = os.path.join(destination_dir, file)
        shutil.move(source_file, destination_file)
    comparator = PowerBIComparator("./data_new/Pair1", "./data_new/Pair2")
    comparator.input_tables()


    
# Test reports

#python src/main.py --email pbi@in516ht.com --password 7rTMTgw#BFBPR*WU --group_id 418fc146-6f6a-4b64-afc8-d8856a0d5b6f --report_id1 745405bd-c702-481b-9e5d-bb3dfc1cc93d --report_id2 fc9354f1-c134-41e9-a443-b1276108b23f
#python src/main.py --email pbi@in516ht.com --password 7rTMTgw#BFBPR*WU --group_id 418fc146-6f6a-4b64-afc8-d8856a0d5b6f --report_id1 5b02eabf-44b8-4766-bec2-924af2a4dab6 --report_id2 3566ecf2-66d1-438c-82cb-d49055839a8b
#python src/main.py --email pbi@in516ht.com --password 7rTMTgw#BFBPR*WU --group_id 418fc146-6f6a-4b64-afc8-d8856a0d5b6f --report_id1 5e0863d1-424c-4336-a960-9168a5fabb87 --report_id2 3b7baa08-2b32-46c8-a172-3e3ee158ff26
#python src/main.py --email pbi@in516ht.com --password 7rTMTgw#BFBPR*WU --group_id 418fc146-6f6a-4b64-afc8-d8856a0d5b6f --report_id1 a7eb754e-6e0d-4e30-adc6-a2e7f0c6e24e --report_id2 28c4ba3f-bffa-48d9-8ab8-9cfbc0567f74
