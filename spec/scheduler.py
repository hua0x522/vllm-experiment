from typing import Optional
from vllm.spec.config import (CacheConfig, SchedulerConfig)

class Schedule():
    def __init__(
        self,
        batch_size: int,
        step: Optional[int],
        ssm_model_list: Optional[str]
    ) -> None:
        self.batch_size = batch_size
        if step is not None:
            self.step = step
        if ssm_model_list is not None:
            self.ssm_model_list = ssm_model_list
        
        
# 模型执行相关部分同vllm scheduler，需要自己注入调度策略
class Scheduler():
    def __init__(
        self,
        scheduler_config: SchedulerConfig,
        cache_config: CacheConfig,
    ) -> None:
        self.scheduler_config = scheduler_config
        self.cache_config = cache_config
        
        # todo，将vllm模型执行相关部分择过来
    
    def get_ssm_peak_mem(self, schedule) -> int:
        # todo 根据schedule信息预测如果以这个schedule来执行某个小模型 小模型所在GPU上会达到的峰值显存
        
    def get_llm_peak_mem(self, schedule) -> Dict[str, int]:
        # todo 根据schedule信息预测如果以这个schedule来执行大模型 各个GPU上会达到的峰值显存, 返回格式为(gpu id, 该GPU上峰值显存)
    
    def get_SSM_schedule(self) -> Schedule:
        # todo return schedule
        
    def get_LLM_schedule(self) -> Schedule:
        # todo return schedule
        
    