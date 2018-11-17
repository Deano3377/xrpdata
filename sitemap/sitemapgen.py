#!/usr/bin/env python

import os
import csv

BUILD_DIR = os.path.join(os.getcwd(), 'build')
LEDGER_START = 32570
LEDGER_END = 43055555

'''
Part 1: Create sitemap index for all accounts.
'''

with open('latest_account_data.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    page, counter = 0, 0
    sitemap_file = open("%s/sitemap-account-%d.txt" % (BUILD_DIR, page), 'wb')
    sitemap_index_header = '<?xml version="1.0" encoding="UTF-8"?><sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
    sitemap_index_footer = '</sitemapindex>'
    sitemap_index_body = "<sitemap><loc>https://data.xrpscan.com/%s</loc></sitemap>" % (os.path.basename(sitemap_file.name))
    
    for row in reader:
        if counter == 50000:
            sitemap_file.close()
            page += 1
            counter = 0
            sitemap_file = open("%s/sitemap-account-%d.txt" % (BUILD_DIR, page), 'wb')
            sitemap_index_body += "<sitemap><loc>https://data.xrpscan.com/%s</loc></sitemap>" % (os.path.basename(sitemap_file.name))

        sitemap = "https://xrpscan.com/account/%s\n" % (row['Account'])
        sitemap_file.write(sitemap)
        counter += 1

    sitemap_file.close()
    with open("%s/sitemap-account-index.xml" % (BUILD_DIR), 'w') as sitemap_index_file:
        sitemap_index = sitemap_index_header + sitemap_index_body + sitemap_index_footer
        sitemap_index_file.write(sitemap_index)

'''
Part 2: Create sitemap index for all ledgers.
'''

def generate_ledger_sitemap():
    page, counter = 0, 0
    sitemap_file = open("%s/sitemap-ledger-%d.txt" % (BUILD_DIR, page), 'wb')
    sitemap_index_header = '<?xml version="1.0" encoding="UTF-8"?><sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
    sitemap_index_footer = '</sitemapindex>'
    sitemap_index_body = "<sitemap><loc>https://data.xrpscan.com/%s</loc></sitemap>" % (os.path.basename(sitemap_file.name))
    
    for ledger_index in xrange(LEDGER_START, LEDGER_END):
        if counter == 50000:
            sitemap_file.close()
            page += 1
            counter = 0
            sitemap_file = open("%s/sitemap-ledger-%d.txt" % (BUILD_DIR, page), 'wb')
            sitemap_index_body += "<sitemap><loc>https://data.xrpscan.com/%s</loc></sitemap>" % (os.path.basename(sitemap_file.name))

        sitemap = "https://xrpscan.com/ledger/%s\n" % (ledger_index)
        sitemap_file.write(sitemap)
        counter += 1
    
    sitemap_file.close()
    with open("%s/sitemap-ledger-index.xml" % (BUILD_DIR), 'w') as sitemap_index_file:
        sitemap_index = sitemap_index_header + sitemap_index_body + sitemap_index_footer
        sitemap_index_file.write(sitemap_index)


'''
Call functions to generate sitemaps
'''
#generate_ledger_sitemap()
