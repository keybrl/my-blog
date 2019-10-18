import json
import os
import sys

from tencent_cos import TencentCOSBucket
from aliyun_oss import AliyunOSSBucket
from utils import FileManager, OSSSynchronizer


if __name__ == '__main__':
    with open('config/blog-cos.json', 'rt', encoding='utf-8') as fp:
        blog_cos = TencentCOSBucket(json.load(fp))

    with open('config/oss-cos.json', 'rt', encoding='utf-8') as fp:
        oss_cos = TencentCOSBucket(json.load(fp))

    with open('config/video-cos.json', 'rt', encoding='utf-8') as fp:
        video_cos = TencentCOSBucket(json.load(fp))

    blog_file = FileManager('../.public')
    oss_file = FileManager('../.oss_assets')
    video_file = FileManager('../.oss_video')

    if 'deploy' in sys.argv:
        OSSSynchronizer(blog_file, blog_cos).sync_from_local_to_oss()
    OSSSynchronizer(oss_file, oss_cos).sync_from_local_to_oss()
    OSSSynchronizer(video_file, video_cos).sync_from_local_to_oss()

