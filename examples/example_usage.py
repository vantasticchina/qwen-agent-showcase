from agents.weather_agent import WeatherAgent
from agents.data_analyst_agent import DataAnalystAgent
from agents.learning_assistant_agent import LearningAssistantAgent
from agents.customer_service_agent import CustomerServiceAgent
from core.config import Config


def example_weather_agent():
    """
    天气查询 Agent 示例
    """
    print("=== 天气查询 Agent 示例 ===")
    
    # 创建配置
    config = Config({
        "model": "qwen-plus",
        "temperature": 0.7
    })
    
    # 创建天气 Agent
    weather_agent = WeatherAgent(config)
    
    # 测试查询
    queries = [
        "北京的天气怎么样？",
        "明天上海天气如何？",
        "广州的天气"
    ]
    
    for query in queries:
        print(f"\n用户: {query}")
        response = weather_agent.get_response(query)
        print(f"Agent: {response}")


def example_data_analyst_agent():
    """
    数据分析师 Agent 示例
    """
    print("\n=== 数据分析师 Agent 示例 ===")
    
    # 创建配置
    config = Config({
        "model": "qwen-plus",
        "temperature": 0.7
    })
    
    # 创建数据分析师 Agent
    analyst_agent = DataAnalystAgent(config)
    
    # 模拟数据文件路径（这里使用一个不存在的路径作为示例）
    query = f"请分析数据，数据路径: sample_data.csv"
    
    print(f"用户: {query}")
    response = analyst_agent.get_response(query)
    print(f"Agent: {response}")


def example_learning_assistant_agent():
    """
    个性化学习助手 Agent 示例
    """
    print("\n=== 个性化学习助手 Agent 示例 ===")
    
    # 创建配置
    config = Config({
        "model": "qwen-plus",
        "temperature": 0.7
    })
    
    # 创建学习助手 Agent
    learning_agent = LearningAssistantAgent(config)
    learning_agent.current_user_id = "user123"  # 模拟用户ID
    
    # 测试学习相关查询
    queries = [
        "推荐一些Python学习资源",
        "我想学习人工智能，有什么课程吗？",
        "给我出一道Python练习题"
    ]
    
    for query in queries:
        print(f"\n用户: {query}")
        response = learning_agent.get_response(query)
        print(f"Agent: {response}")


def example_customer_service_agent():
    """
    智能客服机器人 Agent 示例
    """
    print("\n=== 智能客服机器人 Agent 示例 ===")
    
    # 创建配置
    config = Config({
        "model": "qwen-plus",
        "temperature": 0.7
    })
    
    # 创建客服机器人 Agent
    service_agent = CustomerServiceAgent(config)
    service_agent.current_user_id = "user123"  # 模拟用户ID
    
    # 测试客服相关查询
    queries = [
        "我想查询订单 ORD001 的状态",
        "我的个人信息是什么？",
        "你们的退货政策是什么？",
        "配送需要多长时间？"
    ]
    
    for query in queries:
        print(f"\n用户: {query}")
        response = service_agent.get_response(query)
        print(f"Agent: {response}")


def example_config_usage():
    """
    配置使用示例
    """
    print("\n=== 配置使用示例 ===")
    
    # 创建配置实例
    config = Config({
        "model": "qwen-plus",
        "temperature": 0.7,
        "max_tokens": 1000
    })
    
    print(f"使用的模型: {config.get('model')}")
    print(f"温度设置: {config.get('temperature')}")
    
    # 更新配置
    config.set('temperature', 0.5)
    print(f"更新后的温度设置: {config.get('temperature')}")


if __name__ == "__main__":
    print("Qwen-Agent 示例程序")
    print("=" * 50)
    
    # 运行各个示例
    example_weather_agent()
    example_data_analyst_agent()
    example_learning_assistant_agent()
    example_customer_service_agent()
    example_config_usage()