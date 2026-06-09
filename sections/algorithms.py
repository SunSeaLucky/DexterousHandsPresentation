from execute_util import text


def present():
    text("## 算法")
    text("算法部分先按从感知到控制的链路组织：状态估计、策略学习、仿真到现实。")

    pipeline = ["perception", "policy", "sim2real"]  # @inspect pipeline
    text("- 感知与状态估计：手部姿态、物体状态、接触状态。")
    text("- 策略学习：模仿学习、强化学习、扩散策略、视觉语言动作模型。")
    text("- Sim2Real：域随机化、系统辨识、残差控制、数据闭环。")

    text("这一部分后续可以补：经典论文脉络、训练数据、benchmark 与失败案例。")
