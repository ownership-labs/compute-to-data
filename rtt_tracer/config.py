"""Config module."""
# Copyright 2021 The rtt-tracer Authors
# SPDX-License-Identifier: LGPL-2.1-only

import os
import json
from os import getenv

from rtt_tracer.constant import ExecConstant
from dt_sdk.config import Config as DTConfig
from dt_web3.toolkit.wallet import Wallet


class Config(DTConfig):
    def __init__(self):

        config_path = ExecConstant.CONFIG_FILE
        if not os.path.exists(config_path):
            raise FileNotFoundError(
                f'config file does not exist in {config_path}')

        DTConfig.__init__(self, filename=config_path)
        self._provider_section = 'provider'

    @property
    def wallet(self):
        private_key = self.get(self._provider_section, 'private_key')
        return Wallet(self.web3, private_key=private_key)

    @property
    def query_port(self):
        return self.get(self._provider_section, 'query_port')

    @property
    def assets_path(self):
        return json.loads(self.get(self._provider_section, 'assets_path'))
