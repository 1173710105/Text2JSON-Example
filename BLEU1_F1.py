import os
from Text2JSON.train.evaluator import eval_bleu1_f1
from Text2JSON.predict.prediction import Predict
if __name__ == '__main__':
    # 设置GPU环境
    os.environ["CUDA_VISIBLE_DEVICES"] = '0'
    # 客户端模型路径
    model_path = 'output/model.pt'
    # 初始化模型
    predict_er = Predict()
    # 加载模型
    predict_er.load_model(model_path)
    # 将模型加载到GPU
    predict_er.load_to_gpu()
    # 需要进行F1 测试的标注数据集存放路径，一般用标注的验证集
    label_path = 'data_raw/raw_dev_data.jsonl'
    # 结果输出路径
    output_path = 'output/test_out.jsonl'
    # 验证模型 BLEU1 和 F1
    bleu1, f1 = eval_bleu1_f1(predict_er, label_path, output_path)
