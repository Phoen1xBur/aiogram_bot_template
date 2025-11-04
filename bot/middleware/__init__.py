from . import redis_context

middlewares = [
    redis_context.AddRedisContext(),
]