from Text2JSON.predict.prediction import Predict
from Text2JSON.entity_named_recog.entity_recognition import entity_recognition
import os
import json
if __name__ == '__main__':
    # 设置GPU环境
    os.environ["CUDA_VISIBLE_DEVICES"] = '0'
    # 客户端模型路径
    model_path = 'output/model.pt'
    # 初始化模型
    predict_er = Predict()
    # 加载模型
    predict_er.load_model(model_path)
    # 将模型加载到CPU
    # predict_er.load_to_cpu()
    # 将模型加载到GPU
    predict_er.load_to_gpu()
    # 问句
    question = '有“执行回购业务”经验的的律师有哪些'
    # 对问句进行预处理，进行时间识别，单位识别
    handle_question = entity_recognition(question)
    # 生成JSON语句
    result = predict_er.predict(handle_question, size=50)
    print('字典格式:', result)
    print('json格式:', json.dumps(result, ensure_ascii=False))
