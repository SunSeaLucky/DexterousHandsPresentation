from execute_util import text, image, link


def present():
    text("## 硬件")
    human_hands_and_dexterous_hands()
    drive_method()
    history()

def human_hands_and_dexterous_hands():
    text("## 人手与灵巧手")
    
    text("### 自由度定义")
    text("在物理学和化学中：考虑一个物理系统，**自由度**指：**能够确定所选参数化方案中所有参数值，而被需要的最少参数数量**。来自："), link("https://en.wikipedia.org/wiki/Degrees_of_freedom_(physics_and_chemistry)")
    text("在机器人学中：机器人机构所具有的独立驱动运动（或独立运动输入）的数目")
    
    text("### 自由度与人手")
    image("images/human_finger.png",width=800)
    text("人手结构：腕骨、掌骨、指骨（近节指骨、中节指骨、远节指骨)")
    text("主流观点一般认为人手有 21 个自由度（不包括手腕关节），最严谨的答案是 27 个（包括手腕关节）。来自："), link("https://www.dgp.toronto.edu/~gelkoura/noback/scapaper03.pdf")
    
    text("### 自由度与灵巧手")
    text("在三维空间中，一个物体不受约束，有 6 个自由度：`(x, y, z, roll, yaw, pitch)` ")
    text("**主动自由度**。系统中直接由驱动器（e.g. 电机）驱动的自由度")
    text("**被动自由度**。不由驱动器直接驱动，与主动自由度耦合联动。")
    text("**欠驱动系统**。存在被动自由度的系统")
    
def drive_method():
    text("## 灵巧手的驱动方式")
    
    text("### 直驱")
    
    text("### 绳驱 / 肌腱 / 腱绳")
    
    text("电机安装在手掌或前臂，通过拉紧 / 放松绳索控制手指弯曲和伸展")
    image("images/linkerbot_l30.png")
    text("手指部分轻巧，适合高自由度复杂动作。绳索易磨损，需要定期维护")
    
    text("### 连杆灵巧手")
    
    text("分为 **串联** 和 **并联**")
    
    text("### 新材料驱动")
    
def history():
    text("## 发展历史")