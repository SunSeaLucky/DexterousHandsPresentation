from execute_util import table, text


def present():
    text("## 公司")
    text("公司部分先按产品定位拆开：机器人本体公司、灵巧手供应商、平台/研究机构。")

    table("tables/company.csv")
