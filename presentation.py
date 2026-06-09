from execute_util import link, text
from sections import algorithms, companies, hardware


def main():
    intro()
    hardware.present()
    companies.present()
    algorithms.present()
    closing()


def intro():
    text("# 灵巧手展示分享")
    text("目标：先搭起一个能持续扩展的展示框架，再逐步补内容、资料和图。")

    sections = ["硬件", "公司", "算法"]  # @inspect sections
    text("框架分成三部分：**硬件**、**公司**、**算法**。")
    text("展示形式参考 executable lecture：内容是 Python 程序，运行后生成可交互 trace。")
    text("内部跳转示例："), link(hardware.present)


def closing():
    text("## 后续填充顺序")
    text("1. 先补每部分的问题清单和代表案例。")
    text("2. 再补图片、论文、公司产品页和数据表。")
    text("3. 最后收敛成适合分享的叙事顺序。")


if __name__ == "__main__":
    main()
