"""P&ID tools and CTO block library.

This module provides P&ID-specific AutoCAD operations and integration with the
CAD Tools Online (CTO) symbol library for industrial process flow diagrams.
"""

from __future__ import annotations

from autocad_mcp.pid.cto_library import CTO_CATEGORIES, CTO_ROOT

__all__ = ["CTO_CATEGORIES", "CTO_ROOT"]
