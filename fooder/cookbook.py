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
from fooder.recipe import Recipe

Recipes = {'breakfast': [Recipe('Pancakes',
                                'American',
                                ['flour', 'sugar', 'baking powder', 'milk', 'eggs']),
                         Recipe('French Toast', 'American',
                                ['bread', 'eggs', 'milk', 'cinnamon']),
                         Recipe('Yougurt', 'American',
                                ['yogurt', 'granola']),
                         Recipe('Cereal', 'American',
                                ['cereal', 'milk']), ],

           'lunch': [Recipe('Taco Salad', 'Mexican',
                            ['lettuce', 'tomato', 'cheese', 'taco meat']),
                     Recipe('Coldcuts', 'American',
                            ['bread', 'meat', 'cheese', 'lettuce', 'tomato']),
                     Recipe('Pasta Salad', 'Italian',
                            ['pasta', 'tomato', 'cheese', 'lettuce']),],

           'dinner': [Recipe('Tacos', 'Mexican',
                             ['taco meat', 'lettuce', 'tomato', 'cheese']),
                      Recipe('Pizza', 'American',
                             ['dough', 'sauce', 'cheese', 'toppings']),
                      Recipe('Pasta', 'Italian',
                             ['pasta', 'sauce', 'cheese']),],}

# ============= EOF =============================================