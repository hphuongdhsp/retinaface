from __future__ import print_function

import torch

from .data import cfg_mnet, cfg_re50
from .models.retinaface import RetinaFace
from torch.utils.model_zoo import load_url
from pathlib import Path

FILE_PATH = str(Path(__file__).parent.resolve())




models_urls = {
    'mnet': 'https://www.dropbox.com/s/kn5hkw5ybhnbf88/mobilenet0.25_Final.pth?dl=1',
    'rnet': 'https://www.dropbox.com/s/ikzk3jfggm2zg52/Resnet50_Final.pth?dl=1',
}

def check_keys(model, pretrained_state_dict):
    
    ckpt_keys = set(pretrained_state_dict.keys())
    model_keys = set(model.state_dict().keys())
    used_pretrained_keys = model_keys & ckpt_keys
    unused_pretrained_keys = ckpt_keys - model_keys
    missing_keys = model_keys - ckpt_keys
    # print('Missing keys:{}'.format(len(missing_keys)))
    # print('Unused checkpoint keys:{}'.format(len(unused_pretrained_keys)))
    # print('Used keys:{}'.format(len(used_pretrained_keys)))
    assert len(used_pretrained_keys) > 0, 'load NONE from pretrained checkpoint'
    return True


def remove_prefix(state_dict, prefix):
    ''' Old style model is stored with all names of parameters sharing common prefix 'module.' '''
    # print('remove prefix \'{}\''.format(prefix))
    f = lambda x: x.split(prefix, 1)[-1] if x.startswith(prefix) else x
    return {f(key): value for key, value in state_dict.items()}


def load_model(net='mnet'):
    if net == 'mnet':
        #pretrained_path = FILE_PATH + '/weights/mobilenet0.25_Final.pth'
        # print('Loading pretrained model from {}'.format(pretrained_path))
        model = RetinaFace(cfg=cfg_mnet, phase='test')
    else:
        #pretrained_path = FILE_PATH + '/weights/Resnet50_Final.pth'
        # print('Loading pretrained model from {}'.format(pretrained_path))
        model = RetinaFace(cfg=cfg_re50, phase='test')

    #device = torch.cuda.current_device()
    pretrained_dict = load_url(models_urls[net], map_location=lambda storage, loc: storage)
    if "state_dict" in pretrained_dict.keys():
        pretrained_dict = remove_prefix(pretrained_dict['state_dict'], 'module.')
    else:
        pretrained_dict = remove_prefix(pretrained_dict, 'module.')
    check_keys(model, pretrained_dict)
    model.load_state_dict(pretrained_dict, strict=False)
    # print('Finished loading model!')
    return model
