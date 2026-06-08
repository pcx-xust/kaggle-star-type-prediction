# 模型评估报告

## 1.DummyClassifier基准模型

DummyClassifier采用`most_frequent`策略，即始终预测训练集中占比最高的类别GALAXY。验证集结果显示，该模型的accuracy为0.653815，balanced accuracy为0.333333，macro F1-score为0.263558。

从混淆矩阵可以看出，DummyClassifier将所有验证集样本都预测为GALAXY，因此GALAXY类别的recall为1.00，而QSO和STAR的recall均为0。这说明在类别不均衡数据中，accuracy会受到多数类GALAXY的显著影响，不能单独作为模型优劣的判断依据。

因此，后续正式模型必须重点关注balanced accuracy、macro F1-score以及QSO、STAR两个少数类的recall和F1-score，而不仅仅追求accuracy提升。

## 2.RandomForest Baseline

RandomForestClassifier作为第一个正式Baseline模型，在验证集上取得了明显优于DummyClassifier的结果。模型accuracy为0.956370，balanced accuracy为0.953654，macro F1-score为0.942153，说明模型不仅提升了整体准确率，也能够较好地识别不同类别样本。

从分类报告看，GALAXY的precision、recall和F1-score分别为0.98、0.96和0.97；QSO分别为0.95、0.97和0.96；STAR分别为0.86、0.94和0.90。相比DummyClassifier仅能预测多数类GALAXY，RandomForest已经能够有效识别QSO和STAR两个非多数类。

不过，STAR类别的precision为0.86，低于GALAXY和QSO，说明模型仍会将部分非STAR样本误判为STAR。后续模型优化应重点关注STAR类别的误判来源，并通过特征工程、模型对比或参数调整进一步改善少数类分类质量。

综合来看，RandomForest Baseline已经建立了一个较强的基准模型。后续需要进一步提取特征重要性，验证EDA阶段关于redshift和光度变量重要性的判断，并与ExtraTrees等模型进行对比。