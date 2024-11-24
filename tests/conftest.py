"""Pytest configuration for LLMling LLM provider tests."""

from __future__ import annotations

import pytest


pytest_plugins = ["pytest_asyncio"]


def pytest_collection_modifyitems(items: list[pytest.Item]) -> None:
    """Add asyncio marker to all async tests."""
    for item in items:
        if (
            item.get_closest_marker("asyncio") is None
            and hasattr(item, "callspec")
            and any(param.startswith("async") for param in item.callspec.funcargs)
        ):
            item.add_marker(pytest.mark.asyncio)
