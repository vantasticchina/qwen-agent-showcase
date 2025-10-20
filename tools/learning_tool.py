import random
from tools.base_tool import BaseTool
from typing import Dict, Any


class LearningResourceTool(BaseTool):
    """
    学习资源工具，用于推荐学习资源和生成练习题
    """
    
    def __init__(self):
        """
        初始化学习资源工具
        """
        super().__init__("learning_resource", "Recommend learning resources and generate practice exercises")

        # 模拟学习资源库
        self.resource_library = {
            "python": [
                {"title": "Python基础教程", "url": "https://example.com/python-basics", "type": "tutorial"},
                {"title": "Python进阶指南", "url": "https://example.com/python-advanced", "type": "tutorial"},
                {"title": "Python实战项目", "url": "https://example.com/python-projects", "type": "project"},
            ],
            "ai": [
                {"title": "人工智能入门", "url": "https://example.com/ai-intro", "type": "course"},
                {"title": "机器学习基础", "url": "https://example.com/ml-basics", "type": "tutorial"},
                {"title": "深度学习原理", "url": "https://example.com/dl-principles", "type": "tutorial"},
            ],
            "web": [
                {"title": "前端开发入门", "url": "https://example.com/frontend-basics", "type": "tutorial"},
                {"title": "React实战", "url": "https://example.com/react-practice", "type": "course"},
                {"title": "JavaScript高级特性", "url": "https://example.com/js-advanced", "type": "tutorial"},
            ]
        }
        
        # 模拟练习题库
        self.exercise_library = {
            "python": [
                {"question": "Python中列表和元组有什么区别？", "answer": "列表是可变的，元组是不可变的。"},
                {"question": "如何在Python中创建一个虚拟环境？", "answer": "使用venv模块：python -m venv env_name"},
                {"question": "Python中的装饰器是什么？", "answer": "装饰器是一种设计模式，用于在不修改原函数的情况下增加函数功能。"},
            ],
            "ai": [
                {"question": "什么是过拟合？", "answer": "过拟合是指模型在训练数据上表现很好，但在新数据上表现较差的现象。"},
                {"question": "梯度下降算法的原理是什么？", "answer": "梯度下降通过计算损失函数的梯度，沿着梯度的反方向更新参数来最小化损失。"},
            ]
        }

    def execute(self, params: Dict[str, Any]) -> str:
        """
        执行学习资源推荐或练习题生成
        
        Args:
            params (Dict[str, Any]): 包含查询参数的字典
            
        Returns:
            str: 学习资源或练习题
        """
        query = params.get("query", "")
        subject = params.get("subject", "")
        user_id = params.get("user_id", "default")
        
        # 确定主题
        target_subject = subject.lower() if subject else self._infer_subject_from_query(query)
        
        # 检查是否请求练习题
        if any(keyword in query.lower() for keyword in ["练习", "题目", "question", "test", "quiz", "习题"]):
            return self._generate_exercise(target_subject)
        else:
            return self._recommend_resources(target_subject)

    def _infer_subject_from_query(self, query: str) -> str:
        """
        从查询中推断主题
        
        Args:
            query (str): 用户查询
            
        Returns:
            str: 推断的主题
        """
        query_lower = query.lower()
        if any(keyword in query_lower for keyword in ["python", "py", "编程"]):
            return "python"
        elif any(keyword in query_lower for keyword in ["ai", "人工智能", "机器学习", "ml", "深度学习", "dl"]):
            return "ai"
        elif any(keyword in query_lower for keyword in ["web", "前端", "react", "javascript", "js", "html", "css"]):
            return "web"
        else:
            # 默认返回一个随机主题
            return random.choice(list(self.resource_library.keys()))

    def _recommend_resources(self, subject: str) -> str:
        """
        推荐学习资源
        
        Args:
            subject (str): 学习主题
            
        Returns:
            str: 学习资源推荐
        """
        subject = subject.lower()
        if subject in self.resource_library:
            resources = self.resource_library[subject]
            selected_resources = random.sample(resources, min(2, len(resources)))
            
            result = f"为您推荐以下{subject}学习资源：\n"
            for i, resource in enumerate(selected_resources, 1):
                result += f"{i}. [{resource['title']}]({resource['url']}) - {resource['type']}\n"
            
            return result
        else:
            # 如果找不到特定主题，推荐所有可用主题
            result = f"抱歉，没有找到关于 {subject} 的资源。我们当前提供以下主题的学习资源：\n"
            for topic in self.resource_library.keys():
                result += f"- {topic}\n"
            return result

    def _generate_exercise(self, subject: str) -> str:
        """
        生成练习题
        
        Args:
            subject (str): 学习主题
            
        Returns:
            str: 练习题
        """
        subject = subject.lower()
        if subject in self.exercise_library:
            exercises = self.exercise_library[subject]
            selected_exercise = random.choice(exercises)
            
            result = f"{subject}练习题：\n"
            result += f"问题：{selected_exercise['question']}\n"
            result += f"答案：{selected_exercise['answer']}\n"
            
            return result
        else:
            return f"抱歉，没有找到关于 {subject} 的练习题。我们当前提供以下主题的练习题：{'、'.join(self.exercise_library.keys())}"