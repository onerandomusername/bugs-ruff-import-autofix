from ... import PLANET # this causes invalid code, and ruff realises it.

from ...mars import POSITION_FROM_SUN # this is formatted to the wrong module, but ruff doesn't catch it
