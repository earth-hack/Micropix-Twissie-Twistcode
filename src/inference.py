from fastai import * 
from fastai.vision import *
import torch
import argparse, json
import cv2

def inference(image_path):
    img = open_image(image_path)
    PATH_TO_MODEL = 'stage-2-rn34_satel.pth'

    '''
        USE FASTAI
    '''
    path = 'satellite/'
    df = pd.read_csv(path + 'train_v2.csv')

    tfms = get_transforms(do_flip=False)

    np.random.seed(42)
    src = (ImageItemList.from_csv(path, 'train_v2.csv', folder='train', suffix='.jpg')
        .random_split_by_pct(0.2)
        .label_from_df(label_delim=' '))

    data = (src.transform(tfms, size=362)
            .databunch(num_workers=4).normalize(imagenet_stats))

    learn = create_cnn(data, models.resnet34)
    learn.load(PATH_TO_MODEL[:-4], strict=False, with_opt=False)

    ########################################################################

    pred_class,pred_idx,outputs = learn.predict(img)
    out_max = np.max(outputs.numpy())

    PREDICT_CLASSES = pred_class
    PREDICT_PERCENTAGE = out_max * 100

    output = {
            "confidence":"{0:.2f}".format(round(PREDICT_PERCENTAGE,2)),
            "results":str(PREDICT_CLASSES),
    }

    return output