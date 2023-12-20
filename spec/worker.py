import torch.multiprocessing as mp

# todo continuous batching
class Worker:
    def __init__(
        self,
    ) -> None:
        
    def run_ssm(self, pipe):
        # todo
        # a. 收到model_config后起进程按config执行
        # b. 小模型执行的时候收到finish后结束执行
        # 逻辑大致如下：
        #  while True:
        #      model_config = pipe.recv()
        #      while step!=0 :
        #          execute()
        #          if pipe.poll()!=null:
        #              break
                 
    def run_llm(self, pipe):
        # todo
        # a. 收到model_config后起进程按config执行 
        
        
