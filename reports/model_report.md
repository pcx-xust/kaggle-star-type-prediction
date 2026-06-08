# Final Model Selection Report

## 1. Overall Model Comparison

本阶段将基线建模阶段和颜色指数特征工程阶段的模型结果进行统一比较。参与比较的模型包括DummyClassifier、基线RandomForest、基线ExtraTrees、加入颜色指数特征后的RandomForest以及加入颜色指数特征后的ExtraTrees。比较指标包括Accuracy、Balanced Accuracy和Macro F1。

从总比较结果看，RandomForest+颜色指数特征在Accuracy和Macro F1上取得最高结果，分别为0.959470和0.944721，说明加入颜色指数特征后，模型整体分类准确率和宏平均F1略有提升。相比之下，原始RandomForest模型的Balanced Accuracy为0.953654，高于RandomForest+颜色指数特征的0.942999，说明原始RandomForest在三类样本召回率的均衡性上更优。

## 2. Model Selection

综合当前结果，本文暂时选择RandomForest+颜色指数特征作为后续Kaggle提交的候选模型。选择该模型的主要原因是：其在所有候选模型中取得最高Accuracy和Macro F1，说明该模型在整体分类效果和宏平均分类表现上具有一定优势。同时，颜色指数特征具有明确的天文学含义，能够反映相邻光度波段之间的星等差异，相比单独使用u、g、r、i、z等原始星等特征，具有更强的物理解释基础。

不过，该模型并不是在所有指标上全面最优。与原始RandomForest相比，RandomForest+颜色指数特征的Balanced Accuracy有所下降，说明加入颜色指数后，模型对三类样本的召回均衡性没有进一步改善。因此，后续若更关注STAR类别的稳定识别或类别均衡性能，原始RandomForest仍然是一个有竞争力的候选模型。

## 3. Current Decision

基于当前验证集结果，后续提交阶段优先采用RandomForest+颜色指数特征模型。该模型将在完整train.csv上重新训练，并对test.csv生成预测结果，最终输出submission.csv用于Kaggle提交。

## 4.LightGBM 作为主模型

从Kaggle线上提交结果来看，RandomForest+颜色指数特征模型的Public Score为0.94506，而LightGBM+颜色指数特征模型的Public Score提升至0.95719，提升幅度为0.01213。该结果说明LightGBM不仅在线下验证集上表现更好，而且在未参与训练的测试集上也具有更强的泛化能力。因此，在当前实验阶段，LightGBM+颜色指数特征模型可以作为最终提交模型。

颜色指数特征包括 `u_g`、`g_r`、`r_i`和 `i_z`，它们反映了不同光度波段之间的相对差异。从天文学背景来看，不同类型天体在不同波段上的亮度分布和颜色特征存在差异，因此颜色指数能够为GALAXY、QSO和STAR三分类任务提供有效的补充信息。将颜色指数特征与原始光度特征、红移特征以及空间坐标特征结合后，LightGBM能够进一步捕捉特征之间的非线性交互关系，从而提升分类效果。

最终模型对比如下：

| 模型         | 特征集合              | 验证集Macro F1 | Kaggle Public Score |
| ------------ | --------------------- | -------------: | ------------------: |
| RandomForest | 原始特征+颜色指数特征 |       0.944721 |             0.94506 |
| LightGBM     | 原始特征+颜色指数特征 |       0.956350 |             0.95719 |

因此，本文当前最终选择的模型为LightGBM+颜色指数特征模型。该模型在验证集和Kaggle公开测试集上均取得了更优结果，能够作为当前项目的最佳分类模型。

不过需要指出的是，当前结论主要基于单次训练验证划分和Kaggle Public Score。由于Kaggle最终排名还会受到Private Score影响，因此该模型不能直接表述为比赛意义上的“最终最优模型”。后续若继续优化，可以进一步引入交叉验证、超参数搜索、概率校准、特征筛选以及LightGBM、XGBoost、CatBoost和RandomForest的模型集成，以进一步提升模型稳定性和线上泛化表现。

## 5.最终模型选择与项目结论

本项目围绕恒星类型三分类任务，依次完成了数据探索、基准模型构建、颜色指数特征工程、模型对比和LightGBM调参。分类目标包括`GALAXY`、`QSO`和`STAR`三类。

实验结果表明，DummyClassifier的Macro F1仅为0.263558，只能作为最低基准。RandomForest+颜色指数特征模型取得了较好的分类效果，线下Macro F1为0.944721，Kaggle Public Score为0.94506。进一步引入LightGBM后，模型性能明显提升。LightGBM+颜色指数特征模型在线下验证集上的Accuracy为0.967515，Balanced Accuracy为0.954901，Macro F1为0.956350，对应Kaggle Public Score为0.95719，是当前所有提交中表现最好的模型。

随后，本文对LightGBM进行了5折交叉验证和小范围调参。调参后的LightGBM CV tuned模型取得OOF Macro F1=0.957276，略高于单次LightGBM验证结果。但其Kaggle Public Score为0.95711，低于单次LightGBM模型的0.95719。因此，本文最终仍选择`lgbm_color_submission.csv`对应的LightGBM+颜色指数特征模型作为当前最佳提交模型。

主要模型对比如下：

| 模型                | 特征集合        |                  线下指标 | Kaggle Public Score |
| ----------------- | ----------- | --------------------: | ------------------: |
| DummyClassifier   | 多数类基准       |     Macro F1=0.263558 |                 未提交 |
| RandomForest      | 原始特征+颜色指数特征 |     Macro F1=0.944721 |             0.94506 |
| LightGBM          | 原始特征+颜色指数特征 |     Macro F1=0.956350 |         **0.95719** |
| LightGBM CV tuned | 原始特征+颜色指数特征 | OOF Macro F1=0.957276 |             0.95711 |

综合来看，颜色指数特征`u_g`、`g_r`、`r_i`和`i_z`能够补充不同光度波段之间的差异信息，对天体类别识别具有一定帮助。LightGBM相比RandomForest更适合该结构化表格数据，能够更好地刻画特征之间的非线性关系，因此取得了更优的线下和线上表现。

最终，本文选择LightGBM+颜色指数特征模型作为当前项目的最终模型，提交文件为：

```text
submissions/lgbm_color_submission.csv
```

最终Kaggle Public Score为：

```text
0.95719
```

后续如果继续优化，可以尝试XGBoost、CatBoost或多模型集成；但从当前项目完整性来看，已有实验链条较为清晰，模型效果也已经优于主要基准模型，适合作为本项目的最终建模结果。
