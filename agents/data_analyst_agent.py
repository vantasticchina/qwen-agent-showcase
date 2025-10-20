from agents.base_agent import BaseAgent
from tools.data_analysis_tool import DataAnalysisTool
from core.config import Config


class DataAnalystAgent(BaseAgent):
    """
    数据分析师 Agent，专门处理数据分析相关的请求
    """
    
    def __init__(self, config: Config):
        """
        初始化数据分析师 Agent
        
        Args:
            config (Config): 配置对象
        """
        super().__init__(config)
        self.add_tool(DataAnalysisTool())

    def process_request(self, user_input: str) -> str:
        """
        处理数据分析请求
        
        Args:
            user_input (str): 用户输入的数据分析请求
            
        Returns:
            str: 数据分析结果
        """
        # 检查输入是否包含数据分析相关关键词
        if any(keyword in user_input.lower() for keyword in ["分析", "analyze", "统计", "statistics", "数据", "data"]):
            # 检查是否包含数据源信息
            import re
            path_match = re.search(r'数据路径[:：]\s*([^\s,;]+)', user_input) or \
                            re.search(r'data path[:：]\s*([^\s,;]+)', user_input) or \
                            re.search(r'([^\s,;]+\.(csv|xlsx|json))', user_input)
            
            if path_match:
                data_path = path_match.group(1)
                # 使用数据分析工具
                analysis_tool = self.tools[0]  # 假设数据分析工具是第一个
                result = analysis_tool.execute({"data_path": data_path, "query": user_input})
                return result
            else:
                return "请提供数据分析的路径或文件名。"
        else:
            return "我是数据分析助手，可以帮您分析数据文件并提供洞察。"