from vllm.spec.config import SSMModelConfig 
from typing import Dict, List
import torch.multiprocessing as mp


class SSMExecutor():
    def __init__(
        self,
        ssm_model_config: List[SSMModelConfig],
        ssm_distribution: Dict[str, List[str]],
    ) -> None:
        
        self.ssm_model_config = ssm_model_config
        self.ssm_pipes = Dict[str, Dict[gpu_id, mp.Pipe]]
    
        for ssm in ssm_model_config:
            model_id = ssm.get_model_id()
            gpu_id_list = ssm_distribution[model_id]
            model_id, pipe = self._create_model(ssm, gpu_id_list)
            self.ssm_pipes[model_id] = pipe
    
    def _create_model(self, ssm, gpu_id_list) -> (str, Dict[gpu_id, mp.Pipe]):
        # todo:
        # a. 建一个双向pipe
        # b. 根据gpu_id_list分别在各个指定GPU上起worker，根据ssm config信息对模型进行init(warmup)
        # c. 返回能够代表模型的模型id以及建立好的pipe(Dict[gpuid, pipe])
        
    def execute(self, model_id, schedule, input) -> None:
        # todo:
        # a. schedule解析，获取对应模型(model_id)&gpu的pipe
        # b. 将schedule通过pipe传给worker，从而启动执行
            
    def finish(self, model_id) -> None:
        # todo: 向对应pipe中传finish指令，使该小模型结束正在执行的推理过程，改为空闲待命