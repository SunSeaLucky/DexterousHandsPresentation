from execute_util import link, text
from sections import algorithms, companies, hardware


def main():
    intro()
    companies.present()
    hardware.present()
    algorithms.present()
    closing()


def intro():
    text("# 自我介绍")
    text("- 孙海洋")
    text("- 本科毕业（今年 6 月）于新疆大学，硕士就读于浙江大学")
    text("- 2025.10~2026.6 具身智能研究")
    text("# 分享内容概览")

    # sections = ["硬件", "公司", "算法"]  # @inspect sections
    text("- 公司、硬件、算法")
    # text("展示形式参考 executable lecture：内容是 Python 程序，运行后生成可交互 trace。")
    # link(hardware.present)


def closing():
    text("## 后续填充顺序")
    text("1. 先补每部分的问题清单和代表案例。")
    text("2. 再补图片、论文、公司产品页和数据表。")
    text("3. 最后收敛成适合分享的叙事顺序。")


if __name__ == "__main__":
    main()
