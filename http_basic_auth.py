#!/usr/bin/env python

'''
http_basic_auth.py - Example of retrieving a webpage protected by HTTP basic
                     authentication.

This example is based on the tutorial at 
http://www.voidspace.org.uk/python/articles/authentication.shtml

Author: Eric Saunders
February 2011
'''

import urllib2
import re
import os.path

# Specify the target and credentials
def get_credentials(path):
    credentials = {}
    path_to_creds = os.path.expanduser(path)
    auth_fh = open(path_to_creds, 'r')
    for line in auth_fh:
        if line.strip().startswith('#'):
            continue

        print "line", line

        key, _, value = line.split()

        credentials[key] = value

    auth_fh.close()
    return credentials

credentials = get_credentials('~/credentials/remote_server_example.pwd')

target_url = credentials['target_url']
realm      = None
username   = credentials['username']
password   = credentials['password']


def extract_nightlog_and_fits_from_html(page_handle):
    # Construct the regexes to match the nightlog and fits file names
    night_log_regex = r'.*href=(\d+\.log)'
    night_log_pat   = re.compile(night_log_regex, re.IGNORECASE)

    fits_regex = r'.*href=([a-z_0-9]+\.fits)'
    fits_pat   = re.compile(fits_regex, re.IGNORECASE)

    # Parse the webpage, and extract the links for the night log and all FITS files
    fits_file_names = []
    for line in page_handle:
        nightlog_match = re.match(night_log_pat, line)
        if nightlog_match:
            nightlog_name = nightlog_match.groups()[0]
            print "Found nightlog called:", nightlog_name

        fits_match = re.match(fits_pat, line)
        if fits_match:
            fits_name = fits_match.groups()[0]
            print "Found fits file called:", fits_name
            fits_file_names.append(fits_name)

    return (nightlog_name, fits_file_names)


def download_file(url, file_to_save):
    url_handle  = urllib2.urlopen(url)
    file_handle = open(file_to_save, 'w')
    for line in url_handle:
        file_handle.write(line)
    url_handle.close()
    file_handle.close()
    print "Downloaded:", file_to_save

# Create and configure a password manager
# This manager allows us to get away with not specifying a realm
password_manager = urllib2.HTTPPasswordMgrWithDefaultRealm()
password_manager.add_password(realm, target_url, username, password)

#Create a handler that understands HTTP basic authentication
basic_auth_handler = urllib2.HTTPBasicAuthHandler(password_manager)
opener = urllib2.build_opener(basic_auth_handler)

# Set this handler as the default for use by urllib2
urllib2.install_opener(opener)

# Get the webpage
page_handle = urllib2.urlopen(target_url)

# Find the names of the target files to download
nightlog_name, fits_file_names = extract_nightlog_and_fits_from_html(page_handle)

# Download and save the nightlog
download_file(target_url + nightlog_name, nightlog_name)

# Download and save the fits files
for fits_file_name in fits_file_names:
    download_file(target_url + fits_file_name, fits_file_name)

