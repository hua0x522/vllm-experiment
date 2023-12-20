from vllm.spec.config import (LLMModelConfig, ParallelConfig) 
from typing import Dict, List
import torch.multiprocessing as mp


class LLMExecutor():
    def __init__(
        self,
        llm_model_config: LLMModelConfig,
        parallel_config: ParallelConfig,
    ) -> None:
        
        self.llm_model_config = llm_model_config
        self.parallel_config = parallel_config
        self.pipe_dict = self._create_model()
    
    def _create_model(self, llm_model_config, parallel_config) -> (Dict[str, mp.Pipe]):
        # todo:
        # a. 建并行度个双向pipe
        # b. 根据parallel_config信息起并行度个worker，根据llm_model_config信息对模型进行init(warmup)
        # c. 返回建立好的pipe，格式为(gpu_id, 对应的pipe)
        
    def execute(self, schedule, input) -> None:
        # todo:
        # a. schedule解析
        # b. 将schedule通过pipes传给workers，从而启动执行
            