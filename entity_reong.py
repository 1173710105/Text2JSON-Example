from Text2JSON.entity_named_recog.entity_recognition import entity_recognition

if __name__ == '__main__':
    # 问句
    question = '明年第一季度销售合同签了多少了'
    # 对问句进行预处理，进行时间识别，单位识别
    handle_question = entity_recognition(question)
    print(handle_question)

    question = '“北京慧点科技有限公司”近一个月内发生的风险事件有哪些'
    # 对问句进行预处理，进行时间识别，单位识别
    handle_question = entity_recognition(question)
    print(handle_question)

    question = '帮我导出今年上半年新发案件的台账，包含案件名称、案件编号、涉案金额、原告、被告、第三人'
    # 对问句进行预处理，进行时间识别，单位识别
    handle_question = entity_recognition(question)
    print(handle_question)

    question = '明天上午十二点到下午两点'
    # 对问句进行预处理，进行时间识别，单位识别
    handle_question = entity_recognition(question)
    print(handle_question)

    question = '下月1日到15日'
    # 对问句进行预处理，进行时间识别，单位识别
    handle_question = entity_recognition(question)
    print(handle_question)
