# Copyright (c) 2016 PaddlePaddle Authors. All Rights Reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import paddle.trainer.PyDataProvider2 as pydp2

import_list = [
    nm for nm in dir(pydp2)
    if '_' in nm and nm[0] != '_' and ('value' in nm or 'vector' in nm)
]
import_list.extend(['InputType'])

for nm in import_list:
    globals()[nm] = getattr(pydp2, nm)

__all__ = import_list
