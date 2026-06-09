from execute_util import text


def present():
    text("## 公司")
    text("公司部分先按产品定位拆开：机器人本体公司、灵巧手供应商、平台/研究机构。")

    company_groups = ["机器人本体", "灵巧手供应商", "平台与研究机构"]  # @inspect company_groups
    text("- 机器人本体：关注整机任务、量产能力、应用场景。")
    text("- 灵巧手供应商：关注手部硬件指标、控制接口、生态兼容。")
    text("- 平台/研究机构：关注开源数据、仿真环境、基准任务。")

    text("这一部分后续可以补：公司清单、核心产品、融资/客户/技术路线。")
