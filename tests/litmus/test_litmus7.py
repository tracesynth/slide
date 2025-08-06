import os
import subprocess

def run_cmd(file_name):
# 定义要执行的命令
    command = [
        "litmus7",
        "-mach", "/home/whq/Desktop/slide/tests/litmus/riscv.cfg",  # 指定配置文件
        "-avail", "4",           # 指定可用线程数
        file_name,  # 指定litmus测试文件
        "-o", "SB"               # 指定输出文件夹或输出名
    ]

    try:
        # 使用 subprocess.run 来执行命令并等待完成
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # 输出执行结果
        print("Command executed successfully:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        # 捕获并打印错误信息
        print("Command failed with error:")
        print(e.stderr)

def create_folders_for_litmus_files(directory):
    # 检查指定的目录是否存在
    if not os.path.exists(directory):
        print(f"The directory '{directory}' does not exist.")
        return
    
    # 使用 os.walk 遍历文件夹及其子文件夹
    for root, dirs, files in os.walk(directory):
        for filename in files:
            # 检查文件是否为 .litmus 后缀
            if filename.endswith('.litmus'):
                folder_name = os.path.splitext(filename)[0]  # 去掉文件扩展名
                new_folder_path = os.path.join(directory, folder_name)
                
                # 如果文件夹不存在则创建
                if not os.path.exists(new_folder_path):
                    os.makedirs(new_folder_path)
                    print(f"Created folder: {new_folder_path}")
                else:
                    print(f"Folder '{new_folder_path}' already exists.")
            else:
                print(f"'{filename}' is not a .litmus file, skipping.")

        # run cmd
        run_cmd(filename)


# 指定要扫描的目录
directory_path = "/home/whq/Desktop/slide/tests/input/litmus/manual"



if __name__ == '__main__':
    create_folders_for_litmus_files(directory_path)