import json
import os
import sys

from tencent_cos import TencentCOSBucket
from aliyun_oss import AliyunOSSBucket
from utils import FileManager, OSSSynchronizer


if __name__ == '__main__':
    # with open('config/blog-oss.json', 'rt', encoding='utf-8') as fp:
    #     blog_oss = AliyunOSSBucket(json.load(fp))

    with open('config/blog-cos.json', 'rt', encoding='utf-8') as fp:
        blog_cos = TencentCOSBucket(json.load(fp))

    # with open('config/blog-assets-oss.json', 'rt', encoding='utf-8') as fp:
    #     blog_assets_oss = AliyunOSSBucket(json.load(fp))

    with open('config/blog-assets-cos.json', 'rt', encoding='utf-8') as fp:
        blog_assets_cos = TencentCOSBucket(json.load(fp))

    blog_file = FileManager('../.public')
    blog_assets_file = FileManager('../.oss_assets')

    # OSSSynchronizer(blog_file, blog_oss).sync_from_local_to_oss()
    # OSSSynchronizer(blog_file, blog_cos).sync_from_local_to_oss()
    # OSSSynchronizer(blog_assets_file, blog_assets_oss).sync_from_local_to_oss()
    # OSSSynchronizer(blog_assets_file, blog_assets_cos).sync_from_local_to_oss()

    if 'deploy' in sys.argv:
        OSSSynchronizer(blog_file, blog_cos).sync_from_local_to_oss()
    OSSSynchronizer(blog_assets_file, blog_assets_cos).sync_from_local_to_oss()
