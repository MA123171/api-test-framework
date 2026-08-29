# 接口自动化测试框架

基于 Python + pytest + requests 的接口自动化测试框架，实现数据驱动、配置分离、自动生成测试报告。

## 功能特性

- **数据驱动**：测试数据外置到 JSON 文件，通过 pytest 参数化循环执行
- **配置分离**：基础 URL 抽离到 config.py，切换测试环境只需改一处
- **断言验证**：校验接口状态码与响应字段
- **测试报告**：使用 pytest-html 自动生成 HTML 测试报告

## 项目结构

```
├── config.py          # 配置文件（基础 URL）
├── test_data.json     # 测试数据（数据驱动）
├── test_api.py        # 测试用例
└── report.html        # 测试报告（运行后生成）
```

## 技术栈

- Python 3
- pytest
- requests
- pytest-html

## 快速开始

```bash
# 1. 安装依赖
pip install requests pytest pytest-html

# 2. 运行测试
python -m pytest test_api.py

# 3. 生成测试报告
python -m pytest test_api.py --html=report.html --self-contained-html
```

## 测试结果

运行后可见 `4 passed`，可视化测试报告见 `report.html`。
