import os
import argparse
import shutil

from crawler import Crawler
from comparator import ComparatorPowerBI
from processing import ImageProcessing



if __name__ == "__main__":
    
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--email')
    parser.add_argument('--password')
    parser.add_argument('--group_id1')
    parser.add_argument('--group_id2')
    parser.add_argument('--report_id1')
    parser.add_argument('--report_id2')
    parser.add_argument('--data_folder')


    args = parser.parse_args()

    email = args.email
    password = args.password

    report_id1 = args.report_id1
    group_id2 = args.group_id2
    report_id2 = args.report_id2
    group_id1 = args.group_id1
    
    try:
        shutil.rmtree(args.data_folder)
    except:
        pass
    os.makedirs(args.data_folder)
    os.makedirs(f"{args.data_folder}/screenshots")

    os.makedirs(f"{args.data_folder}/Report1")
    os.makedirs(f"{args.data_folder}/Report2")

    print("START OF THE SCRAPING OF THE FIRST REPORT")
    crawl = Crawler(username=email, password=password, group_id=group_id1, report_id=report_id1, data_path=f"{args.data_folder}/Report1", screenshots_path=f"{args.data_folder}/screenshots", downloads_path=".")
    crawl.crawl()
    print("START OF THE SCRAPING OF THE SECOND REPORT")
    crawl = Crawler(username=email, password=password, group_id=group_id2, report_id=report_id2, data_path=f"{args.data_folder}/Report2", screenshots_path=f"{args.data_folder}/screenshots", downloads_path=".")
    crawl.crawl()
    
    
    print("START OF THE COMPARISON")
    comparator = ComparatorPowerBI(f"{args.data_folder}")
    comparator.create_predictions()
    
    #obj = ImageProcessing()
    #obj.preprocess("./data1/screenshots/screenshot0.png")

    
    
# Test reports

#python main.py --email pbi@in516ht.com --password 7rTMTgw#BFBPR*WU --group_id1 418fc146-6f6a-4b64-afc8-d8856a0d5b6f --group_id2 418fc146-6f6a-4b64-afc8-d8856a0d5b6f --report_id1 745405bd-c702-481b-9e5d-bb3dfc1cc93d --report_id2 fc9354f1-c134-41e9-a443-b1276108b23f --data_folder ./data1 
#python main.py --email pbi@in516ht.com --password 7rTMTgw#BFBPR*WU --group_id1 418fc146-6f6a-4b64-afc8-d8856a0d5b6f --group_id2 418fc146-6f6a-4b64-afc8-d8856a0d5b6f --report_id1 5b02eabf-44b8-4766-bec2-924af2a4dab6 --report_id2 3566ecf2-66d1-438c-82cb-d49055839a8b --data_folder ./data2 
#python main.py --email pbi@in516ht.com --password 7rTMTgw#BFBPR*WU --group_id1 418fc146-6f6a-4b64-afc8-d8856a0d5b6f --group_id2 418fc146-6f6a-4b64-afc8-d8856a0d5b6f --report_id1 5e0863d1-424c-4336-a960-9168a5fabb87 --report_id2 3b7baa08-2b32-46c8-a172-3e3ee158ff26 --data_folder ./data3 
#python main.py --email pbi@in516ht.com --password 7rTMTgw#BFBPR*WU --group_id1 418fc146-6f6a-4b64-afc8-d8856a0d5b6f --group_id2 418fc146-6f6a-4b64-afc8-d8856a0d5b6f --report_id1 a7eb754e-6e0d-4e30-adc6-a2e7f0c6e24e --report_id2 28c4ba3f-bffa-48d9-8ab8-9cfbc0567f74 --data_folder ./data4
#python main.py --email pbi@in516ht.com --password 7rTMTgw#BFBPR*WU --group_id1 418fc146-6f6a-4b64-afc8-d8856a0d5b6f --group_id2 418fc146-6f6a-4b64-afc8-d8856a0d5b6f --report_id1 0223acce-21ac-4154-9e09-d7feeda1830e --report_id2 a86fa9f3-5487-4d8c-aaa2-5385e96d4d4e --data_folder ./data5 
#python main.py --email pbi@in516ht.com --password 7rTMTgw#BFBPR*WU --group_id1 418fc146-6f6a-4b64-afc8-d8856a0d5b6f --group_id2 418fc146-6f6a-4b64-afc8-d8856a0d5b6f --report_id1 09ad60b8-21d5-49c3-ad18-6ea6bfedd01c --report_id2 c7aa2c54-80aa-452f-8ccb-f102b9246dc0 --data_folder ./data6 
#python main.py --email pbi@in516ht.com --password 7rTMTgw#BFBPR*WU --group_id1 418fc146-6f6a-4b64-afc8-d8856a0d5b6f --group_id2 96fae34f-23c8-4bfb-a189-40e661fb32d5 --report_id1 8d6fdbb7-afea-421d-af2c-91a7fdd9e1d0 --report_id2 53df8679-5d15-404c-b195-e72b5779cf4e --data_folder ./data7 
#python main.py --email pbi@in516ht.com --password 7rTMTgw#BFBPR*WU --group_id1 418fc146-6f6a-4b64-afc8-d8856a0d5b6f --group_id2 418fc146-6f6a-4b64-afc8-d8856a0d5b6f --report_id1 00955e1b-f364-4678-8e6b-87dccb729037 --report_id2 5affc50e-90fb-4714-982f-21103a6d02a4 --data_folder ./data8
#
