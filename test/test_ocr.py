# --- test_ocr.py ---
import ddddocr
import sys
import os

def test_single_image(image_path):
    """
    使用 ddddocr 识别单个图片文件。

    参数:
    image_path (str): 图片文件的路径。
    """
    # 1. 检查文件是否存在
    if not os.path.exists(image_path):
        print(f"错误: 文件 '{image_path}' 不存在。")
        return

    try:
        # 2. 初始化 ddddocr
        # show_ad=False 可以禁用每次运行时打印的广告信息
        ocr = ddddocr.DdddOcr()
        print("DdddOcr 模型已加载。")

        # 3. 读取图片文件
        with open(image_path, 'rb') as f:
            image_bytes = f.read()
        print(f"成功读取图片: {image_path}")

        # 4. 调用 OCR 进行识别
        result = ocr.classification(image_bytes)

        # 5. 在控制台输出结果
        print("\n" + "="*30)
        print("      🚀 识别结果 🚀")
        print("="*30)
        print(f"  图片 '{os.path.basename(image_path)}' 的识别内容是: 【 {result} 】")
        print("="*30)

    except Exception as e:
        print(f"处理图片时发生错误: {e}")


if __name__ == "__main__":
    # 检查命令行是否提供了图片路径参数
    if len(sys.argv) > 1:
        # 如果提供了，使用第一个参数作为图片路径
        file_path = sys.argv[1]
    else:
        # 如果没有提供，提示用户输入
        file_path = input("请输入要识别的图片文件路径 (例如: captcha.jpeg): ")

    test_single_image(file_path)