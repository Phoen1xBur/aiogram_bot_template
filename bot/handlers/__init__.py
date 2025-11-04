from . import private
from . import group
from . import channel


routers = (
    *private.routers,
    *group.routers,
    *channel.routers,
)