from execute_util import text, image


def present():
    text("## 算法")
    reinforce_learning()
    imitation_learning()

def reinforce_learning():
    text("核心思想: 通过试错 + 奖励让机器人自主探索出最优操作策略。")
    text("优势: 强大的自适应能力,可以应对复杂环境和不确定性 劣势: 训练时间长,需要大量仿真或真实试错")

    simulated_world()
    real_world()

def imitation_learning():
    directly_from_video()
    data_synthesis()
    teleoperate()
    across_domain_foundation_model()
    post_rl()
    
def directly_from_video():
    text("- Robotic Telekinesis")
    image("images/Robotic_Telekinesis.png", width=800)
    
def data_synthesis():
    text("- retarget")
    text("- D(R,O) Grasp")
    text("- DexGarmentLab")
    text("- DemoGrasp")
    image("images/demo_grasp.png", width=800)
    
def teleoperate():
    text("- 【2024】Tilde。遥操作数据+Diffusion Policy")
    image("images/tilde.png", width=800)
    text("- 【2024】3D Diffusion Policy")
    image("images/3D_Diffusion_Policy.png", width=800)

def across_domain_foundation_model():
    text("NVIDIA GR00T N1、Video Prediction Policy（星动纪元）、π0.5、wall-x（自变量）、Gen0（Generalist AI）")
    text("- BeingH0")
    image("images/being-h0.png", width=800)
    image("images/tokenizer.png")
    text("- DexGraspVLA (cite: 102)")
    image("images/DexGraspVLA.png", width=800)
    text("- UniDex (cite: 4)")
    image("images/UniDex.png", width=800)
    
def post_rl():
    text("- DEXNDM")
    image("images/post_rl.png", width=800)
    text("- DAgger、RECAP")

def retarget():
    text("### 有参考轨迹引导与重定向算法")
    text("- 重定向定义。将一个源对象（通常是人类）的运动数据，经过数学转换后，迁移到一个具有不同尺寸、骨骼比例甚至不同物理结构的目标对象（如虚拟角色、机器人）上，并尽可能保留原动作的意图和神态")
    text("- 应用领域。影视特效与游戏动画、虚拟现实与虚拟主播、机器人模仿学习")
    text("#### 直接关节映射与直接笛卡尔映射")
    text("- 直接关节映射。优点：计算简单。缺点：非线性偏移，无法形成有效的闭合力封闭")
    text("- 直接笛卡尔映射。优点：稍微准了点。缺点：位置对了，但接触法线不对，导致螺旋轴漂移")
    text("#### 现代方法")
    image("images/video_rl.png", width=600)
    text("- 【2022】DexVIP")
    image("images/DexVIP.png", width=800)
    text("- 【2025】**ManipTrans**。模仿学习粗糙手部动作，强化学习网络学残差")
    image("images/maniptrans.png", width=800)
    text("- 【2025】**DexMachina**。PD 控制器增加辅助力")
    image("images/dexmachina.png", width=800)
    image("images/retarget.png", width=800)

def naive_direct_learning():
    text("## 非真机（PPO / SAC）")
    text("### 无参考轨迹引导")
    image("images/rl.png", width=600)
    text("- 【2024】**RoboPianist**。1）使用 DroQ；2）Markov?")
    image("images/robopiano.png", width=800)
    text("- 【2025】ClusterDexGrasp")
    image("images/cluster_grasp.png", width=800)

def simulated_world():
    naive_direct_learning()
    retarget()
    
def real_world():
    text("## 真机（样本效率、环境重置、低层电机控制、相机低延迟通信、奖励函数的物理标定）")
    
    text("- 【2024】SERL（https://arxiv.org/pdf/2401.16013）。基于 RLPD、成功/失败分类器、执行/重置两个模型都训练")
    image("images/SERL.png", width=800)
    text("- 【2023】EUREKA 与 DrEureka。将模拟环境的物理代码摘要和简单的任务目标语言描述作为输入，利用LLM出色的代码编写能力生成初始的Python格式的奖励函数代码；随后，系统在仿真中运行该奖励代码进行短期RL训练，提取性能反馈日志，并将其作为上下文再次喂给LLM，进行无梯度的上下文提示进化优化")
    image("images/eureka.png")
    text("- 智元")
    text("- 自变量")
