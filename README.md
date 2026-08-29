# 接口自动化测试框架

基于 Python + pytest + requests + allure 的接口自动化测试框架，实现数据驱动、配置分离、自动生成测试报告。

## 功能特性

- **数据驱动**：测试数据外置到 JSON 文件，通过 pytest 参数化循环执行
- **配置分离**：基础 URL 抽离到 config.py，切换测试环境只需改一处
- **断言验证**：校验接口状态码与响应字段
- **测试报告**：使用 allure 自动生成可视化测试报告，展示用例执行步骤

## 项目结构

```
├── config.py          # 配置文件（基础 URL）
├── test_data.json     # 测试数据（数据驱动）
├── test_api.py        # 测试用例
├── requirements.txt   # 依赖清单
└── allure-results/    # allure 报告数据（运行后生成）
```

## 技术栈

- Python 3
- pytest
- requests
- allure-pytest

## 快速开始

```bash
# 1. 安装依赖
pip install -r requirements.txt

# 2. 运行测试
python -m pytest test_api.py

# 3. 生成 allure 报告
python -m pytest test_api.py --alluredir=./allure-results
allure serve ./allure-results
```

## 测试结果

运行后可见 `4 passed`，可视化测试报告由 allure 自动生成。
