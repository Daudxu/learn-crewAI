#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from hello_world.crew import HelloWorld

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# 此主文件旨在为您提供在本地运行团队的方式，
# 因此请避免在此文件中添加不必要的逻辑。
# 替换为您想要测试的输入，它将自动
# 插入任何任务和智能体信息

def run():
    """
    运行团队。
    """
    inputs = {
        'topic': '人工智能大语言模型',  # 将主题改为中文
        'current_year': str(datetime.now().year)
    }
    
    try:
        HelloWorld().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    为给定的迭代次数训练团队。
    """
    inputs = {
        "topic": "人工智能大语言模型",  # 将主题改为中文
        'current_year': str(datetime.now().year)
    }
    try:
        HelloWorld().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    从特定任务重放团队执行过程。
    """
    try:
        HelloWorld().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    测试团队执行并返回结果。
    """
    inputs = {
        "topic": "人工智能大语言模型",  # 将主题改为中文
        "current_year": str(datetime.now().year)
    }
    
    try:
        HelloWorld().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
