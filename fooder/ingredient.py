# ===============================================================================
# Copyright 2024 Jake Ross
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ===============================================================================

class Ingredient:
    name: str = ""
    amount: int = 0
    is_staple: bool = False
    is_vegan: bool = False
    is_vegetarian: bool = False
    is_gluten_free: bool = False
    is_peanut_free: bool = False
    is_pescatarian: bool = False


# ============= EOF =============================================