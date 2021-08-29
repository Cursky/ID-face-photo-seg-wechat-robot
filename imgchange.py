##照片换地代码文件


import argparse
import os
import os.path as osp

import cv2
import numpy as np
from paddleseg.utils import get_sys_env, logger

from deploy.infer import Predictor


def parse_args():
    parser = argparse.ArgumentParser(description='HumanSeg inference for video')
    parser.add_argument(
        "--config",
        dest="cfg",
        help="The config file.",
        default="export_model/ppseg_lite_portrait_398x224_with_softmax/deploy.yaml",
        type=str,
        required=False)
    parser.add_argument(
        "--input_shape",
        dest="input_shape",
        help="The image shape [h, w] for net inputs.",
        nargs=2,
        default=[192, 192],
        type=int)
    parser.add_argument(
        '--img_path',
        dest='img_path',
        help='Image including human',
        type=str,
        default=None)
    parser.add_argument(
        '--video_path',
        dest='video_path',
        help='Video path for inference',
        type=str,
        default=None)
    parser.add_argument(
        '--bg_img_path',
        dest='bg_img_path',
        help=
        'Background image path for replacing. If not specified, a white background is used',
        type=str,
        default=None)
    parser.add_argument(
        '--bg_video_path',
        dest='bg_video_path',
        help='Background video path for replacing',
        type=str,
        default=None)
    parser.add_argument(
        '--save_dir',
        dest='save_dir',
        help='The directory for saving the inference results',
        type=str,
        default='./output')

    parser.add_argument(
        '--with_argmax',
        dest='with_argmax',
        help='Perform argmax operation on the predict result.',
        action='store_true')
    parser.add_argument(
        '--not_soft_predict',
        dest='not_soft_predict',
        help=
        'If this is turned on, the prediction result will be output directly without using soft predict',
        action='store_true')

    parser.add_argument(
        '--test_speed',
        dest='test_speed',
        help='Whether to test inference speed',
        action='store_true')

    return parser.parse_args()


def background_replace(args,img_path,bg_img_path):
    """
    img_path:Str 待分割图像路径
    bg_image_path:背景图像路径
    """
    env_info = get_sys_env()
    args.use_gpu = True if env_info['Paddle compiled with cuda'] and env_info[
        'GPUs used'] else False
    predictor = Predictor(args)

    if not osp.exists(args.save_dir):
        os.makedirs(args.save_dir)

    # 图像背景替换
   
    args.img_path = img_path #将参数传递替换
    # print(args.img_path)
    args.bg_image_path = bg_img_path
    # print(args.bg_image_path)
    if not osp.exists(args.img_path):
        raise Exception('The --img_path is not existed: {}'.format(
            args.img_path))
    img = cv2.imread(args.img_path)
    # print(args.bg_image_path)
    bg = get_bg_img(bg_img_path, img.shape)

    comb = predictor.run(img, bg)

    save_name = osp.basename(args.img_path)
    save_path = osp.join(args.save_dir, save_name)
    cv2.imwrite(save_path, comb)


def get_bg_img(bg_img_path, img_shape):
    print(bg_img_path)
    if bg_img_path is None:
        bg = 255 * np.ones(img_shape)#没有就纯白
    elif not osp.exists(bg_img_path):
        raise Exception(
            'The --bg_img_path is not existed: {}'.format(bg_img_path))
    else:
        bg = cv2.imread(bg_img_path)
        # print("写入完成")
    return bg


def image_change(img_path,bg_img_path):

    args = parse_args()
    background_replace(args,img_path,bg_img_path)


