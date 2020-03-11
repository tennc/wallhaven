# -*- coding: utf-8 -*-

# Scrapy settings for wallhaven project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'wallhaven'

SPIDER_MODULES = ['wallhaven.spiders']
NEWSPIDER_MODULE = 'wallhaven.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'wallhaven (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32
HTTPERROR_ALLOWED_CODES =[429]
# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1
# 添加延时，增大下载速度的延时
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16
# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'en',
    'cookie': '__cfduid=dc05fe0595ab101757de07bdd735eb3081583915807; XSRF-TOKEN=eyJpdiI6IlVmQ3lEKzNOQjBiTVhNcVNlNUhVXC9RPT0iLCJ2YWx1ZSI6IitFQm9VTCt3SklrUzVJVklZSFV1dE4rNUNwQ0RXXC95TEFVNURaYmNoRnBjYmw0WUNOQVwvVWlHRFBpTEdDaVdxRSIsIm1hYyI6IjZjZDZhODc2MDlmMzFhYjBhNTBlZjAzYjExNzVkZjBmODYxODY1NTgwZjc4YjcyODg3YTZiOThjMTU1MWY5YjMifQ%3D%3D; wallhaven_session=eyJpdiI6IjFLaXl3SUdUdnRuMVdhWHpPZHNtTEE9PSIsInZhbHVlIjoiVWtMT3VBRU9EalFPRXlOeVgwdjUyZmRMMDlpNjNYOHF3RXFDU1JXVUFkMitnU2ZUTEFSUEJEdEdVekJKNElPeCIsIm1hYyI6IjFjODM2NDRjNGUxZGEyOTIxODkxMTNkYzU2M2YyMzE3MGUzNDZhMzk5YWZlNzI4ODk2NTUwYjMzY2Y1NzBlMGIifQ%3D%3D',
    'referer': 'https://wallhaven.cc/latest?page=5',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.4077.0 Safari/537.36',
    'cf-ray': '57240c065a59eef2-LAX',
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'wallhaven.middlewares.WallhavenSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'wallhaven.middlewares.WallhavenDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'wallhaven.pipelines.WallhavenPipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
