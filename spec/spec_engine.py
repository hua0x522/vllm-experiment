from vllm.spec.config import (CacheConfig, SSMModelConfig, LLMModelConfig,
                              ParallelConfig, SchedulerConfig)
from typing import List
from vllm.spec.llm_executor import LLMExecutor
from vllm.spec.ssm_executor import SSMExecutor
from vllm.spec.mem_manager import MemManager
from vllm.spec.scheduler import Scheduler


class SpecEngine:
    
    def __init__(
        self,
        ssm_model_config: List[SSMModelConfig],
        llm_model_config: LLMModelConfig,
        cache_config: CacheConfig,
        parallel_config: ParallelConfig,
        scheduler_config: SchedulerConfig,
    ) -> None:
        self.ssm_model_config = ssm_model_config
        self.llm_model_config = llm_model_config
        self.cache_config = cache_config
        self.parallel_config = parallel_config
        self.scheduler_config = scheduler_config
        
        # 这里可能可以复用vllm的SequenceGroup 需要再看看
        self.pending_group = List[str]
        self.running_group = List[str]
        
        # 中间结果池 格式为 request_id, output_token_id 
        self.request_pool = Dict[str, List[str]]
        
        self.ssm_distribution = self._get_ssm_distribution()
        self.ssm_executor = SSMExecutor(ssm_model_config, self.ssm_distribution)
        self.llm_executor = LLMExecutor(llm_model_config, parallel_config)
        self.mem_manager = MemManager(cache_config)
        self.scheduler = Scheduler(scheduler_config)
    
    def _get_ssm_distribution(self) -> Dict[str, List[str]]:
        # todo:
        # a. 将小模型在GPU上进行均分，返回的Dict每项格式为(小模型id, gpu id list)    
    
    def run(self) -> None:
        # todo:
        # a. 大/小模型执行后请求新schedule scheduler.get_SSM_schedule() scheduler.get_LLM_schedule()
        # b. 对于小模型根据schedule从pending_group/running group中拿input get_ssm_request()；对于大模型，从request_pool中拿input get_llm_request();
        # c. 大/小模型执行 ssm_executor.execute() llm_executor.execute() 
        # d. 重复上述过程直至两个请求队列均为空

    # 如果用了SequenceGroup，返回的应该是Sequence
    def get_ssm_request(self, bs) ->  List[str]:   
        # todo:
        # a. 先去查running_list，如果有bs个请求则返回
        # b. 如果running_list中请求数num<bs，则再从pending_list中获取bs-num个请求一起返回
        
    def get_llm_request(self, bs) ->  List[str]:   
        # todo:
        # a. 从request_pool中拿bs个request
    