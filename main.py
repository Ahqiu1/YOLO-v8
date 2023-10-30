from ultralytics import YOLO

if __name__ == '__main__':
    # 直接使用预训练权重或yaml文件创建模型
    model = YOLO('yolov8n.pt')
    model.train(**{'cfg': 'ultralytics/cfg/default.yaml', 'data': r"D:\Dataset\Pothole\dataset-train2+4+5-test3\VOCdevkit_Aug4\Dataset\data_Aug4.yaml"})

    #使用预训练权重+配置文件创建模型
    # model = YOLO(r'E:\knowledge\YOLO-v8\ultralytics-main\ultralytics\cfg\models\v8\yolov8-dysnakeconv.yaml')
    # model.load('yolov8n.pt')
    # model.train(**{'cfg': 'ultralytics/cfg/default.yaml', 'data': r"D:\Dataset\Pothole\dataset-train2+4+5-test3\VOCdevkit_Aug4\Dataset\data_Aug4.yaml"})

    # # 模型验证
    # model = YOLO('runs/detect/yolov8n_exp/weights/best.pt')
    # model.val(**{'data': 'dataset/data.yaml'})
    #
    # # 模型推理
    # model = YOLO('runs/detect/yolov8n_exp/weights/best.pt')
    # model.predict(source='dataset/images/test', **{'save': True})