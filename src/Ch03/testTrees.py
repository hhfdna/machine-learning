"""
决策树的测试类
createTree(): 创建决策树，并且持久化到lensesTree.txt中
testTree(): 从保存的文件中恢复决策树模型，并且调用分类算法测试数据

@author: hhf
created on 2018.1.16
"""
from Ch03 import trees

from Ch03 import treePlotter

import pickle

lenses_label=['age','prescript','astigmatic','tearRate']

def createTree():
    fr = open('lenses.txt')
    lenses = [line.strip().split('\t') for line in fr.readlines()]

    lense_tree = trees.createTree(lenses, lenses_label)
    trees.storeTree(lense_tree, './lensesTree.txt')
    treePlotter.createPlot(lense_tree)

def testTree():
    test = ['presbyopic',	'hyper',	'no',	'normal']
    lense_tree = trees.grabTree('./lensesTree.txt')
    lense_type = trees.classify(lense_tree, lenses_label, test)
    print(lense_type)



# createTree()

testTree()