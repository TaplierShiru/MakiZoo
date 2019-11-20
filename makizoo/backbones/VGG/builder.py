from makiflow.layers import *
from makiflow.models import Classificator
import tensorflow as tf

from .utils import get_batchnorm_params, get_maxpool_params
from .blocks import repeat_n_convLayers


def build_VGG(
    input_shape,
    repetition=3,
    include_top=False,
    num_classes=1000,
    use_bias=False,
    activation=tf.nn.relu,
    create_model=False,
    name_model='MakiClassificator'):
    """
    Parameters
    ----------
    input_shape : List
        Input shape of neural network. Example - [32, 128, 128, 3]
        which mean 32 - batch size, two 128 - size of picture, 3 - number of colors
    repetition : int
        Number of repetition convolution per block, usually 3 for VGG16, 4 for VGG 19
    include_top : bool
        If true when at the end of the neural network added Global Avg pooling and Dense Layer without
        activation with the number of output neurons equal to num_classes
    use_bias : bool
        If true, when on layers used bias operation
    activation : tf object
        Activation on every convolution layer
    create_model : bool
        Return build classification model, otherwise return input MakiTensor and output MakiTensor
    name_model : str
        Name of model, if it will be created
    Returns
    ---------
    x : MakiTensor
        Output MakiTensor
    out_f : int
        Number of output feature maps
    """

    if repetition <= 0:
        raise TypeError('repetition should have type int and be more than 0')

    bn_params = get_batchnorm_params()
    maxpool_params = get_maxpool_params()

    in_x = InputLayer(input_shape=input_shape,name='Input')

    for i in range(1, 6):
        # First block
        if i == 1:
            x = repeat_n_convLayers(in_x, num_block=i, n=2, out_f=64,
                                    use_maxpoolLayer=True, bn_params=bn_params, maxpool_params=maxpool_params)[0]
        # Second block
        elif i == 2:
            x = repeat_n_convLayers(x, num_block=i, n=2,
                                    use_maxpoolLayer=True, bn_params=bn_params, maxpool_params=maxpool_params)[0]
        else:
            x = repeat_n_convLayers(x, num_block=i, n=repetition,
                                    use_maxpoolLayer=True, bn_params=bn_params, maxpool_params=maxpool_params)[0]

    if include_top:
        x = FlattenLayer(name='flatten')(x)
        in_f = x.get_shape()[1] * x.get_shape()[2] * x.get_shape()[3]
        x = DenseLayer(in_d=in_f, out_d=4096, name='fc6')(x)
        x = DenseLayer(in_d=4096, out_d=4096, name='fc7')(x)
        output = DenseLayer(in_d=4096, out_d=1000, activation=None, name='fc8')(x)

        if create_model:
            return Classificator(in_x, output, name=name_model)
    else:
        output = x

    return in_x, output