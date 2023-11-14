class Params(object):
    # ----训练相关参数----#
    train_dir = "./cartoon_portrait"  # 数据集存放路径
    output_dir = "./output"  # 生成图片和模型的保存路径
    num_workers = 2  # 多进程加载数据所用的进程数
    img_size = 96  # 图片尺寸
    batch_size = 256  # 批大小
    epoch = 200  # 最大训练轮数
    lr_g = 0.001  # 生成器的学习率
    lr_d = 0.001  # 判别器的学习率
    use_gpu = True  # 是否使用GPU
    nz = 100  # 输入噪声维度
    print_step = 10  # 每多少次迭代输出一次信息
    output_step = 1  # 每多少轮训练输出一次模型和生成图片

    # ----测试相关参数----#
    generated_img_name = "generated_img"  # 生成图片名
    generated_img_num = 64  # 生成图片数量，不大于一个batch_size

