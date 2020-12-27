__all__ = [
    "__version__",
    "AbstractProvider",
    "AbstractResolver",
    "BaseReporter",
    "InconsistentCandidate",
    "Resolver",
    "RequirementsConflicted",
    "ResolutionError",
    "ResolutionImpossible",
    "ResolutionTooDeep",
]

__version__ = "0.5.5.dev0"


from .providers import AbstractProvider, AbstractResolver
from .reporters import BaseReporter
from .resolvers import (
    InconsistentCandidate,
    RequirementsConflicted,
    Resolver,
    ResolutionError,
    ResolutionImpossible,
    ResolutionTooDeep,
)
