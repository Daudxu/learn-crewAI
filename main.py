from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI
import os

# 如果需要设置API密钥，取消下面的注释
# os.environ["OPENAI_API_KEY"] = "你的OpenAI API密钥"

# 选择语言模型，如果有API密钥，可以使用OpenAI，否则可以使用本地模型
llm = ChatOpenAI(temperature=0.7)  # 默认是gpt-3.5-turbo

# 定义代理（Agents）
researcher = Agent(
    role='研究专家',
    goal='深入分析所给主题并提供全面准确的信息',
    backstory='你是一位经验丰富的研究专家，擅长分析问题和寻找关键信息。',
    verbose=True,
    allow_delegation=True,
    llm=llm
)

analyst = Agent(
    role='数据分析师',
    goal='基于研究结果提供数据洞察和趋势分析',
    backstory='你是一位精通数据的分析师，擅长发现数据背后的模式和意义。',
    verbose=True,
    allow_delegation=True,
    llm=llm
)

writer = Agent(
    role='内容创作者',
    goal='将研究和分析转化为清晰、有吸引力的内容',
    backstory='你是一位才华横溢的写作专家，能将复杂信息转化为引人入胜的故事。',
    verbose=True,
    allow_delegation=True,
    llm=llm
)

# 定义任务（Tasks）
research_task = Task(
    description="""
    研究元宇宙(Metaverse)的最新发展趋势。请考虑以下方面：
    1. 元宇宙的当前定义和范围
    2. 主要科技公司在元宇宙领域的投资和发展
    3. 元宇宙在游戏、社交、工作和教育方面的应用
    4. 元宇宙面临的主要技术挑战
    """,
    agent=researcher,
    expected_output='一份关于元宇宙最新发展趋势的研究报告，包含关键领域和挑战。'
)

analysis_task = Task(
    description="""
    基于研究结果，分析元宇宙发展的潜在商业价值和社会影响：
    1. 识别最有前景的元宇宙应用领域
    2. 分析元宇宙可能带来的经济价值
    3. 评估元宇宙对社会互动和工作方式的潜在影响
    4. 指出可能的风险和伦理问题
    
    使用研究专家提供的信息作为你分析的基础。
    """,
    agent=analyst,
    expected_output='一份关于元宇宙商业价值和社会影响的分析报告。',
    context=[research_task]  # 这个任务依赖于研究任务的结果
)

writing_task = Task(
    description="""
    根据研究和分析报告，撰写一篇题为"元宇宙：重塑数字未来的新范式"的文章。
    文章应当：
    1. 介绍元宇宙的概念和发展历程
    2. 详述主要的技术进展和应用场景
    3. 探讨商业价值和投资机会
    4. 分析社会影响和未来展望
    5. 提出对个人和企业的建议
    
    确保文章内容准确、结构清晰、语言生动。
    """,
    agent=writer,
    expected_output='一篇关于元宇宙的综合性文章，约1500-2000字。',
    context=[research_task, analysis_task]  # 这个任务依赖于前两个任务的结果
)

# 创建一个工作小组(Crew)
metaverse_crew = Crew(
    agents=[researcher, analyst, writer],
    tasks=[research_task, analysis_task, writing_task],
    verbose=2,  # 详细日志级别
    process=Process.sequential  # 按顺序执行任务
)

# 主函数
def main():
    print("启动元宇宙研究团队...")
    result = metaverse_crew.kickoff()
    
    print("\n========== 最终成果 ==========")
    print(result)
    
    # 将结果保存到文件
    with open("metaverse_article.txt", "w", encoding="utf-8") as f:
        f.write(result)
    print("\n结果已保存到 metaverse_article.txt")

if __name__ == "__main__":
    main()