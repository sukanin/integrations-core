# (C) Datadog, Inc. 2020-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

from typing import Any

import pytest

from datadog_checks.base import ConfigurationError
from datadog_checks.rethinkdb._config import Config


def test_default_config():
    # type: () -> None
    config = Config(instance={})
    assert config.host == 'localhost'
    assert config.port == 28015


def test_config():
    # type: () -> None
    config = Config(instance={'host': '192.168.121.1', 'port': 28016})
    assert config.host == '192.168.121.1'
    assert config.port == 28016


def test_config_repr():
    # type: () -> None
    config = Config(instance={})
    assert repr(config) == "Config(host='localhost', port=28015)"


@pytest.mark.parametrize('host', [42, True, object()])
def test_invalid_host(host):
    # type: (Any) -> None
    with pytest.raises(ConfigurationError):
        Config(instance={'host': host})


@pytest.mark.parametrize('port', [42.42, -42, True, object()])
def test_invalid_port(port):
    # type: (Any) -> None
    with pytest.raises(ConfigurationError):
        Config(instance={'port': port})