import type { AIGeneratedDietPlan } from "$lib/types";

export function isAIGeneratedDietPlan(
  value: unknown,
): value is AIGeneratedDietPlan {
  if (!Array.isArray(value)) return false;

  return value.every(
    (day) =>
      Array.isArray(day) &&
      day.every(
        (meal) =>
          typeof meal === "object" &&
          meal !== null &&
          typeof meal.name === "string" &&
          typeof meal.description === "string" &&
          Array.isArray(meal.ingredients) &&
          meal.ingredients.every((i: any) => typeof i === "string") &&
          typeof meal.macros === "object" &&
          meal.macros !== null &&
          typeof meal.macros.calories === "number" &&
          typeof meal.macros.protein === "number" &&
          typeof meal.macros.carbs === "number" &&
          typeof meal.macros.fat === "number" &&
          Array.isArray(meal.recipe_in_steps) &&
          meal.recipe_in_steps.every((step: any) => typeof step === "string"),
      ),
  );
}
