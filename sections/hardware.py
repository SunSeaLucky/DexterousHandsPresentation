from execute_util import text


def present():
    text("## 硬件")
    text("灵巧手的硬件部分先建立三个观察维度：结构、驱动、传感。")

    degrees_of_freedom = 20  # @inspect degrees_of_freedom
    text("- 结构：自由度、手指布局、掌部机构、腕手连接。")
    text("- 驱动：电机、腱绳、齿轮、液压/气动，以及力控能力。")
    text("- 传感：触觉、关节编码器、力/扭矩、视觉与本体感知。")

    text("这一部分后续可以补：代表性硬件对比表、拆解图、成本/可靠性分析。")
