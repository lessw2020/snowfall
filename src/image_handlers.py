# useful image utils
# @lessw2020

import cv2
import PIL as pil
from pathlib import PurePath, Path


def cv_load(fn, as_rgb=True):
    """ robustly loads an image using opencv 
    a - modifies Pathlib into str if needed
    b - verifies something loaded and then 
    c - switches to rgb for viewing, or returns as bgr for processing"""

    file_str = ""
    if isinstance(fn, PurePath):
        file_str = str(fn)
    elif isinstance(fn, str):
        file_str = fn
    else:
        RaiseValueError(
            f"odd input type received - {type(fn)}. Expecting str of Path var"
        )
        return

    img_bgr = cv2.imread(file_str)
    if not len(img_bgr):
        print(f"failed to load! {file_str}")
        return None

    if as_rgb:
        img_rgb = toRgb(img_bgr)
        return img_rgb
    else:
        return img_bgr


def toRgb(in_img):
    out_img = cv2.cvtColor(in_img, cv2.COLOR_BGR2RGB)
    return out_img


def toBgr(in_img):
    out_img = cv2.cvtColor(in_img, cv2.COLOR_RGB2BGR)
    return out_img
