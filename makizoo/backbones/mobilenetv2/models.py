# Copyright (C) 2020  Igor Kilbas, Danil Gribanov
#
# This file is part of MakiZoo.
#
# MakiZoo is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# MakiZoo is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Foobar.  If not, see <https://www.gnu.org/licenses/>.


import tensorflow as tf
from makiflow.layers.utils import InitConvKernel
from .builder import build_MobileNetV2


def MobileNetV2_1_0(
        input_shape,
        classes=1000,
        include_top=False,
        create_model=False,
        kernel_initializer=InitConvKernel.HE):
    """
    Create ResNet18 model with certain `input_shape`

    Parameters
    ----------
    input_shape : list
        Input shape into model,
        Example: [1, 300, 300, 3]
    classes : int
        Number of classes for classification task, used if `include_top` is True
    include_top : bool
        If equal to True then additional dense layers will be added to the model,
        In order to build full ResNet18 model
    create_model : bool
        If equal to True then will be created Classification model
        and this method wil return only this obj
    kernel_initializer : str
        Name of type initialization for conv layers,
        For more examples see: makiflow.layers.utils,
        By default He initialization are used

    Returns
    -------
    if `create_model` is False
        in_x : mf.MakiTensor
            Input MakiTensor
        output : mf.MakiTensor
            Output MakiTensor
    if `create_model` is True
        model : mf.models.Classificator
            Classification model

    """
    return  build_MobileNetV2(
        input_shape=input_shape,
        include_top=include_top,
        num_classes=classes,
        use_bias=False,
        activation=tf.nn.relu6,
        create_model=create_model,
        name_model='MobileNetV2_1_0',
        alpha=1.0,
        expansion=6,
        kernel_initializer=kernel_initializer
    )


def MobileNetV2_1_4(
        input_shape,
        classes=1000,
        include_top=False,
        create_model=False,
        kernel_initializer=InitConvKernel.HE):
    """
    Create ResNet18 model with certain `input_shape`

    Parameters
    ----------
    input_shape : list
        Input shape into model,
        Example: [1, 300, 300, 3]
    classes : int
        Number of classes for classification task, used if `include_top` is True
    include_top : bool
        If equal to True then additional dense layers will be added to the model,
        In order to build full ResNet18 model
    create_model : bool
        If equal to True then will be created Classification model
        and this method wil return only this obj
    kernel_initializer : str
        Name of type initialization for conv layers,
        For more examples see: makiflow.layers.utils,
        By default He initialization are used

    Returns
    -------
    if `create_model` is False
        in_x : mf.MakiTensor
            Input MakiTensor
        output : mf.MakiTensor
            Output MakiTensor
    if `create_model` is True
        model : mf.models.Classificator
            Classification model

    """
    return  build_MobileNetV2(
        input_shape=input_shape,
        include_top=include_top,
        num_classes=classes,
        use_bias=False,
        activation=tf.nn.relu6,
        create_model=create_model,
        name_model='MobileNetV2_1_4',
        alpha=1.4,
        expansion=6,
        kernel_initializer=kernel_initializer
    )


def MobileNetV2_0_75(
        input_shape,
        classes=1000,
        include_top=False,
        create_model=False,
        kernel_initializer=InitConvKernel.HE):
    """
    Create ResNet18 model with certain `input_shape`

    Parameters
    ----------
    input_shape : list
        Input shape into model,
        Example: [1, 300, 300, 3]
    classes : int
        Number of classes for classification task, used if `include_top` is True
    include_top : bool
        If equal to True then additional dense layers will be added to the model,
        In order to build full ResNet18 model
    create_model : bool
        If equal to True then will be created Classification model
        and this method wil return only this obj
    kernel_initializer : str
        Name of type initialization for conv layers,
        For more examples see: makiflow.layers.utils,
        By default He initialization are used

    Returns
    -------
    if `create_model` is False
        in_x : mf.MakiTensor
            Input MakiTensor
        output : mf.MakiTensor
            Output MakiTensor
    if `create_model` is True
        model : mf.models.Classificator
            Classification model

    """
    return  build_MobileNetV2(
        input_shape=input_shape,
        include_top=include_top,
        num_classes=classes,
        use_bias=False,
        activation=tf.nn.relu6,
        create_model=create_model,
        name_model='MobileNetV2_0_75',
        alpha=0.75,
        expansion=6,
        kernel_initializer=kernel_initializer
    )


def MobileNetV2_1_3(
        input_shape,
        classes=1000,
        include_top=False,
        create_model=False,
        kernel_initializer=InitConvKernel.HE):
    """
    Create ResNet18 model with certain `input_shape`

    Parameters
    ----------
    input_shape : list
        Input shape into model,
        Example: [1, 300, 300, 3]
    classes : int
        Number of classes for classification task, used if `include_top` is True
    include_top : bool
        If equal to True then additional dense layers will be added to the model,
        In order to build full ResNet18 model
    create_model : bool
        If equal to True then will be created Classification model
        and this method wil return only this obj
    kernel_initializer : str
        Name of type initialization for conv layers,
        For more examples see: makiflow.layers.utils,
        By default He initialization are used

    Returns
    -------
    if `create_model` is False
        in_x : mf.MakiTensor
            Input MakiTensor
        output : mf.MakiTensor
            Output MakiTensor
    if `create_model` is True
        model : mf.models.Classificator
            Classification model

    """
    return  build_MobileNetV2(
        input_shape=input_shape,
        include_top=include_top,
        num_classes=classes,
        use_bias=False,
        activation=tf.nn.relu6,
        create_model=create_model,
        name_model='MobileNetV2_1_3',
        alpha=1.3,
        expansion=6,
        kernel_initializer=kernel_initializer
    )
