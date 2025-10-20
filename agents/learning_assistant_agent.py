from agents.base_agent import BaseAgent
from tools.learning_tool import LearningResourceTool
from core.config import Config


class LearningAssistantAgent(BaseAgent):
    """
    个性化学习助手 Agent，根据用户的学习进度和兴趣提供学习资源和解答疑问
    """
    
    def __init__(self, config: Config):
        """
        初始化学习助手 Agent
        
        Args:
            config (Config): 配置对象
        """
        super().__init__(config)
        self.add_tool(LearningResourceTool())
        # 初始化用户学习档案（简单使用内存存储，实际应使用数据库）
        self.user_profiles = {}

    def process_request(self, user_input: str) -> str:
        """
        处理学习相关请求
        
        Args:
            user_input (str): 用户输入的学习请求
            
        Returns:
            str: 学习助手的响应
        """
        import re
        
        # 检测是否是学习相关请求
        learning_keywords = ["学习", "课程", "教程", "推荐", "练习", "题目", "question", "learn", "study", "education"]
        if any(keyword in user_input.lower() for keyword in learning_keywords):
            # 检测用户ID（在真实场景中，这将来自用户认证系统）
            user_id = getattr(self, 'current_user_id', 'default_user')
            
            # 解析用户请求以获取主题
            subject = self._extract_subject(user_input)
            
            # 使用学习工具
            learning_tool = self.tools[0]  # 假设学习工具是第一个
            params = {
                "query": user_input,
                "subject": subject,
                "user_id": user_id
            }
            
            result = learning_tool.execute(params)
            return result
        else:
            return "我是个性化学习助手，可以根据您的兴趣和进度推荐学习资源，解答学习问题。"
    
    def _extract_subject(self, user_input):
        """
        从用户输入中提取学习主题
        """
        import re
        
        user_lower = user_input.lower()
        
        # 优先使用关键词匹配
        if 'python' in user_lower:
            return 'python'
        elif 'ai' in user_lower or '人工智能' in user_lower or '机器学习' in user_lower or 'ml' in user_lower:
            return 'ai'
        elif 'web' in user_lower or '前端' in user_lower or 'react' in user_lower or 'javascript' in user_lower or 'js' in user_lower:
            return 'web'
        
        # 如果关键词匹配失败，尝试正则匹配
        topic_match = re.search(r'学习(.+?)|推荐(.+?)学习|学习(.+?)资源|tutorial on ([^|]+)|learn ([^|]+)|练习(.+?)|(.+?)练习|(.+?)题目', user_input)
        subject = None
        if topic_match:
            # 提取第一个非空匹配组
            groups = topic_match.groups()
            subject = next((group for group in groups if group is not None and group.strip()), None)
            
            if subject:
                subject = subject.strip()
        
        return subject