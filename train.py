import os
from Text2JSON.train.train_model import ModelTrain

if __name__ == '__main__':
    # 解析后的训练数据存放位置
    train_data_path = 'data/train.jsonl'
    # 解析后的验证数据存放位置
    dev_data_path = 'data/dev.jsonl'
    # 解析后的 URL 数据集存放的路径
    schema_path = 'data/schema.jsonl'
    # 语言预训练模型存放位置
    bert_path = 'chinese_roberta'
    # 配置文件路径
    conf_path = 'conf/model.conf'
    # 模型输出路径
    output_path = 'output'
    # 设置GPU环境
    os.environ["CUDA_VISIBLE_DEVICES"] = '0'
    # 加载模型
    c_model = ModelTrain(conf_path, output_path, train_data_path,
                         dev_data_path, schema_path, bert_path)
    # 训练
    c_model.train()
    # 导出客户端模型
    c_model.dump_client_model()
