# Final Model Selection Report

## 1. Overall Model Comparison

本阶段将基线建模阶段和颜色指数特征工程阶段的模型结果进行统一比较。参与比较的模型包括DummyClassifier、基线RandomForest、基线ExtraTrees、加入颜色指数特征后的RandomForest以及加入颜色指数特征后的ExtraTrees。比较指标包括Accuracy、Balanced Accuracy和Macro F1。

从总比较结果看，RandomForest+颜色指数特征在Accuracy和Macro F1上取得最高结果，分别为0.959470和0.944721，说明加入颜色指数特征后，模型整体分类准确率和宏平均F1略有提升。相比之下，原始RandomForest模型的Balanced Accuracy为0.953654，高于RandomForest+颜色指数特征的0.942999，说明原始RandomForest在三类样本召回率的均衡性上更优。

## 2. Model Selection

综合当前结果，本文暂时选择RandomForest+颜色指数特征作为后续Kaggle提交的候选模型。选择该模型的主要原因是：其在所有候选模型中取得最高Accuracy和Macro F1，说明该模型在整体分类效果和宏平均分类表现上具有一定优势。同时，颜色指数特征具有明确的天文学含义，能够反映相邻光度波段之间的星等差异，相比单独使用u、g、r、i、z等原始星等特征，具有更强的物理解释基础。

不过，该模型并不是在所有指标上全面最优。与原始RandomForest相比，RandomForest+颜色指数特征的Balanced Accuracy有所下降，说明加入颜色指数后，模型对三类样本的召回均衡性没有进一步改善。因此，后续若更关注STAR类别的稳定识别或类别均衡性能，原始RandomForest仍然是一个有竞争力的候选模型。

## 3. Current Decision

基于当前验证集结果，后续提交阶段优先采用RandomForest+颜色指数特征模型。该模型将在完整train.csv上重新训练，并对test.csv生成预测结果，最终输出submission.csv用于Kaggle提交。