#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

# 让中文显示更整齐
pd.set_option("display.unicode.east_asian_width", True)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 200)

# ============================================================
# 1. 员工数据：按部门统计人数、平均薪资、离职率
# ============================================================

employees = pd.DataFrame({
    "员工ID": [1001, 1002, 1003, 1004, 1005, 1006,
              1007, 1008, 1009, 1010, 1011, 1012],
    "部门": ["人力资源部", "人力资源部", "人力资源部",
            "技术部", "技术部", "技术部", "技术部",
            "市场部", "市场部", "市场部",
            "财务部", "财务部"],
    "月薪": [8000, 8500, 9000,
            15000, 16000, 17000, 18000,
            10000, 11000, 12000,
            9500, 10000],
    # 1 表示离职，0 表示在职
    "是否离职": [0, 1, 0,
               1, 0, 1, 0,
               0, 1, 0,
               0, 1],
})

print("=" * 60)
print("原始员工数据")
print(employees)

# groupby：按“部门”分组，然后聚合计算
dept_stats = (
    employees
    .groupby("部门", as_index=False)
    .agg(
        员工人数=("员工ID", "count"),
        平均月薪=("月薪", "mean"),
        离职人数=("是否离职", "sum"),
    )
)

# 计算离职率 = 离职人数 / 员工人数
dept_stats["离职率"] = dept_stats["离职人数"] / dept_stats["员工人数"]

# 先排序，再格式化显示
dept_stats = dept_stats.sort_values("离职率", ascending=False)

dept_stats["平均月薪"] = dept_stats["平均月薪"].round(0).astype(int)
dept_stats["离职率"] = (dept_stats["离职率"] * 100).round(1).astype(str) + "%"

print("=" * 60)
print("按部门统计：人数 / 平均月薪 / 离职人数 / 离职率")
print(dept_stats)


# ============================================================
# 2. 招聘数据：按渠道统计各环节转化率
# ============================================================

recruit = pd.DataFrame({
    "月份": ["1月", "1月", "1月",
            "2月", "2月", "2月",
            "3月", "3月"],
    "渠道": ["BOSS直聘", "智联招聘", "内部推荐",
            "BOSS直聘", "智联招聘", "内部推荐",
            "BOSS直聘", "内部推荐"],
    "简历数": [100, 80, 30,
             120, 90, 40,
             110, 50],
    "面试数": [20, 12, 15,
             25, 14, 20,
             22, 25],
    "录用数": [5, 3, 8,
             6, 4, 10,
             5, 12],
    "入职数": [4, 2, 7,
             5, 3, 9,
             4, 11],
})

print("=" * 60)
print("原始招聘渠道数据")
print(recruit)

# groupby：按“渠道”汇总各环节人数
channel_stats = (
    recruit
    .groupby("渠道", as_index=False)
    .agg(
        简历数=("简历数", "sum"),
        面试数=("面试数", "sum"),
        录用数=("录用数", "sum"),
        入职数=("入职数", "sum"),
    )
)

# 计算各环节转化率
channel_stats["简历到面试率"] = channel_stats["面试数"] / channel_stats["简历数"]
channel_stats["面试到录用率"] = channel_stats["录用数"] / channel_stats["面试数"]
channel_stats["录用到入职率"] = channel_stats["入职数"] / channel_stats["录用数"]
channel_stats["总转化率"] = channel_stats["入职数"] / channel_stats["简历数"]

# 按总转化率从高到低排序
channel_stats = channel_stats.sort_values("总转化率", ascending=False)

# 把比例转成百分比显示
for col in ["简历到面试率", "面试到录用率", "录用到入职率", "总转化率"]:
    channel_stats[col] = (channel_stats[col] * 100).round(1).astype(str) + "%"

print("=" * 60)
print("按招聘渠道统计：各环节转化率")
print(channel_stats)


# ============================================================
# 3. 保存结果到 CSV
# ============================================================

dept_stats.to_csv("部门统计.csv", index=False, encoding="utf-8-sig")
channel_stats.to_csv("招聘渠道统计.csv", index=False, encoding="utf-8-sig")

print("=" * 60)
print("已保存：部门统计.csv 和 招聘渠道统计.csv")


# In[2]:


employees.groupby("部门")["是否离职"].mean()

