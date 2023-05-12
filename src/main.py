from crawler import Crawler
from comparator import PowerBIComparator
import os
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--email')
    parser.add_argument('--password')
    parser.add_argument('--group_id')
    parser.add_argument('--report_id1')
    parser.add_argument('--report_id2')

    args = parser.parse_args()

    email = args.email
    password = args.password

    report_id1 = args.report_id1
    group_id = args.group_id
    report_id2 = args.report_id2

    crawl = Crawler(username=email, password=password, group_id=group_id, report_id=report_id2)

    crawl.crawl()
    
    crawl = Crawler(username=email, password=password, group_id=group_id, report_id=report_id1)

    crawl.crawl()

    


#python src/main.py --email pbi@in516ht.com --password 7rTMTgw#BFBPR*WU --group_id 418fc146-6f6a-4b64-afc8-d8856a0d5b6f --report_id1 745405bd-c702-481b-9e5d-bb3dfc1cc93d --report_id2 fc9354f1-c134-41e9-a443-b1276108b23f