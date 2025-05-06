from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field


class MyCustomToolInput(BaseModel):
    """自定义工具的输入架构。"""
    argument: str = Field(..., description="参数的描述。")

class MyCustomTool(BaseTool):
    name: str = "我的工具名称"
    description: str = (
        "清晰描述这个工具的用途，您的智能体需要这些信息才能使用它。"
    )
    args_schema: Type[BaseModel] = MyCustomToolInput

    def _run(self, argument: str) -> str:
        # 在这里实现功能
        return "这是一个工具输出的示例，忽略它并继续。"
