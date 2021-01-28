from Text2JSON.preprocess_data.process_raw_schema import gen_processed_schema
from Text2JSON.preprocess_data.process_raw_data import gen_processed_data
if __name__ == '__main__':
    # 标注的 URL 数据集的路径
    url_source = 'data_raw/raw_schema.jsonl'
    # 解析后 URL 数据集存放的路径
    url_target = 'data/schema.jsonl'
    # 处理URL
    gen_processed_schema(url_source, url_target)

    # 标注的 训练数据集存放路径
    train_source = 'data_raw/raw_train_data.jsonl'
    # 解析后的训练数据集存放路径
    train_target = 'data/train.jsonl'
    # 处理训练数据
    gen_processed_data(train_source, train_target, url_target)

    # 标注的 验证数据存放路径
    valid_source = 'data_raw/raw_dev_data.jsonl'
    # 解析后的验证数据集存放路径
    valid_target = 'data/dev.jsonl'
    # 处理验证数据
    gen_processed_data(valid_source, valid_target, url_target)


