# 模型评估报告

## 1.DummyClassifier基准模型

DummyClassifier采用`most_frequent`策略，即始终预测训练集中占比最高的类别GALAXY。验证集结果显示，该模型的accuracy为0.653815，balanced accuracy为0.333333，macro F1-score为0.263558。

从混淆矩阵可以看出，DummyClassifier将所有验证集样本都预测为GALAXY，因此GALAXY类别的recall为1.00，而QSO和STAR的recall均为0。这说明在类别不均衡数据中，accuracy会受到多数类GALAXY的显著影响，不能单独作为模型优劣的判断依据。

因此，后续正式模型必须重点关注balanced accuracy、macro F1-score以及QSO、STAR两个少数类的recall和F1-score，而不仅仅追求accuracy提升。
