from execute_util import link, text, image
from sections import algorithms, companies, hardware


def main():
    intro()
    companies.present()
    hardware.present()
    algorithms.present()
    closing()


def intro():
    text("## 自我介绍")
    text("- 孙海洋")
    text("- 河南驻马店市，本科毕业（今年 6 月）于新疆大学，硕士就读（今年 9 月）于浙江大学")
    text("- 2025.10~2026.6 具身智能研究")
    text("## 为什么需要灵巧手?")
    text("- 复杂手内操作")
    image("images/cube.png", width=600)
    text("- 现实世界对人手操作更加友好")
    image("images/door.jpg", width=600)
    


def closing():
    image("images/close.png", width=800)


if __name__ == "__main__":
    main()
