# Scrapy settings for wuba project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'wuba'

SPIDER_MODULES = ['wuba.spiders']
NEWSPIDER_MODULE = 'wuba.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
LOG_LEVEL = 'ERROR'
# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    'cookie':'myLat=""; myLon=""; id58=5W0BvGGExPwmh1lgGx6Oug==; mcity=xianyang; 58home=xianyang; city=xianyang; 58tj_uuid=b62780a2-635c-4dcc-9a65-15cde0a9e64c; als=0; wmda_uuid=5717130b24e203d841a095847202db42; wmda_new_uuid=1; wmda_visited_projects=%3B11187958619315%3B1731916484865; sessionid=8375bf01-c9e4-4cf3-80f8-36a608fb186c; fzq_h=0274b9fb8884fa42807e031234ab43c6_1636091139694_165c312fb20e41fdb09c928506d1b003_2072723435; xxzl_deviceid=yAce7arFNPw6f5VacIb1yi8adms59t%2Fh5we4WlMGTtBHD8pR42Mkr0BOLZwSWXNO; gr_user_id=7b4415aa-bf14-4235-8753-c2a44dea3d5f; new_uv=5; init_refer=; xxzl_cid=8279f39ab0664e768699c85bb6cbe52a; xzuid=334ddc80-010a-475e-b3c7-e5bee11d21eb; wmda_session_id_11187958619315=1636121981195-bbb4942a-bf1e-452b; wmda_session_id_1731916484865=1636121988545-a4d6ff4d-b996-f55e; spm=u-2d2yxv86y3v43nkddh1.BDPCPZ_BT; utm_source=market; new_session=0; gr_session_id_b4113ecf7096b7d6=9884a538-75af-4fec-8a87-150c906ddcb7; ppStore_fingerprint=5DA39940CA79C91E99BFCF602B6D6B3091570EA194616FC9%EF%BC%BF1636122015236; gr_session_id_b4113ecf7096b7d6_9884a538-75af-4fec-8a87-150c906ddcb7=true'
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'wuba.middlewares.WubaSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'wuba.middlewares.WubaDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'wuba.pipelines.WubaPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
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
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
