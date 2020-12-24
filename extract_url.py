from Text2JSON.preprocess_data.extract_schema import extract

if __name__ == '__main__':
    # 标注的训练数据集 和 验证数据集，可支持从多个数据集中抽取URL
    source = ['data_raw/raw_train_data.jsonl', 'data_raw/raw_dev_data.jsonl']
    # 自动标注URL数据文件存放位置
    target = 'data_raw/auto_schema.jsonl'
    # 自动标注URL数据集
    extract(source, target)

