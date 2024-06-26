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
import random

from fooder.cookbook import Recipes


class Meal:
    recipes: list = []
    day_idx: int = 0
    name: str = ""
    style: str = ""

    def __init__(self, kind, datetime, day_idx):
        self.kind = kind
        self.datetime = datetime
        self.day_idx = day_idx

    def generate(self, plan):
        count = 0
        recipes = Recipes[self.kind]
        self.recipes = []
        while 1:
            r = random.choice(recipes)
            self.name = r.name
            self.style = r.style
            if plan.validate(self) or count > len(recipes):
                self.recipes.append(r)
                break
            count += 1
# ============= EOF =============================================
