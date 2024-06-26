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
from collections import Counter
from datetime import timedelta, datetime
from rich.table import Table
from rich.console import Console
from fooder.meal import Meal

console = Console()


class Plan:
    meals: list = []

    def __init__(self, start_datetime=None, end_datetime=None):
        self.start_datetime = start_datetime
        self.end_datetime = end_datetime

    def validate(self, meal):
        if not self.meals:
            return True
        if len(self.meals) < 3:
            return True

        return self.meals[-3].style != meal.style

    def shopping_list(self):
        pass

    def index(self):
        """generate an appropriate index for the plan"""
        table = Table(title="Index")
        table.add_column("Item")
        table.add_column("Count")
        table.add_column("Location")

        counter = Counter()
        for meal in self.meals:
            for recipe in meal.recipes:
                for ingredient in recipe.ingredients:
                    counter[ingredient.name] += 1

        for k, v in sorted(counter.items(), key=lambda x: x[0]):
            table.add_row(k, str(v), "Pantry")
        console.print(table)

    def summary(self):

        console.print(f"Start Date/Time: {self.start_datetime}")
        console.print(f"End Date/Time  : {self.end_datetime}")

        table = Table(title="Meal Plan")
        table.add_column("Kind")
        table.add_column("Name")
        table.add_column("Style")
        table.add_column("Day")
        table.add_column("Datetime")
        for meal in self.meals:
            table.add_row(meal.kind,
                          meal.name,
                          meal.style,
                          str(meal.day_idx),
                          meal.datetime.strftime('%Y-%m-%d %H:%M:%S'))

        console.print(table)


def tokenize_meals(start_datetime, end_datetime):
    tags = (('breakfast', 3), ('lunch', 5), ('dinner', 16))
    current_datetime = start_datetime

    day_idx = 1
    while 1:
        for t, nhours in tags:
            yield t, current_datetime, day_idx
            current_datetime += timedelta(hours=nhours)
            if current_datetime > end_datetime:
                break
        else:
            day_idx += 1
            continue
        break


class Fooder:
    def __init__(self, npeople, start_datetime, end_datetime):
        self.npeople = npeople
        self.start_datetime = datetime.strptime(start_datetime, '%Y-%m-%d %H:%M:%S')
        self.end_datetime = datetime.strptime(end_datetime, '%Y-%m-%d %H:%M:%S')

    def make_plan(self):
        plan = Plan(self.start_datetime, self.end_datetime)
        for mealtoken in tokenize_meals(self.start_datetime,
                                        self.end_datetime):
            meal = Meal(*mealtoken)
            meal.generate(plan)
            plan.meals.append(meal)

        plan.summary()

        plan.shopping_list()
        plan.index()


if __name__ == '__main__':
    f = Fooder(1, '2024-01-01 08:00:00', '2024-01-02 08:00:00')
    f.make_plan()
# ============= EOF =============================================
