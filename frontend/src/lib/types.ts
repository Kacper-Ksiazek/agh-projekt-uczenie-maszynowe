export type Gender = "MALE" | "FEMALE";
export type Goal = "WEIGHT_LOSS" | "WEIGHT_MAINTENANCE" | "WEIGHT_GAIN";
export type ActivityLevel = "SEDENTARY" | "LIGHT" | "MODERATE" | "ACTIVE";
export type CookingTimePerDay = "30_MINUTES" | "1_HOUR" | "OVER_1_HOUR";

export interface DietFormData {
  // Step 1
  age: number;
  height: number;
  weight: number;
  gender: Gender;
  goal: Goal;
  activityLevel: ActivityLevel;
  cookingTime: CookingTimePerDay;

  // Step 2
  allergies: string;
  intolerance: string;
  dislikedFoods: string;
  preferredFoods: string;
  kitchenEquipment: string;

  // Step 3
  budget: number;
  numberOfDays: number;
}

export interface AIGeneratedSingleMeal {
  name: string;
  description: string;

  ingredients: string[];

  macros: {
    calories: number;
    protein: number;
    carbs: number;
    fat: number;
  };

  recipe_in_steps: string[];
}

export type AIGeneratedDietPlan = AIGeneratedSingleMeal[][];
