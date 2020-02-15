import sys
sys.path.append('/usr/local/lib/python3.6/site-packages')
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import urllib.request
from urllib.parse import urljoin
import time
import re
import mysql.connector
from datetime import datetime

