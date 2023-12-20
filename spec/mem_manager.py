
# 同vllm的cache engine，不过需要支持多个模型

class MemManager:
    def __init__(
        self,
        cache_config: CacheConfig,
    ) -> None: