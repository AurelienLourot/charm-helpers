# Copyright 2016 Canonical Limited.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from unittest import TestCase

from mock import patch

from charmhelpers.contrib.hardening.host.checks import profile


class ProfileTestCase(TestCase):

    @patch.object(profile.utils, 'get_settings', lambda x:
                  {'security': {'kernel_enable_core_dump': False, 'ssh_tmout': False}})
    def test_core_dump_disabled(self):
        audits = profile.get_audits()
        self.assertEqual(1, len(audits))
        self.assertTrue(isinstance(audits[0], profile.TemplatedFile))

    @patch.object(profile.utils, 'get_settings', lambda x: {
        'security': {'kernel_enable_core_dump': True, 'ssh_tmout': 300}
    })
    def test_core_dump_enabled(self):
        audits = profile.get_audits()
        self.assertEqual(2, len(audits))
